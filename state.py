"""
Stateless scraper ↔ persistent state helper.
Keeps a single JSON file (state.json) in the bucket defined by $STATE_BUCKET.
"""
import json, os, hashlib
from google.cloud import storage

_BUCKET_NAME = os.environ["STATE_BUCKET"]      # fail loud if missing
_BLOB_NAME   = "state.json"
_storage     = storage.Client()
_bucket      = _storage.bucket(_BUCKET_NAME)


def _blob():
    return _bucket.blob(_BLOB_NAME)


def load() -> dict[str, str]:
    """Return {practice_url: sha256} or empty dict on first run."""
    blob = _blob()
    if blob.exists():
        return json.loads(blob.download_as_text())
    return {}


def save(state: dict[str, str]) -> None:
    _blob().upload_from_string(json.dumps(state), content_type="application/json")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()