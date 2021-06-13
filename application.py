from flask import Flask, jsonify
import sys

from blueprints.hellotracks import hellotracks
from blueprints.braze import braze

application = Flask(__name__)

application.register_blueprint(hellotracks, url_prefix="/hellotracks")
application.register_blueprint(braze, url_prefix="/braze")


@application.route('/')
def hello_world():
    return 'Hello You!'


if __name__ == '__main__':
    application.run(host="0.0.0.0")
