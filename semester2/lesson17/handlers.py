import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from steps import CardProcess
from keyboards import operation_kb

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

pincode = '1111'
balance = 10000


@dp.message_handler(commands='start', state='*')
async def start_process(message: types.Message):
    await message.answer('Привіт! Я бот - банкомат. Для продовження введи номер картки.')
    await CardProcess.CardNumber.set()


@dp.message_handler(content_types='text', state=CardProcess.CardNumber)
async def get_card_number(message: types.Message):
    await message.answer(f'Номер вашої картки - {message.text}, тепер введіть пінкод!')
    await CardProcess.Pincode.set()


@dp.message_handler(content_types='text', state=CardProcess.Pincode)
async def get_pincode(message: types.Message):
    global pincode
    if pincode == message.text:
        await message.answer(f'Ваш пін-код - {message.text}, тепер оберіть операцію', reply_markup=operation_kb)
        await CardProcess.Choose_button.set()
    else:
        await message.answer(f'Ви ввели неправильний пінкод. Спробуйте ще раз')


@dp.callback_query_handler(state=CardProcess.Choose_button)
async def process_operation_choose(callback_query: types.CallbackQuery):
    print(callback_query.data)
    global balance
    if callback_query.data == 'Withdraw':
        await CardProcess.FInish_withdraw.set()
        await callback_query.message.answer(f'Ми можемо видати вам {balance} грн')
    else:
        await CardProcess.Balance.set()
        await callback_query.message.answer(f'Ваш баланс - {balance}')


@dp.message_handler(state=CardProcess.FInish_withdraw)
async def finish(message: types.Message):
    await message.answer(f'Дякую за співпрацю! Для повторної операції напишіть /start')
    await CardProcess.StateOn.set()


if __name__ == '__main__':
    executor.start_polling(dp)
