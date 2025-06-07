from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def handle_start(message: Message):
    await message.answer("Бот работает! Вебхук настроен правильно ✅")
