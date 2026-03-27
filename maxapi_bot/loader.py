"""Модуль инициализации Max бота."""

import logging
from asyncio import get_event_loop

from config_data.config import BOT_TOKEN
from maxapi import Bot, Dispatcher
from maxapi.enums.parse_mode import ParseMode

logger = logging.getLogger(__name__)


async def start_up() -> None:
    """
    Функция, вызываемая при успешном старте бота.

    Выполняется один раз при запуске polling-режима.
    Текущая реализация логирует факт запуска на уровне INFO.

    Пример вывода:
        INFO:root:Bot started

    Может быть расширена для:
        - Подключения к базе данных;
        - Проверки доступности API;
        - Уведомления администраторов о запуске.
    """
    logging.info("Bot started")


async def on_shutdown():
    logging.info("Bot stopped")


bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode("html"))

get_event_loop()
dp = Dispatcher()
