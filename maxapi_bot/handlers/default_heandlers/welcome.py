"""The command module /start."""

import logging

from maxapi import Router

from maxapi.types import Command
from maxapi.types import BotStarted

from config_data.config import START_MESSAGE


start_logger = logging.getLogger(__name__)

router = Router(router_id=__name__)


@router.bot_started()
async def start_command(event: BotStarted) -> None:
    await event.bot.send_message(
        chat_id=event.chat_id,
        # text='Привет! Отправь мне /start'
        text=START_MESSAGE
    )
