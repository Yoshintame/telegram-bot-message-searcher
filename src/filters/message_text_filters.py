from loguru import logger
from pyrogram import filters
import regex
import emoji
from pprint import pprint

from src.utils.fuzzy_filters import bare_check_text_for_keywords, fuzzy_check_text_for_keywords


def fuzzy_check_message_for_keywords(data):
    async def func(flt, _, query):
        keywords, ratio_threshold = flt.data
        ratio = fuzzy_check_text_for_keywords(query.text, keywords, ratio_threshold)

        logger.info(f"{ratio} {query.chat.username} \n {query.text}")
        return ratio > ratio_threshold

    return filters.create(func, data=data)


def bare_check_message_for_keywords(data):
    async def func(flt, _, query):
        keywords = flt.data
        is_pass = bare_check_text_for_keywords(query.text, keywords)

        logger.info(f"Keywords: {is_pass} {query.chat.username} \n {query.text}")
        return is_pass

    return filters.create(func, data=data)


def check_message_for_emojis_amount(data):
    async def func(flt, _, query):
        emojis_ammout = count_amout_of_emojis(str(query.text))

        logger.info(f"Emojis: {emojis_ammout} {query.chat.username} \n {query.text}")
        return emojis_ammout < flt.data

    return filters.create(func, data=data)


def check_message_text_lenght(data):
    async def func(flt, _, query):
        text_message_leght = len(str(query.text))

        logger.info(f"Text lenght: {text_message_leght} {query.chat.username} \n {query.text}")
        return text_message_leght < flt.data

    return filters.create(func, data=data)


def count_amout_of_emojis(text):
    emoji_counter = emoji.emoji_count(text)

    return emoji_counter
