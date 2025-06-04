from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda m: m.text and m.text.strip().lower() == "!hi")
async def say_hi(message: Message):
    await message.answer("👋 Привет! Я бизнес-бот. Чем могу помочь?")
