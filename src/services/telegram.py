import asyncio
import logging
import os
from typing import Iterable

from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

# --- Telegram Configuration ---
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_IDS_STR = os.getenv("TELEGRAM_CHAT_IDS", "")
CHAT_IDS = [cid.strip() for cid in CHAT_IDS_STR.split(",") if cid.strip()]
PRINT_ONLY = os.getenv("LOCAL_ONLY_PRINT") == "1"


async def send_messages(messages: Iterable[str]) -> None:
    """
    Sends a list of messages to all configured Telegram chats asynchronously.

    If LOCAL_ONLY_PRINT is set, it prints messages to the console instead.
    """
    if PRINT_ONLY:
        for msg in messages:
            print(msg)
        return

    if not TOKEN or not CHAT_IDS:
        logging.warning("Telegram token or chat IDs are not configured. Skipping notification.")
        return

    bot = Bot(token=TOKEN)
    tasks = []
    async with bot:
        for msg in messages:
            for chat_id in CHAT_IDS:
                # Create a coroutine for each message to each chat
                tasks.append(
                    bot.send_message(
                        chat_id=chat_id,
                        text=msg,
                        parse_mode=ParseMode.HTML,
                        disable_web_page_preview=True,
                    )
                )

        # Await all send tasks concurrently, gathering any exceptions
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for i, result in enumerate(results):
            if isinstance(result, TelegramError):
                # Determine which chat_id failed
                task_index = i
                chat_id_index = task_index % len(CHAT_IDS)
                failed_chat_id = CHAT_IDS[chat_id_index]
                logging.error(f"Failed to send message to chat {failed_chat_id}: {result}")