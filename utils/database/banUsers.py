import sqlite3 as sqlite
import logging
from datetime import datetime

class BanManager(object):
    def __init__(self, path):
        self.connect = sqlite.connect(path)
        self.connect.execute("pragma foreign_keys = on")
        self.connect.commit()
        self.cur = self.connect.cursor()

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS banUsers(
            id INTEGER UNIQUE,
            banStatus TEXT,
            dateOfBan TEXT,
            commentToBan TEXT,
        );''')
    
    def check_for_ban(self, id):
        self.cur.execute(f"SELECT banStatus FROM banUsers WHERE id = ?", (id,))
        banStatus = self.cur.fetchone()[0]
        if banStatus == "banned":
            return True
        else:
            return False
    
    def ban_user(self, id, comment):
        values = [id, "banned", datetime.now(), comment]
        try:
            self.cur.execute("INSERT INTO banUsers VALUES(?, ?, ?, ?)", values)
            self.connect.commit()
            logging.info(f"User: {values[0]}, забанен")
        except:
            self.cur.execute("UPDATE banUsers SET banStatus = ?, commentToBan = ? WHERE id = ?", (values[1], values[3], values[0],))
            self.connect.commit()
            logging.info(f"User: {values[0]}, забанен")
    
    def unban_user(self, id):
        self.cur.execute("UPDATE banUsers SET banStatus = ?, commentToBan = ? WHERE id = ?", ("unbanned", "", id,))
        self.connect.commit()

    
    def __del__(self):
        self.connect.close()