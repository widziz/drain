from aiogram import Router, Bot
from aiogram.types import Update, BusinessConnectionUpdated, BusinessMessage
from aiogram.filters import Filter
from aiogram.handlers import BaseHandler

# Храним соответствие user_id -> business_connection_id
business_connections = {}

router = Router()

@router.update()
async def handle_all_updates(update: Update, bot: Bot):
    if update.business_connection:
        conn: BusinessConnectionUpdated = update.business_connection
        user_id = conn.user.id
        business_connections[user_id] = conn.id
        print(f"🔗 Подключён бизнес-аккаунт от user_id={user_id}, connection_id={conn.id}")

    elif update.business_message:
        msg: BusinessMessage = update.business_message
        user_id = msg.from_.id
        conn_id = business_connections.get(user_id)

        if conn_id and msg.text and msg.text.strip().lower() == "!hi":
            await bot.send_message(
                chat_id=msg.chat.id,
                text="👋 Привет! Это бизнес-бот.",
                business_connection_id=conn_id
            )
