import pymysql

def insertData(db,cursor):

    sql = "INSERT INTO student (id,name,age)VALUES (1,'tom',18),(2,'kitty',20);"
    try:
        cursor.execute(sql)
        db.commit()

        print("successfully insert data")

    except:
        db.rollback()

def creatTable(cursor):

    cursor.execute("drop database if exists students")
    cursor.execute("create database students")

    cursor.execute("use students")

    sql = "CREATE TABLE IF NOT EXISTS student(id BIGINT,name VARCHAR(20),age INT DEFAULT 1);"

    #cursor.execute("drop table if exists student")

    cursor.execute(sql)

    print("successfully create table")

def readTable(cursor):
    cursor.execute("select * from student")

    results = cursor.fetchall()

    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        print("id = ",id,"name = ",name,"age = ",age, '\n')

    print("successfully show table")

def findRecord(cursor,key,value):

    sql = "select * from student where " + key + "=" + "'"+value+"'"  #select * from database where key = 'value'
    cursor.execute(sql)
    result = cursor.fetchall()

    print(result, "successfully find")

def deleteRecord(cursor,key,value):
    sql = "delete from student where "+ key + "= '" + value+"'"  #delete from table where key = 'value'
    cursor.execute(sql)
    db.commit()

    print("successfully delete")

if __name__ == '__main__':

    db = pymysql.connect(host = "localhost",user = "root",password="root",port = 3306)

    cursor = db.cursor()


    creatTable(cursor)

    insertData(db,cursor)

    readTable(cursor)

    findRecord(cursor,"name","tom")

    deleteRecord(cursor,"name", "tom")

    sql = "update student set age = 30 where id =2"
    cursor.execute(sql)
    db.commit()

    readTable(cursor)

    cursor.close()
    db.close()