START_TEXT = 'Привет! Это бот для просмотра расписания вашего класса в удобном формате.'

MORE_INFO_TEXT = 'Больше информации по команде /help'

GET_CLAS_TEXT = '''Укажите класс, расписание которого вы хотели бы получать по умолчанию

Введите номер и литеру класса так, как прописано в расписании, без пробелов. Пример: 10геохим; 11мат1
'''

GET_GROUP_TEXT = 'Укажите подгруппу (1 или 2):'

ABOUT_TEXT = '''Telegram-бот для просмотра расписания своего класса в удобном формате

Новости о проекте: https://t.me/lyceumbotnews
Исходный код: https://github.com/skosarevv/lyceumbot

dev by Renat Skosarev
<a href="https://vk.com/skosarev">vk</a> • <a href="https://skosarevv.t.me">telegram</a> • <a href="https://github.com/skosarevv">github</a>
'''

DELETE_TEXT = '''Вы отменены. Вас нет и никогда не существовало.

<span class="tg-spoiler">/start для перезапуска</span>
'''

HELP_TEXT = '''Основные команды (больше — в меню):
/get - Расписание
/list - Список доступных дней
/bells - Расписание звонков
/setclass - Изменить класс
/setgroup - Изменить подгруппу
/about - Информация о боте

Для получения расписания на конкретный день введите дату в формате: 25.12
Подробнее: /formats


Обратная связь: @skosarevv
'''

FORMATS_TEXT = '''<b>Доступные форматы запросов:</b>

Ваш класс:
{число}.{месяц}
Пример: 17.01 

Другой класс:
{число}.{месяц} {класс} {подгруппа}
Пример: 17.01 10геохим 1
'''

TEXT_SUCCESS = '✅ Данные сохранены'
TEXT_WIP = 'Work in progress 🪄'

# errors text
TABLE_UPDATING_ERROR = 'Таблица обновляется. Попробуйте ещё раз через 15 секунд.'
INVALID_CLASS_ERROR = 'Некорректный класс! Попробуйте ещё раз.'
INVALID_GROUP_ERROR = 'Некорректная подгруппа! Попробуйте ещё раз.'
INVALID_FORMAT_ERROR = 'Ошибка: некорректный формат'
NO_SCHEDULE_ERROR = 'Ошибка: расписания на этот день нет.'
SIGNUP_ERROR = '❌ Для начала работы с ботом вы должны указать свой класс.'
SPAM_ERROR = '❌ Запрос можно отправлять раз в две секунды.'
SWW_ERROR = '''Что-то пошло не так!
Введите /start для перезагрузки'''
