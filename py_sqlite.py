#coding:utf-8
#@time     :     2018/7/23 19:11
#@Author     :    mengzh
#@file    :{name}.py
# @Site    : 
# @File    : py_sqlite.py
# @Software: PyCharm



import sqlite3
import datetime


#创建数据库和第一个表
def createdb():
    # 创建数据库
    conn = sqlite3.connect('./test.db')
    #创建游标
    cursor = conn.cursor()

    sql = '''
        CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME            TEXT    NOT NULL,
        AGE             INT     NOT NULL,
        ADDRESS         CHAR(50),
        SALARY          REAL);
        '''



    cursor.execute(sql)
    conn.commit()
    conn.close()


def insertdb():

    conn = sqlite3.connect('./test.db')

    cursor = conn.cursor()

    sql = '''
    INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000),(2, 'Allen', 25, 'Texas', 15000.00),(3, 'Teddy', 23, 'Norway', 13000),(4, 'Mark', 30, 'Rich-Mond', 54000.00)
     '''
    cursor.execute(sql)
    conn.commit()
    print("Insert successfully")
    conn.close()







def selectdb():

    conn = sqlite3.connect('./test.db')
    cursor = conn.cursor()
    sql = '''
        SELECT id, name, address, salary from COMPANY
     '''
    cursor.execute(sql)

    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("Address = ", row[2])
        print("Salary = ", row[3])

    conn.close()





def updatedb():
    conn = sqlite3.connect("./test.db")
    cursor = conn.cursor()

    sql = '''
    UPDATE COMPANY set SALARY = 90000 where ID=1
    '''
    cursor.execute(sql)
    conn.commit()
    print("Total number of rows updated:", conn.total_changes)

    c = conn.execute("SELECT id,name,address,salary from COMPANY")
    for row in c:
        print("ID = ",row[0])
        print("NAME = ",row[1])
        print("ADDRESS = ",row[2])
        print("SALARY = ",row[3])


    conn.close()


#test = updatedb()



def deletedb():

    conn = sqlite3.connect("./test.db")

    cursor = conn.cursor()
    sql ='''
    DELETE from COMPANY
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()





def deleteccavdb():
    start_time = datetime.datetime.now()
    conn = sqlite3.connect("./ccav.db")
    cursor = conn.cursor()
    sql = '''
    DELETE FROM white_sha1
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()
    end_time = datetime.datetime.now()
    print ((end_time-start_time).seconds)

test = deleteccavdb()

