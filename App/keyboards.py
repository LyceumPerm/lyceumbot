from constants import db_classes_old, available_days
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_class_list_keyboard():
    classes_button = InlineKeyboardButton('Список классов', callback_data='classes')
    class_list_keyboard = InlineKeyboardMarkup().add(classes_button)
    return class_list_keyboard


def get_class_number_keyboard():
    buttons = [[InlineKeyboardButton('10', callback_data='10'),
               InlineKeyboardButton('11', callback_data='11')]]
    class_number_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return class_number_keyboard


def get_class_profiles_keyboard():
    buttons = []
    for i in range(0, 24, 3):
        buttons.append(
            [InlineKeyboardButton(db_classes_old[i], callback_data=db_classes_old[i]),
             InlineKeyboardButton(db_classes_old[i], callback_data=db_classes_old[i + 1]),
             InlineKeyboardButton(db_classes_old[i], callback_data=db_classes_old[i + 2])]
        )
    class_letter_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=4)

    return class_letter_keyboard


def get_10_class_profiles_keyboard():
    buttons = []

    for i in range(0, 12, 3):
        buttons.append(
            [InlineKeyboardButton(db_classes_old[i], callback_data=db_classes_old[i]),
             InlineKeyboardButton(db_classes_old[i + 1], callback_data=db_classes_old[i + 1]),
             InlineKeyboardButton(db_classes_old[i + 2], callback_data=db_classes_old[i + 2])]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)

def get_11_class_profiles_keyboard():
    buttons = []

    for i in range(12, 24, 3):
        buttons.append(
            [InlineKeyboardButton(db_classes_old[i], callback_data=db_classes_old[i]),
             InlineKeyboardButton(db_classes_old[i + 1], callback_data=db_classes_old[i + 1]),
             InlineKeyboardButton(db_classes_old[i + 2], callback_data=db_classes_old[i + 2])]
        )

    return InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)


def get_group_keyboard():
    buttons = [[InlineKeyboardButton('1', callback_data='1'),
                InlineKeyboardButton('2', callback_data='2')]]
    group_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=2)
    return group_keyboard

def get_days_keyboard():
    days = available_days[-5:]
    buttons = [[InlineKeyboardButton(day, callback_data=day) for day in days]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

