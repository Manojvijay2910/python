import psycopg2

conn = psycopg2.connect(database="employeedb", user="postgres", password="password", host="127.0.0.1", port="5432")
print("Connected To EmployeeDB")

cursor = conn.cursor()
cursor.execute("select * from employee")
rows = cursor.fetchall()
for row in rows:
    print(row)
    
cursor.close()
conn.close()