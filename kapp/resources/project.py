from flask_restful import Resource, reqparse, abort
from kapp import database

parser = reqparse.RequestParser()
parser.add_argument('title')

class Project(Resource):
    def get(self, id):
        result = database.read(id)
        if result is None:
            abort(404)
        return(result)

class ProjectList(Resource):
    def get():
        #TODO: Get all entities
        pass

    def post(self):
        args = parser.parse_args()
        result = database.save(args)
        return(result)
