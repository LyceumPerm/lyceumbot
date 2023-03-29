START = 'Привет! Этот бот предназначен для просмотра расписания своего класса в удобном формате.'

MORE_INFO = 'Больше информации по команде /help'

GET_CLASS_NUMBER = '''Укажите номер вашего класса с помощью кнопок ниже.'''

GET_CLASS = '''Укажите класс, расписание которого вы хотели бы получать по умолчанию

Выберите один из классов с помощью кнопок ниже (можно изменить в любой момент позже).
'''

GET_GROUP = 'Укажите номер вашей подгруппы с помощью кнопок ниже.'

ABOUT = '''Telegram-бот для просмотра расписания своего класса в удобном формате

Новости о проекте: @lyceumbotnews
Исходный код доступен на <a href="https://github.com/skosarevv/lyceumbot">GitHub</a>

dev by Renat Skosarev
<a href="https://vk.com/skosarev">vk</a> • <a href="https://skosarevv.t.me">telegram</a> • <a href="https://github.com/skosarevv">github</a>
'''

DELETE = '''Вы отменены. Вас нет и никогда не существовало.

<span class="tg-spoiler">/start для перезапуска</span>
'''

HELP = '''Основные команды (больше — в меню):
/get - Расписание
/list - Список доступных дней
/bells - Расписание звонков
/setclass - Изменить класс
/setgroup - Изменить подгруппу
/about - Информация о боте

Для получения расписания на конкретный день введите дату в формате: 25.12
Подробнее: /formats


Обратная связь: @skosarevv
Новости о проекте: @lyceumbotnews
'''

FORMATS = '''<b>Доступные форматы запросов:</b>

Ваш класс:
{число}.{месяц}
Пример: 17.01 

Другой класс:
{число}.{месяц} {класс} {подгруппа}
Пример: 17.01 10геохим 1
'''

SUCCESS = '✅ Данные сохранены'
WIP = 'Work in progress 🪄'

REST_DAY = ''

# error texts
SELECT_CLASS_ERROR = 'Для начала работы с ботом выберите класс.'
SELECT_GROUP_ERROR = 'Для начала работы с ботом выберите номер подгруппы.'

TABLE_UPDATING_ERROR = 'Таблица обновляется. Попробуйте ещё раз через 15 секунд.'
INVALID_CLASS_ERROR = 'Некорректный класс! Попробуйте ещё раз.'
INVALID_GROUP_ERROR = 'Некорректная подгруппа! Попробуйте ещё раз.'
INVALID_FORMAT_ERROR = 'Ошибка: некорректный формат'
NO_SCHEDULE_ERROR = 'Ошибка: расписания на этот день нет.'
SIGNUP_ERROR = '❌ Для начала работы с ботом вы должны указать класс и номер подгруппы.'
SPAM_ERROR = '❌ Запрос можно отправлять раз в две секунды.'
SWW_ERROR = '''Что-то пошло не так!
Введите /start для перезагрузки'''

# teacher mode
TEACHER_WARNING = '''<b>Внимание:</b> в «режиме учителя» программа может учитывать пары неправильно, если в таблице некорректно указано имя учителя, или формат ячейки не соответствует стандарту.\n\nБудьте внимательны и сверяйтесь с таблицей: /link'''
SELECT_TEACHER = 'Выберите имя преподавателя из списка ниже:'
SELECT_TDATE = 'Выберите дату с помощью кнопок ниже:'
