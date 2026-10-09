import psycopg2

conn = psycopg2.connect(database="employeedb", user="postgres", password="password", host="127.0.0.1", port="5432")
print("Connected To EmployeeDB")

cursor = conn.cursor()
cursor.execute("insert into employee (name, sal) values ('John', 20000)")
conn.commit()
print("Employee Created")
cursor.close()
conn.close()