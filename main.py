import logging
import argparse
import os

import functions_framework

from monitor import run_once
import notifier

logging.basicConfig(level=logging.INFO)


@functions_framework.http
def main(request):
    """
    Cloud Function HTTP trigger. Cloud Scheduler pings this once an hour.
    """
    msgs = run_once()
    if msgs:
        notifier.send(msgs)
        return f"{len(msgs)} updates sent.", 200
    return "No changes.", 200


def _cli() -> None:
    """
    Run a single cycle from the command line.

    By default, messages are printed to stdout.
    Pass --notify to also send Telegram alerts (requires env vars).
    """
    parser = argparse.ArgumentParser(description="Run one monitor cycle locally")
    parser.add_argument(
        "--notify",
        action="store_true",
        help="Send Telegram messages instead of just printing them",
    )
    args = parser.parse_args()

    if not args.notify:
        os.environ["LOCAL_ONLY"] = "1"

    msgs = run_once()
    if args.notify:
        notifier.send(msgs)
    else:
        print("\n".join(msgs) if msgs else "No changes.")


if __name__ == "__main__":
    _cli()
