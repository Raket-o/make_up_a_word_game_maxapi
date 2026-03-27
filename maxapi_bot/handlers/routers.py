"""User Handler registration module."""

# from maxapi import Dispatcher, F, Router
from maxapi import Dispatcher
# from maxapi.types import CommandStart

# from handlers.custom_handlers.update_dict_words_hand import update_dict
# from handlers.default_heandlers.start import start_command_1, start_command_2
from handlers.custom_handlers.update_dict_words_hand import router as update_dict_router
from handlers.default_heandlers.start import router as start_router
from handlers.default_heandlers.welcome import router as welcome_router

# from states.states import DialogueUserState



# async def register_routers(router: Router):
async def register_routers(dp: Dispatcher):
    """
    The register_routers function. Collects handlers in the main router.
    """
    # router.message.register(start_command_1, CommandStart())
    # router.message_created.register(CommandStart())
    # router.message_created.register(start_router)
    dp.include_routers(start_router)
    dp.include_routers(welcome_router)
    dp.include_routers(update_dict_router)

    # router.message_callback.register(
    #     start_command_1,
    #     F.data.startswith("start_command=")
    # )

    # router.message_created.register(start_command_2, DialogueUserState.input_word)

    # router.message_callback.register(update_dict, F.data == "update_dict_words")
