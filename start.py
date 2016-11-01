# # -*- encoding:utf-8 -*-
import os
import sys
sys.path.append(os.getcwd())
from comm import start_log
from lo_db.db_sql import db_sql
from config import config



if __name__ == '__main__':
    """判断数据库是否存在，是就删除"""
    if os.path.isfile(config.db_file_path):
        os.remove(config.db_file_path)
        db_sql().create_db()#初始化数据库
        start_log.kais()  # 开始分析日志
    else:
        db_sql().create_db()  # 初始化数据库
        start_log.kais()  # 开始分析日志
