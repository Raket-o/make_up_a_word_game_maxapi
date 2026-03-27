"""Модуль запуска Max бота."""

import asyncio

from handlers.routers import register_routers
from loader import bot, dp, start_up
from maxapi import Bot, Dispatcher
from utils import logging
from utils.commands import set_default_commands


async def main(bot: Bot, dp: Dispatcher) -> None:
    """
    Точка входа в Telegram-бота. Запускает основной цикл обработки событий.

    Инициализирует:
        - команды бота (меню /start и др.);
        - обработчики из зарегистрированных роутеров;
        - функцию приветствия при старте;
        - режим polling с пропуском устаревших обновлений.

    Функция `main()` настраивает окружение и запускает Max бота.
    Выполняется через `asyncio.run()` при прямом запуске скрипта.

    Основные этапы:
        1. Установка стандартных команд через `set_default_commands`.
        2. Регистрация хука `start_up` на событие запуска диспетчера.
        3. Подключение всех роутеров (`register_routers`).
        4. Сброс вебхука (если был установлен ранее).
        5. Запуск polling-режима с автоматической перезагрузкой при ошибках.

    Поведение:
        - Использует `skip_updates=True` — пропускает все накопленные обновления до старта.
        - Не требует дополнительной настройки — всё делегировано в `loader` и `handlers`.
    """
    await set_default_commands(bot)

    dp.bot_started(await start_up())

    await register_routers(dp)
    await bot.delete_webhook()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
