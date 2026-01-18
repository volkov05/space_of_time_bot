import asyncio
import logging
from fastapi import FastAPI
from .bot.bot import bot, dp
from .bot.handlers.start import router as start_router

logging.basicConfig(level=logging.INFO)

# FastAPI (пока только для проверки)
app = FastAPI(title="Watch Shop Bot API")
dp.include_router(start_router)

@app.get("/")
async def root():
    return {"status": "ok"}

# Функция запуска бота
async def main():
    logging.info("Бот запускается...")
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())