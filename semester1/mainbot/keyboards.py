from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from func import get_content
content = get_content()
game_choice = InlineKeyboardMarkup()
for match in content:
        response = (f"{match['team_1']} - {match['team_2']}")
        button = InlineKeyboardButton(text=response, callback_data=response)
        game_choice.add(button)

    