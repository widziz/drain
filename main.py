import uvicorn
from app.webhook import app

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.webhook:app", host="0.0.0.0", port=port)
