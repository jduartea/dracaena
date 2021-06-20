import requests
from errors import WunderInternalServerError

DEFAULT_API_URL = "https://humanforest.backend.fleetbird.eu/api/v2"
VEHICLES_ENDPOINT = "/vehicles"


class WunderClient(object):
    """
    Client for WunderMobility API
    """

    def __init__(self, api_key, api_url=None):
        self.api_key = api_key
        self.api_url = api_url or DEFAULT_API_URL
        self.session = requests.Session()
        self.request_url = ""

    def get_vehicles(self) -> list:
        """
        Get all vehicles.

        :return: All vehicles in a list
        """
        self.request_url = f"{self.api_url}/vehicles"
        return self._get_request().json().get("data")

    def get_vehicle(self, vehicle_id: int):
        """
        Get vehicle by vehicle id.

        :param vehicle_id: Vehicle Id
        :return: Vehicle data
        :rtype: dict
        """
        self.request_url = f"{self.api_url}/vehicles/{vehicle_id}"
        return self._get_request().json().get("data")

    def _get_request(self):
        """
        :rtype: requests.Response
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = self.session.get(url=self.request_url, headers=headers)

        if str(response.status_code).startswith("5"):
            raise WunderInternalServerError

        return response

    def _post_request(self, payload: dict):
        """
        :rtype: requests.Response
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = self.session.post(
            url=self.request_url,
            data=payload,
            headers=headers
        )

        if str(response.status_code).startswith("5"):
            raise WunderInternalServerError

        return response
