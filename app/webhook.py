import os
from fastapi import FastAPI, Request
from aiogram.types import Update
from dotenv import load_dotenv

from app.bot import bot, dp
from app.handlers import router as business_router

load_dotenv()

dp.include_router(business_router)

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}
