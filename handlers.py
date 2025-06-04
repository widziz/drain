from aiogram import F
from aiogram.types import Message, BusinessConnection
from aiogram.enums import ChatType
from bot import dp, bot


@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("Привет! Я бизнес-бот.")


@dp.message(F.business_connection)
async def business_connection_handler(message: Message, business_connection: BusinessConnection):
    if business_connection.is_enabled:
        await message.answer("✅ Бот подключён к бизнес-аккаунту!")
    else:
        await message.answer("❌ Бот НЕ подключён к бизнес-аккаунту.")


@dp.message(F.text == "!hi", F.chat.type == ChatType.PRIVATE)
async def hi_handler(message: Message):
    await message.answer("👋 Привет! Чем могу помочь?")
