from typing import Optional, Any, Callable

from aiogram.types import *

from interface.config import keyboards_config


tg_handlers: dict[str, Callable] = {
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

system_names_switch = {
	'handler_type'
}

def check_data_for_primitiveness (data: Any) -> bool:

	result = False

	switch = {
		type(0),
		type(0.0),
		type(0j),
		type(""),
		type(True),
	}
	if type(data) in switch:
		result = True

	return result

def build_object (
	config			: dict[str, Any],
	handler_dict	: dict[str, Callable],
	skipping_names	: set[str]
) -> Any:

	result: object = None
	arg_dict: dict[str, Any] = {}

	handler_type: str 		= config['handler_type']
	handler		: Callable 	= handler_dict[handler_type]

	for arg_name, arg_content in config.items():
		if arg_name in skipping_names:
			continue

		if not check_data_for_primitiveness(data=arg_content):
			arg_content = build_object(
				config			= arg_content,
				handler_dict	= handler_dict,
				skipping_names	= skipping_names
			)

		arg_dict[arg_name] = arg_content


	result = handler(**arg_dict)
	return result


def build_inline_btn (btn_name: str) -> InlineKeyboardButton:

	BTNS: dict 			= keyboards_config['inline_buttons']
	btn_config: dict 	= BTNS[btn_name]

	result_btn: InlineKeyboardButton = build_object(
		config			= btn_config,
		handler_dict	= tg_handlers,
		skipping_names	= system_names_switch
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