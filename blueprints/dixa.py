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
            "customer_id": user_data.get("customerId"),
            "first_name": user_data.get("firstName"),
            "last_name": user_data.get("lastName"),
            "customer_reference": user_data.get("customerReference"),
            "birth_date": user_data.get("birthDate"),
            "street": user_data.get("street"),
            "street_additional": user_data.get("street_additional"),
            "house_number": user_data.get("houseNumber"),
            "zip_code": user_data.get("zipCode"),
            "city": user_data.get("city"),
            "country": user_data.get("country"),
            "blocked": user_data.get("blocked"),
            "registration_date": user_data.get("registrationDate"),
            "activation_date": user_data.get("activationDate")
        }

        if user_data.get("gender") == 1:
            r["gender"] = "Male"
        elif user_data.get("gender") == 1:
            r["gender"] = "Female"
        else:
            r["gender"] = "Unknown"

        return r

    else:
        return Response(status=401)
