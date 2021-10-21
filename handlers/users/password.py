from aiogram.types import CallbackQuery
from loader import dp, bot
from keyboards.inline.pinkod import pinKod
from keyboards.default.course import courses
from states.personalData import PersonalData

PINKOD = []
ORIGINAL = ['nine', 'one', 'four', 'zero', 'three', 'seven']


@dp.callback_query_handler(text='one', state=PersonalData.password)
async def num_one(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='two', state=PersonalData.password)
async def num_two(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='three', state=PersonalData.password)
async def num_three(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='four', state=PersonalData.password)
async def num_four(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='five', state=PersonalData.password)
async def num_five(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='six', state=PersonalData.password)
async def num_six(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='seven', state=PersonalData.password)
async def num_seven(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='eight', state=PersonalData.password)
async def num_eight(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='nine', state=PersonalData.password)
async def num_nine(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='zero', state=PersonalData.password)
async def num_zero(call: CallbackQuery):
    PINKOD.append(call.data)
    print(PINKOD)
    l = len(PINKOD) * '*️⃣'
    await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='back', state=PersonalData.password)
async def back(call: CallbackQuery):
    if len(PINKOD) >= 1:
        PINKOD.pop()
        print(PINKOD)
        l = len(PINKOD) * '*️⃣'
        await call.message.edit_text(f"<b>Boshlash uchun 6 xonali kodni tering\nKOD:</b> {l}", reply_markup=pinKod)


@dp.callback_query_handler(text='confirm', state=PersonalData.password)
async def confirm(call: CallbackQuery):
    if len(PINKOD) >= 1:
        if PINKOD == ORIGINAL:
            PINKOD.clear()
            await call.message.delete()
            await call.message.answer("<b>✔️ Siz qaysi yo'nalishga yozilmoqchisiz?</b>", reply_markup=courses)
        else:
            PINKOD.clear()
            await call.message.delete()
            await call.message.answer(f"<b>🚫 Noto'g'ri kod kiritildi yana urinib ko'ring</b>")
            await call.message.answer(f"<b>Boshlash uchun 6 xonali kodni tering</b>", reply_markup=pinKod)