from pyrogram import filters
from pyrogram.handlers import MessageHandler

from src.config import config
from src.utils.fuzzy_filters import bare_check_text_for_keywords
from src.filters.message_text_filters import bare_check_message_for_keywords, check_message_for_emojis_amount, check_message_text_lenght
from src.utils.utils import get_message_link
from functools import partial


async def get_info(client, message, group):
    chat_id = message.chat.id
    keywords_whitelist_string = '\n'.join(group.keywords_whitelist)
    keywords_blacklist_string = '\n'.join(group.keywords_blacklist)
    max_text_lenght = group.max_text_lenght
    max_emoji_amount = group.max_emoji_amount
    tos_string = '\n'.join(group.forward_tos)
    from_string = '\n'.join(group.chats)
    await client.send_message(chat_id, f"Вайтлист ключевые слова:\n{keywords_whitelist_string}\n\nБлэклист ключевые слова:\n{keywords_blacklist_string}\n\nМаксимальное количество символов:\n{max_text_lenght}\n\nМаксимальное количество эмодзи:\n{max_emoji_amount}\n\nПересылаю в:\n{tos_string}\n\nИщу в:\n{from_string}")


async def send_message_link(client, message, group):
    matched_word = bare_check_text_for_keywords(message.text, group.keywords_whitelist)

    for chat in group.forward_tos:
        await client.send_message(chat, f"Ключевое слово: {matched_word} \n {get_message_link(message)}")


def generate_chat_group_handlers(app):
    for group in config.groups:
        partial_send_message_link = partial(send_message_link, group=group)
        message_handler = MessageHandler(
            partial_send_message_link,
            filters.chat(group.chats) &
            filters.text &
            check_message_for_emojis_amount(group.max_emoji_amount) &
            check_message_text_lenght(group.max_text_lenght) &
            bare_check_message_for_keywords({"keywords": group.keywords_blacklist, "inverted": True}) &
            bare_check_message_for_keywords({"keywords": group.keywords_whitelist, "inverted": False}))
        app.add_handler(message_handler)

        partial_get_info = partial(get_info, group=group)
        message_handler = MessageHandler(partial_get_info, filters.chat(group.forward_tos) & filters.command(["info", "help"]))
        app.add_handler(message_handler)
