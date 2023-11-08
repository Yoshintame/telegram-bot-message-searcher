from pyrogram import filters
from pyrogram.handlers import MessageHandler

from src.config import config
from src.utils.fuzzy_filters import bare_check_text_for_keywords
from src.filters.message_text_filters import bare_check_message_for_keywords
from src.utils.utils import get_message_link
from functools import partial


async def send_message_link(client, message, group):
    matched_word = bare_check_text_for_keywords(message.text, group.keywords)

    for chat in group.forward_tos:
        await client.send_message(chat, f"Ключевое слово: {matched_word} \n {get_message_link(message)}")


def generate_chat_group_handlers(app):
    for group in config.groups:
        partial_send_message_link = partial(send_message_link, group=group)
        message_handler = MessageHandler(partial_send_message_link, filters.chat(group.chats) & filters.text & bare_check_message_for_keywords(group.keywords))
        app.add_handler(message_handler)

