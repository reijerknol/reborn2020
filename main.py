#!/usr/bin/env python

# Import
from src.route import route

# REST API
api = route()

# Run the App
if __name__ == '__main__':
    api.run(host="0.0.0.0", debug=True)
