from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def handle_business_message(message: Message):
    """
    Обрабатывает ВСЕ входящие сообщения.
    Если сообщение пришло из бизнес-чата — отвечает.
    """
    business_id = message.business_connection_id

    if business_id:
        user_id = message.from_user.id
        text = message.text or "[нет текста]"

        print(f"💼 [Business] From user {user_id} — text: {text} — business_id: {business_id}")

        try:
            await message.answer(
                text="Привет, это бизнес чат-бот!",
                business_connection_id=business_id  # 🔑 Обязательно!
            )
        except Exception as e:
            print(f"❌ Ошибка при отправке бизнес-ответа: {e}")
    else:
        print("📥 Сообщение без business_connection_id — игнор.")
