'''Connection to MongoDB.'''

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connection():
    uri = "mongodb+srv://andypan159:W9hw0C06jPfKgYJA@cluster-0.fqh8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-0"
    return MongoClient(uri, server_api=ServerApi('1'))