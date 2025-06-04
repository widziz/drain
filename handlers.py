from aiogram import Router, Bot
from aiogram.types import Update, BusinessConnectionUpdated, BusinessMessage

router = Router()

# Хранилище бизнес-соединений user_id -> business_connection_id
business_connections = {}

@router.update()
async def handle_business_updates(update: Update, bot: Bot):
    if update.business_connection:
        conn: BusinessConnectionUpdated = update.business_connection
        user_id = conn.user.id
        business_connections[user_id] = conn.id
        print(f"🔗 Пользователь {user_id} подключил бизнес-аккаунт: {conn.id}")

    elif update.business_message:
        msg: BusinessMessage = update.business_message
        user_id = msg.from_.id
        conn_id = business_connections.get(user_id)

        if conn_id and msg.text and msg.text.strip().lower() == "!hi":
            await bot.send_message(
                chat_id=msg.chat.id,
                text="👋 Привет! Это бизнес-бот!",
                business_connection_id=conn_id
            )

