"""Модуль обработки запуска бота."""

import logging

from config_data.config import START_MESSAGE
from maxapi import Router
from maxapi.types import BotStarted

start_logger = logging.getLogger(__name__)

router = Router(router_id=__name__)


@router.bot_started()
async def start_command(event: BotStarted) -> None:
    """
    Обработчик события запуска бота пользователем.

    Автоматически вызывается системой MaxAPI при событии `bot_started`, которое происходит,
    когда пользователь впервые начинает диалог с ботом (нажимает «Начать» в интерфейсе).

    Функция отправляет приветственное сообщение, определённое в конфигурации (`START_MESSAGE`),
    в личный чат с пользователем.

    Аргументы:
        event (maxapi.types.BotStarted): Событие старта диалога.
            Содержит:
                - `chat_id` — идентификатор чата с пользователем;
                - `bot` — экземпляр бота, используемый для отправки сообщений.
    """

    await event.bot.send_message(chat_id=event.chat_id, text=START_MESSAGE)
