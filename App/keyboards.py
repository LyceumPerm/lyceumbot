from configuration import CLASSES, AVAILABLE_DAYS, TEACHERS
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def list_classes():
    classes_button = InlineKeyboardButton('Список классов', callback_data='classes')
    class_list_keyboard = InlineKeyboardMarkup().add(classes_button)
    return class_list_keyboard


def select_class_num():
    buttons = [[InlineKeyboardButton('10', callback_data='10'),
                InlineKeyboardButton('11', callback_data='11')]]
    class_number_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return class_number_keyboard


def select_10_profile():
    buttons = []

    for i in range(0, 12, 3):
        buttons.append(
            [InlineKeyboardButton(CLASSES[i], callback_data=CLASSES[i]),
             InlineKeyboardButton(CLASSES[i + 1], callback_data=CLASSES[i + 1]),
             InlineKeyboardButton(CLASSES[i + 2], callback_data=CLASSES[i + 2])]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)


def select_11_profile():
    buttons = []

    for i in range(12, 24, 3):
        buttons.append(
            [InlineKeyboardButton(CLASSES[i], callback_data=CLASSES[i]),
             InlineKeyboardButton(CLASSES[i + 1], callback_data=CLASSES[i + 1]),
             InlineKeyboardButton(CLASSES[i + 2], callback_data=CLASSES[i + 2])]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)


def select_group():
    buttons = [[InlineKeyboardButton('1', callback_data='1'),
                InlineKeyboardButton('2', callback_data='2')]]
    group_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return group_keyboard


def select_day():
    days = AVAILABLE_DAYS[-5:]
    buttons = [[InlineKeyboardButton(day, callback_data=day) for day in days]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def select_day_for_class():
    days = AVAILABLE_DAYS[-5:]
    buttons = [[InlineKeyboardButton(day, callback_data=day + 'c') for day in days]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def select_teacher_part1():
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


def select_teacher_part2():
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


# select day for teacher
def select_tday():
    days = AVAILABLE_DAYS[-5:]
    buttons = [[InlineKeyboardButton(day, callback_data=day + 't') for day in days]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def select_class():
    buttons = []

    for i in range(0, 24, 3):
        buttons.append(
            [InlineKeyboardButton(CLASSES[i], callback_data=CLASSES[i] + 'c'),
             InlineKeyboardButton(CLASSES[i + 1], callback_data=CLASSES[i + 1] + 'c'),
             InlineKeyboardButton(CLASSES[i + 2], callback_data=CLASSES[i + 2] + 'c')]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons)
