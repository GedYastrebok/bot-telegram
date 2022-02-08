import logging as log
from bot_func import who_is_polyushka_bot_func

log.basicConfig(filename='logs.log', format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')

who_is_polyushka_bot = telebot.TeleBot('2139247946:AAEcbs0AGB4-kGyULfJkdITadofLA89d3Ow')

names = "В списке пусто!"

while True:
  try:
    who_is_polyushka_bot_func()
  except Exception:
    log.error('Ошибка в основном цикле\n', exc_info=True)