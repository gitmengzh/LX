
import pymysql


def test2():

    conn = pymysql.connect(host = "localhost", user = "root", passwd = "root",port = 3306 )
    cur = conn.cursor()

   #create database
    #sql1 = "create database test1_db character set utf8;"
    #cur.execute(sql1)

    #create new table
    sql2 = "use test_db;create table test1_tab(id int,name char(20)) character set utf8;"
    cur.execute(sql2)

    #insert data
    sql3 = "insert into test_tab(id,name) values ('1','tom'),('2','lily'),('3','jason')"
    cur.execute(sql3)

    #find data


    sql4 = "select * from test1_db"
    cur.execute(sql4)
    result = cur.fetchall()
    print(result)


test = test2()
