import requests

DEFAULT_API_URL = "https://humanforest.backend.fleetbird.eu/api/v2"
VEHICLES_ENDPOINT = "/vehicles"


class WunderClientError(Exception):
    """
    Represents any Wunder Client Error.
    """

    pass


# class WunderRateLimitError(WunderClientError):
#     def __init__(self, reset_epoch_s):
#         """
#         A rate limit error was encountered.
#         :param float reset_epoch_s: Unix timestamp for when the API may be called again.
#         """
#         self.reset_epoch_s = reset_epoch_s
#         super(WunderClientError, self).__init__()


class WunderInternalServerError(WunderClientError):
    """
    Used for Wunder API responses where response code is of type 5XX suggesting
    Wunder side server errors.
    """

    pass


class WunderClient(object):
    """
    Client for WunderMobility API
    """

    def __init__(self, api_key, api_url=None):
        self.api_key = api_key
        self.api_url = api_url or DEFAULT_API_URL
        self.session = requests.Session()
        self.request_url = ""

    def get_vehicles(self):
        """
        Get all vehicles.

        :return: All vehicles in a list
        :rtype: list
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
