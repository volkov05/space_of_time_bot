from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from ...config import WEBAPP_URL

def main_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🛍 Каталог",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )
    return kb