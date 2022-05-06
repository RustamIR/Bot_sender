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
/help - Получить справку

Как пользоваться ботом:
Администратор:
Может отправлять файл боту. Файл сохраняется в БД

Гость:
Набирает название файла или слова входящие в название документа, и бот пересылает файлы, навзания которых похожи
на то, которое введет гость.

Желательно вводить слова (через пробел) без окончаний или строго с тем окончанием каким заканчивается слово в названии документа!
"""