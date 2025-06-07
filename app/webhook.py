from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from contextlib import asynccontextmanager
from aiogram.types import Update
from app.bot import bot, dp, ensure_webhook
from app.business import router as business_router
from app.handlers import router as default_router
import os

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

# Роутеры
dp.include_router(business_router)
dp.include_router(default_router)

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Startup: setting webhook...")
    await ensure_webhook()
    yield
    await bot.session.close()
    print("✅ Bot session closed")

# FastAPI app
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/webhook/{secret}")
async def telegram_webhook(secret: str, request: Request, bg_tasks: BackgroundTasks):
    print("📬 Webhook triggered")

    if secret != WEBHOOK_SECRET:
        print("❌ Invalid secret received")
        raise HTTPException(status_code=403, detail="Invalid webhook secret")

    try:
        data = await request.json()
        update = Update.model_validate(data, strict=False)
        print(f"📨 Incoming update: {update.event_type}")
        bg_tasks.add_task(dp.feed_update, bot, update)
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        raise HTTPException(status_code=500, detail="Webhook failed")

    return {"ok": True}

