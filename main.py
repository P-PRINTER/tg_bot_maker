from aiogram import Bot, Dispatcher

from handlers import container

import dotenv
import os


dotenv.load_dotenv()


TOKEN	= os.getenv('API_TOKEN')
BOT		= Bot(TOKEN)

RT_LIST	= [
	container.RT
]


if __name__ == '__main__':
	
	DP = Dispatcher()
	DP.include_routers(*RT_LIST)

	DP.run_polling(BOT)