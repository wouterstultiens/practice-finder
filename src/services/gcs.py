import datetime
import json
import logging
import os
import re
import unicodedata
from typing import Any

from google.cloud import storage
from google.cloud.exceptions import NotFound

# --- GCS Configuration ---
BUCKET_NAME = os.environ.get("STATE_BUCKET")
if not BUCKET_NAME:
    logging.warning("STATE_BUCKET environment variable not set. GCS operations will fail.")
    storage_client = None
else:
    storage_client = storage.Client()

STATE_BLOB_NAME = "state.json"
SNAPSHOTS_DIR = "snapshots/"
DIFFS_DIR = "diffs/"
FAILED_DIR = "failures/"


def _get_bucket() -> storage.Bucket:
    if not storage_client:
        raise ConnectionError("GCS client not initialized. Is STATE_BUCKET set?")
    return storage_client.bucket(BUCKET_NAME)


def _slugify(text: str) -> str:
    """Normalizes string, converts to lowercase, removes non-alpha characters, and converts spaces to hyphens."""
    text = text.lower() 
    normalized_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized_text).strip("-")


def load_state() -> dict[str, str]:
    """Loads the last known state from state.json in the GCS bucket."""
    try:
        bucket = _get_bucket()
        blob = bucket.blob(STATE_BLOB_NAME)
        content = blob.download_as_text()
        return json.loads(content)
    except NotFound:
        logging.warning("state.json not found. Assuming first run and returning empty state.")
        return {}
    except Exception as e:
        logging.error(f"Failed to load state from GCS: {e}", exc_info=True)
        return {}


def save_state(state: dict[str, str]) -> None:
    """Saves the current state to state.json in the GCS bucket."""
    try:
        bucket = _get_bucket()
        blob = bucket.blob(STATE_BLOB_NAME)
        blob.upload_from_string(
            json.dumps(state, indent=2, ensure_ascii=False),
            content_type="application/json"
        )
        logging.info("Successfully saved current state to GCS.")
    except Exception as e:
        logging.error(f"Failed to save state to GCS: {e}", exc_info=True)


def archive_snapshot(state: dict[str, str], timestamp: str) -> None:
    """Archives the full state snapshot to a timestamped file in GCS."""
    try:
        blob_name = f"{SNAPSHOTS_DIR}{timestamp}.json"
        bucket = _get_bucket()
        blob = bucket.blob(blob_name)
        blob.upload_from_string(
            json.dumps(state, indent=2, ensure_ascii=False),
            content_type="application/json"
        )
    except Exception as e:
        logging.error(f"Failed to archive snapshot to {blob_name}: {e}", exc_info=True)


def archive_failures(failed_urls: list[str], timestamp: str) -> None:
    """Archives a list of failed URLs to a timestamped file in GCS."""
    if not failed_urls:
        return
    try:
        blob_name = f"{FAILED_DIR}{timestamp}.json"
        bucket = _get_bucket()
        blob = bucket.blob(blob_name)
        blob.upload_from_string(
            json.dumps(failed_urls, indent=2, ensure_ascii=False),
            content_type="application/json"
        )
    except Exception as e:
        logging.error(f"Failed to archive failures to {blob_name}: {e}", exc_info=True)


def save_change_pair(
    practice: dict[str, Any], old_content: str, new_content: str, timestamp: str
) -> None:
    """Saves the 'before' and 'after' content for a detected change."""
    try:
        slug = _slugify(practice["name"])
        blob_name = f"{DIFFS_DIR}{timestamp}/{slug}.json"
        payload = {
            "practice": practice["name"],
            "url": practice["url"],
            "timestamp": timestamp,
            "old": old_content,
            "new": new_content,
        }
        bucket = _get_bucket()
        blob = bucket.blob(blob_name)
        blob.upload_from_string(
            json.dumps(payload, indent=2, ensure_ascii=False),
            content_type="application/json"
        )
    except Exception as e:
        logging.error(f"Failed to save change pair to {blob_name}: {e}", exc_info=True)