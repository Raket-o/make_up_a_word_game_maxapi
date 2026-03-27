"""The keyboard creation module."""

# from maxapi.types import InlineKeyboardMarkup
from maxapi.types import CallbackButton, Attachment
from maxapi.types.attachments.buttons import InlineButtonUnion
# from maxapi.utils.keyboard import InlineKeyboardBuilder
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder


def upd_dict_words_buttons() -> Attachment:
    """
    The function of creating a keyboard to update the dictionary with words.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(
        CallbackButton(
            text='обновить словарь',
            payload='update_dict_words',
        ),
    )
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
