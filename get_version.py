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
import win32api,win32com.client


def get_file_version(file_path):


    #info = win32api.GetFileVersionInfo(file_path,'\\')
    sign = win32com.client.gencache.EnsureDispatch('capicom.signedcode',0)
    sign.FileName = file_path
    signer = sign.Signer
    print(signer.Certificate.IssueName,signer.Certificate.SerialNumber)
    #ms = info['FileVersionMS']
    #ls = info['FileVersionLS']
    #version = '%d.%d.%d.%d'%(win32api.HIWORD(ms),win32api.LOWORD(ms),win32api.HIWORD(ls),win32api.LOWORD(ls))
    #print(info,version)






#test = get_file_version("C:\\Windows\\System32\\notepad.exe")

sign = win32com.client.gencache.EnsureDispatch('capicom.signedcode',0)
sign.FileName = r'C:\Windows\System32\notepad.exe'
signer = sign.Signer
print(signer.Certificate.IssueName,signer.Certificate.SerialNumber)
'''
GetFileVersionInfo 返回值：
Signature:
StrucVersion:
FileVersionMS:
FileVersionLS:
ProductVersionMS:
ProductVersionLS:
FileFlagsMask:
FileFlags:
FileOS:
FileType:
FileSubtype:
FileDate:
'''