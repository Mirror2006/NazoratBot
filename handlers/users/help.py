from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state=None)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "\nMuommo bo'lsa @Bekzod_Rakhimov bilan bog'laning")
    
    await message.answer("\n".join(text))
