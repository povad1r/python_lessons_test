import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from steps import registration
from aiogram.dispatcher.filters.state import State, StatesGroup
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# @dp.message_handler(commands='start', state='*')
# async def start_registration(message: types.Message):
#     await message.answer('Привіт! Для реєстрації напиши /registration.')
#     await registration.Username.set()

# @dp.message_handler(commands='registration', state=registration.Username)
# async def username(message: types.Message):
#     await message.answer('Введи юзернейм!')
#     username = message.text
#     print(username)
#     await registration.Password.set()

# @dp.message_handler(content_types='text', state=registration.Password)
# async def password(message: types.Message):
#     await message.answer('Введи пароль!')
#     password = message.text
#     print(password)
#     await registration.Email.set()

# @dp.message_handler(content_types='text', state=registration.Password)
# async def password(message: types.Message):
#     await message.answer('Введи Email!')
#     email = message.text
#     print(email)
#     await registration.Username.set()

# if __name__ == '__main__':
#     executor.start_polling(dp)

class RegistrationForm(StatesGroup):
    Username = State()
    Password = State()
    Email = State()
    Save = State()

@dp.message_handler(commands='start', state='*')
async def start_registration(message: types.Message):
    await message.answer('Привіт! Я бот для реєстрації. Введи свій юзернейм')
    await RegistrationForm.Username.set()

@dp.message_handler(state=RegistrationForm.Username)
async def username(message: types.Message, state: RegistrationForm):
    await message.answer('Введи пароль!')
    async with state.proxy() as data:
        data['username'] = message.text
    await RegistrationForm.Password.set()

@dp.message_handler(state=RegistrationForm.Password)
async def password(message: types.Message, state: RegistrationForm):
    async with state.proxy() as data:
        data['password'] = message.text
    await message.answer('Введи email!')
    await RegistrationForm.Email.set()

@dp.message_handler(state=RegistrationForm.Email)
async def email(message: types.Message, state: RegistrationForm):
    async with state.proxy() as data:
        data['email'] = message.text
    await RegistrationForm.Save.set()    

@dp.message_handler(state=RegistrationForm.Save)
async def save_data(message: types.Message, state: RegistrationForm):
    async with state.proxy() as data:
        data['save'] = message.text
        with open("C:/Users/User/Desktop/GoITeens/semester2/homework_states/users.txt", 'a') as file:
            file.write(f"Username: {data['username']}, Password: {data['password']}, Email: {data['email']}\n")
    await message.answer('Дякую за реєстрацію! Ваші дані збережено.')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)