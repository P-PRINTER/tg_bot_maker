from typing import Callable, Optional, Any

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

# from tg_objects import constructor

import json


def get_config(config_name: str) -> dict:

	result_config: dict = {}

	config_path: str = f'interface/configs/{config_name}_config.json'
	config_file: object = open(file=config_path, mode='rt', encoding='utf-8')

	result_config = json.load(config_file)
	config_file.close()
	

	return result_config

# commands_config: dict[str, Any] = get_config('commands')
# keyboards_config: dict[str, Any] = get_config('keyboards')
