from typing import Optional, Callable

from aiogram.types import *
import utils

from interface.config import get_config


handler_dict: dict[str, Callable] = {
	'web_app_info'						: WebAppInfo,
	'login_url'							: LoginUrl,
	'switch_inline_query_chosen_chat'	: SwitchInlineQueryChosenChat,
	'callback_game'						: CallbackGame,
	'reply_keyboard_markup'				: ReplyKeyboardMarkup,
	'reply_keyboard_remove'				: ReplyKeyboardRemove,
	'keyboard_button'					: KeyboardButton,
	'inline_keyboard_markup'			: InlineKeyboardButton,
	'inline_keyboard_button'			: InlineKeyboardButton,
}

skipping_names_set: set[str] = {
	'handler_type'
}

def build_inline_btn (btn_name: str) -> InlineKeyboardButton:

	BTNS: dict 			= get_config('keyboards')['inline_buttons']
	btn_config: dict 	= BTNS[btn_name]

	result_btn: InlineKeyboardButton = utils.build_object(
		config			= btn_config,
		handler_dict	= handler_dict,
		skipping_names	= skipping_names_set
	)
	return result_btn

def build_reply_markup (markup: [[str]]) -> list[ list[KeyboardButton] ]:

	result_markup : list[ list[KeyboardButton] ] = []

	for btn_row in markup:

		result_row = []
		for btn_text in btn_row:
			result_row.append( KeyboardButton(text = btn_text) )

		result_markup.append(result_row)

	return result_markup

def build_inline_markup (markup: list[ list[str] ]) -> list[ list[InlineKeyboardButton] ]:

	result_markup: list[ list[InlineKeyboardButton] ] = []
	result_markup = list( map(lambda btn_row: list( map(build_inline_btn, btn_row) ), markup) )

	return result_markup


def build_reply_keyboard (keyboard: dict) -> ReplyKeyboardMarkup:

	result_keyboard = None

	markup 				= build_reply_markup( keyboard['markup'] )
	result_keyboard		= ReplyKeyboardMarkup( keyboard = markup )

	return result_keyboard

def build_remove_keyboard (keyboard: Optional[dict]) -> ReplyKeyboardMarkup:

	result_keyboard = ReplyKeyboardRemove()
	return result_keyboard

def build_inline_keyboard (keyboard: dict) -> InlineKeyboardMarkup:

	result_keyboard = None

	markup 				= build_inline_markup( keyboard['markup'] )
	result_keyboard		= InlineKeyboardMarkup( inline_keyboard = markup )

	return result_keyboard