from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.user.buttons import languages

languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=languages[0])
        ],
        [
            KeyboardButton(text=languages[1])
        ],
        [
            KeyboardButton(text=languages[2])
        ],
        [
            KeyboardButton(text=languages[3])
        ],
        [
            KeyboardButton(text=languages[4])
        ],
        [
            KeyboardButton(text=languages[5])
        ],
        [
            KeyboardButton(text=languages[6])
        ],
        [
            KeyboardButton(text=languages[7])
        ],
        [
            KeyboardButton(text=languages[8])
        ],
        [
            KeyboardButton(text=languages[9])
        ],
    ],
    resize_keyboard=True
)