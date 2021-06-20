import random
from datetime import date

from flask import Blueprint, Response, request

from utils.hellotracks import *
from utils.wunder.client import WunderClient

hellotracks = Blueprint(name="hellotracks", import_name=__name__)
wm = WunderClient(api_key=os.environ.get("WUNDER_BACKEND_API_KEY"))


@hellotracks.route('/create_job', methods=['POST', 'GET'])
def create_job():
    event_name = request.json["eventName"]
    data = request.json["data"]
    if event_name == "backend\\models\\VehicleStateChange::afterInsert" \
            and data["from"] != "fuel level low" and data["to"] == "fuel level low":

        vehicle_id = data["vehicleId"]
        vehicle = wm.get_vehicle(vehicle_id=vehicle_id)

        if request.args.get("random_locations") == "1":
            lat = random.uniform(51.47690572136774, 51.538636920666406)
            lng = random.uniform(-0.18411568297429584, -0.07517897752823008)
        else:
            lat = vehicle.get("lat", 0)
            lng = vehicle.get("lon", 0)

        job = create_job_object(
            job_type=0,
            day=int(date.today().strftime('%Y%m%d')),
            destination_lat=lat,
            destination_lng=lng,
            destination_text="Fuel Level Low",
            custom_attributes={
                "vehicle_id": vehicle_id,
                "mileage": vehicle.get("mileage")
            }
        )

        create_jobs(job_list=[job])

        return Response(status=200)
