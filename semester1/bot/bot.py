import logging
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)
TOKEN = '6231537734:AAH7DYsOj_QATaRqdRYDxQLdi_B2zgJ7V_Y'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Hello! I am echo bot.')
    await message.answer('Hello! I am echo bot.')

@dp.message_handler()
async def echo(message: types.Message):
    user_info = {
        "name": message.from_user.first_name,
        "surname": message.from_user.last_name,
        "username": message.from_user.username,
        "user_id": message.from_user.id
    }
    await message.answer(f'First name: {user_info["name"]}\nLast name: {user_info["surname"]}\nUsername: {user_info["username"]}\nUser_id: {user_info["user_id"]}')
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp) 