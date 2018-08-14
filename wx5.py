#coding:utf-8
#@time     :     2018/8/10 20:14
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : wx.py
# @Software: PyCharm




import wx



'''
class ListBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"List Box",size = (300,200))
        panel = wx.Panel(self,-1)

        sampleList = ['zero', 'one', 'two', 'three']
        listBox = wx.ListBox(panel, -1, (20,20),(80,120),sampleList, wx.LB_SINGLE)
        listBox.SetSelection(3)

'''

bookdata = {
    1:("test1","2011-1-1"),
    2:("test2","2011-2-2"),
    3:("test3","2013-3-3"),

}


class  LibrarySys(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__( self, parent,-1,size=(400,600))

        self.list = wx.ListCtrl(self,-1,style =wx.LC_REPORT)

        self.list.InsertColumn(0, "ID")
        self.list.InsertColumn(1, "name")
        self.list.InsertColumn(2, "date")

        items = bookdata.items()

        for key, data in items:
            index = self.list.InsertItem(self.list.GetItemCount(),str(key))
            self.list.SetItem(index,1,data[0])
            self.list.SetItem(index,2,data[1])

        self.list.SetColumnWidth(0,60)
        self.list.SetColumnWidth(1,230)
        self.list.SetColumnWidth(2,90)

        self.Show()





if __name__ == '__main__':
    app = wx.App()
    fram = LibrarySys(None)
    app.MainLoop()




