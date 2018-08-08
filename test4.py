#coding:utf-8
#@time     :     2018/8/7 20:02
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : test4.py
# @Software: PyCharm


import os, string, shutil, re
import pefile
import codecs, sys
import wx
import struct


# 输出中打印Unicode字符
# sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)

def addToDict(theDict, PEfile_Path, strCompanyName):
    theDict.setdefault(PEfile_Path, []).append(strCompanyName)
    # 存在就在基础上加入列表，不存在就新建个字典key


def IsPeFile(inputFileName):
    '''''判断一个文件是否为PE文件'''
    file = open(inputFileName, 'r')
    dosSign = hex(struct.unpack("h", file.read(2))[0])
    if (dosSign == "0x5a4d"):
        file.seek(0x3c)
        date_fNew = struct.unpack("l", file.read(4))[0]
        file.seek(date_fNew)
        peSign = hex(struct.unpack("h", file.read(2))[0])
        if (peSign == "0x4550"):
            return 1
        else:
            return 0
    else:
        return 0

    # 得到一个文件的厂商信息


# 输入：文件路径
# 输出：字典
def getCompanyName(PEfile_Path):
    if not IsPeFile(PEfile_Path):
        return {}
    else:
        dictCompany = {}
    pe = pefile.PE(PEfile_Path)
    p = re.compile('''''CompanyName:(.+)''')
    for name in p.findall(pe.__str__()):
        uniCompanyName = name.replace('\\x', '\\u').strip()
        # strTemp = uniCompanyName.decode('unicode_escape')
        addToDict(dictCompany, PEfile_Path, uniCompanyName)

    writeDicToFile(dictCompany)  # 写入文件
    return dictCompany


# 得到文件夹中所有文件的厂商信息
# 输入：文件夹路径
# 输出：字典
def getCompanyNameFromDir(dir, dir_callback=None, file_callback=None):
    dictAll = {}
    for root, dirs, files in os.walk(dir):
        for f in files:
            file_path = os.path.join(root, f)
            if file_callback: file_callback(file_path)
            dictAll.update(getCompanyName(file_path))

    return dictAll


def writeDicToFile(dicName, outputFileName="company.txt"):
    """将字典写入文件中"""
    fileOutput = open(outputFileName, "a+")
    for key, value in dicName.items():
        strTemp2 = '' + value[0]
        strChina2 = strTemp2.decode('unicode_escape')

    try:
        fileOutput.write("%-*s" % (110, key))
        fileOutput.write(strChina2.encode('gb2312'))
    #except UnicodeEncodeError, e:
    except:
        pass
        fileOutput.write("\n")

    fileOutput.close()


# 主函数
if __name__ == "__main__":
    getCompanyNameFromDir(u"C:\\Program Files\\Notepad++\\notepad++.exe")
    print
    "ok finish"