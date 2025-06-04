import logging
from fastapi import FastAPI, Request
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from bot import bot, dp
import handlers  # noqa: F401 — импортируем для регистрации хендлеров
from config import WEBHOOK_PATH, WEBHOOK_URL

app = FastAPI()

# Webhook обработка
@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    body = await request.json()
    update = Update.model_validate(body)
    await dp.feed_update(bot, update)
    return {"ok": True}

# Установка webhook при запуске
@app.on_event("startup")
async def on_startup():
    logging.warning("Устанавливаю webhook...")
    await bot.set_webhook(WEBHOOK_URL, secret_token=WEBHOOK_PATH.split("/")[-1])

# Удаление webhook при завершении
@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()
