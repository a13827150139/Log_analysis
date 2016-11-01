import sqlite3
conn = sqlite3.connect('log.db')
cursor = conn.execute("SELECT ip,rejected,from_mail,to_mail,helo_mail  from log")
#cursor = conn.execute("SELECT ip from log")
#my=('INSERT INTO log (ip,rejected,from_mail,to_mail,helo_mail) VALUES ("asda", "asda", "asda", "asda", "%s" )' %('sss'))
# conn.execute(my);
# conn.commit()


#cursor = conn.execute("SELECT ID, file_path, file_size, createdate  from status_file")
for i in cursor:
    print(i)
conn.close()
