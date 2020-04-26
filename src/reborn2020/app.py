from flask import Flask, jsonify, request, make_response

from src.database.mongo import Mongo


class App(object):

    def __init__(self):

        # Request
        self.request = request

        # Jsonify
        self.jsonify = jsonify

        # Flask Framework
        self.flask = Flask(__name__)

        # MongoDB
        self.mongo = Mongo()

    def success(self, data):
        if data:
            if '_id' in data:
                data.pop('_id')
            return self.response({'message': 'Ok', 'result': data}, 200)
        else:
            return self.response({'message': 'Not found'}, 404)

    def result(self, action, base, args=False):
        p = self.auth.parse(request.headers.get('authorization'))
        if p:
            # User
            u = self.mongo.app.user(p['payload']['id'])
            # Check token
            if u and u['token'] == p['token']:
                # Verify token
                v = self.auth.verify(u['secret'], p['payload'], p['signature'])
                if v == True:
                    # return self.success(self.generatetoken({'days': 6}))
                    # return self.success(self.auth.encode('sendtics.com') +'.'+ self.auth.encode('users'))
                    return self.success(getattr(self.mongo.api, action)(
                        self.auth.encode(p['payload']['domain']) + '.' + self.auth.encode(base), args))
                else:
                    return self.unauthorized(v['error'])
            else:
                return self.unauthorized('Invalid Token')
        return self.unauthorized('Unauthorized')

    def unauthorized(self, message):
        return self.response({'message': message}, 401)

    @staticmethod
    def response(data, status):

        if data and status:
            data['status'] = status

            return make_response(jsonify(data), status)
