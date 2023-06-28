from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

red = KeyboardButton(text='Червоний🔴')
yellow = KeyboardButton(text='Жовтий🟡')
green = KeyboardButton(text='Зелений🟢')
traffic_off = KeyboardButton(text='Вимкнути')

lightsall = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(red, yellow, green)
redkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(red)
yellowkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(yellow)
greenkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(green)
traffic_off_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(traffic_off)

request_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(request_contact=True, text='Share my contact'))