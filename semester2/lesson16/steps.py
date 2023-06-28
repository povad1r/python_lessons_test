from aiogram.dispatcher.filters.state import StatesGroup, State


class TrafficLights(StatesGroup):
    StateOn = State()
    StateRed = State()
    StateYellow = State()
    StateGreen = State()
    StateOff = State()

class Flow(StatesGroup):
    RegisterState = State()