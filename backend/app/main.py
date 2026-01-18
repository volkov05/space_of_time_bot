import asyncio
import logging
from fastapi import FastAPI
from .bot.bot import bot, dp
from .bot.handlers.start import router as start_router

logging.basicConfig(level=logging.INFO)

# FastAPI (для проверки)
app = FastAPI(title="Watch Shop Bot API")
dp.include_router(start_router)

@app.get("/")
async def root():
    return {"status": "ok"}

# Запуск бота через событие startup FastAPI
@app.on_event("startup")
async def on_startup():
    logging.info("Запускаем Telegram бота...")
    asyncio.create_task(dp.start_polling(bot))