from sys import platform
from aiogram import types
from pathlib import Path
from utils.db_api.models import *
from config import dp, bot, API_TOKEN, ADMINS


@dp.message_handler(commands=['test'])
async def bot_start(message: types.Message):
    await message.answer("А вот и я!")
    
    
# Сохраняем присланый от пользователя файл
@dp.message_handler(content_types=['document'], user_id=ADMINS)
async def handle_file(message):
    file_name = message.document.file_name
    file_to_path = Path("files", file_name)
    str_path = str(file_to_path)
    
    try:
        file_info = await bot.get_file(message.document.file_id)
        file_path = file_info.file_path
        await bot.download_file(file_path, file_to_path)
            
        file = Documents(file_name=file_name, file_path=str_path)
        session.add(file)
        session.commit()
        await message.answer("Пожалуй, я сохраню это")
    except Exception as e:
        await message.answer(e)
        raise e


@dp.message_handler()
async def find_file_key(message):
    text = message.text
    k_words = text.split(' ')
    print(f"k_words = {k_words}")

    all_files = session.query(Documents).all()
    f_names = []
    for item in all_files:
        f_names.append(item.file_name)
    print(f"f_names = {f_names}")

    for file in all_files:
        flag = True

        for item in k_words:
            f = str(file.file_name).lower().rfind(item.lower()) # -1 если не входит
            if f == -1:
                flag = False

        f_name = file.file_name
        
        if flag:
            print(f"f_name = {f_name} - Подходит!")
            if platform == "darwin":
                # Для MAC OS
                await message.reply_document(open(f'files/{file.file_name}', 'rb'))
            elif platform == "win32":
                # Для Windows
                await message.reply_document(open(f'files\\{file.file_name}', 'rb'))