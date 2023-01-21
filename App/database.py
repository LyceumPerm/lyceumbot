import sqlite3

DB_PATH = 'lyceumbot.db'


class UserTable:
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()

    def save_user(self, telegram_id, username, name, clas, group):
        query = 'INSERT INTO user (telegram_id, username, name, clas_id, "group")  VALUES (?, ?, ?, (SELECT id FROM class WHERE name = ?), ?);'
        self.cur.execute(query, (telegram_id, username, name, clas, group))
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

    def update_user(self, id, telegram_id, username, name, clas, group):
        query = 'UPDATE user SET telegram_id = ?, username = ?, name = ?, clas_id = (SELECT id from class WHERE name = ?), "group" = ? WHERE id = ?;'
        self.cur.execute(query, (telegram_id, username, name, clas, group, id))
        self.con.commit()

    def get_state(self, telegram_id):
        query = 'SELECT `state` FROM user WHERE telegram_id = ?;'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_state(self, telegram_id, state):
        query = 'UPDATE user SET state = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (state, telegram_id))
        self.con.commit()

    def get_clas(self, telegram_id):
        query = 'SELECT name FROM class WHERE id = (SELECT clas_id FROM user WHERE telegram_id = ?)'
        # query = 'SELECT clas FROM user WHERE telegram_id = ?;'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_clas(self, telegram_id, clas):
        query = 'UPDATE user SET clas_id = (SELECT id FROM class WHERE name = ?) WHERE telegram_id = ?;'
        self.cur.execute(query, (clas, telegram_id))
        self.con.commit()

    def get_group(self, telegram_id):
        query = 'SELECT "group" FROM user WHERE telegram_id = ?;'
        result = self.cur.execute(query, (telegram_id,)).fetchone()
        return result[0]

    def set_group(self, telegram_id, group):
        query = 'UPDATE user SET `group` = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (group, telegram_id))
        self.con.commit()

    def get_lastmessage(self, telegram_id):
        query = 'SELECT last_message FROM user WHERE telegram_id = ?;'
        return self.cur.execute(query, (telegram_id,)).fetchone()[0]

    def set_lastmessage(self, telegram_id, last_message):
        query = 'UPDATE user SET last_message = ? WHERE telegram_id = ?;'
        self.cur.execute(query, (last_message, telegram_id))
        self.con.commit()


class ScheduleTable:
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()

    def save(self, date: str, number: int, name: str, clas: str, group: int, classroom: str):
        query = 'INSERT INTO schedule (date, number, name, clas_id, "group", classroom) VALUES (?, ?, ?, (SELECT id FROM class WHERE name = ?), ?, ?);'
        self.cur.execute(query, (date, number, name, clas, group, classroom))
        self.con.commit()

    def get(self, date: str, clas: str, group: int):
        clas_id = self.cur.execute('SELECT id FROM class WHERE name = ?', (clas,)).fetchone()[0]
        query = 'SELECT * FROM schedule WHERE date = ? and clas_id = ? and "group" = ? ORDER BY number;'
        return self.cur.execute(query, (date, clas_id, group)).fetchall()

    def clear(self):
        query = 'DELETE FROM schedule;'
        self.cur.execute(query)
        self.con.commit()
