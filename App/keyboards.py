from constants import db_classes
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


def get_class_letters_keyboard():
    buttons = []
    for i in range(0, 24, 3):
        buttons.append(
            [InlineKeyboardButton(db_classes[i], callback_data=db_classes[i]),
             InlineKeyboardButton(db_classes[i], callback_data=db_classes[i + 1]),
             InlineKeyboardButton(db_classes[i], callback_data=db_classes[i + 2])]
        )
    class_letter_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, row_width=4)

    return class_letter_keyboard


def get_10_class_letters_keyboard():
    ten_class_letter_keyboard = InlineKeyboardMarkup()
    for i in range(12):
        ten_class_letter_keyboard.add(InlineKeyboardButton(db_classes[i], callback_data=db_classes[i]))
    return ten_class_letter_keyboard

def get_11_class_letters_keyboard():
    ten_class_letter_keyboard = InlineKeyboardMarkup()
    for i in range(12, 25):
        ten_class_letter_keyboard.add(InlineKeyboardButton(db_classes[i], callback_data=db_classes[i]))
    return ten_class_letter_keyboard


def get_class_letter_keyboard():
    class_letter_keyboard = InlineKeyboardMarkup()
    for i in range(12):
        letter = db_classes[i]
        class_letter_keyboard.add(InlineKeyboardButton(letter, callback_data=letter))
    return class_letter_keyboard
