from flask import jsonify
from flask import request
from src.app import App
from flask_cors import CORS

from werkzeug.exceptions import abort
import json
from bson import ObjectId

# app = Flask(__name__)
# CORS(app)

app = App()
CORS(app.flask)

#run the application that does database manipulation
def route():
    return app.flask


@app.flask.route("/api/v1/company", methods=["POST"])
def create_company():
    if not request.json or not 'name' in request.json:
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

@app.flask.route("/api/v1/company/<string:id>", methods=["GET"])
def getCompanyById(id):
    company = app.mongo.companyDB.getCompanyById(id)
    app.mongo.companyDB.getAllMarkers()
    return JSONEncoder().encode(company), 200


@app.flask.route("/api/v1/getAllMarkers")
def getAllMarkers():
    markers = app.mongo.companyDB.getAllMarkers()
    return JSONEncoder().encode(markers), 200

class Company:

    def __init__(self, name, address, businessType, issues, numberOfJobs, whatHappened, whatNeed, socialNetworks, email,
                 phone):
        self.name = name
        self.address = address
        self.businessType = businessType
        self.issues = issues
        self.numberOfJobs = numberOfJobs
        self.whatHappened = whatHappened
        self.whatNeed = whatNeed
        self.socialNetworks = socialNetworks
        self.email = email
        self.phone = phone


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)