import json
import requests
from dotenv import dotenv_values
from flask import Blueprint, request, Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

wunder = Blueprint(name="wunder", import_name=__name__)
config = dotenv_values(".env")

client = WebClient(token=config["SLACKBOT_DRACAENA_TOKEN"])


@wunder.route('', methods=['POST'])
def all_events():
    try:
        result = client.chat_postMessage(
            channel=config["SLACKBOT_DRACAENA_CHANNEL_ID"],
            text="Hello world!"
        )
        print(result)

    except SlackApiError as e:
        print(f"Error: {e}")

    payload = request.json

    # headers = {'Content-Type': 'application/json'}
    # data = {"text": "```" + json.dumps(payload, indent=4) + "```"}
    # requests.post(url=config["SLACKBOT_DRACAENA_WEBHOOK_URL"], headers=headers, data=json.dumps(data))

    return Response(status=200)
