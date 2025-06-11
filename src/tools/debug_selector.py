import argparse
import asyncio
import logging
import sys

import aiohttp
from dotenv import load_dotenv

from config import PRACTICES
from src.core.scraper import fetch_and_parse, HEADERS

# Basic logging setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


async def main() -> None:
    """CLI tool to debug a CSS selector for a specific practice."""
    load_dotenv()  # Load .env for any potential config needs

    parser = argparse.ArgumentParser(
        description="Debug a CSS selector for a vacancy page.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "index",
        type=int,
        help="Index of the practice in the `config.PRACTICES` list.",
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Also print the full, prettified HTML of the fetched page for inspection."
    )
    args = parser.parse_args()

    if not 0 <= args.index < len(PRACTICES):
        logging.error(f"Error: Index {args.index} is out of bounds. "
                      f"Please provide an index between 0 and {len(PRACTICES) - 1}.")
        sys.exit(1)

    practice_config = PRACTICES[args.index]
    name = practice_config['name']
    url = practice_config['url']
    selector = practice_config['selector']

    logging.info(f"--- Debugging: '{name}' ---")
    logging.info(f"URL: {url}")
    logging.info(f"Selector: '{selector}'")
    if practice_config.get('ignore_selectors'):
        logging.info(f"Ignoring: {practice_config['ignore_selectors']}")
    logging.info(f"Mode: {'HTML' if practice_config['get_html'] else 'Text'}")
    print("-" * 30)

    try:
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            content = await fetch_and_parse(session, practice_config, debug_mode=args.html)
            print("\n--- EXTRACTED CONTENT ---\n")
            print(content)
            print("\n--- END OF CONTENT ---")
    except Exception as e:
        logging.error(f"An error occurred during fetching or parsing: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())