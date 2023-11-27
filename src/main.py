from src.bot import init_bot, get_token
import asyncio

from src.config import config
from pyrogram import Client
from pprint import pprint


def token():
    asyncio.run(get_token())

def bot():
    init_bot()

def main():
    pprint(config)
    bot()

if __name__ == "__main__":
    main()