from flask import Flask, request
from flask_restful import reqparse, Resource, Api

from nichescore.app import api, db
from nichescore.models import Animal


class AnimalsResource(Resource):
    def get(self, animal_id):
        animal = db.session.query(Animal).filter_by(id=animal_id).first()
        if not animal:
            return {'message': 'Not found'}, 404
        return {animal_id: animal}

    def put(self, animal_id):
        animal = db.query(Animal).filter_by(id=animal_id)
        animal.color = request.form['color']
        db.session.commit()
        return {animal_id: animal}


class AnimalsListResource(Resource):

    def get(self):
        return [{animal.id: {'name': animal.name, 'color': animal.color}} for animal in db.session.query(Animal).all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('color')
        args = parser.parse_args()
        if not 'name' in args or not 'color' in args:
            # we return bad request since we require name and color
            return {'message': 'Missing required parameters.'}, 400
        new_animal = Animal(name=args['name'], color=args['color'])
        db.session.add(new_animal)
        db.session.commit()
        return {new_animal.id: {'name': animal.name, 'color': animal.color}}, 201

api.add_resource(AnimalsResource, 'animal/<animal_id>')
api.add_resource(AnimalsListResource, 'animals')