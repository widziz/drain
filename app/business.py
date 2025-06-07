from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.business_connection_id)
async def handle_business_message(message: Message):
    business_id = message.business_connection_id
    user_id = message.from_user.id

    print(f"💼 Business message from {user_id}, business_id: {business_id}")
    
    await message.answer(
        "Привет, это бизнес чат-бот!",
        business_connection_id=business_id  # Обязательное поле для ответа
    )
