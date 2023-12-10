from aiogram import Router, F, types


MSG_RT = Router()



@MSG_RT.message(F.text == "lol")
async def lol_msg_handler (msg: types.Message):

	pass