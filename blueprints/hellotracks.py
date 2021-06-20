import json
import requests
import random
from datetime import date
from dotenv import dotenv_values
from flask import Blueprint, jsonify, Response, request
from utils.hellotracks import *

hellotracks = Blueprint(name="hellotracks", import_name=__name__)
config = dotenv_values(".env")


@hellotracks.route('/', methods=['GET'])
def hello():
    return 'Hello from hellotracks'


@hellotracks.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from hellotracks."}
    return jsonify(output)


@hellotracks.route('/create_job', methods=['POST'])
def create_job():
    if request.json["eventName"] == "vehicleStateChanged" and request.json["data"]["vehicleStateId"] == 4:
        lat = random.uniform(51.47690572136774, 51.538636920666406)
        lon = random.uniform(-0.18411568297429584, -0.07517897752823008)

        job = create_job_object(
            job_type=0,
            destination_lat=lat,
            destination_lng=lon,
            destination_text="Fuel Level Low!",
            custom_attributes={
                "vehicle_id": request.json["data"]["carId"],
                "hardware_id": request.json["data"]["hardwareId"]
            }
        )

        create_jobs(job_list=list(job))

        return Response(status=200)