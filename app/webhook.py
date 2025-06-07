from fastapi import FastAPI, Request, HTTPException
from aiogram.types import Update
from app.bot import bot, dp
from app.handlers import router as default_router
from app.business import router as business_router
import os

# Получаем секрет из переменных окружения
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

# Регистрируем роутеры
dp.include_router(business_router)   # 💼 Сначала бизнес
dp.include_router(default_router)    # 👤 Потом обычные

# Инициализация FastAPI
app = FastAPI()

# Корневой эндпоинт для проверки статуса
@app.get("/")
async def root():
    return {"status": "ok"}

# Webhook-эндпоинт
@app.post("/webhook/{secret}")
async def telegram_webhook(secret: str, request: Request):
    if secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Invalid webhook secret")

    try:
        data = await request.json()
        update = Update.model_validate(data, strict=False)
        await dp.feed_update(bot, update)
    except Exception as e:
        print(f"❌ Webhook processing error: {e}")
        raise HTTPException(status_code=500, detail="Webhook error")

    return {"ok": True}
