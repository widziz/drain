# app/handlers.py
from aiogram import Router, F
from aiogram.types import Message

router = Router()

# Обработка бизнес-сообщений
@router.message(F.business_connection_id)
async def business_handler(message: Message):
    await message.answer(
        text="Привет, это бизнес чат-бот!",
        business_connection_id=message.business_connection_id
    )

# (опционально) обработка обычных сообщений
@router.message()
async def fallback_handler(message: Message):
    await message.answer("Это не бизнес-сообщение.")
