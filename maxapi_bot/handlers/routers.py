"""Модуль регистрации роутеров."""

from handlers.custom_handlers.update_dict_words_hand import router as update_dict_router
from handlers.default_heandlers.start import router as start_router
from handlers.default_heandlers.welcome import router as welcome_router
from maxapi import Dispatcher


async def register_routers(dp: Dispatcher):
    """
    Регистрирует все маршруты (роутеры) бота в основном диспетчере.

    Эта функция объединяет логически разделённые обработчики из разных модулей
    в единую систему маршрутизации через `Dispatcher.include_routers()`.

    Порядок важен:
        - События обрабатываются в порядке регистрации.
        - Более специфичные или приоритетные роутеры следует регистрировать раньше,
          если есть пересечение фильтров.

    Аргументы:
        dp (maxapi.Dispatcher): Экземпляр диспетчера, в который будут включены роутеры.
            Передаётся из основного модуля запуска бота (например, `main.py`).
    """
    dp.include_routers(start_router)
    dp.include_routers(welcome_router)
    dp.include_routers(update_dict_router)
