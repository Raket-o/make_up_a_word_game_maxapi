"""
Модуль: Обработчик обновления словаря слов.

Содержит асинхронную функцию `update_dict`, которая обновляет внутренний словарь слов,
используемый для поиска комбинированных слов (например, в игре типа "Составь слова").

Функция может быть вызвана через:
    - callback-запрос (нажатие кнопки)

После обновления отправляет подтверждение пользователю и перезапускает команду /start.
"""

import logging

from handlers.default_heandlers.start import start_command_1
from maxapi import F, Router
from maxapi.types import MessageCallback
from utils.make_word import find_words_obj

# Настройка логгера
update_dict_logger = logging.getLogger(__name__)

router = Router(router_id=__name__)


@router.message_callback(F.callback.payload == "update_dict_words")
async def update_dict(event: MessageCallback) -> None:
    """
    Обработчик callback-запроса для обновления внутреннего словаря слов.

    При нажатии кнопки с payload 'update_dict_words' перезагружает список слов,
    используемый ботом для генерации или проверки комбинированных слов
    (например, в мини-игре «Составь слова»). Источник — текстовый файл на диске.

    Аргументы:
        event (maxapi.types.MessageCallback): Объект события от Max,
            содержащий callback-данные. Используется для доступа к сообщению
            и информации о пользователе.

    Процесс:
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

    await event.message.answer("Словарь обновлён")

    await start_command_1(event)
