from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5101940487:AAFRGeg3q4LM8z9lLvRJIcw81eHPYAHFOU4'

storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
ADMINS = [
    291800214
] # посмотреть свой Id в get bot id