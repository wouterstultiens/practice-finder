# monitor.py
"""
Orchestrates one crawl / diff / notify cycle.

Logic:
    • download every configured vacancy page (see config.PRACTICES)
      concurrently via aiohttp
    • compare against the previous HTML snapshot stored in GCS
    • persist the new state and archive a timestamped JSON snapshot
    • if any fetches failed, write a second JSON listing those URLs
    • return a list[str] with human-readable Telegram messages
"""

from __future__ import annotations

import asyncio
import datetime
import logging
import aiohttp
from typing import List, Tuple, Dict

from fetch import fetch_content_async, HEADERS
from config import PRACTICES
from state import load_state, save_state, archive_snapshot, archive_failures, save_change_pair
from diff_summary import summarize_change

_LOG = logging.getLogger(__name__)


def _now() -> str:
    """ISO-8601 helper for logs (UTC)."""
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


def _timestamp() -> str:
    """Return timestamp string like 20250605_153000"""
    return datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")


async def _run_async(ts: str) -> Tuple[Dict[str, str], List[str], List[str]]:
    """
    Concurrently fetch every configured vacancy page.
    Returns a tuple of (current_state, messages, failed_urls).
    """
    previous = load_state()
    current: Dict[str, str] = {}
    messages: List[str] = []
    failed: List[str] = []

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async def worker(p: dict) -> None:
            name, url = p["name"], p["url"]
            try:
                html = await fetch_content_async(
                    session, url, p["selector"], p["get_full_html"]
                )
                current[url] = html

                if url not in previous:
                    messages.append(
                        f"🆕 <b>{name}</b> toegevoegd aan de watch-list.\n"
                        f"🔗 <a href='{url}'>Open vacaturepagina</a>"
                    )
                elif previous[url] != html:
                    # Save old/new HTML
                    save_change_pair(url, previous[url], html, ts)
                    # Generate Dutch summary
                    summary = summarize_change(previous[url], html)
                    messages.append(
                        f"✏️ <b>{name}</b> vacaturepagina is gewijzigd.\n"
                        f"🔗 <a href='{url}'>Bekijk pagina</a>\n"
                        f"{summary}"
                    )
            except Exception as exc:
                _LOG.warning("Fetch failed for %s: %s", url, exc)
                messages.append(f"⚠️ <b>{name}</b> kon niet worden opgehaald.")
                failed.append(url)

        await asyncio.gather(*(worker(p) for p in PRACTICES))

    return current, messages, failed


def run_once() -> List[str]:
    """
    Synchronous wrapper for the Cloud Function / CLI.

    Returns:
        A list of Telegram‐ready messages. If empty, no changes detected.
    """
    ts = _timestamp()
    current, messages, failed = asyncio.run(_run_async(ts))

    archive_snapshot(current)
    archive_failures(failed, ts)
    save_state(current)

    _LOG.info("Cycle finished %s – %d msgs, %d fails", _now(), len(messages), len(failed))
    return messages
