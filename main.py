import uvicorn
from app.webhook import app

if __name__ == "__main__":
    uvicorn.run("app.webhook:app", host="0.0.0.0", port=10000)
