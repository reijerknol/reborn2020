import json
from typing import Optional

from bson import ObjectId
from flask import request
from flask_cors import CORS
from werkzeug.exceptions import abort
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from src.app import App

app = App()
CORS(app.flask)

# run the application that does database manipulation
def route():
    return app.flask


@app.flask.route("/api/v1/company", methods=["POST"])
def create_company():
    if not request.json or 'name' not in request.json:
        abort(400)
    company = Company.from_dict(request.json)
    app.mongo.companyDB.create(company.to_dict())
    return JSONEncoder().encode(request.json), 201


@app.flask.route("/api/v1/company/<company_id>", methods=["GET"])
def get_company_by_id(company_id):
    company = app.mongo.companyDB.get_company_by_id(company_id)
    return JSONEncoder().encode(company), 200


@app.flask.route("/api/v1/getAllMarkers")
def get_all_markers():
    markers = app.mongo.companyDB.get_all_markers()
    return JSONEncoder().encode(markers), 200


@app.flask.route("/api/v1/findCompany/<query>")
def find_company(query):
    companies = app.mongo.companyDB.find_company(query)
    return JSONEncoder.encode(companies), 200


@app.flask.route("/api/v1/counters")
def get_counters():
    companies = app.mongo.companyDB.get_counters()
    return JSONEncoder.encode(companies), 200


@dataclass_json
@dataclass
class Company:
    type: str
    name: str
    address: Optional[str] = None
    business: Optional[str] = None
    issues_other: Optional[str] = None
    help: Optional[str] = None
    help_other: Optional[str] = None
    business_type: Optional[str] = None
    issues: Optional[str] = None
    business_help: Optional[str] = None
    business_help_other: Optional[str] = None
    jobs: Optional[str] = None
    problem: Optional[str] = None
    needs: Optional[str] = None
    social: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company_name: Optional[str] = None
    story: Optional[str] = None
    coords: Optional[str] = None
    emailadress: Optional[str] = None


class JSONEncoder(json.JSONEncoder):
    def default(self, input_object):
        if isinstance(input_object, ObjectId):
            return str(input_object)
        return json.JSONEncoder.default(self, input_object)
