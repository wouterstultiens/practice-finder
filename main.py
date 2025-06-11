import argparse
import asyncio
import logging
import os
from typing import Any

import functions_framework
from dotenv import load_dotenv

from src.core.monitor import run_once
from src.services.telegram import send_messages

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Load environment variables from .env file for local development
load_dotenv()


@functions_framework.http
def main_http(request: Any) -> tuple[str, int]:
    """
    HTTP-triggered Cloud Function entry point.
    Cloud Scheduler should be configured to ping this endpoint.
    """
    logging.info("Cloud Function triggered.")
    try:
        messages = asyncio.run(run_once())
        if messages:
            asyncio.run(send_messages(messages))
            logging.info(f"Successfully sent {len(messages)} notifications.")
            return f"{len(messages)} updates sent.", 200
        else:
            logging.info("Run complete. No changes detected.")
            return "No changes detected.", 200
    except Exception as e:
        logging.error(f"An error occurred in the main execution block: {e}", exc_info=True)
        # Optionally send an error notification
        # asyncio.run(send_messages([f"🚨 Vacancy Monitor failed: {e}"]))
        return "An internal error occurred.", 500


def cli_main() -> None:
    """
    Command-line interface (CLI) for local execution.
    """
    parser = argparse.ArgumentParser(
        description="Run the vacancy monitor once from the command line."
    )
    parser.add_argument(
        "--notify",
        action="store_true",
        help="Send notifications to Telegram. Requires environment variables.",
    )
    args = parser.parse_args()

    if not args.notify:
        os.environ["LOCAL_ONLY_PRINT"] = "1"
        logging.info("Running in local-only mode. Notifications will be printed to the console.")

    messages = asyncio.run(run_once())

    if not messages:
        print("Run complete. No changes detected.")
        return

    if args.notify:
        logging.info(f"Sending {len(messages)} notifications to Telegram...")
        asyncio.run(send_messages(messages))
        logging.info("Notifications sent.")
    else:
        print("\n--- DETECTED CHANGES ---\n")
        print("\n\n".join(messages))
        print("\n--- END OF CHANGES ---")


if __name__ == "__main__":
    cli_main()