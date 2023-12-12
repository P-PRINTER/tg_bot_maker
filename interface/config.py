from typing import Callable, Optional, Any

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

from tg_objects import constructor

import json


def get_config(config_name: str) -> dict:

	result_config: dict = {}

	config_path: str = f'interface/configs/{config_name}_config.json'
	config_file: object = open(file=config_path, mode='rt', encoding='utf-8')

	result_config = json.load(config_file)
	config_file.close()

	return result_config

commands_config: dict[str, Any] = get_config('commands')
keyboards_config: dict[str, Any] = get_config('keyboards')

# reply_keyboards:	dict[str, ReplyKeyboardMarkup]	= {}
# inline_keyboards:	dict[str, InlineKeyboardMarkup]	= {}

# for kb_name, kb_content in keyboards_config['keyboards'].items():

# 	keyboard_dict: dict = None
# 	build_keyboard_func: Callable = None

# 	if 		kb_content['type'] == 'reply':
# 		keyboard_dict 			= reply_keyboards
# 		build_keyboard_func 	= constructor.build_reply_keyboard

# 	elif	kb_content['type'] == 'inline':
# 		keyboard_dict 			= inline_keyboards
# 		build_keyboard_func 	= constructor.build_inline_keyboard

# 	elif	kb_content['type'] == 'remove':
# 		keyboard_dict			= reply_keyboards
# 		build_keyboard_func		= constructor.build_remove_keyboard

# 	keyboard_dict[kb_name] = build_keyboard_func(kb_content)