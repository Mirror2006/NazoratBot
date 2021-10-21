from aiogram.types import Message
from loader import dp, bot
from keyboards.inline.pinkod import pinKod
from states.personalData import PersonalData


@dp.message_handler(text_contains="PIN-KOD", state=None)
async def kod(message: Message):
    await message.answer(f"<b>Boshlash uchun 6 xonali kodni tering</b>", reply_markup=pinKod)
    await PersonalData.password.set()