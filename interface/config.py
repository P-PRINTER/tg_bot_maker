import json
from typing import Any, Callable

commands_config: dict = None
with open('commands_config.json', 'rt') as file:
	commands_config = json.load(file)

keyboards_config: dict = None
with open('keyboards_config.json', 'rt') as file:
	keyboards_config = json.load(file)