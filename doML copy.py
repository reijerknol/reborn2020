from flask import Flask
from flask import request,
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

path = '../data2/'


@app.route("/company", methods=["POST"])

def hello():
    #
    # imagefile = request.files.get('imagefile', '')
    #
    # return json.dumps({"type": "", "probability": ""}, sort_keys=True)

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

