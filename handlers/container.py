from typing import Any, Optional, Union, Callable

from aiogram import Bot, Dispatcher, Router
from aiogram import filters

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

from interface import config
from tg_objects import constructor


def build_router (filter_type: str, exception_list: list[str] = None) -> Router:

	pass

def build_handler (config: dict[str, Any], handler) -> Callable:

	pass

RT 		= Router()
CMD_PREFIX	= config.commands_config['prefix']

def make_cmd_handler (
	rt: Router,
	prefix: str,
	command_name: str,
	answer_args: dict[str, Union[str, ReplyKeyboardMarkup, InlineKeyboardMarkup]],
	answer_type: str = 'text',
	need_delete_msg: bool = False
) -> None:
	@rt.message( filters.Command(prefix = prefix, commands = {command_name}) )
	async def links_cmd_handler (msg: types.Message):

		switch: dict[str, Callable] = {
			'text'		: msg.answer,
			'photo'		: msg.answer_photo,
			'sticker'	: msg.answer_sticker,
		}

		answer: Callable = switch[answer_type]
		await answer(
			answer_args['content'],
			reply_markup 	= answer_args['reply_markup']
		)

		if need_delete_msg:
			await msg.delete()


def build_answer_arg (arg_name: str, command_config: dict[str, Union[int, str, bool]]) -> Union[
	str,
	ReplyKeyboardMarkup,
	InlineKeyboardMarkup,
	None
]:

	if not(arg_name in command_config):
		return None			#None

	result_arg: Optional[ Union[
		ReplyKeyboardMarkup,
		InlineKeyboardMarkup,
		str
	] ] = None

	keyboard_dict: dict = config.keyboards_config['keyboards']
	if arg_name == 'reply_markup' and command_config['reply_markup'] in keyboard_dict:

		keyboard_name:		str		= command_config['reply_markup']
		keyboard_config:	dict	= keyboard_dict[keyboard_name]

		if		keyboard_config['type'] == 'reply':
			result_arg = constructor.build_reply_keyboard(keyboard_config)
		elif	keyboard_config['type'] == 'inline':
			result_arg = constructor.build_inline_keyboard(keyboard_config)
		elif	keyboard_config['type'] == 'remove':
			result_arg = constructor.build_remove_keyboard(keyboard_config)
		else:
			result_arg = None

		return result_arg

	elif arg_name != 'reply_markup':

		result_arg = command_config[arg_name]


	return result_arg


for cmd in config.commands_config['commands']:

	reply_markup: Optional[ Union[
		ReplyKeyboardMarkup,
		InlineKeyboardMarkup
	] ] = build_answer_arg('reply_markup', cmd)

	make_cmd_handler(
		rt 				= RT,
		prefix 			= CMD_PREFIX,
		command_name	= cmd['name'],
		answer_args 	= {
			'content': cmd['content'],
			'reply_markup': reply_markup
		},
		answer_type 	= cmd["content_type"],
		need_delete_msg = False
	)
