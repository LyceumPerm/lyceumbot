CLASSES = ['10био', '10геохим', '10исс1', '10исс2', '10линг1', '10линг2', '10мат', '10матэк', '10мед', '10фил',
           '10фм', '10эк', '11био', '11биохим', '11гео', '11исс', '11линг1', '11линг2', '11мат1', '11мат2', '11мед',
           '11фил', '11фм', '11эк']

PROFILES = ['био', 'геохим', 'исс1', 'исс2', 'линг1', 'линг2', 'мат', 'матэк', 'мед', 'фил', 'фм', 'эк',
            'биохим', 'гео', 'исс', 'мат1', 'мат2']

# дополнительные (альтернативные) названия профилей
ALT_PROFILES = {
    'б': 'био',
    'гх': 'геохим',
    'исс-1': 'исс1', 'ис1': 'исс1', 'ис-1': 'исс1',
    'исс-2': 'исс2', 'ис2': 'исс2', 'ис-2': 'исс2', 'иис2': 'исс2',
    'линг-1': 'линг1',
    'линг-2': 'линг2',
    'м': 'мат',
    'мэ': 'матэк',
    # мед
    'ф': 'фил',
    'физмат': 'фм',
    'э': 'эк',

    'бх': 'биохим',
    'г': 'гео',
    'ис': 'исс',
    'мат-1': 'мат1', 'м1': 'мат1',
    'мат-2': 'мат2', 'м2': 'мат2',
}

TEACHERS = ['Альянаки С.И.', 'Басманова А.С.', 'Баталова Л.Г.', 'Бежина И.Н.', 'Бушин В.Н.', 'Быстрова Н.Я.',
            'Вавилин А.С.', 'Веревкина И.Н.', 'Гачегова Л.В.', 'Гашева Л.И.', 'Демидова М.И.', 'Жувак И.В.',
            'Журавлева Л.С.', 'Загребина Г.Е.', 'Зотина И.М.', 'Иванов С.В.', 'Ильина Н.С.', 'Каменских О.В.',
            'Комаров В.А.', 'Конев А.И.', 'Коровина К.С.', 'Кощеева А.Н.', 'Князева Е.А.', 'ᅠ', 'Мартилова Н.Л.',
            'Мартынова М.Н.', 'Микрюков Д.А.', 'Нагорнюк О.И.', 'Некрасов О.О.', 'Осташова Е.В.', 'Панова Е.А.',
            'Поварницына Е.С.', 'Полушкина М.А.', 'Радаева О.С.', 'Ракина Е.А.', 'Ромодина Т.П.', 'Соболева Т.И.',
            'Сонинский П.Г.', 'Сорокина А.В.', 'Сутоцкая М.Ю.', 'Филенко А.Е.', 'Филенко Д.А.', 'Фомичева Н.В.',
            'Чепурин А.В.', 'Чернышев А.Ю.', 'Чигодайкина Е.В.', 'Чугунова О.О.', 'ᅠ']

# дополнительные (альтернативные) строки с именами учителей
ALT_TEACHERS = {
    'альянаки': 'Альянаки С.И.',
    'басманова': 'Басманова А.С.',
    'баталова': 'Баталова Л.Г.',
    'бежина': 'Бежина И.Н.',
    'бушин': 'Бушин В.Н.',
    'быстрова': 'Быстрова Н.Я.',
    'вавилин': 'Вавилин А.С.',
    'веревкина': 'Веревкина И.Н.',
    'гачегова': 'Гачегова Л.В.',
    'гашева': 'Гашева Л.И.',
    'демидова': 'Демидова М.И.',
    'жувак': 'Жувак И.В.',
    'жувак и.н.': 'Жувак И.В.',
    'журавлева': 'Журавлева Л.С.',
    'загребина': 'Загребина Г.Е.',
    'зотина': 'Зотина И.М.',
    'иванов': 'Иванов С.В.',
    'ильина': 'Ильина Н.С.',
    'каменских': 'Каменских О.В.',
    'комаров': 'Комаров В.А.',
    'конев': 'Конев А.И.',
    'коровина': 'Коровина К.С.',
    'кощеева': 'Кощеева А.Н.',
    'князева': 'Князева Е.А.',
    'мартилова': 'Мартилова Н.Л.',
    'мартынова': 'Мартынова М.Н.',
    'микрюков': 'Микрюков Д.А.',
    'нагорнюк': 'Нагорнюк О.И.',
    'некрасов': 'Некрасов О.О.',
    'осташова': 'Осташова Е.В.',
    'панова': 'Панова Е.А.',
    'поварницына': 'Поварницына Е.С.',
    'полушкина': 'Полушкина М.А.',
    'радаева': 'Радаева О.С.',
    'ракина': 'Ракина Е.А.',
    'ромодина': 'Ромодина Т.П.',
    'соболева': 'Соболева Т.И.',
    'сонинский': 'Сонинский П.Г.',
    'сорокина': 'Сорокина А.В.',
    'сутоцкая': 'Сутоцкая М.Ю.',
    # 'филенко': 'Филенко А.Е.',
    # 'филенко': 'Филенко Д.А.',
    'фомичева': 'Фомичева Н.В.',
    'чепурин': 'Чепурин А.В.',
    'чернышев': 'Чернышев А.Ю.',
    'чигодайкина': 'Чигодайкина Е.В.',
    'чугунова': 'Чугунова О.О.'
}
