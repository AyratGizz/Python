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
    item1 = telebot.types.KeyboardButton('📢 Разместить свои услуги')
    item2 = telebot.types.KeyboardButton('🔎 Найти услугу')
    item3 = telebot.types.KeyboardButton('📁 Мои размещенные услуги')
    item4 = telebot.types.KeyboardButton('📖 Информация')
    item5 = telebot.types.KeyboardButton('📲 Регистрация')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     'Добро пожаловать, <b>{0.first_name}</b>!\n'
                     'Вы находитесь в боте для размещения и поиска услуг\n'
                     'в жилищном комплексе "Царёво Village"'
                     'Выберите действие нажатием кнопки ⤵️'.
                     format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)  #
    # reply_markup - прикрепление кнопки к сообщению


# Считывание введенного текста (нажатой кнопки, которая передаёт текст)
@bot.message_handler(content_types=['text'])
def send_text(message):
    # if message.text == ''
    # bot.send_message(message.chat.id, message.text) - пересылает в ответ то же сообщение (попугай)
    if message.chat.type == 'private':
        if message.text == '📢 Разместить свои услуги':
            # bot.send_message(message.chat.id, str(random.randint(1, 1000)))
            # Ин лайновая клавиатура
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton('🚚 Транспорт, перевозки', callback_data='perevozki')
            item2 = telebot.types.InlineKeyboardButton('🔧 Ремонт и отделка', callback_data='remont')
            item3 = telebot.types.InlineKeyboardButton('🧱 Строительство', callback_data='stroika')
            item4 = telebot.types.InlineKeyboardButton('🪪 Мастер на час', callback_data='master_chas')
            item5 = telebot.types.InlineKeyboardButton('🪚 Сад, благоустройство', callback_data='sadovod')
            item6 = telebot.types.InlineKeyboardButton('🧴 Красота, здоровье', callback_data='krasota_zdorovie')
            item7 = telebot.types.InlineKeyboardButton('🛠 Ремонт техники', callback_data='remont_tehniki')
            item8 = telebot.types.InlineKeyboardButton('🪜 Установка техники', callback_data='ustanovka_tehniki')
            item9 = telebot.types.InlineKeyboardButton('⛽️ Оборудование, производство', callback_data='proizvodstvo')
            item10 = telebot.types.InlineKeyboardButton('👨🏻‍🎓 Обучение, курсы', callback_data='obuchenie_kursi')
            item11 = telebot.types.InlineKeyboardButton('📒 Деловые услуги', callback_data='delovie_uslugi')
            item12 = telebot.types.InlineKeyboardButton('📡 IT, интернет, телеком', callback_data='it_internet')
            item13 = telebot.types.InlineKeyboardButton('📣 Реклама, полиграфия', callback_data='reklama_poligraph')
            item14 = telebot.types.InlineKeyboardButton('🧹 Уборка', callback_data='uborka')
            item15 = telebot.types.InlineKeyboardButton('🪡 Бытовые услуги', callback_data='bitovie_uslugi')
            item16 = telebot.types.InlineKeyboardButton('🎉 Праздники, мероприятия', callback_data='prazdniki')
            item17 = telebot.types.InlineKeyboardButton('🛒 Доставка еды и продуктов', callback_data='dostavka_edi')
            item18 = telebot.types.InlineKeyboardButton('🎥 Фото и видеосъёмка', callback_data='foto_video')
            item19 = telebot.types.InlineKeyboardButton('🧕🏻 Няни, сиделки', callback_data='nani_sidelki')
            item20 = telebot.types.InlineKeyboardButton('🦮 Уход за животными', callback_data='uhod_zhivotnie')
            item21 = telebot.types.InlineKeyboardButton('🖼 Искусство', callback_data='iskusstvo')
            item22 = telebot.types.InlineKeyboardButton('👮🏻‍♂️ Охрана, безопасность',
                                                        callback_data='ohrana_bezopasnost')
            item23 = telebot.types.InlineKeyboardButton('🛵 Доставка, курьеры', callback_data='dostavka_kureri')
            item24 = telebot.types.InlineKeyboardButton('📝 Другое', callback_data='drugoe')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                       item13, item14, item15, item16, item17, item18, item19, item20, item21, item22,
                       item23, item24)

            bot.send_message(message.chat.id, 'Выберите категорию услуг ⤵️', reply_markup=markup)
            # reply_markup=markup - Прикрепляем к сообщению
        elif message.text == '🔎 Найти услугу':
            bot.send_message(message.chat.id, 'Мы занимаемся разработкой данного раздела...')

        elif message.text == '📁 Мои размещенные услуги':
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
        else:
            bot.send_message(message.chat.id, 'Извините! Я не знаю такой команды...')


# Обработка нажатия кнопок ин лайновой клавиатуры категории
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'perevozki':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🚙 Автосервис 🛠', callback_data='avtoservis')
                item2 = telebot.types.InlineKeyboardButton('🫧 Автомойка, детейлинг', callback_data='avtomoiki')
                item3 = telebot.types.InlineKeyboardButton('🔑 Аренда авто 🏎', callback_data='arenda_avto')
                item4 = telebot.types.InlineKeyboardButton('🚛 Грузоперевозки', callback_data='gruzoperevozki')
                item5 = telebot.types.InlineKeyboardButton('🏋🏻‍♂️ Грузчики', callback_data='gruzhiki')
                item6 = telebot.types.InlineKeyboardButton('📦 Переезды', callback_data='pereezdi')
                item7 = telebot.types.InlineKeyboardButton('🚜 Спецтехника', callback_data='spec_tehnika')
                item8 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Выберите подкатегорию *Транспорт, перевозки ⤵️', reply_markup=markup)


            elif call.data == 'remont':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🧱 Ремонт квартир и домов', callback_data='remont_kvartir')
                item2 = telebot.types.InlineKeyboardButton('🚰 Сантехника', callback_data='santehnika')
                item3 = telebot.types.InlineKeyboardButton('🔌 Электрика', callback_data='elektrika')
                item4 = telebot.types.InlineKeyboardButton('🪛 Сборка и ремонт мебели', callback_data='remont_mebeli')
                item5 = telebot.types.InlineKeyboardButton('🪟 Остекление', callback_data='osteklenie')
                item6 = telebot.types.InlineKeyboardButton('🎨 Обои и малярные работы', callback_data='oboi_maljar')
                item7 = telebot.types.InlineKeyboardButton('☔️ Потолки', callback_data='potolki')
                item8 = telebot.types.InlineKeyboardButton('🥌 Полы', callback_data='poli')
                item9 = telebot.types.InlineKeyboardButton('🥽 Штукатурные работы', callback_data='stukaturnie_raboti')
                item10 = telebot.types.InlineKeyboardButton('🚪 Двери', callback_data='dveri')
                item11 = telebot.types.InlineKeyboardButton('🧩 Плиточные работы', callback_data='plitka_raboti')
                item12 = telebot.types.InlineKeyboardButton('🪚 Столярка - плотник', callback_data='stoljarka_plotnik')
                item13 = telebot.types.InlineKeyboardButton('⛏ Гипсокартонные работы',
                                                            callback_data='gipsokarton_raboti')
                item14 = telebot.types.InlineKeyboardButton('🪜 Высотные работы', callback_data='rabota_na_visote')
                item15 = telebot.types.InlineKeyboardButton('⛓ Металлоконструкции и ковка', callback_data='metal_kovka')
                item16 = telebot.types.InlineKeyboardButton('🛡 Изоляция', callback_data='izoljacia')
                item17 = telebot.types.InlineKeyboardButton('🖇 Ремонт офиса', callback_data='remont_ofisa')
                item18 = telebot.types.InlineKeyboardButton('🌪 Вентиляция', callback_data='ventiljacia')
                item19 = telebot.types.InlineKeyboardButton('📓 Другое', callback_data='drugoe_remont')
                item20 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                           item13, item14, item15, item16, item17, item18, item19, item20)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Выберите подкатегорию *Ремонт и отделка ⤵️', reply_markup=markup)

            elif call.data == 'stroika':
                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('🏚 Строительство бань, саун',
                                                           callback_data='stroika_bani')
                item2 = telebot.types.InlineKeyboardButton('🏘 Строительство домов, коттеджей',
                                                           callback_data='stroika_doma')
                item3 = telebot.types.InlineKeyboardButton('👷🏻‍♂️ Отделка деревянных домов, бань, саун',
                                                           callback_data='otdelka_domov_saun')
                item4 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2, item3, item4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Выберите подкатегорию *Строительство ⤵️', reply_markup=markup)

            elif call.data == 'master_chas':
                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('Кнопка',
                                                           callback_data='stroika_bani')
                item2 = telebot.types.InlineKeyboardButton('🔙 Назад', callback_data='back')
                markup.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Оказание услуг осуществляется только в пределах '
                                           'ЖК "Царёво Village"', reply_markup=markup)

                # -----------------------------------------------------------------------------

                item4 = telebot.types.InlineKeyboardButton('🪪 Мастер на час', callback_data='master_chas')
                item5 = telebot.types.InlineKeyboardButton('🪚 Сад, благоустройство', callback_data='sadovod')
                item6 = telebot.types.InlineKeyboardButton('🧴 Красота, здоровье', callback_data='krasota_zdorovie')
                item7 = telebot.types.InlineKeyboardButton('🛠 Ремонт техники', callback_data='remont_tehniki')
                item8 = telebot.types.InlineKeyboardButton('🪜 Установка техники', callback_data='ustanovka_tehniki')
                item9 = telebot.types.InlineKeyboardButton('⛽️ Оборудование, производство',
                                                           callback_data='proizvodstvo')
                item10 = telebot.types.InlineKeyboardButton('👨🏻‍🎓 Обучение, курсы', callback_data='obuchenie_kursi')
                item11 = telebot.types.InlineKeyboardButton('📒 Деловые услуги', callback_data='delovie_uslugi')
                item12 = telebot.types.InlineKeyboardButton('📡 IT, интернет, телеком', callback_data='it_internet')
                item13 = telebot.types.InlineKeyboardButton('📣 Реклама, полиграфия', callback_data='reklama_poligraph')
                item14 = telebot.types.InlineKeyboardButton('🧹 Уборка', callback_data='uborka')
                item15 = telebot.types.InlineKeyboardButton('🪡 Бытовые услуги', callback_data='bitovie_uslugi')
                item16 = telebot.types.InlineKeyboardButton('🎉 Праздники, мероприятия', callback_data='prazdniki')
                item17 = telebot.types.InlineKeyboardButton('🛒 Доставка еды и продуктов', callback_data='dostavka_edi')
                item18 = telebot.types.InlineKeyboardButton('🎥 Фото и видеосъёмка', callback_data='foto_video')
                item19 = telebot.types.InlineKeyboardButton('🧕🏻 Няни, сиделки', callback_data='nani_sidelki')
                item20 = telebot.types.InlineKeyboardButton('🦮 Уход за животными', callback_data='uhod_zhivotnie')
                item21 = telebot.types.InlineKeyboardButton('🖼 Искусство', callback_data='iskusstvo')
                item22 = telebot.types.InlineKeyboardButton('👮🏻‍♂️ Охрана, безопасность',
                                                            callback_data='ohrana_bezopasnost')
                item23 = telebot.types.InlineKeyboardButton('🛵 Доставка, курьеры', callback_data='dostavka_kureri')
                item24 = telebot.types.InlineKeyboardButton('📝 Другое', callback_data='drugoe')
            # Кнопка назад в инлайн клавиатуре
            elif call.data == 'back':
                markup = telebot.types.InlineKeyboardMarkup(row_width=2)
                item1 = telebot.types.InlineKeyboardButton('🚚 Транспорт, перевозки', callback_data='perevozki')
                item2 = telebot.types.InlineKeyboardButton('🔧 Ремонт и отделка', callback_data='remont')
                item3 = telebot.types.InlineKeyboardButton('🧱 Строительство', callback_data='stroika')
                item4 = telebot.types.InlineKeyboardButton('🪪 Мастер на час', callback_data='master_chas')
                item5 = telebot.types.InlineKeyboardButton('🪚 Сад, благоустройство', callback_data='sadovod')
                item6 = telebot.types.InlineKeyboardButton('🧴 Красота, здоровье', callback_data='krasota_zdorovie')
                item7 = telebot.types.InlineKeyboardButton('🛠 Ремонт техники', callback_data='remont_tehniki')
                item8 = telebot.types.InlineKeyboardButton('🪜 Установка техники', callback_data='ustanovka_tehniki')
                item9 = telebot.types.InlineKeyboardButton('⛽️ Оборудование, производство',
                                                           callback_data='proizvodstvo')
                item10 = telebot.types.InlineKeyboardButton('👨🏻‍🎓 Обучение, курсы', callback_data='obuchenie_kursi')
                item11 = telebot.types.InlineKeyboardButton('📒 Деловые услуги', callback_data='delovie_uslugi')
                item12 = telebot.types.InlineKeyboardButton('📡 IT, интернет, телеком', callback_data='it_internet')
                item13 = telebot.types.InlineKeyboardButton('📣 Реклама, полиграфия', callback_data='reklama_poligraph')
                item14 = telebot.types.InlineKeyboardButton('🧹 Уборка', callback_data='uborka')
                item15 = telebot.types.InlineKeyboardButton('🪡 Бытовые услуги', callback_data='bitovie_uslugi')
                item16 = telebot.types.InlineKeyboardButton('🎉 Праздники, мероприятия', callback_data='prazdniki')
                item17 = telebot.types.InlineKeyboardButton('🛒 Доставка еды и продуктов', callback_data='dostavka_edi')
                item18 = telebot.types.InlineKeyboardButton('🎥 Фото и видеосъёмка', callback_data='foto_video')
                item19 = telebot.types.InlineKeyboardButton('🧕🏻 Няни, сиделки', callback_data='nani_sidelki')
                item20 = telebot.types.InlineKeyboardButton('🦮 Уход за животными', callback_data='uhod_zhivotnie')
                item21 = telebot.types.InlineKeyboardButton('🖼 Искусство', callback_data='iskusstvo')
                item22 = telebot.types.InlineKeyboardButton('🚔 Охрана, безопасность',
                                                            callback_data='ohrana_bezopasnost')
                item23 = telebot.types.InlineKeyboardButton('🛵 Доставка, курьеры', callback_data='dostavka_kureri')
                item24 = telebot.types.InlineKeyboardButton('📝 Другое', callback_data='drugoe')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12,
                           item13, item14, item15, item16, item17, item18, item19, item20, item21, item22,
                           item23, item24)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Выберите категорию услуг ⤵️', reply_markup=markup)

            # Обработка нажатия кнопок ин лайновой клавиатуры подкатегории Транспорт
            elif call.data == 'avto':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Раздел на разработке...', reply_markup=None)


    except Exception as e:
        print(repr(e))


# Для постоянной работы бота и отслеживания поступающих сообщений
bot.polling(none_stop=True)
