import os
import logging
import asyncio
from typing import Iterable

import httpx
from telegram import Bot, constants
from telegram.request import HTTPXRequest

_LOG = logging.getLogger(__name__)

_LOCAL_ONLY = os.getenv("LOCAL_ONLY") == "1"
_TOKEN = os.getenv("BOT_TOKEN")
_IDS = [cid.strip() for cid in os.getenv("CHAT_IDS", "").split(",") if cid.strip()]

# --------------------------------------------------------------------------- #
# Build a Bot – stay compatible with both older (≤20.2) and newer PTB versions #
# --------------------------------------------------------------------------- #
_bot: Bot | None = None
if not _LOCAL_ONLY and _TOKEN and _IDS:
    request = HTTPXRequest(
        connection_pool_size=50,
        pool_timeout=30,
        connect_timeout=30,
        read_timeout=30,
    )
    _bot = Bot(token=_TOKEN, request=request)
else:
    _LOG.info("Running in LOCAL_ONLY mode – messages will be printed to stdout.")


def send(messages: Iterable[str]) -> None:
    """
    Send each message to each chat sequentially.
    A dedicated event-loop keeps Cloud Functions’ loop untouched.
    """
    if _LOCAL_ONLY or _bot is None:
        for msg in messages:
            print(msg)
        return

    async def _send_all() -> None:
        for msg in messages:
            for cid in _IDS:
                try:
                    await _bot.send_message(
                        chat_id=cid,
                        text=msg,
                        parse_mode=constants.ParseMode.HTML,
                        disable_web_page_preview=True,
                    )
                except Exception as exc:
                    _LOG.warning("Error sending to chat %s: %s", cid, exc)

        # tidy up sockets, if this PTB version exposes a session
        if hasattr(_bot, "session"):
            try:
                await _bot.session.aclose()
            except Exception:
                pass
            
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(_send_all())
    finally:
        loop.close()
