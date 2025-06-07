import uvicorn
from app.webhook import app
from app.bot import ensure_webhook

@app.on_event("startup")
async def on_startup():
    await ensure_webhook()

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.webhook:app", host="0.0.0.0", port=port)
