# notifier.py

import os
import logging
import asyncio
from typing import Iterable
from telegram import Bot, constants

_LOG = logging.getLogger(__name__)
_LOG.info("🚀 notifier.py v2 loading")   # <<— temporary version check
_bot = Bot(token=os.environ["BOT_TOKEN"])
_IDS = [cid.strip() for cid in os.environ["CHAT_IDS"].split(",") if cid.strip()]


def send(messages: Iterable[str]) -> None:
    """
    Send each message to all chat IDs.
    Builds all coroutines and runs them on a fresh asyncio event loop.
    """

    async def _send_all():
        for msg in messages:
            coros = []
            for cid in _IDS:
                coros.append(
                    _bot.send_message(
                        chat_id=cid,
                        text=msg,
                        parse_mode=constants.ParseMode.HTML,
                    )
                )
            if not coros:
                continue

            # Gather all send_message coroutines for this single message
            results = await asyncio.gather(*coros, return_exceptions=True)
            for res in results:
                if isinstance(res, Exception):
                    _LOG.warning("Error sending to one chat: %s", res)

    try:
        # asyncio.run creates a fresh event loop, runs until complete, then closes it.
        asyncio.run(_send_all())
    except Exception as exc:
        _LOG.warning("Error while sending messages: %s", exc)
