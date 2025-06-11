import asyncio
import datetime
import logging
from typing import Any

import aiohttp

from config import PRACTICES
from src.core.scraper import fetch_and_parse, HEADERS
from src.services import gcs, llm

# --- Configuration ---
CONCURRENCY_LIMIT = 10
MAX_RETRIES = 2
BACKOFF_FACTOR = 2.0  # Seconds to wait, doubles each retry

async def _fetch_with_retry(
    session: aiohttp.ClientSession,
    practice_config: dict[str, Any],
    semaphore: asyncio.Semaphore
) -> tuple[str, str | None]:
    """Fetches a single URL with retries and exponential backoff."""
    url = practice_config["url"]
    async with semaphore:
        for attempt in range(MAX_RETRIES + 1):
            try:
                content = await fetch_and_parse(session, practice_config)
                return url, content
            except Exception as e:
                if attempt == MAX_RETRIES:
                    logging.error(f"Final attempt failed for {url}: {e}")
                    return url, None
                wait_time = BACKOFF_FACTOR ** attempt
                logging.warning(f"Attempt {attempt + 1} failed for {url}. Retrying in {wait_time:.1f}s... Error: {e}")
                await asyncio.sleep(wait_time)
    return url, None # Should not be reached


async def _process_results(
    results: list[tuple[str, str | None]],
    run_timestamp: str
) -> tuple[dict[str, str], list[str], list[str]]:
    """Processes fetched results to generate state, messages, and failures."""
    previous_state = gcs.load_state()
    current_state: dict[str, str] = {}
    messages: list[str] = []
    failed_urls: list[str] = []

    # Create a reverse mapping from URL to practice config for easy lookup
    url_to_practice = {p["url"]: p for p in PRACTICES}

    for url, content in results:
        practice = url_to_practice[url]
        name = practice["name"]

        if content is None:
            failed_urls.append(url)
            messages.append(f"⚠️ <b>{name}</b> kon niet worden opgehaald.")
            continue

        current_state[url] = content
        previous_content = previous_state.get(url)

        if previous_content is None:
            msg = (f"🆕 <b>{name}</b> is toegevoegd aan de monitor.\n"
                   f"🔗 <a href='{url}'>Bekijk vacaturepagina</a>")
            messages.append(msg)
        elif previous_content != content:
            gcs.save_change_pair(practice, previous_content, content, run_timestamp)
            summary = await llm.summarize_change(previous_content, content)
            msg = (f"✏️ <b>{name}</b> vacaturepagina is gewijzigd.\n"
                   f"🔗 <a href='{url}'>Bekijk vacaturepagina</a>\n\n{summary}")
            messages.append(msg)

    return current_state, messages, failed_urls


async def run_once() -> list[str]:
    """
    Executes a single, full monitoring cycle.

    1. Fetches all pages concurrently.
    2. Compares with previous state from GCS.
    3. Generates summaries for changes.
    4. Archives new state, changes, and failures to GCS.
    5. Returns a list of notification messages.
    """
    start_time = datetime.datetime.now(datetime.timezone.utc)
    run_timestamp = start_time.strftime("%Y%m%d_%H%M%S")
    logging.info(f"Starting monitoring cycle with timestamp {run_timestamp}.")

    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = [_fetch_with_retry(session, p, semaphore) for p in PRACTICES]
        results = await asyncio.gather(*tasks)

    current_state, messages, failed_urls = await _process_results(results, run_timestamp)

    if current_state:
        gcs.archive_snapshot(current_state, run_timestamp)
        gcs.save_state(current_state)

    if failed_urls:
        gcs.archive_failures(failed_urls, run_timestamp)

    duration = (datetime.datetime.now(datetime.timezone.utc) - start_time).total_seconds()
    logging.info(
        f"Cycle finished in {duration:.2f}s. "
        f"Found {len(messages)} updates and {len(failed_urls)} failures."
    )
    return messages