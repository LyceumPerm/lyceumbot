import re
import datetime

from aiogram import Bot, Dispatcher, executor, types

from app.util.exceptions import *
from app.data.database import UserRepository
from app.config import TOKEN, SPAM_RESTRICTION, URL, MESSAGES_LOG_PATH
from app.util.constants import ALT_PROFILES
from app.keyboards.classes import *
from app.keyboards.teacher import *
from app.util.formatter import *
import app.util.texts as texts

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

message_logger = open(MESSAGES_LOG_PATH, 'a', encoding='utf8')
user_db = UserRepository()


# CALLBACK HANDLERS

@dp.callback_query_handler(text="classes")
async def classes(callback: types.CallbackQuery):
    await log(callback)

    text = 'Список классов:\n\n'
    for i in range(24):
        text += CLASSES[i] + '\n'
        if i == 11:
            text += '\n'
    await callback.answer(text=text, show_alert=True)


@dp.callback_query_handler(text=['10', '11'])
async def set_class_number(callback: types.CallbackQuery):
    await log(callback)

    tg_id = callback.from_user.id

    func = select_10_profile() if callback.data == '10' else select_11_profile()
    await bot.edit_message_text(texts.GET_CLASS, tg_id, callback.message.message_id, reply_markup=func)
    user_db.set_state(tg_id, 1)

    user_db.set_class_number(tg_id, int(callback.data))
    await callback.answer()


@dp.callback_query_handler(text=CLASSES)
async def set_class_profile(callback: types.CallbackQuery):
    await log(callback)

    tg_id = callback.from_user.id

    await bot.edit_message_text(texts.GET_GROUP, tg_id, callback.message.message_id,
                                reply_markup=select_group())
    user_db.set_state(tg_id, 2)

    user_db.set_class_number(tg_id, int(callback.data[:2]))
    user_db.set_class_profile(tg_id, callback.data[2:])
    await callback.answer()


@dp.callback_query_handler(text=['1', '2'])
async def set_group(callback: types.CallbackQuery):
    await log(callback)

    tg_id = callback.from_user.id
    await bot.edit_message_text(texts.SUCCESS, tg_id, callback.message.message_id)
    user_db.set_state(tg_id, 3)

    user_db.set_group(tg_id, int(callback.data))
    await callback.answer()
    await bot.send_message(tg_id, texts.HELP)


@dp.callback_query_handler(text=TEACHERS)
async def select_teacher(callback: types.CallbackQuery):
    await log(callback)

    tg_id = callback.from_user.id
    if callback.data == 'ᅠ':
        await callback.answer()
        return

    await bot.edit_message_text(texts.TEACHER_WARNING, tg_id, callback.message.message_id, parse_mode='HTML')
    await bot.send_message(tg_id, f'Преподаватель: {callback.data}\n{texts.SELECT_TDATE}',
                           reply_markup=select_day_for_teacher(), parse_mode='HTML')
    await callback.answer()


@dp.callback_query_handler(text=['teachers_prev', 'teachers_next'])
async def change_teacher_page(callback: types.CallbackQuery):
    await log(callback)
    await bot.edit_message_text(texts.SELECT_TEACHER, callback.from_user.id, callback.message.message_id,
                                reply_markup=select_teacher_1() if callback.data == 'teachers_prev' else select_teacher_2())
    await callback.answer()


@dp.callback_query_handler(text=list(map(lambda item: item + 't', AVAILABLE_DAYS)))
async def get_teacher_schedule(callback: types.CallbackQuery):
    teacher_name = callback.message.text[callback.message.text.index(':') + 2: callback.message.text.index('\n')]

    await log(callback, teacher_name=teacher_name)
    answer_text = await get_schedule_for_teacher(callback.data[:-1], teacher_name)

    await bot.send_message(callback.from_user.id, answer_text)
    await callback.answer()


@dp.callback_query_handler(text=list(map(lambda item: item + 'c', CLASSES)))
async def get_class_list(callback: types.CallbackQuery):
    await log(callback)
    tg_id = callback.from_user.id

    await bot.edit_message_text(f'Класс: {callback.data[:-1]}\nВыберите день с помощью кнопок ниже:', tg_id,
                                callback.message.message_id, reply_markup=select_day_for_class())
    await callback.answer()


@dp.callback_query_handler(text=list(map(lambda item: item + 'c', AVAILABLE_DAYS[-5:])))
async def get_class_schedule(callback: types.CallbackQuery):
    await log(callback)
    tg_id = callback.from_user.id

    date = callback.data[:-1]
    class_number = int(callback.message.text[7:9])
    class_profile = callback.message.text[9:callback.message.text.find('\n')]

    await bot.send_message(tg_id, await get_schedule_for_class(date, class_number, class_profile), parse_mode='HTML')
    await callback.answer()


@dp.callback_query_handler()
async def get_by_button(callback: types.CallbackQuery):
    if callback.data in ['ᅠ', 'None']:
        await callback.answer()
        return
    await log(callback)

    tg_id = callback.from_user.id
    if not await process_checks(tg_id, spam=True):
        await callback.answer(show_alert=False)
        return
    try:
        schedule = await get_schedule_for_group(callback.data, user_db.get_class_number(tg_id),
                                                user_db.get_class_profile(tg_id), user_db.get_group(tg_id))
        await callback.message.answer(schedule, parse_mode='HTML')
    except ParsingProcessException:
        await callback.message.answer(texts.TABLE_UPDATING_ERROR)
    await callback.answer(show_alert=False)


# COMMAND HANDLERS

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await log(message)

    tg_id = message.from_user.id

    if not user_db.user_exists(tg_id):
        user_db.save_user(tg_id, message.from_user.username, message.from_user.first_name, None, None, None)
        await message.answer(texts.START)
        await message.answer('Для начала у' + texts.GET_CLASS_NUMBER[1:], reply_markup=select_class_num())

    elif user_db.get_state(tg_id) in [0, 1, 2]:
        user_db.set_state(message.from_user.id, 0)
        await message.answer(texts.GET_CLASS_NUMBER, reply_markup=select_class_num())

    else:
        await message.answer(f'{texts.START}\n\n{texts.MORE_INFO}')


@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    await log(message)
    await message.answer(texts.HELP, parse_mode='HTML')


@dp.message_handler(commands=['get'])
async def get(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return
    await message.answer('Введите дату или выберите из кнопок ниже:', reply_markup=select_day())


@dp.message_handler(commands=['class'])
async def get_for_class(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id, signup=False):
        return
    await message.answer('Выберите класс с помощью кнопок ниже:', reply_markup=select_class())


@dp.message_handler(commands=['link'])
async def link(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id, signup=False):
        return
    await message.answer('Ссылка на таблицу с расписанием:\n' + URL, disable_web_page_preview=True)


@dp.message_handler(commands=['list'])
async def get_days_list(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return

    answer_text = 'Список доступных дней:\n\n'
    for i in range(0, len(AVAILABLE_DAYS), 5):
        answer_text += ' '.join(AVAILABLE_DAYS[i: i + 5]) + '\n'
    await message.answer(answer_text)


@dp.message_handler(commands=['setclass'])
async def set_class(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return
    await message.answer(texts.GET_CLASS_NUMBER, reply_markup=select_class_num())


@dp.message_handler(commands=['setgroup'])
async def set_group(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return

    if user_db.get_state(message.from_user.id) in [0, 1]:
        await set_class()
        return

    await message.answer(texts.GET_GROUP, reply_markup=select_group())


@dp.message_handler(commands=['t', 'teacher'])
async def teacher(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id, signup=False):
        return
    await message.answer(texts.SELECT_TEACHER, reply_markup=select_teacher_1())


@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return
    await message.answer(texts.WIP)


@dp.message_handler(commands=['bells'])
async def bells(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return
    with open('app/resources/bells.jpg', 'rb') as photo:
        await message.answer_photo(photo)


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return

    await message.answer(texts.ABOUT, parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(commands=['formats'])
async def formats(message: types.Message):
    await log(message)
    if not await process_checks(message.from_user.id):
        return

    await message.answer(texts.FORMATS, parse_mode='HTML')


@dp.message_handler(commands=['delete'])
async def delete(message: types.Message):
    """Deletes user from Database"""
    await log(message)

    user_db.delete_user(message.from_user.id)
    await message.answer(texts.DELETE, parse_mode='HTML')


# MESSAGES HANDLER

@dp.message_handler()
async def process_messages(message: types.Message):
    await log(message)

    tg_id = message.from_user.id
    message_text = message.text
    try:
        state = user_db.get_state(tg_id)
    except TypeError:
        await message.answer(texts.SWW_ERROR)
        return

    if state in [0, 1]:
        # class processing
        user_db.set_state(tg_id, 0)
        await message.answer(texts.SIGNUP_ERROR)
        await message.answer(texts.GET_CLASS_NUMBER, reply_markup=select_class_num())

    elif state == 2:
        # group processing
        await message.answer(texts.SIGNUP_ERROR)
        await message.answer(texts.GET_GROUP, reply_markup=select_group())

    elif state == 3:
        # date processing
        if not await process_checks(tg_id, signup=True, spam=False):
            return

        clas_number = user_db.get_class_number(tg_id)
        clas_profile = user_db.get_class_profile(tg_id)
        group = user_db.get_group(tg_id)

        if re.fullmatch(r'\d\d([. ])\d\d', message_text):
            date = '.'.join(message_text.split()) if ' ' in message_text else message_text

        elif re.fullmatch(r'\d\d\.\d\d .* .*', message_text):
            elements = message_text.split()
            date = elements[0]
            clas_number = elements[1][:2]
            clas_profile = elements[1][2:]
            group = int(elements[2])

        elif re.fullmatch(r'\d\d \d\d .* .*', message_text):
            elements = message_text.split()
            date = f'{elements[0]}.{elements[1]}'
            clas_number = elements[2][:2]
            clas_profile = elements[2][2:]
            group = int(elements[3])

        else:
            await message.answer(texts.INVALID_FORMAT_ERROR)
            await message.answer(texts.FORMATS, parse_mode='HTML')
            return

        if clas_profile in ALT_PROFILES:
            clas_profile = ALT_PROFILES[clas_profile]

        try:
            if date not in AVAILABLE_DAYS:
                raise DateException()

            schedule = await get_schedule_for_group(date, clas_number, clas_profile, group)
            await message.answer(schedule, parse_mode='HTML')
        except DateException:
            await message.answer(texts.NO_SCHEDULE_ERROR)
        except ClasException:
            await message.answer(texts.INVALID_CLASS_ERROR, reply_markup=list_classes())
        except GroupException:
            await message.answer(texts.INVALID_GROUP_ERROR)
        except ParsingProcessException:
            await message.answer(texts.TABLE_UPDATING_ERROR)
    else:
        await message.answer(texts.SWW_ERROR)


# UTIL FUNCTIONS

async def log(data: types.Message | types.CallbackQuery, teacher_name: str = False):
    user_info = f'id: {data.from_user.id}, first_name: {data.from_user.first_name}, ' \
                f'last_name: {data.from_user.last_name}, username: {data.from_user.username}'

    newline = f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' \
              f'[{"msg" if isinstance(data, types.Message) else "clb"}] ' \
              f'({user_info}) ' \
              f'{(teacher_name + " - ") if teacher_name else ""}{data.text if isinstance(data, types.Message) else data.data}\n'

    message_logger.write(newline)
    message_logger.flush()


# если не прошли проверки - возвращает False
async def process_checks(id, signup=True, spam=False, user_exists=True):
    if user_exists and not user_db.user_exists(id):
        await bot.send_message(id, texts.SWW_ERROR)
        return
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
    if user_db.get_state(id) in [0, 1, 2]:
        user_db.set_state(id, 0)
        await bot.send_message(id, texts.SIGNUP_ERROR)
        await bot.send_message(id, texts.GET_CLASS_NUMBER, reply_markup=select_class_num())
        return False
    return True


async def check_spam(id):
    now = datetime.datetime.now()
    last_message = datetime.datetime.strptime(user_db.get_lastmessage(id), '%Y-%m-%d %H:%M:%S.%f')

    if abs((last_message - now).total_seconds()) < SPAM_RESTRICTION:
        await bot.send_message(id, texts.SPAM_ERROR)
        return False

    user_db.set_lastmessage(id, now)
    return True


def main():
    executor.start_polling(dp, skip_updates=False)


if __name__ == '__main__':
    main()
