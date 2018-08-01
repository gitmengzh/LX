#coding:utf-8
#@time     :     2018/8/1 19:50
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : get_version.py
# @Software: PyCharm

#编写一个查看CCAV所有文件得签名，版本信息得带界面工具
#1 先编写不带界面工具
#2 编写带界面工具
#3 打包成exe
import win32api


def get_file_version(file_path):


    version = win32api.GetFileVersionInfo(file_path,'\\')
    print(version)





test = get_file_version("C:\\Windows\\System32\\notepad.exe")