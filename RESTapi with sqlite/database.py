#a simple program to load up a server and search in api form

import sqlite3

from flask import Flask, jsonify, request
## printing out the data

db = sqlite3.connect("employees.sqlite")
cursor = db.cursor()
cursor.execute("SELECT * FROM employee")

#returns as a list
fulllist = cursor.fetchall()
print(fulllist)

for _id, name, email, DOB, designation in fulllist:
    pass




app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It Works!'})

@app.route('/data', methods=['GET'])
def returnall():
    return jsonify({'list': fulllist})

@app.route('/data/<string:name>', methods=['GET'])
def returnOne(name):
    names = [fulllist for fulllist in fulllist if fulllist[1] == name]
    return jsonify({'name' : names[0]})

@app.route('/data', methods=['POST'])
def addone():
    new = {"ID" : request.json["_id"], "name:" : request.json["name"], "email" : request.json["email"], "DOB" : request.json["DOB"], "Designation" : request.json["Designation"]}

    fulllist.append(new)
    return jsonify({'fulllist'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
