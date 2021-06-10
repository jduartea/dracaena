from flask import Flask, jsonify
import sys

from blueprints.hellotracks import hellotracks
from blueprints.braze import braze

app = Flask(__name__)

app.register_blueprint(hellotracks, url_prefix="/api/v1/hellotracks")
app.register_blueprint(braze, url_prefix="/api/v1/braze")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
