import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from steps import *

TOKEN='6510906460:AAEXXm8v5gB1uxLdEq0RTfs4ZI65FdbYE50'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database()

@dp.message_handler(state=Registration.set_name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('Nice!\nNow enter your age.')
    await Registration.set_age.set()




if __name__ == '__main__':
    executor.start_polling(dp)