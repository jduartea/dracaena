from flask import Blueprint, jsonify

braze = Blueprint(name="braze", import_name=__name__)


@braze.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from braze."}
    return jsonify(output)
