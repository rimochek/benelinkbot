import sqlite3 as sqlite
import logging

class UsersManager(object):
    def __init__(self, path):
        self.connect = sqlite.connect(path)
        self.connect.execute("pragma foreign_keys = on")
        self.connect.commit()
        self.cur = self.connect.cursor()

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER UNIQUE,
            userName TEXT,
            realName TEXT,
            language TEXT,
            age TEXT,
            userType TEXT,
            phoneNumber TEXT,
            location TEXT
        );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS banUsers(
            id INTEGER UNIQUE,
            banStatus TEXT,
            dateOfBan TEXT,
            commentToBan TEXT
        );''')
        self.connect.commit()
    
    def add_user(self, message):
        values = [message.chat.id, message.from_user.username, None, "en", None, None, None, None]
        try:
            self.cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)", values)
            self.connect.commit()
            logging.info(f"User: {values[0]}, добавлен в базу данных")
            return True
        except:
            logging.info(f"User: {values[0]}, не может быть добавлен в БД, так как он уже там находится")
            return False
    
    def check_user_in_base(self, id):
        self.cur.execute(f"SELECT * FROM users WHERE id = {id}")
        user = self.cur.fetchone()
        if user:
            return True
        else:
            return False
    
    def set_user_language(self, id, language):
        self.cur.execute(f"UPDATE users SET language = ? WHERE id = ?", (language, id,))
        self.connect.commit()
        logging.info(f"User: {id}, поменял язык на {language}")

    def get_user_language(self, id):
        self.cur.execute(f"SELECT language FROM users WHERE id = {id}")
        language = self.cur.fetchone()[0]
        return language
    
    def set_user_type(self, id, userType):
        self.cur.execute(f"UPDATE users SET userType = ? WHERE id = ?", (userType, id,))
        self.connect.commit()
        logging.info(f"User: {id}, поставил тип пользователя: {userType}")
    
    def get_user_type(self, id):
        self.cur.execute(f"SELECT userType FROM users WHERE id = ?", (id,))
        userType = self.cur.fetchone()[0]
        return userType

    def set_name(self, id, name):
        self.cur.execute(f"UPDATE users SET realName = ? WHERE id = ?", (name, id,))
        self.connect.commit()
        logging.info(f"User: {id}, поставил себе имя: {name}")
    
    def get_name(self, id):
        self.cur.execute(f"SELECT realName FROM users WHERE id = ?", (id,))
        name = self.cur.fetchone()[0]
        return name

    def set_phone_number(self, id, number):
        self.cur.execute(f"UPDATE users SET phoneNumber = ? WHERE id = ?", (number, id,))
        self.connect.commit()
        logging.info(f"User: {id}, поставил номер: {number}")
    
    def get_phone_number(self, id):
        self.cur.execute(f"SELECT phoneNumber FROM users WHERE id = ?", (id,))
        number = self.cur.fetchone()[0]
        return number

    def set_location(self, id, location):
        self.cur.execute(f"UPDATE users SET location = ? WHERE id = ?", (location, id,))
        self.connect.commit()
        logging.info(f"User: {id}, поставил локацию: {location}")
    
    def get_location(self, id):
        self.cur.execute(f"SELECT location FROM users WHERE id = ?", (id,))
        location = self.cur.fetchone()[0]
        return location
    
    def __del__(self):
        self.connect.close()