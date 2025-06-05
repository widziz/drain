from aiogram import Router, Bot
from aiogram.types import BusinessMessage

router = Router()

@router.message()
async def handle_business_message(message: BusinessMessage, bot: Bot):
    if message.text:
        await bot.send_message(
            chat_id=message.chat.id,
            text="👋 Привет! Это бизнес-чат-бот.",
            business_connection_id=message.business_connection_id
        )
