import pymysql

def connect_mysql():
     conn = pymysql.connect(host="localhost",user="root",password="root",db="world",port=3306)

     cur = conn.cursor()
     sql1 = "select Name from city"

     try:
         cur.execute(sql1)
         result1 = cur.fetchone()


         #len1=len(results)
         print(result1)


     except Exception as e:
         raise e
     finally:
         conn.close()




test = connect_mysql()

