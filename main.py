import os
from fastapi import FastAPI, Request
from aiogram.types import Update
from bot import bot, dp
import asyncio
import logging

import handlers  # подключаем обработчики

WEBHOOK_SECRET = "d50ef92a7c4d3bad7c453a3610e06869"
WEBHOOK_PATH = f"/webhook/{WEBHOOK_SECRET}"

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Устанавливаем вебхук Telegram
    webhook_url = f"https://drain-5mb6.onrender.com{WEBHOOK_PATH}"
    await bot.set_webhook(webhook_url)
    logging.info(f"Webhook установлен: {webhook_url}")

@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()

@app.post(WEBHOOK_PATH)
async def webhook_handler(request: Request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"status": "ok"}
