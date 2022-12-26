from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os


"""Запуск бота только для локальной машины через bat-файл"""
bot = Bot(os.getenv('TOKEN'))

dp = Dispatcher(bot)
