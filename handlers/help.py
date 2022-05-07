from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from config import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(HELP_MESSAGE)



HELP_MESSAGE = """

Добро пожаловать в нашего бота!
Поддерживаемые команды:
/start - Начать диалог
/help_admin - Справка для администратора
/help_guests - Справка для гостей
"""

@dp.message_handler(commands=['help_guests'])
async def help_for_quests(message):
    await message.answer('Как пользоваться ботом. \n'
    'Гость набирает название файла или слова входящие в название документа, \
    и бот пересылает файлы, навзания которых похожи на то, которое введет гость.\n'
    '\n'
    'Водить ключевые слова через пробел и без окончаний или строго с тем окончанием \
каким заканчивается слово в названии документа!\n'
'\n'
'Пример: \n'
'Название файла: Годовой отчет N кампании.pdf\n'
'Ключевые слова: год отчет камп')

     

@dp.message_handler(commands=['help_admin'])
async def help_for_admin(message):
      await message.answer('Администратор:\n'
    'Может отправлять файл боту. Файл сохраняется в БД. Отправлять следует по одному файлу.')


