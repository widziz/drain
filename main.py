import uvicorn
from app.webhook import app
from app.bot import ensure_webhook

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await ensure_webhook()
    yield
    await bot.session.close()

app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.webhook:app", host="0.0.0.0", port=port)
