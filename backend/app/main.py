import logging
from fastapi import FastAPI, Request
from .bot.bot import bot, dp
from .bot.handlers.start import router as start_router
from aiogram.types import Update

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Watch Shop Bot API")

# Регистрируем роутер aiogram
dp.include_router(start_router)

@app.get("/")
async def root():
    return {"status": "ok"}

# Webhook endpoint для Telegram
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    await dp.feed_update(update)  #
    return {"ok": True}

# Установка webhook при старте FastAPI
@app.on_event("startup")
async def on_startup():
    WEBHOOK_URL = "https://space-of-time-bot.onrender.com/webhook"
    logging.info(f"Устанавливаем webhook: {WEBHOOK_URL}")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(WEBHOOK_URL)
    logging.info("Webhook установлен")