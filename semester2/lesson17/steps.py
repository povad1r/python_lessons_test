from aiogram.dispatcher.filters.state import StatesGroup, State


class CardProcess(StatesGroup):
    StateOn = State()
    CardNumber = State()
    Pincode = State()
    Withdraw = State()
    Balance = State()
    FInish_withdraw = State()
    Balance_finish = State()
    Choose_button = State()