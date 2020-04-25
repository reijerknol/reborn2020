import json

from bson import ObjectId
from flask import request
from flask_cors import CORS
from werkzeug.exceptions import abort

from src.app import App

# app = Flask(__name__)
# CORS(app)

app = App()
CORS(app.flask)


# run the application that does database manipulation
def route():
    return app.flask


@app.flask.route("/api/v1/company", methods=["POST"])
def create_company():
    if not request.json or 'name' not in request.json:
        abort(400)
    company = {
        'type': request.json['type'],
        'name': request.json['name'],
        'address': request.json['address'],
        'businessType': request.json['businessType'],
        'issues': request.json['issues'],
        'numberOfJobs': request.json['numberOfJobs'],
        'whatHappened': request.json['whatHappened'],
        'whatNeed': request.json['whatNeed'],
        'socialNetworks': request.json['socialNetworks'],
        'email': request.json['email'],
        'phone': request.json['phone'],
        'coords': {
            'lat': float(request.json['coords']['lat']),
            'lng': float(request.json['coords']['lng'])
        }
    }
    app.mongo.companyDB.create(company)
    return JSONEncoder().encode(company), 201


@app.flask.route("/api/v1/company/<company_id>", methods=["GET"])
def get_company_by_id(company_id):
    company = app.mongo.companyDB.get_company_by_id(company_id)
    app.mongo.companyDB.get_all_markers()
    return JSONEncoder().encode(company), 200


@app.flask.route("/api/v1/getAllMarkers")
def get_all_markers():
    markers = app.mongo.companyDB.get_all_markers()
    return JSONEncoder().encode(markers), 200


class Company:
    def __init__(self,
                 name,
                 address,
                 business_type,
                 issues,
                 number_of_jobs,
                 what_happened,
                 what_need,
                 social_networks,
                 email,
                 phone):
        self.name = name
        self.address = address
        self.businessType = business_type
        self.issues = issues
        self.numberOfJobs = number_of_jobs
        self.whatHappened = what_happened
        self.whatNeed = what_need
        self.socialNetworks = social_networks
        self.email = email
        self.phone = phone


class JSONEncoder(json.JSONEncoder):
    def default(self, input_object):
        if isinstance(input_object, ObjectId):
            return str(input_object)
        return json.JSONEncoder.default(self, input_object)
