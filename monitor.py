# state.py
"""
Persist full page‐content snapshots to GCS.

- state.json holds the latest content for each URL (used for diffing).
- snapshots/YYYYMMDD_HHMMSS.json archives the full content of each run.
"""

import os, json, datetime
from google.cloud import storage

_BUCKET_NAME = os.environ["STATE_BUCKET"]
_storage = storage.Client()
_bucket  = _storage.bucket(_BUCKET_NAME)

_STATE_BLOB    = "state.json"
_SNAPSHOTS_DIR = "snapshots/"


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
    blob.upload_from_string(json.dumps(state, ensure_ascii=False), content_type="application/json")


def archive_snapshot(state: dict[str, str]) -> None:
    """
    Write a timestamped JSON file under snapshots/, e.g.:
      snapshots/20250604_210000.json
    containing the full { url: content } map.
    """
    now = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    name = f"{_SNAPSHOTS_DIR}{now}.json"
    blob = _blob(name)
    blob.upload_from_string(json.dumps(state, ensure_ascii=False), content_type="application/json")
