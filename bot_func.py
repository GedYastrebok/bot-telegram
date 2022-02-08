def who_is_polyushka_bot_func():
  import telebot
  import codecs
  import collections
  @who_is_polyushka_bot.message_handler(commands=['start'])
  def start_message(message):
    who_is_polyushka_bot.send_message(message.chat.id, 'Вон кнопки, тыркай', reply_markup=keyboard)

  keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
  keyboard.row('Добавить', "Отчёт")

  @who_is_polyushka_bot.message_handler(content_types=['text'])
  def send_text(message):

    if message.text.lower() == 'добавить':
      who_is_polyushka_bot.send_message(message.chat.id, 'Пиши-пиши, не отвлекайся')
      who_is_polyushka_bot.register_next_step_handler(message, next_processing)

    elif message.text.lower() == 'отчёт':
      who_is_polyushka_bot.send_message(message.chat.id, names)

    else:
      who_is_polyushka_bot.send_message(message.chat.id, "В кнопочки тыкай, в кно-поч-ки.")


  @who_is_polyushka_bot.message_handler(content_types=['audio', 'location', 'photo', 'sticker'])
  def send_text(message):

    who_is_polyushka_bot.send_message(message.chat.id, 'В кнопочки тыкни')


  def next_processing(message):

    global names

    if (message.content_type == 'text'):
      if message.text in names:
        msg = 'Было, неоригинальный ты мой человечек!'
      else:
        new_name = str(message.text)
        if message.from_user.first_name != None:
          writer_name = str(message.from_user.first_name)
        elif message.from_user.username != None:
          writer_name = str(message.from_user.username)
        else:
          writer_name = 'милый человек'
        with open('list.txt', 'a+b') as names_file:
          names_file.write((new_name + '\n').encode('utf-8'))
        with open('list.txt', 'rt', encoding='utf-8') as names_file:
          names = str(names_file.read())
        msg = "Окей, " + writer_name + ", обращение записано."
    else:
      msg = 'Иди буквы учи!'

    who_is_polyushka_bot.send_message(message.chat.id, msg)

  who_is_polyushka_bot.polling()