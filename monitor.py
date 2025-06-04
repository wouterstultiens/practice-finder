# monitor.py
"""
Orchestrates one crawl / diff / notify cycle.

Logic:
    • download every configured vacancy page (see config.PRACTICES)
    • compare against the previous HTML snapshot stored in GCS
    • persist the new state and archive a timestamped JSON snapshot
    • return a list[str] with human-readable Telegram messages
"""

from __future__ import annotations

import datetime, logging
from typing import List

from fetch import fetch_content
from config import PRACTICES                    # single source of truth
from state import load_state, save_state, archive_snapshot

_LOG = logging.getLogger(__name__)


def _now() -> str:  # ISO-8601 helper for logs
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


def run_once() -> List[str]:
    """
    Runs a single monitoring cycle.

    Returns
    -------
    list[str]
        One line per user-facing update message (empty → nothing changed).
    """
    previous = load_state()       # {url: html}
    current: dict[str, str] = {}
    messages: list[str] = []

    for p in PRACTICES:
        name, url = p["name"], p["url"]
        try:
            html = fetch_content(url, p["selector"], p["get_full_html"])
            current[url] = html
        except Exception as exc:   # network / selector / HTTP error
            _LOG.warning("Fetch failed for %s: %s", url, exc)
            messages.append(f"⚠️ <b>{name}</b> could not be fetched.")
            continue

        if url not in previous:
            messages.append(f"🆕 <b>{name}</b> added to watch-list.")
        elif previous[url] != html:
            messages.append(f"✏️ <b>{name}</b> vacancy page changed.")

    # -- persistence ----------------------------------------------------
    save_state(current)
    archive_snapshot(current)
    _LOG.info("Cycle finished %s – %d messages", _now(), len(messages))
    return messages
