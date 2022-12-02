import logging
import config
from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Инициализируем соединение с базой данных
db = SQLighter('db.db')


# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если пользователя нет, то создаем запись
        db.add_subscriber(message.from_user.id)
    else:
        # если пользователь есть в БД, то обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)

    await message.answer('Вы успешно подписались')


# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если пользователя нет, то добавляем его с неактивной подпиской
        db.add_subscriber(message.from_user.id, False)
        await message.answer('Вы и так не подписаны.')
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.add_subscriber(message.from_user.id, False)
        await message.answer('Вы успешно отписаны от рассылки.')


# # Эхо
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
