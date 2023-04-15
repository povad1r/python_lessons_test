import logging
from aiogram import Bot, Dispatcher, executor, types
from func import get_content, source
from keyboards import game_choice
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Здравствуйте!\nЭтот бот отслеживает ближайшие киберспортивные матчи по дисциплине Dota 2.\nВы можете посмотреть список предстоящих матчей, используя команду /matches.\nДля каждой игры вы можете узнать учавствующие команды, время начала, текущий счёт и турнир, в рамках которого провидится встреча.', reply_markup=game_choice)


@dp.message_handler(commands='matches')
async def matches(message: types.Message):
    content = get_content()
    for match in content:
        response = (f"Tournament: {match['tournament']}\nMatch time: {match['time']}\n{match['team_1']} - {match['team_2']}")
        await message.answer((response))


if __name__ == '__main__':
    executor.start_polling(dp)
