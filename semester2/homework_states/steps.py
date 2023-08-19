from aiogram.dispatcher.filters.state import StatesGroup, State


class registration(StatesGroup):
    Username = State()
    Password = State()
    Email = State()
