



def checkSql(key='name',value='tom'):
    sql = "delete from student where " + key + "=" + value

    print(sql)



test = checkSql()