import logging

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )


"""
DEBUG — уровень отладочной информации, зачастую помогает при разработке приложения на машине программиста.
INFO — уровень вспомогательной информации о ходе работы приложения/скрипта.
WARNING — уровень предупреждения. Например, мы можем предупреждать о том, что та или иная функция будет удалена в будущих версиях вашего приложения.
ERROR — с таким уровнем разработчики пишут логи с ошибками, например, о том, что внешний сервис недоступен.
CRITICAL — уровень сообщений после которых работа приложения продолжаться не может.
"""
