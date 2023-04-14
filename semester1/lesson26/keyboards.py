from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import films

film_choice = InlineKeyboardMarkup()
for film in films:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choice.add(button)
#     inline_keyboard=[
#         [InlineKeyboardButton(text='Джон Уік 4 (16+)',callback_data='Джон Уік 4 (16+)')],
#         [InlineKeyboardButton(text='Підземелля і дракони: Честь злодіїв (12+)', callback_data='Підземелля і дракони')],
#         [InlineKeyboardButton(text='Екзорцист Ватикану (16+)', callback_data= 'Екзорцист Ватикану (16+)')]
#     ]
# )