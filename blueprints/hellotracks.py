from flask import Blueprint, jsonify

hellotracks = Blueprint(name="hellotracks", import_name=__name__)


@hellotracks.route('/', methods=['GET'])
def hello():
    return 'Hello from hellotracks'


@hellotracks.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from hellotracks."}
    return jsonify(output)
