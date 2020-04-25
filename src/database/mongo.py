# Import
from pymongo import MongoClient

# Databases


mongo = MongoClient('localhost', 27017)


# Mongo
class Mongo:

    def __init__(self):
        self.app = mongo['myDatabase']
