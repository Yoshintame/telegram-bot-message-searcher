from pyrogram import Client

from src.config import config
from src.plugins.handlers import generate_chat_group_handlers


def init_bot():
    app = Client("message-searcher", api_id=config.api_id, api_hash=config.api_hash)

    generate_chat_group_handlers(app)

    app.run()
