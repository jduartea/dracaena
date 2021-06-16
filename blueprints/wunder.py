import requests
from dotenv import dotenv_values
from flask import Blueprint, jsonify, request

wunder = Blueprint(name="wunder", import_name=__name__)
config = dotenv_values(".env")


@wunder.route('/', methods=['POST'])
def all_events():
    payload = str(request.json)
    data = {"text": "test from dracaena"}
    requests.post(url=config["SLACK_WEBHOOK_URL"], data=data)
