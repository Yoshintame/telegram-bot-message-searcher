import re
from typing import List, Optional

import yaml
from pydantic import BaseModel
from src.consts import CONFIG_PATH


class GroupSchema(BaseModel):
    name: str
    chats: List[str | int]
    keywords: List[str]


class ConfigSchema(BaseModel):
    api_id: int
    api_hash: str
    phone_number: str
    forward_tos: List[str | int]
    groups: List[GroupSchema]
    session_string: Optional[str] = None


def prepare_config_keywords(config):
    for group in config.groups:
        group.keywords = [keyword.lower().strip() for keyword in group.keywords]
        group.keywords = [re.sub(r'\s{2,}', ' ', keyword) for keyword in group.keywords]
        group.keywords = check_duplicates(group.keywords)
        group.keywords.sort()
    return config


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
config = prepare_config_keywords(config)
