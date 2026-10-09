import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="password",database="mydb")
if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(3, 'Rahul', 30000)")
    conn.commit()
    print("Employee Added")
except:
    conn.rollback()

cursor.close()

conn.close()