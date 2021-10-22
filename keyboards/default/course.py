from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧑‍💻 Dasturlash'),
            KeyboardButton(text='💻 Boshqa kurslar'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
