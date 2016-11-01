# -*- encoding:utf-8 -*-
import sqlite3
from config import config

class db_sql:
    def __init__(self):
        self.sqlit_db = ("sqlite3.connect(%s)" % config.db_file_path)
    def create_db(self):
        conn = sqlite3.connect(config.db_file_path)
        conn.execute('''CREATE TABLE log
            (ID integer PRIMARY KEY autoincrement,
            ip           CHAR(50)    NOT NULL,
            rejected            CHAR(50)     NOT NULL,
            from_mail        CHAR(50),
            to_mail          CHAR(50),
            helo_mail         CHAR(50),
            createdate      datetime default (datetime('now', 'localtime')));''')
        conn.close()




