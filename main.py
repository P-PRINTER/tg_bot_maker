from aiogram import Bot, Dispatcher

from handlers.routers.message_router import MSG_RT
from handlers.routers.command_router import CMD_RT

import dotenv
import os


dotenv.load_dotenv()


TOKEN	= os.getenv('API_TOKEN')
BOT		= Bot(TOKEN)

RT_LIST	= [
	MSG_RT,
	CMD_RT
]


if __name__ == '__main__':
	
	DP = Dispatcher()
	for rt in RT_LIST:
		DP.include_router(rt)

	DP.run_polling(BOT)