from aiogram import Bot, Dispatcher

from handlers import container


RT_LIST	= [
	container.RT
]


run_bot(bot_token: str)
	
	DP = Dispatcher()
	DP.include_routers(*RT_LIST)

	BOT = Bot(bot_token)

	DP.run_polling(BOT)