from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.config import AVAILABLE_DAYS
from app.util.constants import TEACHERS


# select day for teacher
def select_day_for_teacher():
    days = AVAILABLE_DAYS[-5:]
    buttons = [[InlineKeyboardButton(day, callback_data=day + 't') for day in days]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# select teacher: page 1
def select_teacher_1():
    buttons = []
    for i in range(0, 24, 3):
        buttons.append(
            [InlineKeyboardButton(TEACHERS[i], callback_data=TEACHERS[i]),
             InlineKeyboardButton(TEACHERS[i + 1], callback_data=TEACHERS[i + 1]),
             InlineKeyboardButton(TEACHERS[i + 2], callback_data=TEACHERS[i + 2])]
        )
    buttons.append(
        [InlineKeyboardButton('ℹ Страница: 1', callback_data='None'),
         InlineKeyboardButton('➡ Следующая', callback_data='teachers_next')]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)


# select teacher: page 2
def select_teacher_2():
    buttons = []
    for i in range(24, 48, 3):
        buttons.append(
            [InlineKeyboardButton(TEACHERS[i], callback_data=TEACHERS[i]),
             InlineKeyboardButton(TEACHERS[i + 1], callback_data=TEACHERS[i + 1]),
             InlineKeyboardButton(TEACHERS[i + 2], callback_data=TEACHERS[i + 2])]
        )
    buttons.append(
        [InlineKeyboardButton('ℹ Страница: 2', callback_data='None'),
         InlineKeyboardButton('⬅ Предыдущая', callback_data='teachers_prev')]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)
