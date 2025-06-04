
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET_TOKEN")
WEBHOOK_BASE = os.getenv("WEBHOOK_BASE")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(lambda message: message.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать в бизнес-бота!")

@dp.message(lambda message: message.text == ".hi")
async def hi_cmd(message: types.Message):
    await message.answer("Привет! Это бизнес-бот.")

app = FastAPI()

SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=f"/webhook/{WEBHOOK_SECRET}")

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(f"{WEBHOOK_BASE}/webhook/{WEBHOOK_SECRET}")
