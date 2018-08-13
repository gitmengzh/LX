import wx,get_version1

datadic = get_version1.get_file_version1("C:\\Program Files (x86)\\COMODO\\test")


class Display_file(wx.Frame):
    def __init__(self, parent, title):

        wx.Frame.__init__(self,parent, title = title,size = (600,400))

        self.list = wx.ListCtrl(self,-1,style = wx.LC_REPORT)
        self.list.InsertColumn(0, "ID")
        self.list.InsertColumn(1,"filename")
        self.list.InsertColumn(2,"filepath")
        self.list.InsertColumn(3,"fileversion")

        items = datadic.items()
        for key,data in items:
            pass



        self.list.SetColumn(0,60)
        self.list.SetColumn(1,230)
        self.list.SetColumn(2,500)
        self.list.SetColumn(3,100)

        self.Show()


    if __name__ == "__main__":
        app = wx.App()
        frame = Display_file(None,"Display file")
        app.MainLoop()