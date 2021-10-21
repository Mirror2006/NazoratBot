from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💻 Foundation'),
            KeyboardButton(text='🧑‍💻 Dasturlash'),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
