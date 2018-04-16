#script to add more employees into database

import sqlite3

db = sqlite3.connect("employees.sqlite")

cursor = db.cursor()
cursor.execute("SELECT * FROM employee")

#returns as a list
# print(cursor.fetchall())

def extractall():
    for _id, name, email, DOB, designation in db.execute("SELECT * FROM employee"):
        print(_id)
        print(name)
        print(email)
        print(DOB)
        print(designation)
        print("--"*30)

#testing notes
# cursor.execute("INSERT INTO employee(name, email, DOB, designation) VALUES('tom', 'tom@gmkas.com', '090109', 'ceo')")

def addemployee():
    newName= input("Please enter the name")
    newemail= input("Please enter the email")
    newDOB= input("Please enter the DOB in DDMMYY format without /")
    newdesignation = input("Please enter designation")
    updatesql = cursor.execute("INSERT INTO employee(name, email, DOB, designation) VALUES('{}', '{}', '{}', '{}')".format(newName, newemail, newDOB, newdesignation))
    cursor.connection.commit()
    cursor.close()

print("{} rows updated".format(cursor.rowcount))
addemployee()
extractall()
db.close()

