import json
import requests
import random
from datetime import date
from flask import Blueprint, jsonify, Response, request

hellotracks = Blueprint(name="hellotracks", import_name=__name__)


@hellotracks.route('/', methods=['GET'])
def hello():
    return 'Hello from hellotracks'


@hellotracks.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from hellotracks."}
    return jsonify(output)


@hellotracks.route('/create_job', methods=['POST', 'GET'])
def create_job():
    if request.json["data"]["vehicleStateId"] == 4:
        lat = random.uniform(51.47690572136774, 51.538636920666406)
        lon = random.uniform(-0.18411568297429584, -0.07517897752823008)
        today = date.today()

        workers = ["jose.duarte@humanforest.co.uk", "victor.aguayo@humanforest.co.uk",
                   "agustin.guilisasti@humanforest.co.uk"]
        worker = random.choices(workers, k=1)[0]

        payload = {"auth": {}, "data": {}}
        payload["auth"]["usr"] = "jose.duarte@humanforest.co.uk"
        payload["auth"]["key"] = "7EF691EF8C404ACF1AF7EF99B8FFE10E"
        payload["data"]["jobs"] = []

        job = {
            "type": 0,
            "destinationLat": lat,
            "destinationLng": lon,
            "destinationText": "Fuel Level Low",
            "custom_vehicle_id": request.json["data"]["carId"],
            "custom_vehicle_state_id": request.json["data"]["vehicleStateId"],
            "custom_hardware_id": request.json["data"]["hardwareId"],
            "worker": worker,
            "day": int(today.strftime('%Y%m%d'))
        }

        payload["data"]["jobs"].append(job)

        requests.post(
            url="https://hellotracks.com/api/createjobs",
            headers={
                "Content-Type": "text/plain; charset=utf-8"
            },
            data=json.dumps(payload))
        return Response(status=200)