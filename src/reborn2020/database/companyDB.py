from bson.objectid import ObjectId


class CompanyDB(object):

    def __init__(self, mongo):
        # API Database
        self.db = mongo["reborn2020"]
        self.collection = self.db["companies"]

    def get_company_by_id(self, company_id):
        myquery = {"_id": ObjectId(company_id)}

        found_company = self.collection.find_one(myquery)
        return found_company

    def get_all_markers(self):
        return [[x["coords"], x["_id"], x["type"]] for x in self.collection.find()]

    def create(self, company):
        self.collection.insert_one(company)
        return self.collection.find_one({'name': company.get('name')})
