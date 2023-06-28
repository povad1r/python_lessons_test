from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os 
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from keyboards import *
from parse_news import parse_default_news, parse_economic_news

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer('Привіт! Щоб переглянути новини натисни на кнопку:', reply_markup=news)

@dp.message_handler()
async def get_news(message: types.Message, state: FSMContext):
    if message.text == 'Політичні новини':
        await message.answer('Новини були отримані. Обирай їх за допомогою кнопки:', reply_markup=choice)
        await state.set_state('read_default_news')
    elif message.text == 'Економічні новини':
        await message.answer('Новини були отримані. Обирай їх за допомогою кнопки:', reply_markup=choice)
        await state.set_state('read_economic_news')

@dp.callback_query_handler(state='*', text='0')
async def end_reading(callback: types.CallbackQuery, state:FSMContext):
    await callback.answer('Перегляд завершено. Щоб прочитати новини ще раз - напишіть /start')
    await state.finish()


@dp.callback_query_handler(state='read_default_news')
async def read_default_news(callback: types.CallbackQuery, state: FSMContext):
    news = parse_default_news()
    if callback.data == '1':
        await callback.message.answer(
            f'{news[0]["title"]}\n'
            f'{news[0]["text"]}\n'
            f'Джерело: {news[0]["link"]}'
            f' Чи бажаєте прочитати щось інше?', reply_markup=choice
        )
    elif callback.data == '2':
        await callback.message.answer(
            f'{news[1]["title"]}\n'
            f'{news[1]["text"]}\n'
            f'Джерело: {news[1]["link"]}'
            f' Чи бажаєте прочитати щось інше?', reply_markup=choice
        )

@dp.callback_query_handler(state='read_economic_news')
async def read_economic_news(callback: types.CallbackQuery, state: FSMContext):
    news = parse_economic_news()
    if callback.data == '1':
        await callback.message.answer(
            f'{news[0]["title"]}\n'
            f'{news[0]["text"]}\n'
            f'Джерело: {news[0]["link"]}'
            f' Чи бажаєте прочитати щось інше?', reply_markup=choice
        )
    elif callback.data == '2':
        await callback.message.answer(
            f'{news[1]["title"]}\n'
            f'{news[1]["text"]}\n'
            f'Джерело: {news[1]["link"]}'
            f' Чи бажаєте прочитати щось інше?', reply_markup=choice
        )


if __name__ == '__main__':
    executor.start_polling(dp)