from flask import Flask, jsonify, abort, request, json
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)




# def init_db():
#     """For use on command line for setting up
#     the database.
#     """
#
#     db.drop_all()
#     db.create_all()
#
#     test_memory = Memory(text=app.config["FIRST_MESSAGE"])
#     db.session.add(test_memory)
#     db.session.commit()


# class ComplexEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, complex):
#             return [obj.real, obj.imag]
#         # Let the base class default method raise the TypeError
#         return json.JSONEncoder.default(self, obj)


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30))
    DOB = db.Column(db.Date)
    Designation = db.Column(db.String(50))

    def __init__(self, name, email, DOB, Designation):
        self.name = name
        self.email = email
        self.DOB = datetime.datetime.strptime(DOB, "%d%m%Y").date()
        self.Designation = Designation

    # def __str__(self):
    #     return str(self.__class__) + ": " + str(self.__dict__)


@app.route('/', methods=['GET'])
def test():
    return jsonify()

@app.route('/dev/', methods = ['GET'])
def index():
    return jsonify({'developers': Developer.query.all()})

@app.route('/dev/<int:id>/')
def get_dev(id):
    return jsonify({'developer': Developer.query.get(id)})

@app.route('/dev/', methods = ['POST'])
def create_dev():
    if not request.json or not 'name' in request.json:
        abort(400)
    dev = Developer(request.json.get('name'), request.json.get('email'), request.json.get('DOB'), request.json.get('Designation'))
    db.session.add(dev)
    db.session.commit()

    dev2 = Developer.id, Developer.name, Developer.email, dev.DOB, Developer.Designation
    print(dev2)
    print(dev.name)
    print(dev)
    print(Developer)
    return jsonify(dev.name, dev.email, dev.DOB, dev.Designation)
    # # json.dumps(dev, cls=ComplexEncoder)
    # return jsonify({'Developer': dev}), 201

@app.route('/dev/<int:id>', methods = ['DELETE'])
def delete_dev(id):
    db.session.delete(Users.query.get(id))
    db.session.commit()
    return jsonify( { 'result': True } )

@app.route('/dev/<int:id>', methods = ['PUT'])
def update_dev(id):
    dev = Developer.query.get(id)
    dev.name = request.json.get('name', dev.name)
    dev.email = request.json.get('email', dev.name)
    dev.DOB = request.json.get('DOB',dev.name)
    dev.Designation = request.json.get('Designation', dev.Designation)
    db.session.commit()

    return jsonify( { 'dev': dev } )

db.create_all()

if __name__ == '__main__':
    app.run()