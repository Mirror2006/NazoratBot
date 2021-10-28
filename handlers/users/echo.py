from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    msg = "⛔️ Xato buyruq kiritildi /start qiling."
    await message.answer(msg)
