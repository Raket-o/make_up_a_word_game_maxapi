"""Модуль обработки команды /start."""

import logging

from config_data.config import ADMINS_ID, START_MESSAGE
from keyboards.inline.upd_dict_words_kb import upd_dict_words_buttons
from maxapi import F, Router
from maxapi.types import MessageCreated
from utils.make_word import find_words_obj

start_logger = logging.getLogger(__name__)

router = Router(router_id=__name__)


async def start_command_1(event: MessageCreated) -> None:
    """
    Отправляет стартовое сообщение пользователю при запуске бота или перезапуске сценария.

    Поведение зависит от прав пользователя:
        - Если пользователь входит в список администраторов (`ADMINS_ID`),
          отображает дополнительную клавиатуру с кнопкой «Обновить словарь».
        - В остальных случаях отправляет только текст приветствия.

    Аргументы:
        event (maxapi.types.MessageCreated): Событие создания сообщения,
            содержащее данные о пользователе и контексте.
    """
    user_id = event.from_user.user_id
    first_name = event.from_user.first_name

    if user_id in ADMINS_ID:
        kb = await upd_dict_words_buttons()
        await event.message.answer(text=START_MESSAGE, attachments=[kb])
    else:
        await event.message.answer(START_MESSAGE)

    start_logger.info(f"start_logger-UserID={user_id} {first_name}")


@router.message_created(F.message.body.text)
async def start_command_2(event: MessageCreated) -> None:
    """
    Обработчик текстового ввода для поиска слов, составленных из заданных букв.

        Принимает строку от пользователя, передаёт её в `find_words_obj.get_find_words()`,
        который находит все допустимые слова, используя внутренний словарь.

        Результат:
            - Если слова найдены: группирует их по количеству букв и отправляет списком.
            - Если ничего не найдено: предлагает попробовать другие буквы.

        После ответа автоматически перезапускает приветственное меню через `start_command_1`.

        Аргументы:
            event (maxapi.types.MessageCreated): Событие с текстовым сообщением от пользователя.
                Ожидается, что `event.message.body.text` содержит строку с буквами.

    """
    dict_words: dict[int:list[str]] = await find_words_obj.get_find_words(
        event.message.body.text.lower()
    )

    if dict_words:
        answer = ""
        for count_letter, words in dict_words.items():
            answer += f"Слова из {count_letter} букв: {', '.join(words)}" + "\n\n"
        await event.message.answer(answer)
    else:
        await event.message.answer(
            "Что-то слишком тяжело, давай попробуем другие буквы"
        )

    await start_command_1(event)
