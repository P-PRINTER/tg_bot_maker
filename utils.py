from typing import Optional, Any, Callable

from aiogram.types import *


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
