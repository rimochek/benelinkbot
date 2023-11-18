import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMINS_TG_ID = os.getenv("ADMINS_TG_ID")