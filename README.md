# Bot_send_file

Бот для сохранения документов определенной аудитории.

    В config.py добавьте свой id и токен бота.

Администратор может добавлять документы в чат бота, которые будут сохраняться в директории files/{file_name}

Гости могут получать документы загруженные в бота по ключевым словам. То есть пользователь водит слова, которые могут находится в названии документа.

    Например: 
        Название документа: 'Годовой отчет N кампании'
        Ключевые слова: "год", "отче", "кампани"

    Ключевые слова должны либо совпадать полностью либо иметь часть совпадений:
        Пример: 'год', 'одов', 'тче' и тд.
    
    
