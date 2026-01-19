import asyncio
import logging
import httpx
from datetime import datetime

from fastapi import FastAPI, Request
from aiogram.types import Update

from .bot.bot import bot, dp
from .bot.handlers.start import router as start_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Watch Shop Bot API")
dp.include_router(start_router)

RENDER_URL = "https://space-of-time-bot.onrender.com/"
WEBHOOK_URL = f"{RENDER_URL}webhook"


# =====================
# Статистика бота
# =====================

class BotStats:
    def __init__(self):
        self.start_time = datetime.utcnow()
        self.total_updates = 0
        self.unique_users = set()
        self.last_activity = None

    def register_update(self, user_id: int | None):
        self.total_updates += 1
        self.last_activity = datetime.utcnow()
        if user_id:
            self.unique_users.add(user_id)

    def snapshot(self):
        uptime = datetime.utcnow() - self.start_time
        return {
            "uptime_minutes": round(uptime.total_seconds() / 60, 2),
            "total_updates": self.total_updates,
            "unique_users": len(self.unique_users),
            "last_activity": self.last_activity.isoformat() if self.last_activity else None,
        }


stats = BotStats()


# =====================
# Routes
# =====================

@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update(**data)

    user_id = None
    if update.message and update.message.from_user:
        user_id = update.message.from_user.id

    stats.register_update(user_id)

    await dp.feed_update(update=update, bot=bot)
    return {"ok": True}


# =====================
# Keep-alive + лог статистики
# =====================

async def keep_alive_with_stats():
    async with httpx.AsyncClient() as client:
        while True:
            try:
                await client.get(RENDER_URL)
                snapshot = stats.snapshot()

                logging.info(
                    "📊 СТАТИСТИКА | Время работы: %s мин | Пользователи: %s | Обновления: %s | Последняя активность: %s",
                    snapshot["uptime_minutes"],
                    snapshot["unique_users"],
                    snapshot["total_updates"],
                    snapshot["last_activity"],
                )

            except Exception as e:
                logging.warning(f"Keep-alive error: {e}")

            await asyncio.sleep(14 * 60)


# =====================
# Startup
# =====================

@app.on_event("startup")
async def on_startup():
    logging.info(f"Устанавливаем webhook: {WEBHOOK_URL}")

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(WEBHOOK_URL)

    asyncio.create_task(keep_alive_with_stats())

    logging.info("🚀 Сервер и бот успешно запущены")