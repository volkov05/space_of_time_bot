from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from ..config import BOT_TOKEN

# Устанавливаем parse_mode через DefaultBotProperties
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()