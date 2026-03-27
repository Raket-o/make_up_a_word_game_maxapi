"""The telegram launch module of the bot."""

import asyncio

from maxapi import Bot, Dispatcher

from handlers.routers import register_routers
from loader import bot, dp, start_up
from utils import logging
from utils.commands import set_default_commands


async def main(bot: Bot, dp: Dispatcher) -> None:
    """The main function. Launches the bot."""
    await set_default_commands(bot)

    dp.bot_started(await start_up())
    # dp.bot_stopped(await on_shutdown())

    await register_routers(dp)
    await bot.delete_webhook()

    # await dp.start_polling(bot)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
