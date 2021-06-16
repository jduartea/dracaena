import json
import requests
from dotenv import dotenv_values
from flask import Blueprint, request, Response

wunder = Blueprint(name="wunder", import_name=__name__)
config = dotenv_values(".env")


@wunder.route('', methods=['POST'])
def all_events():
    payload = request.json

    headers = {'Content-Type': 'application/json'}
    data = {"text": json.dumps(payload)}
    requests.post(url=config["SLACK_WEBHOOK_URL"], headers=headers, data=json.dumps(data))

    return Response(status=200)
