#coding:utf-8
#@time     :     2019/1/10 2:59
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : requet1.py
# @Software: PyCharm

import requests

r = requests.get(url='https://www.baidu.com')

print(r.status_code)

