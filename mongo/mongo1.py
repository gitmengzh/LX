#coding:utf-8
#@time     :     2019/1/14 3:22
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : mongo1.py
# @Software: PyCharm


from pymongo import  MongoClient

conn = MongoClient('127.0.0.1',27017)
db = conn.mytest1
my_set = db.test_set

my_set.insert({"name":"zhangsan","age":18})

for i in my_set.find():
    print(i)