import re
from datetime import datetime
from pprint import pprint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from exceptions import ClasException, GroupException, DateException, ParsingProcessException
from table import Table
from database import UserTable, ScheduleTable
from constants import TOKEN, alt_classes, table_indexes, classes_10, classes_11, SPAM_RESTRICTION, new_table
from texts import *
from keyboards import classes_list_keyboard

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

message_logger = open('logs/messages.log', 'a', encoding='utf8')
user_db = UserTable()
schedule_db = ScheduleTable()


# CALLBACK HANDLERS

@dp.callback_query_handler(text="classes")
async def classes(callback: types.CallbackQuery):
    await log(callback.message.text)

    text = 'Список классов:\n\n'
    for i in classes_10:
        text += i + '\n'
    text += '\n'
    for i in classes_11:
        text += i + '\n'
    await callback.answer(text=text, show_alert=True)


@dp.callback_query_handler()
async def get_by_button(callback: types.CallbackQuery):
    id = callback.from_user.id
    if not await process_checks(id, signup=True, spam=True):
        await callback.answer(show_alert=False)
        return
    try:
        await callback.message.answer(await get_schedule(callback.data, user_db.get_clas(id), user_db.get_group(id)))
    except ParsingProcessException:
        await callback.message.answer(TABLE_UPDATING_ERROR)
    await callback.answer(show_alert=False)


# COMMAND HANDLERS

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await log(message)

    id = message.from_user.id

    if not user_db.user_exists(id):
        user_db.save_user(id, message.from_user.username, message.from_user.first_name, None, None)
        await message.answer(START_TEXT)
        await message.answer('Для начала у' + GET_CLAS_TEXT[1:], reply_markup=classes_list_keyboard)

    elif user_db.get_state(id) in [0, 1]:
        user_db.set_state(message.from_user.id, 0)
        await message.answer(GET_CLAS_TEXT, reply_markup=classes_list_keyboard)

    else:
        await message.answer(f'{START_TEXT}\n\n{MORE_INFO_TEXT}')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await log(message)

    await message.answer(HELP_TEXT, parse_mode='HTML')


@dp.message_handler(commands=['get'])
async def get(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return

    if ' ' in message.text:
        await process_messages(message)
        return

    available_days = await get_available_days()
    keyboard = InlineKeyboardMarkup()

    for i in range(len(available_days) - 5, len(available_days)):
        keyboard.add(InlineKeyboardButton(available_days[i], callback_data=available_days[i]))

    await message.answer('Введите дату или выберите из кнопок ниже:', reply_markup=keyboard)


@dp.message_handler(commands=['list'])
async def list(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    days_list = await get_available_days()
    text = 'Список доступных дней:\n\n'
    for i in days_list:
        text += i + ' '
    await message.answer(text)


@dp.message_handler(commands=['setclass'])
async def set_class(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    await message.answer(GET_CLAS_TEXT, reply_markup=classes_list_keyboard)
    user_db.set_state(message.from_user.id, 0)


@dp.message_handler(commands=['setgroup'])
async def set_group(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    if user_db.get_clas(message.from_user.id) not in table_indexes:
        await set_class(message)
        return
    await message.answer(GET_GROUP_TEXT)
    user_db.set_state(message.from_user.id, 1)


@dp.message_handler(commands=['teacher'])
async def teacher(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    await message.answer(TEXT_WIP)


@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    await message.answer(TEXT_WIP)


@dp.message_handler(commands=['bells'])
async def bells(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    with open('resources/bells.jpg', 'rb') as photo:
        await message.answer_photo(photo)


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    await message.answer(ABOUT_TEXT, parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(commands=['formats'])
async def formats(message: types.Message):
    await log(message)
    if not await check_signup(message.from_user.id):
        return

    await message.answer(FORMATS_TEXT, parse_mode='HTML')


@dp.message_handler(commands=['delete'])
async def delete(message: types.Message):
    """Deletes user from Database"""
    await log(message)

    user_db.delete_user(message.from_user.id)
    await message.answer(DELETE_TEXT, parse_mode='HTML')


# MESSAGES HANDLER

@dp.message_handler()
async def process_messages(message: types.Message):
    await log(message)

    id = message.from_user.id
    text = message.text
    try:
        state = user_db.get_state(id)
    except TypeError:
        await message.answer(SWW_ERROR)
        return

    if state == 0:
        # class processing

        clas = text.lower()
        if clas in alt_classes:
            clas = alt_classes[clas]
        if clas in new_table:
            user_db.set_clas(id, clas)
            user_db.set_state(id, 1)
            await message.answer(GET_GROUP_TEXT)
        else:
            await message.answer(INVALID_CLASS_ERROR)
            await message.answer(GET_CLAS_TEXT, reply_markup=classes_list_keyboard)

    elif state == 1:
        # group processing
        if text in ('1', '2'):
            user_db.set_group(id, text)
            user_db.set_state(id, 2)
            await message.answer(TEXT_SUCCESS)
            await help(message)

        else:
            await message.answer(INVALID_GROUP_ERROR)
            await message.answer(GET_GROUP_TEXT)

    elif state == 2:
        # date processing
        if not await process_checks(id, signup=True, spam=False):
            return

        if not text.startswith('/get'):
            if not await process_checks(id, signup=False, spam=True):
                return

        clas = user_db.get_clas(id)
        if clas in alt_classes:
            clas = alt_classes[clas]
        group = user_db.get_group(id)
        date = None

        if text.startswith('/get'):
            if '.' in text:
                date = text.split(' ')[1]
            else:
                date = text.split()[1] + '.' + text.split()[2]
        elif re.fullmatch(r'\d\d([. ])\d\d', text):
            if ' ' in text:
                text = '.'.join(text.split())
            date = text
        elif re.fullmatch(r'\d\d\.\d\d .* .*', text):
            elements = text.split()
            date = elements[0]
            clas = elements[1]
            group = int(elements[2])
        elif re.fullmatch(r'\d\d \d\d .* .*', text):
            elements = text.split()
            date = f'{elements[0]}.{elements[1]}'
            clas = elements[2]
            group = int(elements[3])
        else:
            await message.answer(INVALID_FORMAT_ERROR)
            await message.answer(FORMATS_TEXT, parse_mode='HTML')
            return

        try:
            if date not in await get_available_days():
                raise DateException()

            schedule = await get_schedule(date, clas, group)
            await message.answer(schedule)
        except DateException:
            await message.answer(NO_SCHEDULE_ERROR)
        except ClasException:
            await message.answer(INVALID_CLASS_ERROR, reply_markup=classes_list_keyboard)
        except GroupException:
            await message.answer(INVALID_GROUP_ERROR)
        except ParsingProcessException:
            await message.answer(TABLE_UPDATING_ERROR)
    else:
        await message.answer(SWW_ERROR)


# UTIL FUNCTIONS

async def log(message):
    message_logger.write(str(message) + '\n')
    message_logger.flush()


async def get_available_days():
    with open('resources/schedule/available.txt', 'r') as file:
        result = file.read().split('\n')
    return result


# deprecated
async def get_schedule_old(date, clas, group):
    table = Table(date)
    schedule = table.get_schedule(date, clas, group)
    classrooms = table.get_classrooms(date, clas, group)

    text = f'{clas} • группа {group} • {date}\n\n'
    for i in range(len(schedule)):
        if schedule[i] is not None:
            text += f'{i + 1}. {schedule[i]}    [{classrooms[i] if classrooms[i] != "None" else " — "}]\n'
        else:
            text += f'{i + 1}. ✖ \n'

    return text


async def get_schedule(date: str, clas: str, group: int):
    schedule = schedule_db.get(date, clas, group)
    if len(schedule) != 5:
        raise ParsingProcessException

    result = f'{clas} • группа {group} • {date}\n\n'
    for i in range(5):
        if schedule[i][3] is not None:
            classroom = schedule[i][6]
            result += f'{schedule[i][2]}. {schedule[i][3]}    [{classroom if classroom != "None" else " — "}]\n'
        else:
            if schedule[i][2] != 5:
                result += f'{i + 1}. ✖ \n'

    return result


# если не прошли проверки - возвращает False
async def process_checks(id, signup=True, spam=False):
    if signup and spam:
        return await check_signup(id) and await check_spam(id)
    if signup:
        return await check_signup(id)
    if spam:
        return await check_spam(id)
    return True


async def check_signup(id):
    if not user_db.user_exists(id):
        return False
    if user_db.get_state(id) in [0, 1]:
        user_db.set_state(id, 0)
        await bot.send_message(id, SIGNUP_ERROR)
        await bot.send_message(id, GET_CLAS_TEXT, reply_markup=classes_list_keyboard)
        return False
    return True


async def check_spam(id):
    last_time = int(user_db.get_lastmessage(id))
    now_time = str(datetime.now().time())[0:8].split(':')
    now = 60 * 60 * int(now_time[0]) + 60 * int(now_time[1]) + int(now_time[2])

    if abs(now - last_time) < SPAM_RESTRICTION:
        await bot.send_message(id, SPAM_ERROR)
        return False
    user_db.set_lastmessage(id, now)
    return True


#


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
