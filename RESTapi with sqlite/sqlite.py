#script to create the database

import sqlite3

db = sqlite3.connect("employees.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS employee (_id INTEGER PRIMARY KEY, name TEXT, email TEXT, DOB TEXT, designation TEXT)")

db.execute("INSERT INTO employee(_id, name, email, DOB, designation) VALUES(1, 'Rahul', 'rahulsinghpython@gmail.com', '050195', 'Programmer')")

db.execute("INSERT INTO employee(_id, name, email, DOB, designation) VALUES(2, 'Jaguir', '123@gmail.com', '100888', 'Lead Programmer')")

db.execute("INSERT INTO employee(_id, name, email, DOB, designation) VALUES(3, 'Kannan', 'abc@gmail.com', '050195', 'Business Head')")




## printing out the data
cursor = db.cursor()
cursor.execute("SELECT * FROM employee")

#returns as a list
# print(cursor.fetchall())


for _id, name, email, DOB, designation in cursor:
    print(_id)
    print(name)
    print(email)
    print(DOB)
    print(designation)
    print("--"*30)

cursor.close()
db.commit()
db.close()

