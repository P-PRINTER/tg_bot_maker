from typing import Optional, Any, Callable

from aiogram.types import *

from config import keyboards_config


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

def build_tg_object (config: dict[str, Any]) -> Any:

	result: object = None
	arg_dict: dict[str, Any] = {}

	handler_type: str 		= config['handler_type']
	handler		: Callable 	= tg_handlers[handler_type]

	for arg_name, arg_content in config.items():
		if arg_name in system_names_switch:
			continue

		if not check_data_for_primitiveness(arg_content):
			arg_content = build_tg_object(arg_content)

		arg_dict[arg_name] = arg_content


	result = handler(**arg_dict)
	return result

def build_arg (arg_name: str, config: dict) -> Any:

	result_arg: Any = None

	if not(arg_name in config):
		return result_arg

	result_arg = config[arg_name]
	if not check_data_for_primitiveness(result_arg):
		result_arg = build_tg_object(result_arg)


	# if handler_func:
	# 	result_arg = handler_func( config[arg_name] )
	# else:
	# 	result_arg = config[arg_name]

	return result_arg


# def web_app_builder (config: dict[str, Any]) -> WebAppInfo:

# 	# WebAppInfo arguments
# 	url: str = config['url']

# 	return WebAppInfo(url = url)

# def login_url_builder (config: dict[str, Any]) -> LoginUrl:

# 	# LoginUrl arguments
# 	url: 					str 			= config['url']
# 	forward_text: 			Optional[str]	= build_arg('forward_text', config)
# 	bot_username:			Optional[str] 	= build_arg('bot_username', config)
# 	request_write_access:	Optional[bool] 	= build_arg('request_write_access', config)

# 	return LoginUrl(
# 		url 					= url,
# 		forward_text 			= forward_text,
# 		bot_username 			= bot_username,
# 		request_write_access 	= request_write_access
# 	)

# def switch_inline_query_chosen_chat_builder (config: dict[str, Any]) -> SwitchInlineQueryChosenChat:

# 	# SwitchInlineQueryChosenChat arguments
# 	query: 					Optional[str]	= build_arg('query', config)
# 	allow_user_chats: 		Optional[bool]	= build_arg('allow_user_chats', config)
# 	allow_bot_chats: 		Optional[bool]	= build_arg('allow_bot_chats', config)
# 	allow_group_chats: 		Optional[bool]	= build_arg('allow_group_chats', config)
# 	allow_channel_chats: 	Optional[bool]	= build_arg('allow_channel_chats', config)

# 	return SwitchInlineQueryChosenChat(
# 		query					= query,
# 		allow_user_chats		= allow_user_chats,
# 		allow_bot_chats			= allow_bot_chats,
# 		allow_group_chats		= allow_group_chats,
# 		allow_channel_chats		= allow_channel_chats
# 	)

# def callback_game_builder (config: dict[str, Any]) -> CallbackGame:

# 	return CallbackGame()


# def build_btn_arg (arg_name, btn_config) -> Any:

# 	if not(arg_name in btn_config):
# 		return None

# 	return btn_config[arg_name]



def build_inline_btn (btn_name: str) -> InlineKeyboardButton:

	BTNS: dict 			= keyboards_config['inline_buttons']
	btn_config: dict 	= BTNS[btn_name]

	result_btn: InlineKeyboardButton = build_tg_object(btn_config)
	return result_btn

	# text:								str = build_arg('text', btn_config)
	# url: 								Optional[
	# 	str] 								= build_arg('url', btn_config)
	# callback_data: 						Optional[
	# 	str] 								= build_arg('callback_data', btn_config)
	# web_app: 							Optional[
	# 	types.WebAppInfo] 					= build_arg(
	# 		'web_app',
	# 		btn_config,
	# 		web_app_builder
	# 	)
	# login_url: 							Optional[
	# 	types.LoginUrl]						= build_arg(
	# 		'login_url',
	# 		btn_config,
	# 		login_url_builder
	# 	)
	# switch_inline_query: 				Optional[
	# 	str] 								= build_arg(
	# 		'switch_inline_query',
	# 		btn_config
	# 	)
	# switch_inline_query_current_chat: 	Optional[
	# 	str] 								= build_arg(
	# 		'switch_inline_query_current_chat',
	# 		btn_config
	# 	)
	# switch_inline_query_chosen_chat: 	Optional[
	# 	types.SwitchInlineQueryChosenChat]	= build_arg(
	# 		'switch_inline_query_chosen_chat',
	# 		btn_config,
	# 		switch_inline_query_chosen_chat_builder
	# 	)
	# callback_game: 						Optional[
	# 	types.CallbackGame] = build_arg(
	# 		'callback_game',
	# 		btn_config,
	# 		callback_game_builder
	# 	)
	# pay: 								Optional[
	# 	bool]								= build_arg('pay', btn_config)
	
	# return InlineKeyboardButton(
	# 	text 								= text,
	# 	url 								= url,
	# 	callback_data 						= callback_data,
	# 	web_app								= web_app,
	# 	login_url 							= login_url,
	# 	switch_inline_query 				= switch_inline_query,
	# 	switch_inline_query_current_chat 	= switch_inline_query_current_chat,
	# 	switch_inline_query_chosen_chat 	= switch_inline_query_chosen_chat,
	# 	callback_game 						= callback_game,
	# 	pay 								= pay
	# )


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