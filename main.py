import os
from fastapi import FastAPI, Request
import httpx
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post(f"/webhook/{WEBHOOK_SECRET}")
async def telegram_webhook(req: Request):
    data = await req.json()
    
    # Business connection event
    if "business_connection" in data:
        conn = data["business_connection"]
        print("Business connected:", conn)
        return {"ok": True}
    
    # Check for incoming message
    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text.lower().startswith("!hi"):
            await send_message(chat_id, "👋 Привет! Бизнес бот на связи.")
    
    return {"ok": True}

async def send_message(chat_id, text):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )

# 💡 Ручной вызов один раз для установки webhook
# import asyncio
# async def set_webhook():
#     async with httpx.AsyncClient() as client:
#         await client.post(f"{API_URL}/setWebhook", json={
#             "url": f"https://drain-5mb6.onrender.com/webhook/{WEBHOOK_SECRET}"
#         })
# asyncio.run(set_webhook())

