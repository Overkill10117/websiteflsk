import sqlite3

con = sqlite3.connect("employee.db")
print("data opened successfully")

con.execute("create table employees(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, address TEXT NOT NULL)")
print("table created successfully")

con.close()