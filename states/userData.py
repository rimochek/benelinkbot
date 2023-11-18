from aiogram.fsm.state import StatesGroup, State

class Register(StatesGroup):
    started_registration = State()
    choosing_language = State()
    choosing_user_type = State()
    setting_name = State()
    setting_age = State()
    setting_phone_number = State()
    setting_location = State()
    
