"""Bot Telegram Initialization module."""

import logging
from asyncio import get_event_loop

from maxapi import Bot, Dispatcher
from maxapi.enums.parse_mode import ParseMode
# from maxapi.client.bot import DefaultBotProperties
# from maxapi.enums import ParseMode

from config_data.config import BOT_TOKEN

logger = logging.getLogger(__name__)


async def start_up() -> None:
    """The start_up function. Outputs text to the console at startup."""
    logging.info("Bot started")


# async def on_shutdown() -> None:
#     """The on_shutdown function. Outputs text to the console at startup."""
#     logging.info("Bot stopped")


bot = Bot(
    token=BOT_TOKEN,
    parse_mode=ParseMode("html")
)

loop = get_event_loop()
dp = Dispatcher()
