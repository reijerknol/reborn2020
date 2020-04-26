from flask import request
from flask_cors import CORS
from werkzeug.exceptions import abort

from reborn2020.app import App
from reborn2020.json import JSONEncoder

app = App()
CORS(app.flask)


def route():
    return app.flask


@app.flask.route("/api/v1/company", methods=["POST"])
def create_company():
    if not request.json or 'name' not in request.json:
        abort(400)

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
