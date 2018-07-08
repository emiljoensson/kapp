import os

TESTING = True
DEBUG = True

# The secret key is used by Flask to encrypt session cookies
SECRET_KEY = 'secret'

# Mongo configuration
# If using mongolab, the connection URI is available from the mongolab control
# panel. If self-hosting on compute engine, replace the values below.
MONGO_URI = 'mongodb://user:password@127.0.0.1:27017/database'
