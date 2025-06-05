# state.py
"""
Persist full page‐content snapshots to GCS.

- state.json holds the latest content for each URL (used for diffing).
- snapshots/YYYYMMDD_HHMMSS.json archives the full content of each run.
- snapshots/failed/YYYYMMDD_HHMMSS.json archives any URLs that failed during that run.
"""

import hashlib
import urllib.parse
import os
import json
import datetime
from google.cloud import storage

_BUCKET_NAME = os.environ["STATE_BUCKET"]
_storage = storage.Client()
_bucket = _storage.bucket(_BUCKET_NAME)

_STATE_BLOB = "state.json"
_SNAPSHOTS_DIR = "snapshots/"
_FAILED_DIR = "snapshots/failed/"


def _blob(name: str):
    return _bucket.blob(name)


def load_state() -> dict[str, str]:
    """
    Load the current state.json, returns { url: content }.
    If state.json does not exist yet, returns {}.
    """
    blob = _blob(_STATE_BLOB)
    if blob.exists():
        return json.loads(blob.download_as_text())
    return {}


def save_state(state: dict[str, str]) -> None:
    """
    Overwrite state.json with the given map { url: content }.
    """
    blob = _blob(_STATE_BLOB)
    blob.upload_from_string(
        json.dumps(state, ensure_ascii=False),
        content_type="application/json",
    )


def archive_snapshot(state: dict[str, str]) -> str:
    """
    Write a timestamped JSON file under snapshots/, e.g.:
      snapshots/20250604_210000.json
    containing the full { url: content } map.
    Returns the timestamp string (YYYYMMDD_HHMMSS) so callers can reuse it.
    """
    now = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    name = f"{_SNAPSHOTS_DIR}{now}.json"
    _blob(name).upload_from_string(
        json.dumps(state, ensure_ascii=False),
        content_type="application/json",
    )
    return now


def archive_failures(failed_urls: list[str], ts: str) -> None:
    """
    Persist a JSON list of URLs that failed during this run.
    Writes to snapshots/failed/YYYYMMDD_HHMMSS.json.
    """
    if not failed_urls:
        return
    name = f"{_FAILED_DIR}{ts}.json"
    _blob(name).upload_from_string(
        json.dumps(failed_urls, ensure_ascii=False),
        content_type="application/json",
    )


def save_change_pair(url: str, old_html: str, new_html: str, ts: str) -> None:
    """
    Bewaart bij een gedetecteerde wijziging twee losse bestanden in de bucket:
      diffs/<YYYYMMDD_HHMMSS>/<hash>/old.html
      diffs/<YYYYMMDD_HHMMSS>/<hash>/new.html
    """
    slug = hashlib.sha1(url.encode()).hexdigest()[:10]          # korte hash → map-naam
    path = f"diffs/{ts}/{slug}"
    _blob(f"{path}/old.html").upload_from_string(old_html, content_type="text/html")
    _blob(f"{path}/new.html").upload_from_string(new_html, content_type="text/html")