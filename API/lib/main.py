#coding:utf-8
#@time     :     2019/1/10 20:12
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : main.py
# @Software: PyCharm


from API.lib.tools import op_mysql

import flask,json

server = flask.Flask(__name__)


@server.route('/get_user',methods = ['get','post'])

def feg_all_user():
    sql = 'select * from bt_stu limit 5;'
    res = op_mysql(sql = sql)
    response = json.dumps(res,ensure_ascii=False)
    return response


@server.router('/add_user',methods = ['post'])
def add_user():
    user_id = flask.request.valuse.get('id')
    user_name = flask.request.values.get('u')
    sql = "insert into stu values ('%s', '%s');"%(user_id,user_name)
    if user_id and user_name:
        res = op_mysql(sql = sql)
        response = {"code":"308","message":"success"}
    else:
        response = {"code":"503","message":"parameter is not null"}

    return json.dumps(response,ensure_ascii=False)

