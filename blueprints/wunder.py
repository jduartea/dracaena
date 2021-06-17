import json
from datetime import datetime
from dotenv import dotenv_values
from flask import Blueprint, request, Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

wunder = Blueprint(name="wunder", import_name=__name__)
config = dotenv_values(".env")

client = WebClient(token=config["SLACKBOT_DRACAENA_TOKEN"])


@wunder.route('', methods=['POST'])
def all_events():
    payload = request.json
    timestamp = payload["timestamp"]
    event_name = payload["eventName"]
    data = payload["data"]
    print(config["SLACKBOT_DRACAENA_CHANNEL_ID"])
    try:
        result = client.chat_postMessage(
            channel=config["SLACKBOT_DRACAENA_CHANNEL_ID"],
            blocks=[
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Timestamp:* {datetime.fromtimestamp(timestamp)} ({timestamp})"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Event Name:* {event_name}"
                        }
                    ]
                }
            ]
        )

        client.chat_postMessage(
            channel=config["SLACKBOT_DRACAENA_CHANNEL_ID"],
            thread_ts=result["ts"],
            text=f"```{json.dumps(data, indent=2)}```"
        )

    except SlackApiError as e:
        print(f"Error: {e}")

    # headers = {'Content-Type': 'application/json'}
    # data = {"text": "```" + json.dumps(payload, indent=4) + "```"}
    # requests.post(url=config["SLACKBOT_DRACAENA_WEBHOOK_URL"], headers=headers, data=json.dumps(data))

    return Response(status=200)
