from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from data.languagePreset import languages, general
from loader import bot, admins, dbban, db
from keyboards.user.register import send_register
from states.userData import Register


def admin_handlers(func):
    async def wrapped(*args):
        message = list(args)[0]
        if message.from_user.id in admins:
            return await func(*args)
    return wrapped


def user_handlers(func):
    async def wrapped(*args):
        message = list(args)[0]
        if await db.check_user_in_base(message.id):
            lg = db.get_user_language(message.id)
            if not await dbban.check_for_ban(message.id):
                return await func(*args)
            else:
                await bot.send_message(
                    message.from_user.id,
                    languages[lg]["youBanned"],
                    reply_markup=ReplyKeyboardRemove()
                )
        else:
            await bot.send_message(
                message.from_user.id,
                general["youNotRegistered"],
                reply_markup=send_register(),
                )
            await FSMContext.set_state(Register.started_registration)
    return wrapped