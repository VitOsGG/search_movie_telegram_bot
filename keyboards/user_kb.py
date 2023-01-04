#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

b1 = types.KeyboardButton(text='🌝 Эмоция')
b2 = types.KeyboardButton(text='🎬 Жанр')
b3 = types.KeyboardButton(text='🌎 Страна')
b4 = types.KeyboardButton(text='🎞 Хочу совет!')
b5 = types.KeyboardButton(text='🗿 Интересный факт^^')


kb_user = types.ReplyKeyboardMarkup(resize_keyboard=True)


kb_user.row(b1, b2).add(b3).add(b4).add(b5)
