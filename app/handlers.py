from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.business_connection_id)
async def business_handler(message: Message):
    await message.answer(
        text="Привет, это бизнес чат-бот!",
        business_connection_id=message.business_connection_id
    )

@router.message()
async def fallback_handler(message: Message):
    await message.answer("Это обычный бот. Напишите нам через бизнес-аккаунт!")
