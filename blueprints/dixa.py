import os

from flask import Blueprint, request, Response

from utils.wunder.client import WunderClient

dixa = Blueprint(name="dixa", import_name=__name__)

wm = WunderClient(api_key=os.environ.get("WUNDER_BACKEND_API_KEY"))


@dixa.route("/search_user", methods=["GET"])
def search_user():
    user_email = request.args.get("email")
    if request.headers.get("Authorization") == os.environ.get("DIXA_CONTENT_CARDS_TOKEN") and \
            os.environ.get("DIXA_CONTENT_CARDS_TOKEN") is not None:

        return wm.get_user_by_email(user_email)

    else:
        return Response(status=401)
