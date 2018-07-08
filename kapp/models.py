from pymodm import MongoModel, fields

class ProjectModel(MongoModel):
    #TODO: owner = fields.ReferenceField(User)
    title = fields.CharField()
    created = fields.CharField()
    class Meta:
        collection_name = 'project'
