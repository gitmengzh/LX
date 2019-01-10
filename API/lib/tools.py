#coding:utf-8
#@time     :     2019/1/10 20:13
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : tools.py
# @Software: PyCharm

import pymysql
from API.conf import setting


def op_mysql(sql):
    conn = pymysql.connect(host=setting.MYSQL_HOST,user = setting.USER,
                           password = setting.PASSWORRD,port = setting.PORT,
                           charset = 'utf-8',db = setting.DB)

    cur = conn.cursor(cursor = pymysql.cursors.DictCursor)

    cur.execute(sql)
    sql_start = sql[:6].upper()
    if sql_start == 'SELECT':
        res = cur.fetchall()
    else:
        conn.connect()
        res = 'ok'
    cur.close()
    conn.close()
    return res