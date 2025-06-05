import os
import logging
import asyncio
from typing import Iterable
from telegram import Bot, constants

_LOG = logging.getLogger(__name__)

_LOCAL_ONLY = os.getenv("LOCAL_ONLY") == "1"
_TOKEN = os.getenv("BOT_TOKEN")
_IDS = [cid.strip() for cid in os.getenv("CHAT_IDS", "").split(",") if cid.strip()]

_bot: Bot | None = None
if not _LOCAL_ONLY and _TOKEN and _IDS:
    _bot = Bot(token=_TOKEN)
else:
    _LOG.info("Running in LOCAL_ONLY mode – messages will be printed to stdout.")


def send(messages: Iterable[str]) -> None:
    """
    Send each message to all chat IDs, or print them if running locally.
    """
    if _LOCAL_ONLY or _bot is None:
        for msg in messages:
            print(msg)
        return

    async def _send_all():
        for msg in messages:
            coros = [
                _bot.send_message(
                    chat_id=cid,
                    text=msg,
                    parse_mode=constants.ParseMode.HTML,
                )
                for cid in _IDS
            ]
            if not coros:
                continue

            results = await asyncio.gather(*coros, return_exceptions=True)
            for res in results:
                if isinstance(res, Exception):
                    _LOG.warning("Error sending to one chat: %s", res)

    try:
        asyncio.run(_send_all())
    except Exception as exc:
        _LOG.warning("Error while sending messages: %s", exc)
