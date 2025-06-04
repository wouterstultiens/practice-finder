import logging
import asyncio
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
