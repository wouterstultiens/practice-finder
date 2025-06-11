import argparse
import asyncio
import json
import logging
import os
import random
import sys

from dotenv import load_dotenv
from google.cloud import storage
from google.cloud.exceptions import NotFound

from src.services import llm

# Basic logging setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def _get_random_diff_blob(gcs_client: storage.Client, bucket_name: str, timestamp_prefix: str | None) -> storage.Blob:
    """Picks a random diff JSON file from the GCS bucket."""
    bucket = gcs_client.bucket(bucket_name)
    prefix = f"diffs/{timestamp_prefix}/" if timestamp_prefix else "diffs/"
    
    logging.info(f"Searching for diffs in gs://{bucket_name}/{prefix}...")
    
    blobs = list(bucket.list_blobs(prefix=prefix))
    json_blobs = [b for b in blobs if b.name.endswith(".json")]

    if not json_blobs:
        logging.error(f"No diff JSON files found in 'gs://{bucket_name}/{prefix}'.")
        logging.error("Try running the main monitor first to generate some diffs.")
        sys.exit(1)
        
    return random.choice(json_blobs)


async def main() -> None:
    """CLI tool to test the LLM prompt against a real change from GCS."""
    load_dotenv()

    # --- Environment Variable Check ---
    bucket_name = os.getenv("STATE_BUCKET")
    if not bucket_name:
        logging.error("STATE_BUCKET environment variable is not set. Please add it to your .env file.")
        sys.exit(1)
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(
        description="Test the LLM prompt by fetching a random change from GCS.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--ts",
        help="Optional: specify a timestamp folder (e.g., '20231120_140000') to narrow the search."
    )
    args = parser.parse_args()

    # --- Main Logic ---
    try:
        gcs_client = storage.Client()
        blob = _get_random_diff_blob(gcs_client, bucket_name, args.ts)
        
        logging.info(f"📄 Picked random change: gs://{bucket_name}/{blob.name}")
        
        data = json.loads(blob.download_as_text())
        old_content, new_content = data["old"], data["new"]

        print("\n" + "="*50)
        print(f"PRACTICE: {data.get('practice', 'N/A')}")
        print(f"URL: {data.get('url', 'N/A')}")
        print("="*50 + "\n")

        print("--- OLD CONTENT (first 500 chars) ---\n")
        print(old_content[:500] + ('...' if len(old_content) > 500 else ''))
        print("\n--- NEW CONTENT (first 500 chars) ---\n")
        print(new_content[:500] + ('...' if len(new_content) > 500 else ''))

        print("\n--- GENERATING LLM SUMMARY... ---\n")
        summary = await llm.summarize_change(old_content, new_content)

        print("✅ --- PROMPT RESULT --- ✅\n")
        # The summary is already HTML escaped, but we print it raw here.
        print(summary)
        print("\n" + "✅" * 15)

    except NotFound:
        logging.error(f"Bucket '{bucket_name}' not found or you don't have access.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())