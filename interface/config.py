import json
from typing import Any


commands_config: dict[str, Any] = None
with open(file='interface/commands_config.json', mode='rt', encoding='utf-8') as file:

	commands_config = json.load(file)

keyboards_config: dict[str, Any] = None
with open(file='interface/keyboards_config.json', mode='rt', encoding='utf-8') as file:
	
	keyboards_config = json.load(file)