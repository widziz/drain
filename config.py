import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = "d50ef92a7c4d3bad7c453a3610e06869"
WEBHOOK_PATH = f"/webhook/{WEBHOOK_SECRET}"
WEBHOOK_URL = f"https://drain-5mb6.onrender.com{WEBHOOK_PATH}"
