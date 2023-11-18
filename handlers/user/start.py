from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart

from states.userData import Register
from data.languagePreset import languages as lang
from data.languagePreset import general
from loader import db
from keyboards.user.languages import languages
from keyboards.user import buttons, register, menu
from utils.getLocation import get_location

router = Router()

@router.message(CommandStart())
async def welcome(message: types.Message, state: FSMContext):
    if db.add_user(message):
        await message.answer(
            text=general["start"],
            reply_markup=languages
        )
        await state.set_state(Register.choosing_language)
    else:
        await message.answer(
            text=lang[db.get_user_language(message.chat.id)]["secondStart"],
            reply_markup=menu.send_menu(message.from_user.id, db.get_user_language(message.from_user.id))
        )
        await state.clear()

@router.message(Register.choosing_language, F.text.in_(buttons.languages))
async def choose_language(message: types.Message, state: FSMContext):
    lg = ""
    match(message.text):
        case "Kazakh":
            lg = "kz"
        case "English":
            lg = "en"
        case "Russian":
            lg = "ru"
        case "Spanish":
            lg = "es"
        case "Polish":
            lg = "pl"
        case "Azerbaijani":
            lg = "az"
        case "Turkish":
            lg = "tr"
        case "Chinese":
            lg = "zh"
        case "Tajik":
            lg = "tg"
        case "Uzbek":
            lg = "uz"
        case _:
            message.answer(general["incorrectAnswer"])
            return 0
    await message.answer(
        text=lang[lg]["chooseUserType"],
        reply_markup=register.send_usertypes(lg)
    )
    db.set_user_language(message.from_user.id, lg)

    await state.set_state(Register.choosing_user_type)

@router.message(Register.choosing_user_type, F.text.in_(buttons.volunteer + buttons.consumer))
async def choose_user_type(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    if message.text in buttons.volunteer:
        db.set_user_type(message.from_user.id, "volunteer")
    elif message.text in buttons.consumer:
        db.set_user_type(message.from_user.id, "consumer")
    await message.answer(
        text=lang[lg]["writeName"],
        reply_markup=ReplyKeyboardRemove()
    )

    await state.set_state(Register.setting_name)

@router.message(Register.setting_name, F.text)
async def setting_name(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    db.set_name(message.from_user.id, message.text)
    await message.answer(
        text=lang[lg]["writeAge"],
        reply_markup=ReplyKeyboardRemove()
    )

    await state.set_state(Register.setting_age)

@router.message(Register.setting_age, F.text)
async def setting_age(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    try:
        if int(message.text) <= 120:
            await message.answer(
                text=lang[lg]["writePhoneNumber"],
                reply_markup=register.send_contact(lg)
            )
            
            await state.set_state(Register.setting_phone_number)
        else:
            await message.answer(
                text=lang[lg]["wrongAge"],
                reply_markup=ReplyKeyboardRemove()
            )
    except:
        await message.answer(
            text=lang[lg]["wrongAge"],
            reply_markup=ReplyKeyboardRemove()
        )

@router.message(Register.setting_phone_number, F.contact)
async def setting_phone_number_by_contact(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    db.set_phone_number(message.from_user.id, message.contact.phone_number)
    await message.answer(
        text=lang[lg]["sendLocation"],
        reply_markup=register.send_location(lg)
    )

    await state.set_state(Register.setting_location)

@router.message(Register.setting_phone_number, F.text)
async def setting_phone_number(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    for i in message.text:
        if i.isalpha():
            await message.answer(
                text=lang[lg]["wrongNumber"],
            )
            return 0
    db.set_phone_number(message.from_user.id, message.text)
    await message.answer(
        text=lang[lg]["sendLocation"],
        reply_markup=register.send_location(lg)
    )

    await state.set_state(Register.setting_location)

@router.message(Register.setting_location, F.location)
async def setting_location_by_location(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    latitude = message.location.latitude
    longitude = message.location.longitude
    city, country = get_location(latitude, longitude)
    await message.answer(
        text=lang[lg]["registerEnded"],
    )
    await message.answer(
        text=lang[lg]["menu"]
    )
    db.set_location(message.from_user.id, city + ", " + country)

    await state.clear()

@router.message(Register.setting_location, F.text)
async def setting_location(message: types.Message, state: FSMContext):
    lg = db.get_user_language(message.from_user.id)
    await message.answer(
        text=lang[lg]["registerEnded"],
    )
    await message.answer(
        text=lang[lg]["menu"]
    )
    db.set_location(message.from_user.id, message.text)

    await state.clear()
