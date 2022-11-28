from config import TOKEN
import random
import requests
from datetime import datetime
import telebot

bot = telebot.TeleBot(TOKEN)


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nСтоимость BTC: {sell_price}$"


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # Меню - кнопки
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)  # resize_keyboard - автоматический размер кнопок
    item1 = telebot.types.KeyboardButton('🎲 Рандомное число')
    item2 = telebot.types.KeyboardButton('😊 Как дела?')
    item3 = telebot.types.KeyboardButton('💰 Цена Bitcoin')
    item4 = telebot.types.KeyboardButton('📖 Информация')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     'Добро пожаловать, {0.first_name}!\nЯ - <u><b>{1.first_name}</b></u>, бот созданный для Вас!'.
                     format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)  #
    # reply_markup - прикрепление кнопки к сообщению


# Считывание введенного текста (нажатой кнопки, которая передаёт текст)
@bot.message_handler(content_types=['text'])
def send_text(message):
    # bot.send_message(message.chat.id, message.text) - пересылает в ответ то же сообщение (попугай)
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(1, 1000)))
        elif message.text == '😊 Как дела?':

            # Ин лайновая клавиатура
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton('Хорошо', callback_data='good')
            item2 = telebot.types.InlineKeyboardButton('Не очень', callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как? 😇', reply_markup=markup)
            # reply_markup=markup - Прикрепляем к сообщению
        elif message.text == '💰 Цена Bitcoin':
            bot.send_message(message.chat.id, get_data())

        elif message.text == '📖 Информация':
            bot.send_message(message.chat.id,
                             'Я - бот <u><b>{1.first_name}</b></u>, созданный разработчиком '
                             '<b>Гиззатуллиным Айратом</b>'
                             ' в качестве домашнего задания семинара по "Знакомству '
                             'с языком Python" в школе GeekBrains!'.
                             format(message.from_user, bot.get_me()), parse_mode='html')
        else:
            bot.send_message(message.chat.id, 'Что? Я не знаю такого...')


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


# Для постоянной работы бота и отслеживания поступающих сообщений
bot.polling(none_stop=True)
