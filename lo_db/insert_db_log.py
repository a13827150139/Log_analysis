# -*- encoding:utf-8 -*-
import sqlite3
conn = sqlite3.connect('DB/log.db')
cursor = conn.execute("SELECT ip,rejected,from_mail,to_mail,helo_mail  from log")
my=('INSERT INTO log (ip,rejected,from_mail,to_mail,helo_mail) VALUES ("asda", "asda", "asda", "asda", "%s" )' %('sss'))
conn.execute(my);
conn.commit()