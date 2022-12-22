from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/По_эмоциям')
b2 = KeyboardButton('/По_жанру')
b3 = KeyboardButton('/По_странам')
b4 = KeyboardButton('/Хочу_совет!')
b5 = KeyboardButton('/Интересный_факт^^')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True)

kb_user.row(b1, b2).add(b3).add(b4).add(b5)
