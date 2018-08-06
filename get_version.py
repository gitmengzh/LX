#coding:utf-8
#@time     :     2018/8/1 19:50
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : get_version.py
# @Software: PyCharm

#编写一个查看CCAV所有文件得签名，版本信息得带界面工具
#1 先编写不带界面工具,完成获取文件版本号工具，接下来其他属性
#2 编写带界面工具
#3 打包成exe
import win32api,win32com.client
import os,re


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

'''sign = win32com.client.gencache.EnsureDispatch('capicom.signedcode',0)
sign.FileName = r'C:\Windows\System32\notepad.exe'
signer = sign.Signer
print(signer.Certificate.IssueName,signer.Certificate.SerialNumber)'''
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

#通过OS.walk获取文件夹所有指定文件，包括子文件夹中
def get_all_files(folder_path):
    path2 = {}
    path = []
    filenames = []
    for maindir, subdir,file_name_list in os.walk(folder_path):
        for filename in file_name_list:
            if filename.endswith(('.exe','.dll','.sys')):
                apath = os.path.join(maindir,filename)
                path.append(apath)
                filenames.append(filename)

                #合并两个字典，将字典传给get_version函数
                path1 = dict(zip(path, filenames))
                path2.update(path1)

        print(path2)
        return (path2)
    try:
        new_path = os.path.join(maindir,subdir)
        test = get_all_files(new_path)
    except:
        print('no subdir')
        exit()





#test3 = get_all_files("C:\\Program Files (x86)\\COMODO\\test")

def get_file_version1(folder_path):
    file_path = get_all_files(folder_path)
    i = 0
    dict2 ={}
    for key in file_path:

        pe_names = list(file_path.values())
        try:
            info = win32api.GetFileVersionInfo(key,'\\')
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))

            dict1 = {pe_names[i]: version}
            dict2.update(dict1)
            i=i+1
        except:
            print("the file no version:" + key)


    print(dict2)

#test1 = get_all_files("C:\\Program Files (x86)\\COMODO\\COMODO Secure Shopping")
#test1 = get_file_version1("C:\\Program Files (x86)\\COMODO\\COMODO Secure Shopping")
test2 = get_file_version1("C:\\Program Files (x86)\\COMODO\\test")
#test3 = get_all_files("C:\\Program Files (x86)\\COMODO\\test")


























#test
def dict_test():
    dict1 = {'1:1','2:2','3:3'}
    dict2 = {'4:4','5:5','6:6'}
    dict1.update(dict2)
    print(dict1)


#test4 = dict_test()