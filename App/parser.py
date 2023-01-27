from openpyxl import load_workbook

from constants import weektable_classes, PROFILES
from database import ScheduleTable


class TableParser:
    def __init__(self, file_path: str):
        self.wb = load_workbook(file_path)
        self.sheet = self.wb['1 неделя ']
        self.schedule_db = ScheduleTable()

    def parse(self):
        days = {'понедельник': '23.01', 'вторник': '24.01', 'среда': '25.01', 'четверг': '26.01', 'пятница': '27.01'}  # TODO update

        for clas in range(3, 76, 3):
            if clas == 39:
                continue
            if clas > 39:
                clas -= 1

            merged_cells = self.sheet.merged_cells

            for day in range(4, 25, 5):
                date = days[self.sheet.cell(day, 1).value.lower()]
                for row in range(day, day + 5):

                    merged = False
                    for i in str(merged_cells).split():
                        if str(i).startswith(self.sheet.cell(row, clas).coordinate):
                            merged = True

                    number = row - day + 1
                    subject1 = self.sheet.cell(row, clas).value
                    try:
                        teacher1 = subject1[subject1.index('(') + 1: subject1.index(')')]
                        subject1 = subject1[:subject1.index('(') - 1]
                    except:
                        teacher1 = None


                    subject2 = self.sheet.cell(row, clas + 1).value
                    try:
                        teacher2 = subject1[subject1.index('(') + 1: subject1.index(')')]
                        subject2 = subject2[:subject1.index('(') - 1]
                    except:
                        teacher2 = None

                    classroom = str(self.sheet.cell(row, clas + 2).value)
                    if classroom.endswith('.0'):
                        classroom = classroom[:-2]

                    clas_to_write = PROFILES[weektable_classes.index(str(self.sheet.cell(2, clas).value))]
                    clas_number = clas_to_write[:2]
                    clas_profile = clas_to_write[2:]

                    if merged:
                        self.schedule_db.save(date, number, subject1, teacher1, clas_number, clas_profile, 1, classroom)
                        self.schedule_db.save(date, number, subject1, teacher1, clas_number, clas_profile, 2, classroom)
                    else:
                        classrooms = [classroom, classroom]
                        if '/' in classroom and classroom.lower() not in ['сп/з', 'с/з', 'а/з', 'акт/з', 'сп/зал',
                                                                          'с/зал', 'а/зал', 'акт/зал']:
                            classrooms = classroom.split('/')
                        self.schedule_db.save(date, number, subject1, teacher1, clas_number, clas_profile, 1, classrooms[0])
                        self.schedule_db.save(date, number, subject2, teacher2, clas_number, clas_profile, 2, classrooms[1])

    def clear(self):
        self.schedule_db.clear()


if __name__ == '__main__':
    parser = TableParser('resources/schedule/23.01week.xlsx')
    parser.clear()
    parser.parse()
