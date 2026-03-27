"""
Модуль: Обработчик обновления словаря слов.

Содержит асинхронную функцию `update_dict`, которая обновляет внутренний словарь слов,
используемый для поиска комбинированных слов (например, в игре типа "Составь слова").

Функция может быть вызвана через:
    - callback-запрос (нажатие кнопки),
    - обычное сообщение (для отладки или ручного запуска).

После обновления отправляет подтверждение пользователю и перезапускает команду /start.
"""

import logging
from typing import Union

from maxapi import types, F, Router
from maxapi.context import MemoryContext
from maxapi.types import MessageCreated, MessageCallback

from handlers.default_heandlers.start import start_command_1
from utils.make_word import find_words_obj


# Настройка логгера
update_dict_logger = logging.getLogger(__name__)

router = Router(router_id=__name__)



# @router.message_callback("update_dict_words")
@router.message_callback(F.callback.payload == 'update_dict_words')
# async def message_callback(event: MessageCallback):
#     await event.answer(
#         new_text=f'Вы нажали на кнопку {event.callback.payload}!'
#     )
async def update_dict(callback: MessageCallback, context: MemoryContext) -> None:
    """
    Обновляет внутренний словарь слов из текстового файла.

    Эта функция вызывается при получении команды или callback-запроса на обновление словаря.
    Перезагружает список слов через метод `update_dict_words()` объекта `find_words_obj`.

    Args:
        callback (Union[types.CallbackQuery, types.Message]): Входящее сообщение или колбэк.
            Поддерживается вызов как от Message, так и от CallbackQuery.
        context (FSMContext): Контекст состояния конечного автомата. Очищается после выполнения.

    Workflow:
        1. Вызывает `find_words_obj.update_dict_words()` — перечитывает файл со словами.
        2. Логирует факт обновления.
        3. Отправляет пользователю сообщение: "Словарь обновлён".
        4. Очищает текущее состояние FSM.
        5. Перезапускает стартовую команду (`start_command_1`).

    Пример использования:
        - Пользователь нажимает кнопку "Обновить словарь".
        - Бот перечитывает `russian_nouns.txt` и применяет изменения без перезапуска.

    Logging:
        Уровень INFO: записывает факт обновления словаря.
    """
    find_words_obj.update_dict_words()
    update_dict_logger.info("Словарь слов был успешно обновлён")

    # if isinstance(event, types.CallbackQuery):
    #     await event.message.answer("Словарь обновлён")
    #     await event.answer()
    # else:
    await callback.message.answer("Словарь обновлён")

    await context.clear()
    await start_command_1(callback, context)
