import os

from flask import Blueprint, request, Response

from utils.wunder.client import WunderClient

dixa = Blueprint(name="dixa", import_name=__name__)

wm = WunderClient(api_key=os.environ.get("WUNDER_BACKEND_API_KEY"))


@dixa.route("/search_user", methods=["GET"])
def get_user_data():
    user_email = request.args.get("email")
    if request.headers.get("Authorization") == os.environ.get("DIXA_CONTENT_CARDS_TOKEN") and \
            os.environ.get("DIXA_CONTENT_CARDS_TOKEN") is not None:

        user_data = wm.get_user_by_email(user_email)
        r = {
            "email_query": user_email,
            "first_name": user_data.get("firstName"),
            "last_name": user_data.get("lastName"),
            "customer_reference": user_data.get("customerReference")
        }
        return r

    else:
        return Response(status=401)
