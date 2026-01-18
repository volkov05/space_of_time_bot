from aiogram import Router, types
from aiogram.filters import Command
from ..keyboards.main import main_keyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        text=f"Привет, {message.from_user.first_name}! Добро пожаловать в Watch Shop Bot.",
        reply_markup=main_keyboard()
    )