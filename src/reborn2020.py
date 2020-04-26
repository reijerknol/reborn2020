#!/usr/bin/env python
import sys

from reborn2020.endpoint.routes import route


def main(debug=False):
    flask = route()
    flask.run(host="0.0.0.0", debug=debug)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "--debug":
        main(debug=True)
    else:
        main()
