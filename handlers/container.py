from typing import Any, Optional, Union, Callable

from aiogram import Bot, Dispatcher, Router
from aiogram import filters

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

from interface.keyboards import reply_keyboards, inline_keyboards
from interface.config import commands_config
# from utils import *

# import dotenv
# import os


# dotenv.load_dotenv()


# TOKEN	= os.getenv('API_TOKEN')
# BOT		= Bot(TOKEN)

# RT_LIST	= [
# 	MSG_RT,
# 	CMD_RT
# ]

def build_router (filter_type: str, exception_list: list[str] = None) -> Router:

	pass


RT 		= Router()
CMD_PREFIX	= commands_config['prefix']

def make_cmd_handler (
	rt: Router,
	prefix: str,
	command: str,
	answer_args: dict[str, Union[str, ReplyKeyboardMarkup, InlineKeyboardMarkup]],
	answer_type: str = 'text',
	need_delete_msg: bool = False
) -> None:
	@rt.message( filters.Command(prefix = prefix, commands = {command}) )
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


def build_answer_arg (arg_name: str, command: dict[str, Union[int, str, bool]]) -> Union[
	str,
	ReplyKeyboardMarkup,
	InlineKeyboardMarkup,
	None
]:

	if not(arg_name in command):
		return None			#None

	result_arg: Optional[ Union[
		ReplyKeyboardMarkup,
		InlineKeyboardMarkup,
		str
	] ] = None


	if arg_name == 'reply_markup' and command[arg_name] in reply_keyboards:
		result_arg = reply_keyboards[ command[arg_name] ]
		return result_arg			#ReplyKeyboardMarkup
	elif arg_name == 'reply_markup' and command[arg_name] in inline_keyboards:
		result_arg = inline_keyboards[ command[arg_name] ]
		return result_arg			#InlineKeyboardMarkup
	elif arg_name == 'reply_markup':
		return result_arg 			#None


	result_arg = command[arg_name]

	return result_arg


for cmd in commands_config['commands']:

	reply_markup: Optional[ Union[
		ReplyKeyboardMarkup,
		InlineKeyboardMarkup
	] ] = build_answer_arg('reply_markup', cmd)

	make_cmd_handler(
		rt 				= RT,
		prefix 			= CMD_PREFIX,
		command 		= cmd['name'],
		answer_args 	= {
			'content': cmd['content'],
			'reply_markup': reply_markup
		},
		answer_type 	= cmd["content_type"],
		need_delete_msg = False
	)



# if __name__ == '__main__':
	
# 	DP = Dispatcher()
# 	for rt in RT_LIST:
# 		DP.include_router(rt)

# 	DP.run_polling(BOT)