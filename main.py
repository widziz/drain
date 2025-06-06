import uvicorn
import asyncio
from app.webhook import app
from app.bot import ensure_webhook

# Установка вебхука при старте
@app.on_event("startup")
async def on_startup():
    await ensure_webhook()

if __name__ == "__main__":
    uvicorn.run("app.webhook:app", host="0.0.0.0", port=10000)
