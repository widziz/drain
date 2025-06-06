from fastapi import FastAPI, Request
from aiogram.types import Update

from app.bot import bot, dp
from app.handlers import router as business_router

dp.include_router(business_router)

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data, strict=False)
    await dp.feed_update(bot, update)
    return {"ok": True}
