"""
Orchestrates one crawl / diff / notify cycle.
"""

from __future__ import annotations

import asyncio
import datetime
import logging
import aiohttp
from typing import Dict, List, Tuple

from fetch import fetch_content_async, HEADERS
from config import PRACTICES
from state import (
    load_state,
    save_state,
    archive_snapshot,
    archive_failures,
    save_change_pair,
)
from diff_summary import summarize_change

_LOG = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# Tunables                                                                     #
# --------------------------------------------------------------------------- #
_CONCURRENCY = 10           # hard cap on simultaneous HTTP requests
_RETRIES = 2                # extra tries per URL
_BACKOFF_BASE = 2.0         # exponential back-off (seconds^attempt)

# --------------------------------------------------------------------------- #
def _now() -> str:
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


def _timestamp() -> str:
    return datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")


async def _fetch_with_retry(
    session: aiohttp.ClientSession,
    url: str,
    selector: str,
    get_full_html: bool,
) -> str:
    """Retry wrapper with exponential back-off."""
    for attempt in range(_RETRIES + 1):
        try:
            return await fetch_content_async(session, url, selector, get_full_html)
        except Exception:
            if attempt == _RETRIES:
                raise
            await asyncio.sleep(_BACKOFF_BASE ** attempt)


async def _run_async(ts: str) -> Tuple[Dict[str, str], List[str], List[str]]:
    previous = load_state()
    current: Dict[str, str] = {}
    messages: List[str] = []
    failed: List[str] = []

    connector = aiohttp.TCPConnector(limit=_CONCURRENCY)
    semaphore = asyncio.Semaphore(_CONCURRENCY)

    async with aiohttp.ClientSession(headers=HEADERS, connector=connector) as session:

        async def worker(practice: dict) -> None:
            name, url = practice["name"], practice["url"]
            async with semaphore:
                try:
                    html = await _fetch_with_retry(
                        session, url, practice["selector"], practice["get_full_html"]
                    )
                    current[url] = html

                    if url not in previous:
                        messages.append(
                            f"🆕 <b>{name}</b> toegevoegd aan de watch-list.\n"
                            f"🔗 <a href='{url}'>Open vacaturepagina</a>"
                        )
                    elif previous[url] != html:
                        save_change_pair(name, url, previous[url], html, ts)
                        summary = summarize_change(previous[url], html)
                        messages.append(
                            f"✏️ <b>{name}</b> vacaturepagina is gewijzigd.\n"
                            f"🔗 <a href='{url}'>Open vacaturepagina</a>\n\n{summary}"
                        )
                except Exception:
                    _LOG.exception("Fetch failed for %s", url)
                    messages.append(f"⚠️ <b>{name}</b> kon niet worden opgehaald.")
                    failed.append(url)

        await asyncio.gather(*(worker(p) for p in PRACTICES))

    return current, messages, failed


def run_once() -> List[str]:
    ts = _timestamp()
    current, messages, failed = asyncio.run(_run_async(ts))

    archive_snapshot(current)
    archive_failures(failed, ts)
    save_state(current)

    _LOG.info("Cycle finished %s – %d msgs, %d fails", _now(), len(messages), len(failed))
    return messages
