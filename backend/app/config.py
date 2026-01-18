import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

DATABASE_URL = os.getenv("DATABASE_URL")

TILDA_API_KEY = os.getenv("TILDA_API_KEY")
TILDA_PROJECT_ID = os.getenv("TILDA_PROJECT_ID")

PAYMENT_SECRET = os.getenv("PAYMENT_SECRET")

WEBAPP_URL = os.getenv("WEBAPP_URL")
