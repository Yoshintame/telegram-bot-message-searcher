import re
from typing import List, Optional

import yaml
from pydantic import BaseModel
from src.consts import CONFIG_PATH


class GroupSchema(BaseModel):
    name: str
    chats: List[str | int]
    forward_tos: List[str | int]
    keywords_whitelist: Optional[List[str]] = None
    keywords_blacklist: Optional[List[str]] = None
    max_text_lenght: Optional[int] = None
    max_emoji_amount: Optional[int] = None


class ConfigSchema(BaseModel):
    api_id: int
    api_hash: str
    phone_number: str
    groups: List[GroupSchema]
    session_string: Optional[str] = None


def prepare_config(config):
    for group in config.groups:
        group.keywords_blacklist = prepare_config_keywords(group.keywords_blacklist)
        group.keywords_whitelist = prepare_config_keywords(group.keywords_whitelist)
    return config


def prepare_config_keywords(keywords):
    keywords = [keyword.lower().strip() for keyword in keywords]
    keywords = [re.sub(r'\s{2,}', ' ', keyword) for keyword in keywords]
    keywords = check_duplicates(keywords)
    keywords.sort()
    return keywords


def check_duplicates(keywords):
    unique_keywords = []
    for keyword1 in keywords:
        is_duplicate = False
        for keyword2 in unique_keywords:
            if keyword1 in keyword2 or keyword2 in keyword1:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_keywords.append(keyword1)
    return unique_keywords


def parse_config(config_file, config_model):
    with open(config_file, "r") as file:
        config_data = yaml.safe_load(file)

    config = config_model(**config_data)

    return config


config = parse_config(CONFIG_PATH, ConfigSchema)
config = prepare_config(config)
