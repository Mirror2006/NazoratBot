from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuLogin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔐 PIN-KOD'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
