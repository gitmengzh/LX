import pymysql

def connect_mysql():
     conn = pymysql.connect(host="localhost",user="root",password="root",db="world",port=3306)

     cur = conn.cursor()
     sql1 = "select Name from city"

     try:
         cur.execute(sql1)
         results = cur.fetchall()

         len1=len(results)
         print(results,len1)


     except Exception as e:
         raise e
     finally:
         conn.close()




test = connect_mysql()

