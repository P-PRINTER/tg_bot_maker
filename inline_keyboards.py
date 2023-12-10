from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



IBTN1	= InlineKeyboardButton(
	text = '1',
	url = 'https://www.youtube.com/watch?v=pWqzA8fRrNs&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12',
	callback_data = "1"
)
IBTN2	= InlineKeyboardButton(
	text = '2',
	url = 'https://www.youtube.com/watch?v=pWqzA8fRrNs&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12',
	callback_data = "2"
)
IBTN3	= InlineKeyboardButton(
	text = '3',
	url = 'https://www.youtube.com/watch?v=pWqzA8fRrNs&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=12',
	callback_data = "3"
)

IKB = InlineKeyboardMarkup(inline_keyboard = [[IBTN1, IBTN2], [IBTN3]])