"""
Detect content changes for every practice.
Return a list of user-friendly messages that must be broadcast.
"""
from datetime import datetime
from typing import List
from config import PRACTICES
from fetch import fetch_content
import state, logging

_LOG = logging.getLogger(__name__)


def run_once() -> List[str]:
    previous = state.load()
    now_hash  = {}
    changes: List[str] = []

    for p in PRACTICES:
        try:
            text = fetch_content(p["url"], p["selector"], p["get_full_html"])
        except Exception as exc:
            _LOG.warning("Fetch failed for %s: %s", p["url"], exc)
            continue

        h = state.digest(text)
        now_hash[p["url"]] = h

        if previous.get(p["url"]) and previous[p["url"]] != h:
            ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
            changes.append(f"🔔 <b>{p['name']}</b> updated (<a href=\"{p['url']}\">vacature</a>) – {ts}")

    state.save(now_hash)
    return changes