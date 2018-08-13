#coding:utf-8
#@time     :     2018/7/24 20:40
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : wx1.py
# @Software: PyCharm


import wx
def test():

    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "hello world!")
    frame.Show(True)
    app.MainLoop()