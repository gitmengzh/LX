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


def get_folder_pe_file(folder_path):

    #re.match(r'.exe.dll.sys')

    #file_tpye = ([])
    names = os.listdir(folder_path)
    path = []
    pe_names = []
    for name in names:
        path = folder_path+'\\'+name
        if os.path.isdir(path):
            path = folder_path+'\\'+name
        else:
            if name.endswith(('.exe','.dll','.sys')):
                pe_names = name
                print(pe_names)
                file_path = folder_path+'\\'+pe_names






#test = get_folder_pe_file("C:\\Program Files (x86)\\COMODO\\COMODO Secure Shopping")
#test = get_folder_pe_file("C:\\Program Files (x86)\\COMODO\\test")

#通过OS.walk获取文件夹所有指定文件，包括子文件夹中
def get_all_files(folder_path):

    for maindir, subdir,file_name_list in os.walk(folder_path):
        for filename in file_name_list:
            if filename.endswith(('.exe','.dll','.sys')):
                apath = os.path.join(maindir,filename)
                path = []
                filenames = []
                path.append(apath)
                filenames.append(filename)

                #如何合并两个字典，将字典传给get_version函数
                path1 = dict(zip(path, filenames))
                path2 = dict(path1)
                path2.update(path2)

    print(path2)

    try:
        new_path = os.path.join(maindir,subdir)
        test = get_all_files(new_path)
    except:
        print('no subdir')
        exit()



    # return apath,filename

#test3 = get_all_files("C:\\Program Files (x86)\\COMODO\\test")

def get_file_version1(folder_path):
    file_path = get_all_files(folder_path)
    pe_names = file_path[1]
    try:
        info = win32api.GetFileVersionInfo(file_path[0], '\\')
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))

        dict = {pe_names: version}
    except:
        print("the file no version")


    print(dict)

#test1 = get_all_files("C:\\Program Files (x86)\\COMODO\\COMODO Secure Shopping")
#test2 = get_file_version1("C:\\Program Files (x86)\\COMODO\\test")
test3 = get_all_files("C:\\Program Files (x86)\\COMODO\\test")


