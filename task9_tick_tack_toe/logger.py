import logging


# создаем логгер
logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)

# создаем хендлеры
match_file_handler = logging.FileHandler('matches.log')
rev_file_handler = logging.FileHandler('revanche.log')
match_file_handler.setLevel(logging.DEBUG)
rev_file_handler.setLevel(logging.INFO)

# настройка форматирования
match_format = logging.Formatter('%(asctime)s - %(message)s')
rev_format = logging.Formatter('%(asctime)s - %(message)s')
match_file_handler.setFormatter(match_format)
rev_file_handler.setFormatter(rev_format)

# добавляем хендлеры в логгеры
logger.addHandler(match_file_handler)
logger.addHandler(rev_file_handler)
