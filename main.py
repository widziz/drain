from fastapi import FastAPI, Request
import httpx
import os
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = FastAPI()

# Обработка входящих апдейтов от Telegram
@app.post("/webhook/{webhook_token}")
async def handle_webhook(webhook_token: str, request: Request):
    if webhook_token != WEBHOOK_SECRET:
        return {"error": "invalid secret"}

    update = await request.json()

    # Если это обычное сообщение из лички
    if "message" in update:
        message = update["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text")

        if text == "!hi":
            await send_message(chat_id, "Привет! Это бизнес-бот 🛍️")

    # Если это обновление бизнес-подключения
    if "business_connection" in update:
        # Пример простой реакции
        conn = update["business_connection"]
        print("Новое бизнес-подключение:", conn)

    return {"ok": True}


async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": text
        })


@app.get("/")
def root():
    return {"message": "Бизнес бот работает!"}


# Установка вебхука (вызывается один раз вручную)
async def set_webhook():
    url = f"https://drain-5mb6.onrender.com/webhook/{WEBHOOK_SECRET}"
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{TELEGRAM_API}/setWebhook", json={"url": url})
        print(resp.json())


# Можно вызвать установку вручную, если нужно
# asyncio.run(set_webhook())
