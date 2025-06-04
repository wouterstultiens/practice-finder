# notifier.py

"""
Tiny wrapper around python-telegram-bot for broadcast only.
Environment:
- BOT_TOKEN          Telegram bot token
- CHAT_IDS           Comma-separated list of chat IDs that should receive alerts
"""
import os
import logging
import asyncio
from typing import Iterable
from telegram import Bot, constants

_LOG = logging.getLogger(__name__)
_bot = Bot(token=os.environ["BOT_TOKEN"])
_IDS = [cid.strip() for cid in os.environ["CHAT_IDS"].split(",") if cid.strip()]

def send(messages: Iterable[str]) -> None:
    """
    Send each message to all chat IDs. Under the hood, we build a list of
    coroutines and run them via asyncio.run, so that Bot.send_message actually happens.
    """
    for msg in messages:
        _LOG.info(f"Sending message: {msg}")
        # Build one coroutine per chat ID
        coros = []
        for cid in _IDS:
            _LOG.info(f"To id: {cid}")
            coros.append(
                _bot.send_message(
                    chat_id=cid,
                    text=msg,
                    parse_mode=constants.ParseMode.HTML,
                )
            )

        # Run all of them in a freshly created event loop
        try:
            asyncio.run(asyncio.gather(*coros))
        except Exception as exc:
            _LOG.warning("Error while sending messages: %s", exc)
