from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

BOT_TOKEN = "7712265453:AAEbDMm6Xikg9vawNF1737AsrDG_FyKOsAQ"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
