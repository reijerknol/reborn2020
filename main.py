from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import json
import pymongo


from werkzeug.exceptions import abort

app = Flask(__name__)
CORS(app)

myClient = pymongo.MongoClient("mongodb://localhost:27017")
myDb = myClient["mydatabase"]

@app.route("/api/v1/company", methods=["POST"])

def create_company():
    if not request.json or not 'name' in request.json:
        abort(400)
    # company = Company()
    # company.name = request.json['name']

    company = {
        'name': request.json['name'],
        'address': request.json['address'],
        'businessType': request.json['businessType'],
        'issues': request.json['issues'],
        'numberOfJobs': request.json['numberOfJobs'],
        'whatHappened': request.json['whatHappened'],
        'socialNetworks': request.json['socialNetworks'],
        'email': request.json['email'],
        'phone': request.json['phone']
    }
    print(company)
    return jsonify({'task': company}), 201

if __name__ == "__main__":
    app.run(debug=True)

class Company :

    def __init__(self, name, address, businessType, issues, numberOfJobs, whatHappened, socialNetworks, email, phone):
        self.name = name
        self.address = address
        self.businessType = businessType
        self.issues = issues
        self.numberOfJobs = numberOfJobs
        self.whatHappened = whatHappened
        self.socialNetworks = socialNetworks
        self.email = email
        self.phone = phone

