from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

classes_button = InlineKeyboardButton('Список классов', callback_data='classes')
classes_list_keyboard = InlineKeyboardMarkup().add(classes_button)
