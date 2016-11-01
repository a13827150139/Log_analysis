# -*- encoding:utf-8 -*-
log_file = 'log_dir/file.log'
db_file_path="lo_db/log.db"
match = ['NOQUEUE'] #首次匹配出日志行的关键字
rule = {"ip":"(\d+\.\d+\.\d+\.\d+)",
      "rejected":"(rejected:.*;)",
      "from_mail":"from=<([a-zA-Z0-9_\.\-]*@+[a-zA-Z0-9_\.\-]*)", #匹配邮箱
      "to_mail":"to=<([a-zA-Z0-9_\.\-]*@+[a-zA-Z0-9_\.\-]*)",
      "helo_mail":"helo=<(.*)>"
      }
tp = (rule["ip"],rule["rejected"],rule["from_mail"],rule["to_mail"],rule["helo_mail"])

file=1


#print (tp.index(rule["rejected"]))

