from aiogram import types
from aiogram.dispatcher import FSMContext
from data.questions import questions
from loader import dp
from states.personalData import PersonalData, Question


@dp.message_handler(text_contains="Dasturlash", state=PersonalData.password)
async def enter_data(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await Question.full_name.set()


@dp.message_handler(text_contains="Foundation", state=PersonalData.password)
async def enter_data(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.full_name)
async def answer_fullname(message: types.Message, state: FSMContext):
    full_name = message.text

    await state.update_data(
        {'full_name': full_name}
    )
    await message.answer("Telefon raqamingizni kiriting")
    await PersonalData.next()


@dp.message_handler(state=Question.full_name)
async def answer_fullname(message: types.Message, state: FSMContext):
    full_name = message.text

    await state.update_data(
        {'full_name': full_name}
    )
    await message.answer("Telefon raqamingizni kiriting")
    await Question.next()


@dp.message_handler(state=PersonalData.phone_number)
async def answer_phone(message: types.Message, state: FSMContext):
    phone_number = message.text

    await state.update_data(
        {'phone_number': phone_number}
    )
    await message.answer(f"{questions['Found'][0]}")
    await PersonalData.next()
    #     Ma'lumotlarni qayta o'qiymiz
    # data = await state.get_data()
    # name = data.get('full_name')
    # phone_number = data.get('phone_number')
    #
    # msg = "📄 <b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    # msg += f"🙎‍♂️ <b>Topshiruvchi - {name}</b>\n"
    # msg += f"📞 <b>Telefon raqam - {phone_number}</b>\n"
    # await message.answer(msg)
    # await state.finish()


@dp.message_handler(state=Question.phone_number)
async def answer_phone(message: types.Message, state: FSMContext):
    phone_number = message.text

    await state.update_data(
        {'phone_number': phone_number}
    )
    await message.answer(f"{questions['Dev'][0]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound1)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer1': answer}
    )
    await message.answer(f"{questions['Found'][1]}")
    await PersonalData.next()
    #
    # # Ma'lumotlarni qayta o'qiymiz
    # data = await state.get_data()
    # name = data.get('full_name')
    # phone_number = data.get('phone_number')
    # answer = data.get('answer')
    #
    # msg = "📄 <b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    # msg += f"🙎‍♂️ <b>Topshiruvchi - {name}</b>\n"
    # msg += f"📞 <b>Telefon raqam - {phone_number}</b>\n\n"
    # msg += f"❓ <b>Savol - {answer}</b>"
    # await message.answer(msg)
    # await PersonalData.previous()


@dp.message_handler(state=Question.questionFound1)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer1': answer}
    )
    await message.answer(f"{questions['Dev'][1]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound2)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer2': answer}
    )
    await message.answer(f"{questions['Found'][2]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound2)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer2': answer}
    )
    await message.answer(f"{questions['Dev'][2]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound3)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer3': answer}
    )
    await message.answer(f"{questions['Found'][3]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound3)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer3': answer}
    )
    await message.answer(f"{questions['Dev'][3]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound4)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer4': answer}
    )
    await message.answer(f"{questions['Found'][4]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound4)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer4': answer}
    )
    await message.answer(f"{questions['Dev'][4]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound5)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer5': answer}
    )
    await message.answer(f"{questions['Found'][5]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound5)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer5': answer}
    )
    await message.answer(f"{questions['Dev'][5]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound6)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer6': answer}
    )
    await message.answer(f"{questions['Found'][6]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound6)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer6': answer}
    )
    await message.answer(f"{questions['Dev'][6]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound7)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer7': answer}
    )
    await message.answer(f"{questions['Found'][7]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound7)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer7': answer}
    )
    await message.answer(f"{questions['Dev'][7]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound8)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer8': answer}
    )
    await message.answer(f"{questions['Found'][8]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound8)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer8': answer}
    )
    await message.answer(f"{questions['Dev'][8]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound9)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer9': answer}
    )
    await message.answer(f"{questions['Found'][9]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound9)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer9': answer}
    )
    await message.answer(f"{questions['Dev'][9]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound10)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer10': answer}
    )
    await message.answer(f"{questions['Found'][10]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound10)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer10': answer}
    )
    await message.answer(f"{questions['Dev'][10]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound11)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer11': answer}
    )
    await message.answer(f"{questions['Found'][11]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound11)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer11': answer}
    )
    await message.answer(f"{questions['Dev'][11]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound12)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer12': answer}
    )
    await message.answer(f"{questions['Found'][12]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound12)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer12': answer}
    )
    await message.answer(f"{questions['Dev'][12]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound13)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer13': answer}
    )
    await message.answer(f"{questions['Found'][13]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound13)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer13': answer}
    )
    await message.answer(f"{questions['Dev'][13]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound14)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer14': answer}
    )
    await message.answer(f"{questions['Found'][14]}")
    await PersonalData.next()


@dp.message_handler(state=Question.questionFound14)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer14': answer}
    )
    await message.answer(f"{questions['Dev'][14]}")
    await Question.next()


@dp.message_handler(state=PersonalData.questionFound15)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer15': answer}
    )

    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get('full_name')
    phone_number = data.get('phone_number')
    a1 = data.get('answer1')
    a2 = data.get('answer2')
    a3 = data.get('answer3')
    a4 = data.get('answer4')
    a5 = data.get('answer5')
    a6 = data.get('answer6')
    a7 = data.get('answer7')
    a8 = data.get('answer8')
    a9 = data.get('answer9')
    a10 = data.get('answer10')
    a11 = data.get('answer11')
    a12 = data.get('answer12')
    a13 = data.get('answer13')
    a14 = data.get('answer14')
    a15 = data.get('answer15')

    msg = "📄 <b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    msg += f"🙎‍♂️ <b>Topshiruvchi</b> - <i>{name}</i>\n"
    msg += f"📞 <b>Telefon raqam</b> - <i>{phone_number}</i>\n"
    msg += f"❓ <b>{questions['Found'][0]}</b> - <i>{a1}</i>\n"
    msg += f"❓ <b>{questions['Found'][1]}</b> - <i>{a2}</i>\n"
    msg += f"❓ <b>{questions['Found'][2]}</b> - <i>{a3}</i>\n"
    msg += f"❓ <b>{questions['Found'][3]}</b> - <i>{a4}</i>\n"
    msg += f"❓ <b>{questions['Found'][4]}</b> - <i>{a5}</i>\n"
    msg += f"❓ <b>{questions['Found'][5]}</b> - <i>{a6}</i>\n"
    msg += f"❓ <b>{questions['Found'][6]}</b> - <i>{a7}</i>\n"
    msg += f"❓ <b>{questions['Found'][7]}</b> - <i>{a8}</i>\n"
    msg += f"❓ <b>{questions['Found'][8]}</b> - <i>{a9}</i>\n"
    msg += f"❓ <b>{questions['Found'][9]}</b> - <i>{a10}</i>\n"
    msg += f"❓ <b>{questions['Found'][10]}</b> - <i>{a11}</i>\n"
    msg += f"❓ <b>{questions['Found'][11]}</b> - <i>{a12}</i>\n"
    msg += f"❓ <b>{questions['Found'][12]}</b> - <i>{a13}</i>\n"
    msg += f"❓ <b>{questions['Found'][13]}</b> - <i>{a14}</i>\n"
    msg += f"❓ <b>{questions['Found'][14]}</b> - <i>{a15}</i>\n\n"
    msg1 = f"👨‍💻 Amaliy topshiriq\n\n \t<b>{questions['Practical']}</b>\n\n⚠️ <i>Barchasini qilib bo'lgach nazoratchiga ko'rsating!</i>"
    await message.answer(msg)
    await message.answer(msg1)
    await state.finish()


@dp.message_handler(state=Question.questionFound15)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer15': answer}
    )
    await message.answer(f"{questions['Dev'][15]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev1)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer16': answer}
    )
    await message.answer(f"{questions['Dev'][16]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev2)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer17': answer}
    )
    await message.answer(f"{questions['Dev'][17]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev3)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer18': answer}
    )
    await message.answer(f"{questions['Dev'][18]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev4)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer19': answer}
    )
    await message.answer(f"{questions['Dev'][19]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev5)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer20': answer}
    )
    await message.answer(f"{questions['Dev'][20]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev6)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer21': answer}
    )
    await message.answer(f"{questions['Dev'][21]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev7)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer22': answer}
    )
    await message.answer(f"{questions['Dev'][22]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev8)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer23': answer}
    )
    await message.answer(f"{questions['Dev'][23]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev9)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer24': answer}
    )
    await message.answer(f"{questions['Dev'][24]}")
    await Question.next()


@dp.message_handler(state=Question.questionDev10)
async def answer_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {'answer25': answer}
    )

    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get('full_name')
    phone_number = data.get('phone_number')
    a1 = data.get('answer1')
    a2 = data.get('answer2')
    a3 = data.get('answer3')
    a4 = data.get('answer4')
    a5 = data.get('answer5')
    a6 = data.get('answer6')
    a7 = data.get('answer7')
    a8 = data.get('answer8')
    a9 = data.get('answer9')
    a10 = data.get('answer10')
    a11 = data.get('answer11')
    a12 = data.get('answer12')
    a13 = data.get('answer13')
    a14 = data.get('answer14')
    a15 = data.get('answer15')
    a16 = data.get('answer16')
    a17 = data.get('answer17')
    a18 = data.get('answer18')
    a19 = data.get('answer19')
    a20 = data.get('answer20')
    a21 = data.get('answer21')
    a22 = data.get('answer22')
    a23 = data.get('answer23')
    a24 = data.get('answer24')
    a25 = data.get('answer25')

    msg = "📄 <b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    msg += f"🙎‍♂️ <b>Topshiruvchi</b> - <i>{name}</i>\n"
    msg += f"📞 <b>Telefon raqam</b> - <i>{phone_number}</i>\n"
    msg += f"❓ <b>{questions['Found'][0]}</b> - <i>{a1}</i>\n"
    msg += f"❓ <b>{questions['Found'][1]}</b> - <i>{a2}</i>\n"
    msg += f"❓ <b>{questions['Found'][2]}</b> - <i>{a3}</i>\n"
    msg += f"❓ <b>{questions['Found'][3]}</b> - <i>{a4}</i>\n"
    msg += f"❓ <b>{questions['Found'][4]}</b> - <i>{a5}</i>\n"
    msg += f"❓ <b>{questions['Found'][5]}</b> - <i>{a6}</i>\n"
    msg += f"❓ <b>{questions['Found'][6]}</b> - <i>{a7}</i>\n"
    msg += f"❓ <b>{questions['Found'][7]}</b> - <i>{a8}</i>\n"
    msg += f"❓ <b>{questions['Found'][8]}</b> - <i>{a9}</i>\n"
    msg += f"❓ <b>{questions['Found'][9]}</b> - <i>{a10}</i>\n"
    msg += f"❓ <b>{questions['Found'][10]}</b> - <i>{a11}</i>\n"
    msg += f"❓ <b>{questions['Found'][11]}</b> - <i>{a12}</i>\n"
    msg += f"❓ <b>{questions['Found'][12]}</b> - <i>{a13}</i>\n"
    msg += f"❓ <b>{questions['Found'][13]}</b> - <i>{a14}</i>\n"
    msg += f"❓ <b>{questions['Found'][14]}</b> - <i>{a15}</i>\n"
    msg += f"❓ <b>{questions['Dev'][15]}</b> - <i>{a16}</i>\n"
    msg += f"❓ <b>{questions['Dev'][16]}</b> - <i>{a17}</i>\n"
    msg += f"❓ <b>{questions['Dev'][17]}</b> - <i>{a18}</i>\n"
    msg += f"❓ <b>{questions['Dev'][18]}</b> - <i>{a19}</i>\n"
    msg += f"❓ <b>{questions['Dev'][19]}</b> - <i>{a20}</i>\n"
    msg += f"❓ <b>{questions['Dev'][20]}</b> - <i>{a21}</i>\n"
    msg += f"❓ <b>{questions['Dev'][21]}</b> - <i>{a22}</i>\n"
    msg += f"❓ <b>{questions['Dev'][22]}</b> - <i>{a23}</i>\n"
    msg += f"❓ <b>{questions['Dev'][23]}</b> - <i>{a24}</i>\n"
    msg += f"❓ <b>{questions['Dev'][24]}</b> - <i>{a25}</i>\n"
    msg1 = f"👨‍💻 Amaliy topshiriq\n\n \t<b>{questions['Practical']}</b>\n\n⚠️ <i>Barchasini qilib bo'lgach nazoratchiga ko'rsating!</i>"
    await message.answer(msg)
    await message.answer(msg1)
    await state.finish()
