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
    # company = Company(**request.json)
    # print(company)
    # company = {
    #     'type': request.json['type'],
    #     'name': request.json['name'],
    #     'address': request.json['address'],
    #     'business': request.json['business'],
    #     'business_other': request.json['business_other'],
    #     'issues': request.json['issues'],
    #     'issues_other': request.json['issues_other'],
    #     'help': request.json['help'],
    #     'help_other': request.json['help_other'],
    #     'business_help': request.json['business_help'],
    #     'business_help_other': request.json['business_help_other'],
    #     'jobs': request.json['jobs'],
    #     'problem': request.json['problem'],
    #     'needs': request.json['needs'],
    #     'social': request.json['social'],
    #     'email': request.json['email'],
    #     'phone': request.json['phone'],
    #     'company_name': request.json['company_name'],
    #     'story': request.json['story'],
    #     'coords': {
    #         'lat': float(request.json['coords']['lat']),
    #         'lng': float(request.json['coords']['lng'])
    #     }
    # }
    app.mongo.companyDB.create(request.json)
    return JSONEncoder().encode(request.json), 201


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
                 type=None,
                 name=None,
                 address=None,
                 business=None,
                 business_type=None,
                 issues=None,
                 issues_other=None,
                 help=None,
                 help_other=None,
                 business_help=None,
                 business_help_other=None,
                 jobs=None,
                 problem=None,
                 needs=None,
                 social=None,
                 email=None,
                 phone=None,
                 company_name=None,
                 story=None,
                 coords=None
                    ):
        self.type = type
        self.name = name
        self.address = address
        self.business = business
        self.issues_other = issues_other
        self.help = help
        self.help_other = help_other
        self.business_type = business_type
        self.issues = issues
        self.business_help = business_help
        self.business_help_other = business_help_other
        self.jobs = jobs
        self.problem = problem
        self.needs = needs
        self.social = social
        self.email = email
        self.phone = phone
        self.company_name = company_name
        self.story = story
        self.coords = coords



class JSONEncoder(json.JSONEncoder):
    def default(self, input_object):
        if isinstance(input_object, ObjectId):
            return str(input_object)
        return json.JSONEncoder.default(self, input_object)
