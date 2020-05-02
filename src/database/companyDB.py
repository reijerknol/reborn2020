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
        return [[x["coords"], x["_id"], x["type"]] for x in self.collection.find() if "coords" in x and x["coords"]]

    def find_company(self, query):
        myquery = {"$or": [{"$text": {"$search": query}}, {"jobs": query}]}
        result = self.collection.find(myquery)
        return [{key: val for key, val in item.items() if key not in ["email", "phone", "coords"]} for item in result]


    def get_counters(self):
        all_companies = self.collection.find().count()
        jobs_danger = sum([int(item["jobs"])for item in self.collection.find({"type": "needHelp"})])
        companies_rescued = self.collection.find({"type": "story"})

        return {
            "all_companies": all_companies,
            "jobs_danger": jobs_danger,
            "companies_rescued": companies_rescued.count(),
            "jobs_rescued": 0
        }

    def create(self, company):
        self.collection.insert_one(company)
        return self.collection.find_one({'name': company.get('name')})
