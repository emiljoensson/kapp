#from kapp import models
from google.cloud import datastore
import json

#TODO: 	datastore.Client(current_app.config['PROJECT_ID'])
def get_client():
    return datastore.Client('kapp-209616')

builtin_list = list

# [START from_datastore]
def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application by adding the key id as a key-value pair inside the entity
    i.e from
        <Entity('project', 562) {'title': 'hello'}>
    to:
        <Entity('project', 562) {'title': 'hello', 'id': 562}>
    and then converts it into JSON, ie:
        { "title": "GCP Console", "created": 1531135300, "id": 5629499534213120 }
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()
        print(entity)
    entity['id'] = entity.key.id

    # to JSON
    entity = '{' + str(entity).rsplit('{', 1)[1]
    entity = entity[:-1].replace("'", '"')

    return json.loads(entity)
# [END from_datastore]


def read(id=None):
    ds = get_client()
    key = ds.key('project', int(id))
    query = ds.get(key)
    entity = from_datastore(query) # will be None if entity doesn't exist
    return entity
