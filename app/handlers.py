from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.business_connection_id)
async def handle_business_message(message: Message):
    business_id = message.business_connection_id
    chat_id = message.chat.id

    await message.bot.send_message(
        chat_id=chat_id,
        text="Привет, это бизнес чат-бот!",
        business_connection_id=business_id
    )
