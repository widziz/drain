from aiogram import Router, Bot
from aiogram.types import Update

router = Router()

# Словарь user_id -> business_connection_id
business_connections = {}

@router.update()
async def handle_business_updates(update: Update, bot: Bot):
    if update.business_connection:
        conn = update.business_connection
        user_id = conn.user.id
        business_connections[user_id] = conn.id
        print(f"🔗 Бизнес-аккаунт подключен: {user_id} -> {conn.id}")

    elif update.business_message:
        msg = update.business_message
        user_id = msg.from_.id
        chat_id = msg.chat.id
        text = msg.text or ""
        conn_id = business_connections.get(user_id)

        if conn_id:
            await bot.send_message(
                chat_id=chat_id,
                text="👋 Привет! Это чат-бот.",
                business_connection_id=conn_id
            )
