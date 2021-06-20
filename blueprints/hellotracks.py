import random
from datetime import date

from flask import Blueprint, jsonify, Response, request

from utils.hellotracks import *

load_dotenv()

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
    event_name = request.json["eventName"]
    data = request.json["data"]
    if event_name == "backend\\models\\VehicleStateChange::afterInsert" \
            and data["to"] == "fuel level low":
        vehicle_id = data["vehicleId"]
        lat = random.uniform(51.47690572136774, 51.538636920666406)
        lon = random.uniform(-0.18411568297429584, -0.07517897752823008)

        job = create_job_object(
            job_type=0,
            day=int(date.today().strftime('%Y%m%d')),
            destination_lat=lat,
            destination_lng=lon,
            destination_text="Fuel Level Low!!!",
            custom_attributes={
                "vehicle_id": vehicle_id
            }
        )

        create_jobs(job_list=[job])

        return Response(status=200)
