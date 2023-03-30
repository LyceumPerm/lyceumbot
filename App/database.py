import sqlite3

DB_PATH = 'lyceumbot.db'


class UserTable:
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()

    def save_user(self, telegram_id, username, name, clas_number, clas_profile, group):
        query = 'INSERT INTO user (telegram_id, username, name, class_number, class_profile, class_group)  VALUES (?, ?, ?, ?, (SELECT id FROM profile WHERE name = ?), ?);'
        self.cur.execute(query, (telegram_id, username, name, clas_number, clas_profile, group))
        self.con.commit()

    def get_user(self, telegram_id):
        query = 'SELECT * FROM user WHERE telegram_id = ?;'
        return self.cur.execute(query, (telegram_id,)).fetchone()

    def get_all_users(self):
        query = 'SELECT * FROM user;'
        return self.cur.execute(query).fetchall()

    def user_exists(self, telegram_id):
        return self.get_user(telegram_id) is not None

    def delete_user(self, telegram_id):
        query = 'DELETE FROM user WHERE telegram_id = ?;'
        self.cur.execute(query, (telegram_id,))
        self.con.commit()

    def update_user(self, id, telegram_id, username, name, clas_number, clas_profile, group):
        query = 'UPDATE user SET telegram_id = ?, username = ?, name = ?, class_number = ?, class_profile = (SELECT id from profile WHERE name = ?), class_group = ? WHERE id = ?;'
        self.cur.execute(query, (telegram_id, username, name, clas_number, clas_profile, group, id))
        self.con.commit()

    def get_state(self, telegram_id):
        query = 'SELECT `state` FROM user WHERE telegram_id = ?;'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_state(self, telegram_id, state):
        query = 'UPDATE user SET state = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (state, telegram_id))
        self.con.commit()

    def get_class_number(self, telegram_id):
        query = 'SELECT class_number FROM user WHERE telegram_id = ?;'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_class_number(self, telegram_id, clas_number):
        query = 'UPDATE user SET class_number = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (clas_number, telegram_id))
        self.con.commit()

    def get_class_profile(self, telegram_id):
        query = 'SELECT name FROM profile WHERE id = (SELECT class_profile FROM user WHERE telegram_id = ?);'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_class_profile(self, telegram_id, clas_profile):
        query = 'UPDATE user SET class_profile = (SELECT id FROM profile WHERE name = ?) WHERE telegram_id = ?;'
        self.cur.execute(query, (clas_profile, telegram_id))
        self.con.commit()

    def get_group(self, telegram_id):
        query = 'SELECT class_group FROM user WHERE telegram_id = ?;'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_group(self, telegram_id, group):
        query = 'UPDATE user SET class_group = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (group, telegram_id))
        self.con.commit()

    def get_lastmessage(self, telegram_id):
        query = 'SELECT prev_msg_time FROM user WHERE telegram_id = ?;'
        return self.cur.execute(query, (telegram_id,)).fetchone()[0]

    def set_lastmessage(self, telegram_id, last_message):
        query = 'UPDATE user SET prev_msg_time = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (last_message, telegram_id))
        self.con.commit()


class ScheduleTable:
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()

    def save(self, date: str, number: int, name: str, teacher: str, clas_number: int, clas_profile: str, group: int,
             classroom: str):
        query = 'INSERT INTO schedule (date, number, name, teacher, class_number, class_profile, class_group, classroom) VALUES (?, ?, ?, ?, ?, (SELECT id FROM profile WHERE name = ?), ?, ?);'
        self.cur.execute(query, (date, number, name, teacher, clas_number, clas_profile, group, classroom))
        self.con.commit()

    def get(self, date: str, clas_number: int, clas_profile: str):
        clas_profile = self.cur.execute('SELECT id FROM profile WHERE name = ?', (clas_profile,)).fetchone()[0]
        query = 'SELECT * FROM schedule WHERE date = ? and class_number = ? and class_profile = ? ORDER BY number;'
        return self.cur.execute(query, (date, clas_number, clas_profile)).fetchall()

    def get_for_group(self, date: str, clas_number: int, clas_profile: str, group: int):
        clas_profile = self.cur.execute('SELECT id FROM profile WHERE name = ?', (clas_profile,)).fetchone()[0]
        query = 'SELECT * FROM schedule WHERE date = ? and class_number = ? and class_profile = ? and class_group = ? ORDER BY number;'
        return self.cur.execute(query, (date, clas_number, clas_profile, group)).fetchall()

    def get_for_teacher(self, date: str, teacher: str):
        query = 'SELECT * FROM schedule WHERE date = ? and teacher = ? ORDER BY number;'
        return self.cur.execute(query, (date, teacher)).fetchall()

    def clear(self, days_to_delete):
        query = 'DELETE FROM schedule WHERE date IN (?, ?, ?, ?, ?);'
        self.cur.execute(query, days_to_delete)
        self.con.commit()
