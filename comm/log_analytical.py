# -*- encoding:utf-8 -*-
import re
from config import config
import os
import sqlite3
from config.config import tp

def log_analytical():
    '''reject日志分析获取 IP,收件人,发件人,拒收原因,helo标识
       如果日志文件是静态的用这个来执行
                                             '''
    fsize = os.path.getsize(config.log_file)
    conn = sqlite3.connect('DB/log.db')
    with open(config.log_file, 'r') as r2:
        while r2.tell() < fsize:
            logline = r2.readline().strip()
            #导入匹配规则
            pwd = ("%s|%s|%s|%s|%s" % tp)
            # 循环配置文件里面包含的关键字
            for Keyword in config.match:
                b = re.search(Keyword, logline)
                if b is not None:
                    end = re.findall(pwd, b.string)
                    #长度为5就匹配正常，否则日志里面有其他日志包含了config.match（NOQUEUE）
                    if len(end) >= len(tp):
                        ip = end[tp.index(config.rule["ip"])][tp.index(config.rule["ip"])]#获取IP地址
                        rejected = end[tp.index(config.rule["rejected"])][tp.index(config.rule["rejected"])]
                        from_mail = end[tp.index(config.rule["from_mail"])][tp.index(config.rule["from_mail"])]#获取发件人
                        to_mail = end[tp.index(config.rule["to_mail"])][tp.index(config.rule["to_mail"])]#获取收件人
                        Helo_mail = end[tp.index(config.rule["helo_mail"])][tp.index(config.rule["helo_mail"])]
                        print (rejected, to_mail, Helo_mail, to_mail, ip)
                        sql=('INSERT INTO log (ip,rejected,from_mail,to_mail,Helo_mail) VALUES ( "%s", "%s", "%s", "%s","%s" )' %(ip, rejected, from_mail, to_mail, Helo_mail))
                        conn.execute(sql);
                        conn.commit()
        conn.close()
        return r2.tell()
if __name__ == '__main__':
    log_analytical()

