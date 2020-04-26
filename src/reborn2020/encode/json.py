#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import json

from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, input_object):
        if isinstance(input_object, ObjectId):
            return str(input_object)
        return json.JSONEncoder.default(self, input_object)
