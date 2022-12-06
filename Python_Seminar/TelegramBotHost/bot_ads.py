from config import TOKEN
import random
import requests
from datetime import datetime
import telebot
import sqlite3

bot = telebot.TeleBot(TOKEN)


# ------------- Команда Старт ---------------
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/Hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # Меню - кнопки
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # resize_keyboard - подгон автоматического размера кнопок
    item1 = telebot.types.KeyboardButton('📢Подать объявление')
    item2 = telebot.types.KeyboardButton('📁Мои объявления')
    item3 = telebot.types.KeyboardButton('🔎Поиск объявлений')
    item4 = telebot.types.KeyboardButton('📖 Информация')
    item5 = telebot.types.KeyboardButton('📲 Регистрация')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     'Добро пожаловать, <b>{0.first_name}</b>!\n'
                     'Вы находитесь в боте для размещения и поиска объявлений.\n'
                     'Выберите действие нажатием кнопки ⤵️'.
                     format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)  #
    # reply_markup - прикрепление кнопки к сообщению


# Считывание введенного текста (нажатой кнопки, которая передаёт текст)
@bot.message_handler(content_types=['text'])
def send_text(message):
    # if message.text == ''
    # bot.send_message(message.chat.id, message.text) - пересылает в ответ то же сообщение (попугай)
    if message.chat.type == 'private':
        if message.text == '📢Подать объявление':
            # bot.send_message(message.chat.id, str(random.randint(1, 1000)))
            # Ин лайновая клавиатура
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton('🚗 Транспорт', callback_data='transport')
            item2 = telebot.types.InlineKeyboardButton('🛞️ Автозапчасти', callback_data='avtozapchasti')
            item3 = telebot.types.InlineKeyboardButton('🏘 Недвижимость', callback_data='nedvigimost')
            item4 = telebot.types.InlineKeyboardButton('🧰 Работа', callback_data='rabota')
            item5 = telebot.types.InlineKeyboardButton('📋 Услуги', callback_data='uslugi')
            item6 = telebot.types.InlineKeyboardButton('🛼 Личные вещи', callback_data='veshi')
            item7 = telebot.types.InlineKeyboardButton('🛋 Для дома', callback_data='dom')
            item8 = telebot.types.InlineKeyboardButton('📺 Техника', callback_data='tehnika')
            item9 = telebot.types.InlineKeyboardButton('🦄 Животные', callback_data='zhivotnie')
            item10 = telebot.types.InlineKeyboardButton('⛷ Хобби и отдых', callback_data='hobbi')
            item11 = telebot.types.InlineKeyboardButton('💰 Для бизнеса', callback_data='biznes')
            item12 = telebot.types.InlineKeyboardButton('♻️ Обмен', callback_data='obmen')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

            bot.send_message(message.chat.id, 'Выберите категорию ⤵️', reply_markup=markup)
            # reply_markup=markup - Прикрепляем к сообщению
        elif message.text == '📁Мои объявления':
            bot.send_message(message.chat.id, 'Мы занимаемся разработкой данного раздела...')

        elif message.text == '🔎Поиск объявлений':
            bot.send_message(message.chat.id, 'Мы занимаемся разработкой данного раздела...')

        elif message.text == '📖 Информация':
            bot.send_message(message.chat.id,
                             'Я - бот <u><b>{1.first_name}</b></u>, созданный разработчиком '
                             '<b>Гиззатуллиным Айратом</b>'
                             ' в качестве домашнего задания семинара по "Знакомству '
                             'с языком Python" в школе GeekBrains!\n'
                             .format(message.from_user, bot.get_me()), parse_mode='html')

        elif message.text == '📲 Регистрация':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_phone = telebot.types.KeyboardButton('Номер телефона', request_contact=True)
            back = telebot.types.KeyboardButton('🔙 Назад')
            markup.add(button_phone, back)
            bot.send_message(message.chat.id, 'Нажмите кнопку -> Номер телефона ⬇️', reply_markup=markup)

        elif message.text == '🔙 Назад':
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('📢 Подать объявление')
            item2 = telebot.types.KeyboardButton('📁 Мои объявления')
            item3 = telebot.types.KeyboardButton('🔎 Поиск объявлений')
            item4 = telebot.types.KeyboardButton('📖 Информация')
            item5 = telebot.types.KeyboardButton('📲 Номер телефона')
            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id,
                             'Выберите пункт меню ⤵️'.
                             format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Извините! Я ещё не знаю такой команды...')


# Обработка нажатия кнопок ин лайновой клавиатуры категории
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'transport':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🚙 Автомобили', callback_data='avto')
                item2 = telebot.types.InlineKeyboardButton('🏍 Мотоциклы', callback_data='moto')
                item3 = telebot.types.InlineKeyboardButton('🚚 Грузовики', callback_data='gruzovik')
                item4 = telebot.types.InlineKeyboardButton('⛵️ Водный', callback_data='vodnie')
                item5 = telebot.types.InlineKeyboardButton('🛴 СИМ', callback_data='sim')
                item6 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Транспорт ⤵️', reply_markup=markup)

            elif call.data == 'avtozapchasti':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🔩 Запчасти ⚙', callback_data='zapchasti')
                item2 = telebot.types.InlineKeyboardButton('🔮 Аксессуары 📿', callback_data='aksessuari')
                item3 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Автозапчасти ⤵️', reply_markup=markup)

            elif call.data == 'nedvigimost':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🏪 Аренда 🔑', callback_data='arenda')
                item2 = telebot.types.InlineKeyboardButton('🏢 Квартиры', callback_data='kvartiri')
                item3 = telebot.types.InlineKeyboardButton('🚪 Комнаты', callback_data='komnati')
                item4 = telebot.types.InlineKeyboardButton('🏠 Дома', callback_data='doma')
                item5 = telebot.types.InlineKeyboardButton('🏕 Земля', callback_data='zemlja')
                item6 = telebot.types.InlineKeyboardButton('🔐 Гаражи', callback_data='garagi')
                item7 = telebot.types.InlineKeyboardButton('🏦 Коммерческая', callback_data='kommercheskaja')
                item8 = telebot.types.InlineKeyboardButton('🌐 Зарубежная', callback_data='zarubezhnaja')
                item9 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Недвижимость ⤵️', reply_markup=markup)

            elif call.data == 'rabota':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('📰 Вакансии', callback_data='vakansii')
                item2 = telebot.types.InlineKeyboardButton('🔖 Резюме', callback_data='rezume')
                item3 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Работа ⤵️', reply_markup=markup)

            elif call.data == 'uslugi':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('📣 Предложить услугу', callback_data='predlozhenie')
                item2 = telebot.types.InlineKeyboardButton('🛎 Заказать услугу', callback_data='zakaz_uslug')
                item3 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Услуги ⤵️', reply_markup=markup)

            elif call.data == 'veshi':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🥼 Одежда', callback_data='odezhda')
                item2 = telebot.types.InlineKeyboardButton('👟 Обувь', callback_data='obuv')
                item3 = telebot.types.InlineKeyboardButton('👼🏻 Детские', callback_data='detskie')
                item4 = telebot.types.InlineKeyboardButton('🧸 Игрушки', callback_data='igrushki')
                item5 = telebot.types.InlineKeyboardButton('⌚️ Часы, украшения 💍', callback_data='chasi_ukas')
                item6 = telebot.types.InlineKeyboardButton('🧼 Уход', callback_data='uhod')
                item7 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6, item7)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Личные вещи ⤵️', reply_markup=markup)

            elif call.data == 'dom':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🪑 Мебель', callback_data='mebel')
                item2 = telebot.types.InlineKeyboardButton('🍶 Посуда', callback_data='posuda')
                item3 = telebot.types.InlineKeyboardButton('🥭 Продукты', callback_data='produktie')
                item4 = telebot.types.InlineKeyboardButton('🪴 Растения', callback_data='rastenia')
                item5 = telebot.types.InlineKeyboardButton('🧱 Стройматериалы', callback_data='stroimaterial')
                item6 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Для дома ⤵️', reply_markup=markup)

            elif call.data == 'tehnika':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🎥 Аудио - Видео', callback_data='audio_video')
                item2 = telebot.types.InlineKeyboardButton('🎮 Приставки', callback_data='pristavki')
                item3 = telebot.types.InlineKeyboardButton('💻 Компьютеры', callback_data='komputeri')
                item4 = telebot.types.InlineKeyboardButton('🖨 Оргтехника', callback_data='orgtehnika')
                item5 = telebot.types.InlineKeyboardButton('📱 Телефоны', callback_data='telefoni')
                item6 = telebot.types.InlineKeyboardButton('🖥 Планшеты', callback_data='plansheti')
                item7 = telebot.types.InlineKeyboardButton('📷 Фототехника', callback_data='fototehnika')
                item8 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Бытовая техника ⤵️', reply_markup=markup)

            elif call.data == 'zhivotnie':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🦮 Собаки', callback_data='sobaki')
                item2 = telebot.types.InlineKeyboardButton('🐈 Кошки', callback_data='koshki')
                item3 = telebot.types.InlineKeyboardButton('🦜 Птицы', callback_data='ptici')
                item4 = telebot.types.InlineKeyboardButton('🐠 Аквариум', callback_data='akvarium')
                item5 = telebot.types.InlineKeyboardButton('🦴 Товары животным', callback_data='tovari_zhivotnim')
                item6 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Животные ⤵️', reply_markup=markup)

            elif call.data == 'hobbi':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🎿 Туризм', callback_data='turizm')
                item2 = telebot.types.InlineKeyboardButton('🚴 ‍Велосипеды', callback_data='velosipedi')
                item3 = telebot.types.InlineKeyboardButton('📚 Книги', callback_data='knigi')
                item4 = telebot.types.InlineKeyboardButton('🪙 Коллекционирование', callback_data='kollekcioner')
                item5 = telebot.types.InlineKeyboardButton('🎼 Музыка', callback_data='muzika')
                item6 = telebot.types.InlineKeyboardButton('🎣 Охота и Рыбалка', callback_data='ohota_ribalka')
                item7 = telebot.types.InlineKeyboardButton('🏋️‍Спортивное', callback_data='sportivnoe')
                item8 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Хобби и отдых ⤵️', reply_markup=markup)

            elif call.data == 'biznes':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🛍 Готовый бизнес', callback_data='gotovi_biznes')
                item2 = telebot.types.InlineKeyboardButton('🛒 Оборудование', callback_data='oborudovanie_biz')
                item3 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Для бизнеса ⤵️', reply_markup=markup)

            elif call.data == 'obmen':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🎅🏻 Дарение', callback_data='darenie')
                item2 = telebot.types.InlineKeyboardButton('🗣 Ищу тебя', callback_data='ishu_tebya')
                item3 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3)
                bot.send_message(call.message.chat.id, 'Выберите подкатегорию *Обмен ⤵️', reply_markup=markup)

            # Кнопка назад в инлайн клавиатуре
            elif call.data == 'back':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🚗 Транспорт', callback_data='transport')
                item2 = telebot.types.InlineKeyboardButton('⚙️ Автозапчасти', callback_data='avtozapchasti')
                item3 = telebot.types.InlineKeyboardButton('🏘 Недвижимость', callback_data='nedvigimost')
                item4 = telebot.types.InlineKeyboardButton('🧰 Работа', callback_data='rabota')
                item5 = telebot.types.InlineKeyboardButton('📋 Услуги', callback_data='uslugi')
                item6 = telebot.types.InlineKeyboardButton('🛼 Личные вещи', callback_data='veshi')
                item7 = telebot.types.InlineKeyboardButton('🛋 Для дома', callback_data='dom')
                item8 = telebot.types.InlineKeyboardButton('📺 Техника', callback_data='tehnika')
                item9 = telebot.types.InlineKeyboardButton('🦄 Животные', callback_data='zhivotnie')
                item10 = telebot.types.InlineKeyboardButton('⛷ Хобби и отдых', callback_data='hobbi')
                item11 = telebot.types.InlineKeyboardButton('💰 Для бизнеса', callback_data='biznes')
                item12 = telebot.types.InlineKeyboardButton('♻️ Обмен', callback_data='obmen')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
                bot.send_message(call.message.chat.id, 'Выберите категорию ⤵️', reply_markup=markup)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Транспорт
            elif call.data == 'avto':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'moto':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'gruzovik':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'vodnie':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'sim':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Автозапчасти
            elif call.data == 'zapchasti':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'aksessuari':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Недвижимость
            elif call.data == 'arenda':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'kvartiri':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'komnati':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'doma':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'zemlja':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'garagi':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'kommercheskaja':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'zarubezhnaja':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Работа
            elif call.data == 'vakansii':  # Ищу сотрудника
                # ----------------------------------------------------------------------
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'rezume':  # Ищу работу
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Услуги
            elif call.data == 'predlozhenie':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'zakaz_uslug':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Личные вещи
            elif call.data == 'odezhda':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'obuv':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'detskie':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'igrushki':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'chasi_ukas':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'uhod':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Для дома
            elif call.data == 'mebel':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'posuda':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'produktie':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'rastenia':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'stroimaterial':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Техника
            elif call.data == 'audio_video':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'pristavki':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'komputeri':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'orgtehnika':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'telefoni':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'plansheti':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'fototehnika':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Животные
            elif call.data == 'sobaki':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'koshki':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'ptici':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'akvarium':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'tovari_zhivotnim':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Хобби и отдых
            elif call.data == 'turizm':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'velosipedi':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'knigi':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'kollekcioner':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'muzika':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'ohota_ribalka':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'sportivnoe':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Для бизнеса
            elif call.data == 'gotovi_biznes':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'oborudovanie_biz':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Обмен
            elif call.data == 'darenie':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)
            elif call.data == 'ishu_tebya':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)

    except Exception as e:
        print(repr(e))


# Для постоянной работы бота и отслеживания поступающих сообщений
bot.polling(none_stop=True)
