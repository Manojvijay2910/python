import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="password",database="mydb")
if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()
cursor.execute("select * from emp")

rows = cursor.fetchall()
print("Total Number of records:", cursor.rowcount)
for row in rows:
    print(row)

cursor.close()

conn.close()