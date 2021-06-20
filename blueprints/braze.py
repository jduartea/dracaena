import json
import logging
import os

import requests
from flask import Blueprint, jsonify, request, Response

braze = Blueprint(name="braze", import_name=__name__)


@braze.route('', methods=['GET'])
def home():
    return os.environ.get("TEST_MESSAGE")


@braze.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from braze."}
    return jsonify(output)


@braze.route('/unsubscribe/<customer_id>', methods=['POST'])
def respond(customer_id):
    if request.headers['token'] == os.environ.get("BRAZE_UNSUBSCRIBE_TOKEN"):
        url = "https://humanforest.backend.fleetbird.eu/api/v2/customers/" + customer_id

        payload = {"newsletterEnabled": False}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv("WUNDER_BACKEND_API_KEY")}'
        }
        requests.patch(url=url, headers=headers, data=json.dumps(payload))
        logging.info("Subscription disabled for customer_id " + customer_id)
        return Response(status=200)
    else:
        logging.error("Unauthorized. Subscription for customer_id " + customer_id + " wasn't updated in Wunder.")
        return Response(status=401)
