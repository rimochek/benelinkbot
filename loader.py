from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from geopy.geocoders import Nominatim

from data.config import TOKEN, ADMINS_TG_ID
from utils.database.usersData import UsersManager
from utils.database.banUsers import BanManager

storage = MemoryStorage()
dbban = BanManager("data/usersinfo.db")
db = UsersManager("data/usersinfo.db")
dp = Dispatcher(storage=storage)
geolocator = Nominatim(user_agent="geoapiExercises")
bot = Bot(token=TOKEN)
admins = ADMINS_TG_ID