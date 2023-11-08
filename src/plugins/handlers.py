from pyrogram import filters
from pyrogram.handlers import MessageHandler

from src.config import config
from src.utils.fuzzy_filters import bare_check_text_for_keywords
from src.filters.message_text_filters import bare_check_message_for_keywords
from src.utils.utils import get_message_link
from functools import partial


async def get_info(client, message, group):
    chat_id = message.chat.id
    keywords_string = '\n'.join(group.keywords)
    tos_string = '\n'.join(group.forward_tos)
    from_string = '\n'.join(group.chats)
    await client.send_message(chat_id, f"Ключевые слова:\n{keywords_string}\n\nПересылаю в:\n{tos_string}\n\nИщу в:\n{from_string}")


async def send_message_link(client, message, group):
    matched_word = bare_check_text_for_keywords(message.text, group.keywords)

    for chat in group.forward_tos:
        await client.send_message(chat, f"Ключевое слово: {matched_word} \n {get_message_link(message)}")


def generate_chat_group_handlers(app):
    for group in config.groups:
        partial_send_message_link = partial(send_message_link, group=group)
        message_handler = MessageHandler(partial_send_message_link, filters.chat(group.chats) & filters.text & bare_check_message_for_keywords(group.keywords))
        app.add_handler(message_handler)

        partial_get_info = partial(get_info, group=group)
        message_handler = MessageHandler(partial_get_info, filters.chat(group.forward_tos) & filters.command(["info", "help"]))
        app.add_handler(message_handler)
