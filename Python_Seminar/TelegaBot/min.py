import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # Меню - кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # resize_keyboard - маленькая кнопка
    item1 = types.KeyboardButton('🎲 Рандомное число')
    item2 = types.KeyboardButton('😊 Как дела?')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <u><b>{1.first_name}</b></u>, бот созданный для Вас!".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)  #
    # reply_markup - прикрепление кнопки к сообщению


# Считывание введенного текста (нажатой кнопки, которая передаёт текст)
@bot.message_handler(content_types=['text'])
def lalala(message):
    # bot.send_message(message.chat.id, message.text) - пересылает в ответ то же сообщение (попугай)
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(1, 1000)))
        elif message.text == '😊 Как дела?':

            # Ин лайновая клавиатура
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
            item2 = types.InlineKeyboardButton('Не очень', callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как? 😇', reply_markup=markup)
            # reply_markup=markup - Прикрепляем к сообщению
        else:
            bot.send_message(message.chat.id, 'Я не знаю что и ответить 🤪')


# Обработка нажатия кнопок ин лайновой клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и очень хорошо')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает! Держись!')
            # Отредактировать сообщение и удалить прикрепленные кнопки после их нажатия
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='😊 Как дела?', reply_markup=None)
            # Создать уведомление
            # bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=True,
            #                           text='Это тест уведомления')


    except Exception as e:
        print(repr(e))


# Для постоянной работы бота
bot.polling(none_stop=True)
