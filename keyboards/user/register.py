from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.user.buttons import get_lang_id, volunteer, consumer, sendContact, sendLocation

def send_register():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Registration")
            ]
        ],
        resize_keyboard=True
    )
    
    return markup

def send_usertypes(lang):
    id = get_lang_id(lang)
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=volunteer[id]),
                KeyboardButton(text=consumer[id])
            ]
        ],
        resize_keyboard=True
    )
    
    return markup

def send_contact(lang):
    id = get_lang_id(lang)
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=sendContact[id], request_contact=True)
            ]
        ],
        resize_keyboard=True
    )

    return markup

def send_location(lang):
    id = get_lang_id(lang)
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=sendLocation[id], request_location=True)
            ]
        ],
        resize_keyboard=True
    )

    return markup