from fastapi import FastAPI, Request, HTTPException
from aiogram.types import Update
from app.bot import bot, dp
from app.handlers import router as default_router
from app.business import router as business_router
import os

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

# Подключаем роутеры
dp.include_router(business_router)   # Сначала бизнес
dp.include_router(default_router)    # Потом обычные

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/webhook/{secret}")

print("🛎️ Received update:", data)

async def telegram_webhook(secret: str, request: Request):
    if secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Invalid webhook secret")

    try:
        data = await request.json()
        update = Update.model_validate(data, strict=False)
        await dp.feed_update(bot, update)
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        raise HTTPException(status_code=500, detail="Webhook failed")

    return {"ok": True}

# Корректное завершение aiohttp-сессии бота при остановке
@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    print("✅ Bot session closed")

