#coding:utf-8
#@time     :     2018/7/23 18:34
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : test3.py
# @Software: PyCharm



def test1():
    item1 = (1,2,3,4,5,6,7,8,9)

    a = item1[1]
    print(a)
    for a in item1:
        print(a)

def test2(filename,outfile):
    file1 = open(filename)
    file2 = open(outfile,'w')
    for file_line in file1:
        outfile = file2.write(file_line)
        print(file_line)
    file1.close()
    file2.close()

#test1 = test1()
test2 = test2("C:\\pro\\LX\\testfile\\filename.txt","C:\\pro\\LX\\testfile\\outfile.txt")