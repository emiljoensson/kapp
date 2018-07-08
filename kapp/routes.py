from .resources import *

def init_resources(api):
    api.add_resource(Project, '/project/<int:id>')
    api.add_resource(ProjectList, '/project')
