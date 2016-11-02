# -*- encoding:utf-8 -*-
# -*- encoding:utf-8 -*-
import re
import sqlite3
from config.config import tp
import os
import sys
from config import config
import time
import sqlite3

sys.path.append(os.getcwd())


def log(oldsize,fsize):
    """处理动态的日志"""
    if oldsize > fsize:
        #如果已处理字符比文件的字符大，表示日志文件已切割，重新开始匹配。
        start_size = 0
        return start_size
    with open(config.log_file, 'r') as r2:
        while oldsize < fsize:
            #从指定游标开始匹配
            r2.seek(oldsize)
            logline = r2.readline().strip()
            #返回最新游标
            oldsize = r2.tell()
            start_size = oldsize
            
            # 导入匹配规则
            pwd = ("%s|%s|%s|%s|%s" % tp)
	    conn = sqlite3.connect(config.db_file_path)
            # 循环配置文件里面包含的关键字
            for Keyword in config.match:
                b = re.search(Keyword, logline)
                if b is not None:
                    end = re.findall(pwd, b.string)
	 	    if len(end) >= len(tp):
                        ip = end[tp.index(config.rule["ip"])][tp.index(config.rule["ip"])]  # 获取IP地址
                        rejected = end[tp.index(config.rule["rejected"])][tp.index(config.rule["rejected"])]
                        from_mail = end[tp.index(config.rule["from_mail"])][tp.index(config.rule["from_mail"])]  # 获取发件人
                        to_mail = end[tp.index(config.rule["to_mail"])][tp.index(config.rule["to_mail"])]  # 获取收件人
                        Helo_mail = end[tp.index(config.rule["helo_mail"])][tp.index(config.rule["helo_mail"])]
			print(rejected, to_mail, Helo_mail, to_mail, ip)
                        sql = (
                        'INSERT INTO log (ip,rejected,from_mail,to_mail,Helo_mail) VALUES ( "%s", "%s", "%s", "%s","%s" )' % (
                        ip, rejected, from_mail, to_mail, Helo_mail))
                        conn.execute(sql);
                        conn.commit()
	    conn.close()
	    return start_size
def old_or_new():
    """获取文件大小"""
    if os.path.exists(config.log_file):
        fsize = os.path.getsize(config.log_file)
        return fsize
    else:
        return False

def kais():
    start_size = 0
    while True:
        #判断文件有没有改变，有改变则执行日志分析函数
        if start_size != old_or_new():
            start_size=log(start_size, old_or_new())
        else :
           time.sleep(5)
