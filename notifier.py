"""
Tiny wrapper around python-telegram-bot for broadcast only.
Environment:
- BOT_TOKEN          Telegram bot token
- CHAT_IDS           Comma-separated list of chat IDs that should receive alerts
"""
import os, logging
from typing import Iterable
from telegram import Bot, constants

_LOG = logging.getLogger(__name__)
_bot  = Bot(token=os.environ["BOT_TOKEN"])
_bot.run()
_IDS  = [cid.strip() for cid in os.environ["CHAT_IDS"].split(",") if cid.strip()]


def send(messages: Iterable[str]) -> None:
    for msg in messages:
        _LOG.info(f"Sending message: {msg}")
        for cid in _IDS:
            _LOG.info(f"To id: {cid}")
            try:
                _bot.send_message(chat_id=cid, text=msg, parse_mode=constants.ParseMode.HTML)
            except Exception as exc:  # pragma: no cover
                _LOG.warning("Cannot send to %s: %s", cid, exc)