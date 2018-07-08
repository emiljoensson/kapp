from flask_pymongo import PyMongo, MongoClient
from kapp import models
from pymodm import connect

#TODO: Connect using the URI in config.py
client = MongoClient('mongodb://localhost:27017/')
db = client.kapp

# Connect PyMODM
#TODO: Connect using the URI in config.py
connect('mongodb://localhost:27017/kapp')

# dev debug stuff
from pprint import pprint
print(client.database_names())
pprint(db.collection_names())
cursor = db.project.find({})
for document in cursor:
    pprint(document)
#db.project.drop()
