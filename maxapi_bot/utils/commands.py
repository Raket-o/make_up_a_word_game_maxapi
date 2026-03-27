"""The command module for the bot."""
from maxapi import Bot, types


async def set_default_commands(bot: Bot) -> None:
    """
    The function adds commands to the bot.
    """
    commands = [
        types.BotCommand(name="start", description="Запустить бота"),
    ]

    # await bot.set_my_commands(commands)
