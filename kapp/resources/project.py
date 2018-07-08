from flask import jsonify
from flask_restful import Resource, reqparse, abort
from kapp import database
from kapp.models import ProjectModel
import time, json

parser = reqparse.RequestParser()
parser.add_argument('title')

class Project(Resource):
    def get(self, id):
        return {'message': 'Project'}

class ProjectList(Resource):
    def post(self):
        args = parser.parse_args()
        project = ProjectModel(args['title'], time.time()).save().to_son()
        print(project)
        #TODO: return the object as json, at least the neccessary fields
