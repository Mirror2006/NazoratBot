from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.login import menuLogin
from loader import dp


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, <b>{message.from_user.full_name}</b>\nBotdan foydalanish uchun 🔑 KODni kiriting!",
                         reply_markup=menuLogin)
