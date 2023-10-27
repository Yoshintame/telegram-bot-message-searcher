from src.consts import TELEGRAM_BASE_URL


def get_message_link(message):
    return f"{TELEGRAM_BASE_URL}/{message.chat.username}/{message.id}"