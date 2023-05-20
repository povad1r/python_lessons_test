import logging

from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os 
from dotenv import load_dotenv
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from parse_weather import parse_weather
load_dotenv()

TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(text='Hello I am weather bot!')    

# @dp.message_handler(text='Hello')
# async def greetings(message:types.Message):
#     name = message.from_user.full_name
#     await message.answer(f'Hello {name}.\nMy name is Geralt')

@dp.message_handler(commands=['Weather'])
async def weather(message:types.Message):
    await message.answer(f'Enter your city')
    

@dp.message_handler()
async def handle_city(message: types.Message):
    city = message.text
    weather_data = parse_weather(city)
    weather = weather_data['main']
    precipitation = weather_data['weather'][0]['main'] 
    humidity = weather['humidity']
    pressure = weather['pressure'] *  0.0075
    temp = weather['temp'] - 273.15
    await message.answer(f"Weather in {city}:"
                        f"\nTemperature: {round(temp)}°C"
                        f"\nHumidity: {humidity}%"
                        f"\nSky: {precipitation}"
                        f"\nPressure: {round(pressure, 2)}")


@dp.message_handler(commands=['info'])
async def user_info(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    telegram_id = message.from_id
    lang = message.from_user.language_code

    await message.answer(f'ID: {telegram_id}\nFIRST_NAME: {first_name}\nLAST_NAME: {last_name}\nUSERNAME: @{username}\nLANGUAGE: {lang}')



if __name__ == '__main__':
    executor.start_polling(dp)