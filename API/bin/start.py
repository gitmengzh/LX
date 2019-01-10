#coding:utf-8
#@time     :     2019/1/10 20:12
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : start.py
# @Software: PyCharm


import sys,os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,BASE_PATH)



from API.lib.main import server

server.run(port = 8080,host = "0.0.0.0", debug = True)