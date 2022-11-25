import logging
import telebot
import config
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await  message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

# bot = telebot.TeleBot(TOKEN)

# Для постоянной работы бота и отслеживания поступающих сообщений
# bot.polling(none_stop=True)
