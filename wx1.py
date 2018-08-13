#coding:utf-8
#@time     :     2018/7/24 20:40
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : wx1.py
# @Software: PyCharm

import wx


app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "hello world!")
frame.Show(True)
app.MainLoop()



def wx1():
    app = wx.App(False)
    window = wx.Frame(None,title = "wxPyton", size = (100,300))
    panel = wx.Panel(window)
    label = wx.StaticText(panel,label = "Hello world", pos =(100,100))
    window.Show(True)
    app.MainLoop()

test = wx1()