from app.data.database import ScheduleRepository
from app.util import texts
from app.util.constants import PROFILES
from app.util.exceptions import ClasException, GroupException, ParsingProcessException


# Функции берут данные из базы и генерируют (и форматируют) текст для сообщения с ответом
# todo переписать бы красивее

schedule_repository = ScheduleRepository()

async def get_schedule_for_class(date: str, clas_number: int, clas_profile: str) -> str:
    """Возвращает текст сообщения с расписанием для всего класса"""
    if await check_date(date):
        return texts.REST_DAY[date]

    if clas_profile not in PROFILES:
        raise ClasException

    schedule = schedule_repository.get(date, clas_number, clas_profile)
    if len(schedule) != 10:
        return texts.TABLE_UPDATING_ERROR

    result_text = f'{str(schedule[0][5]) + (PROFILES[schedule[0][6] - 1])} • {date}\n\n'

    for i in range(0, 10, 2):
        lesson1 = schedule[i][3]
        teacher1 = schedule[i][4]
        classroom1 = schedule[i][8]

        lesson2 = schedule[i + 1][3]
        teacher2 = schedule[i + 1][4]
        classroom2 = schedule[i + 1][8]

        # не отображаем пятую пару, если её нет
        if schedule[i][2] == 5 and lesson1 is None and lesson2 is None:
            continue

        if lesson1 is None:
            lesson1 = '✖'
            teacher1 = ''
            classroom1 = 'None'
        if lesson2 is None:
            lesson2 = '✖'
            teacher2 = ''
            classroom2 = 'None'

        if lesson1 == lesson2 and teacher1 == teacher2 and classroom1 == classroom2:
            if lesson1 == '✖':
                result_text += f'{schedule[i][2]}. {lesson1}\n'
            else:
                result_text += f'{schedule[i][2]}. {lesson1}{" (" + teacher1 + ")" if teacher1 else ""}   ' \
                               f'[{classroom1 if classroom1 != "None" else " — "}]\n'
        else:
            result_text += f'{schedule[i][2]}. {lesson1}{" (" + teacher1 + ")" if teacher1 else ""} [{classroom1 if classroom1 != "None" else " — "}]\n' \
                           f'     {lesson2}{" (" + teacher2 + ")" if teacher2 else ""} [{classroom2 if classroom2 != "None" else " — "}]\n'

    return result_text


async def get_schedule_for_group(date: str, clas_number: int, clas_profile: str, group: int) -> str:
    """Возвращает текст сообщения с расписанием для подгруппы класса"""
    if await check_date(date):
        return texts.REST_DAY[date]
    if clas_profile not in PROFILES:
        raise ClasException
    if group not in [1, 2]:
        raise GroupException

    schedule = schedule_repository.get_for_group(date, clas_number, clas_profile, group)
    if len(schedule) != 5:
        raise ParsingProcessException

    result_text = f'{str(schedule[0][5]) + (PROFILES[schedule[0][6] - 1])} • группа {group} • {date}\n\n'

    for i in range(5):
        if schedule[i][3] is not None:
            classroom = schedule[i][8]
            teacher_name = schedule[i][4]
            result_text += f'{schedule[i][2]}. {schedule[i][3]}{" (" + teacher_name + ")" if teacher_name else ""}   ' \
                           f'[{classroom if classroom != "None" else " — "}]\n'
        else:
            if schedule[i][2] != 5:
                result_text += f'{i + 1}. ✖ \n'

    return result_text


async def get_schedule_for_teacher(date: str, teacher_name: str) -> str:
    """Возвращает текст сообщения с расписанием для учителя"""
    if await check_date(date):
        return texts.REST_DAY[date]

    schedule = schedule_repository.get_for_teacher(date, teacher_name)
    added_classes = []  # пары, которые уже добавлены в сообщение
    answer_text = f'{date} • {teacher_name}\n\n'

    for i in range(1, 6):
        lessons = []
        for line in schedule:
            if line[2] == i:
                lessons.append(line)
        if lessons:
            for clas in lessons:
                if f'{i}{clas[5]}{PROFILES[clas[6] - 1]}' not in added_classes:
                    answer_text += f'{i}. {clas[5]}{PROFILES[clas[6] - 1]} - {clas[3]}   ' \
                                   f'[{clas[8] if clas[8] not in ["None", "", None] else " — "}]\n'
                    added_classes.append(f'{i}{clas[5]}{PROFILES[clas[6] - 1]}')
        else:
            answer_text += f'{i}.\n'

    return answer_text


async def check_date(date):
    return date in texts.REST_DAY
