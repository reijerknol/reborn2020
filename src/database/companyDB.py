from bson.objectid import ObjectId


class CompanyDB:

    def __init__(self, mongo):

        # API Database
        self.db = mongo["reborn2020"]
        self.collection = self.db["companies"]

    def getCompanyById(self, id):
        myquery = {"_id": ObjectId(id)}

        foundCompany = self.collection.find_one(myquery)
        return foundCompany


    def getAllMarkers(self):
        markers = []
        allCoords = self.collection.find({"coords": 1})
        print(allCoords)
        for x in allCoords:
            print(x)
        return markers

    # Read Record
    # def read(self, name, arg=False):
    #
    #     if arg:
    #
    #         return self.api[name].find_one(arg['query'])
    #
    #     else:
    #
    #         items = []
    #
    #         for item in self.api[name].find():
    #             item.pop('_id')
    #
    #             items.append(item)
    #
    #         return items

    # Create Record
    def create(self, company):
        self.collection.insert_one(company)
        return self.collection.find_one({'name': company.get('name')})
        #
        # if arg:
        #
        #     co = self.api[name]
        #
        #     id = arg['id'] = co.count() + 1
        #
        #     if co.insert_one(arg):
        #         return co.find_one({'id': id})

    # Update
    # def update(self, name, arg):
    #
    #     co = self.api[name]
    #
    #     if co.update_one(arg['query'], {'$set': arg['data']}).matched_count > 0:
    #         return co.find_one(arg['query'])
    #
    # # Delete
    # def delete(self, name, arg=False):
    #
    #     co = self.api[name]
    #
    #     if not co.delete_one(arg['query']):
    #         return