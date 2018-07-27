#coding:utf-8
#@time     :     2018/1/30 20:05
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : RemoteWindows.py
# @Software: PyCharm



import  wmi
def remote(ipaddress,user,password):
    conn = wmi.WMI(ipaddress,user=user, password=password)
    for sys in conn.Win32_OperatingSystem():
        print "Version:%s" % sys.Caption.encode("UTF8"), "Vernum:%s" % sys.BuildNumber  # system information
        print sys.OSArchitecture.encode("UTF8")  # OS architecture
        print sys.NumberOfProcesses  # OS process

    try:
        filename = r"C:\Users\Administrator\Desktop\test\test.bat"
        cmd_callbat = r"cmc /c call %s" %filename
        #cmd_callbat = r"cmd.exe /c call calc.exe"
        #cmd_callbat = r"start C:\test.bat"
        conn.Win32_Process.Create(CommandLine = cmd_callbat)
        print "run successfully"
    except Exception as e:
            print(e)



if __name__ == "__main__":
    remote(ipaddress = "172.0.1.12", user = "work", password = "123")