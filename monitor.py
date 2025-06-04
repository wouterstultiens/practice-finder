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
from config import PRACTICES                    # single source of truth
from state import load_state, save_state, archive_snapshot, archive_failures

_LOG = logging.getLogger(__name__)


def _now() -> str:
    """ISO-8601 helper for logs (UTC)."""
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


async def _run_async() -> Tuple[Dict[str, str], List[str], List[str]]:
    """
    Concurrently fetch every configured vacancy page.
    Returns a tuple of (current_state, messages, failed_urls).
    """
    previous = load_state()       # {url: html}
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
                    messages.append(f"🆕 <b>{name}</b> added to watch-list.")
                elif previous[url] != html:
                    messages.append(f"✏️ <b>{name}</b> vacancy page changed.")
            except Exception as exc:
                _LOG.warning("Fetch failed for %s: %s", url, exc)
                messages.append(f"⚠️ <b>{name}</b> could not be fetched.")
                failed.append(url)

        # Fire off all fetches concurrently
        await asyncio.gather(*(worker(p) for p in PRACTICES))

    return current, messages, failed


def run_once() -> List[str]:
    """
    Synchronous wrapper for the Cloud Function / CLI.

    Returns:
        A list of Telegram‐ready messages. If empty, no changes detected.
    """
    # 1) Perform all fetches concurrently
    current, messages, failed = asyncio.run(_run_async())

    # 2) Persist results
    ts = archive_snapshot(current)       # write snapshots/YYYYMMDD_HHMMSS.json
    archive_failures(failed, ts)         # write snapshots/failed/YYYYMMDD_HHMMSS.json
    save_state(current)                  # update state.json

    _LOG.info("Cycle finished %s – %d msgs, %d fails", _now(), len(messages), len(failed))
    return messages
