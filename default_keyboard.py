from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button2 = KeyboardButton(text="About me")
    button3 = KeyboardButton(text="Media url")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button2, button3]
        ],
        resize_keyboard=True
    )
    return rkm



