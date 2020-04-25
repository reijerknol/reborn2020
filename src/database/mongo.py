# Import
from pymongo import MongoClient

from src.database.companyDB import CompanyDB

# Databases
# mongo = MongoClient('localhost', 27017)
mongo = MongoClient('localhost', 27017, username="root", password="example")  # Ivo's config


# db = mongo["reborn2020"]


# Mongo
class Mongo:

    def __init__(self):
        self.companyDB = CompanyDB(mongo)
