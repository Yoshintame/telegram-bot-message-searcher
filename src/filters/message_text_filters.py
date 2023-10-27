from loguru import logger
from pyrogram import filters

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

        logger.info(f"{is_pass} {query.chat.username} \n {query.text}")
        return is_pass

    return filters.create(func, data=data)
