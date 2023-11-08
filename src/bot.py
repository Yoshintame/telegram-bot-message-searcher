from pyrogram import Client

from src.config import config
from src.plugins.handlers import generate_chat_group_handlers

async def get_token():
    async with Client("message-searcher", phone_number=config.phone_number, api_id=config.api_id, api_hash=config.api_hash, in_memory=True) as app:
        print(await app.export_session_string())


def init_bot():
    app = Client("message-searcher", phone_number=config.phone_number, api_id=config.api_id, api_hash=config.api_hash, session_string=config.session_string)

    generate_chat_group_handlers(app)

    app.run()

    print(app.export_session_string())
