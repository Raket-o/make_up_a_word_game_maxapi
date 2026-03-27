"""The command module /start."""

import logging

from maxapi import types, F, Router
from maxapi.context import MemoryContext

from maxapi.types import MessageCreated, Command
from maxapi.types import BotStarted

from config_data.config import ADMINS_ID, START_MESSAGE
from keyboards.inline.upd_dict_words_kb import upd_dict_words_buttons
from states.states import DialogueUserState
from utils.make_word import find_words_obj

start_logger = logging.getLogger(__name__)

router = Router(router_id=__name__)


# @router.message_created(Command("start"))
# @router.message_created(F.message.body.text)
async def start_command_1(event: MessageCreated) -> None:
    """
    Output of the START_MESSAGE and waiting for user input.
    """
    print("start_command_1")
    user_id = event.from_user.user_id
    first_name = event.from_user.first_name

    if user_id in ADMINS_ID:
        kb = upd_dict_words_buttons()
        await event.message.answer(text=START_MESSAGE, attachments=[kb])
    else:
        await event.message.answer(START_MESSAGE)

    start_logger.info(f"start_logger-UserID={user_id} {first_name}")

    # await context.set_state(DialogueUserState.input_word)


# @router.message_created(DialogueUserState.input_word)
@router.message_created(F.message.body.text)
async def start_command_2(event: MessageCreated, context: MemoryContext) -> None:
    """
    Outputs words to the user using the specified characters.
    """
    print("start_command_2")

    dict_words: dict[int:list[str]] = await find_words_obj.get_find_words(event.message.body.text.lower())

    if dict_words:
        answer = ""
        for count_letter, words in dict_words.items():
            answer += f"Слова из {count_letter} букв: {', '.join(words)}" + "\n\n"
        await event.message.answer(answer)
    else:
        await event.message.answer("Что-то слишком тяжело, давай попробуем другие буквы")

    await start_command_1(event)
