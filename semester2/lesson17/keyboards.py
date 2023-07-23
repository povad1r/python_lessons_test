from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

operation_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зняти готівку', callback_data='Withdraw'),
            InlineKeyboardButton(text='Баланс', callback_data='Balance')
        ]
    ]
)
