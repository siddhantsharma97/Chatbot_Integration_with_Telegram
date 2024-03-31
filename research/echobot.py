from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    await message.reply("HI I am an Echobot powered by telegram")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)