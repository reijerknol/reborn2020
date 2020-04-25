from flask import jsonify
from flask import request
from src.app import App

from werkzeug.exceptions import abort

# app = Flask(__name__)
# CORS(app)

app = App()

#run the application that does database manipulation
def route():
    return app.flask


@app.flask.route("/api/v1/company", methods=["POST"])
def create_company():
    if not request.json or not 'name' in request.json:
        abort(400)
    company = {
        'name': request.json['name'],
        'address': request.json['address'],
        'businessType': request.json['businessType'],
        'issues': request.json['issues'],
        'numberOfJobs': request.json['numberOfJobs'],
        'whatHappened': request.json['whatHappened'],
        'whatNeed': request.json['whatNeed'],
        'socialNetworks': request.json['socialNetworks'],
        'email': request.json['email'],
        'phone': request.json['phone']
    }
    # print(company)
    return jsonify({'task': company}), 201


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
