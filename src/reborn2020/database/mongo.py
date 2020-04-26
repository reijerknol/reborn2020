# Import
from pymongo import MongoClient

from reborn2020.database.companyDB import CompanyDB

# Databases if running on local mongo
# mongo = MongoClient('localhost', 27017)

# If you use the docker-compose use the line below!!
mongo = MongoClient('mongo', 27017, username="root", password="s3cr3t")


# db = mongo["reborn2020"]


# Mongo
class Mongo(object):

    def __init__(self):
        self.companyDB = CompanyDB(mongo)
