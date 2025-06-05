# state.py
import hashlib
import urllib.parse
import os
import json
import datetime
import re
import unicodedata
from google.cloud import storage

_BUCKET_NAME = os.environ["STATE_BUCKET"]
_storage = storage.Client()
_bucket = _storage.bucket(_BUCKET_NAME)

_STATE_BLOB = "state.json"
_SNAPSHOTS_DIR = "snapshots/"
_FAILED_DIR = "snapshots/failed/"

def _blob(name: str):
    return _bucket.blob(name)

def _slug(name: str) -> str:
    txt = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    txt = re.sub(r"[^a-zA-Z0-9]+", "-", txt).strip("-").lower()
    return txt

def load_state() -> dict[str, str]:
    blob = _blob(_STATE_BLOB)
    if blob.exists():
        return json.loads(blob.download_as_text())
    return {}

def save_state(state: dict[str, str]) -> None:
    blob = _blob(_STATE_BLOB)
    blob.upload_from_string(
        json.dumps(state, ensure_ascii=False),
        content_type="application/json",
    )

def archive_snapshot(state: dict[str, str]) -> str:
    now = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    name = f"{_SNAPSHOTS_DIR}{now}.json"
    _blob(name).upload_from_string(
        json.dumps(state, ensure_ascii=False),
        content_type="application/json",
    )
    return now

def archive_failures(failed_urls: list[str], ts: str) -> None:
    if not failed_urls:
        return
    name = f"{_FAILED_DIR}{ts}.json"
    _blob(name).upload_from_string(
        json.dumps(failed_urls, ensure_ascii=False),
        content_type="application/json",
    )

def save_change_pair(practice: str, url: str, old_html: str, new_html: str, ts: str) -> None:
    name = f"diffs/{ts}/{_slug(practice)}.json"
    payload = {
        "practice": practice,
        "url": url,
        "old": old_html,
        "new": new_html,
    }
    _blob(name).upload_from_string(
        json.dumps(payload, ensure_ascii=False),
        content_type="application/json",
    )
