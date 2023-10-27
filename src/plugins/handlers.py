from pyrogram import filters
from pyrogram.handlers import MessageHandler

from src.config import config
from src.filters.message_text_filters import bare_check_message_for_keywords
from src.utils.utils import get_message_link


async def send_message_link(client, message):
    for chat in config.forward_tos:
        await client.send_message(chat, get_message_link(message))


def generate_chat_group_handlers(app):
    for group in config.groups:
        app.add_handler(
            MessageHandler(
                send_message_link,
                filters.chat(group.chats) & bare_check_message_for_keywords(group.keywords)))
