from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda message: message.business_connection_id is not None)
async def business_handler(message: Message):
    await message.answer(
        text="Привет, это бизнес чат-бот!",
        business_connection_id=message.business_connection_id
    )
