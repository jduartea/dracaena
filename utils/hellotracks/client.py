import json

import requests

DEFAULT_API_URL = "https://hellotracks.com/api"

# Jobs Endpoints
CREATE_JOBS_ENDPOINT = "/createjobs"
GET_JOBS_ENDPOINT = "/getjobs"
EDIT_JOBS_ENDPOINT = "/editjobs"
DELETE_JOBS_ENDPOINT = "/deletejobs"
ARCHIVE_JOBS_ENDPOINT = "/archivejobs"
RESTORE_JOBS_ENDPOINT = "/restorejobs"
DISTRIBUTE_JOBS_ENDPOINT = "/distributejobs"
OPTIMIZE_ROUTE_ENDPOINT = "/optimizeroute"

# Location and Tracks Endpoints
LOCATE_ENDPOINT = "/locate"
GET_TRACKS_ENDPOINT = "/gettracks"

# Account Management Endpoints
CREATE_ACCOUNT_ENDPOINT = "/createaccount"
EDIT_ACCOUNT_ENDPOINT = "/editaccount"
GET_ACCOUNTS_ENDPOINT = "/getaccounts"

# Places Endpoints
CREATE_PLACE_ENDPOINT = "/createplace"
EDIT_PLACE_ENDPOINT = "/editplace"
GET_PLACE_ENDPOINT = "/getplace"

# Reports Endpoints
CREATE_REPORT_ENDPOINT = "/createreport"


class HellotracksClient(object):
    """Client for Hellotracks API."""

    def __init__(self, user, api_key, api_url=None):
        self.user = user
        self.api_key = api_key
        self.api_url = api_url or DEFAULT_API_URL
        self.session = requests.Session()
        self.request_url = ""

    def _api_call(self, method: str, endpoint: str, data: dict) -> requests.Response:
        """
        Call Hellotracks API via HTTP request.

        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        Use ``GET``, ``POST``, etc.
        :param endpoint: Hellotracks endpoint
        :param data: Data to be sent to Hellotracks
        :return: Response object
        """

        headers = {
            "Content-Type": "text/plain; charset=uft-8"
        }

        auth = {
            "usr": self.user,
            "key": self.api_key
        }

        payload = {"auth": auth, "data": data}

        response = requests.request(method=method,
                                    url=self.api_url + endpoint,
                                    headers=headers,
                                    data=json.dumps(payload))
        return response

    def get_all_jobs_for_day(self, worker: str = "*", **kwargs) -> requests.Response:
        """Get jobs from Hellotracks.

        :param worker: Worker value (email). To retrieve jobs that are not assigned to a worker, set worker:"". To request all jobs for all workers for a specific date, set worker:"*" (default).
        :key day: (optional) Day in YYYYMMDD format as int. Defaults to today. To retrieve jobs with no date assigned, set day:0.
        :key team: (optional) Filter to only request jobs for a specific team.
        :key int order_id: (optional) Filter to request a specific job.
        :key order_ids: (optional) Filter to request multiple specific jobs.
        :key progress_success: (optional) Filter to only retrieve jobs that are marked as successfully completed. For this, set the value to 1, else set it either to 0 or do not set the field at all.
        :return: Response object
        """

        data = {"worker": worker}

        if "day" in kwargs:
            data["day"] = kwargs["day"]
        if "team" in kwargs:
            data["team"] = kwargs["team"]
        if "order_id" in kwargs:
            data["orderId"] = kwargs["order_id"]
        if "order_ids" in kwargs:
            data["orderIds"] = []
            data["orderIds"].extend(kwargs["order_ids"])
        if "progress_success" in kwargs:
            data["progressSuccess"] = kwargs["progress_success"]

        response = self._api_call(method="POST", endpoint=GET_JOBS_ENDPOINT, data=data)
        return response

    def delete_jobs(self, job_id_list: list, notify=True) -> requests.Response:
        """
        Delete jobs from Hellotracks. Deleted jobs will be deleted entirely, this action cannot be undone.

        Consider archiving jobs if you want to keep related data in the system.

        :param job_id_list: A list that contains job_id to be deleted
        :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress
            |  status of this job changed. To omit creating notifications for this job modification, set notify: False.
        :return: Response object
        """

        data = {
            "jobs": {job_id: {} for job_id in job_id_list},
            "notify": notify
        }

        response = self._api_call(method="POST", endpoint=DELETE_JOBS_ENDPOINT, data=data)
        return response

    def archive_jobs(self, job_id_list: list, notify=True) -> requests.Response:
        """Archive jobs from Hellotracks.(

        Archived jobs can easily be restored in the Hellotracks Dashboard or via the /restorejobs endpoint.

        :param job_id_list: A list that contains job_id to be deleted
        :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress
            |  status of this job changed. To omit creating notifications for this job modification, set notify: False.
        :return: Response object
        """

        data = {
            "jobs": {job_id: {} for job_id in job_id_list},
            "notify": notify
        }

        response = self._api_call(method="POST", endpoint=ARCHIVE_JOBS_ENDPOINT, data=data)
        return response

    def restore_jobs(self, job_id_list: list, notify=True) -> requests.Response:
        """Restore previously archived jobs from Hellotracks.

        :param job_id_list: A list that contains job_id to be deleted
        :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress
            |  status of this job changed. To omit creating notifications for this job modification, set notify: False.
        :return: Response object
        """

        data = {
            "jobs": {job_id: {} for job_id in job_id_list},
            "notify": notify
        }
        response = self._api_call(method="POST", endpoint=RESTORE_JOBS_ENDPOINT, data=data)
        return response

    def edit_jobs(self, modified_jobs: dict, notify=True) -> requests.Response:
        """Edit jobs in Hellotracks.

        You can change job properties and update job status/progress.

        Compare Job API Object to see all modifiable attributes (all which are marked as RW in the column R/W. You are
        not able to change the id of a job, but most job properties are modifiable.

        For the ``modified_jobs`` argument, use a dictionary as::

            {
                "job_1":
                    {"attribute_1": "test1"},
                    {"attribute_2": "test2"}
                "job_2":
                    {"attribute_3": "test3"}
            }

        :param modified_jobs: A dictionary that contains jobs and attributes to be modified.
        :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress status
            of this job changed. To omit creating notifications for this job modification, set notify: False.
        :return: Response object
        """

        data = {
            "jobs": modified_jobs,
            "notify": notify
        }
        response = self._api_call(method="POST", endpoint=EDIT_JOBS_ENDPOINT, data=data)
        return response

    def create_jobs(self, job_list: list, auto_assign=False) -> requests.Response:
        """Create jobs in Hellotracks.

        Use the Job API Object to see all writable attributes.

        For the ``job_list`` argument, use a list as::

            [
                {
                    "attribute_1": "test1",
                    "attribute_2": "test2"
                },
                {
                    "attribute_3": "test3"
                }
            ]
        Where each element in the list is a job object.

        **Note:** Although optional, it is recommended to set ``uidSecondary`` on creating a new job. It will be guaranteed
        that only 1 job exists with this unique id. The value can be any kind of text, the only constraint is that it needs
        to be unique inside your company account.

        :param job_list: A list that contains jobs and attributes to be modified. Example::
         [{"job_1": {"attribute_1": "test1"}, "job_2": ...}]
        :param auto_assign: (optional) Defaulting to False, and indicates that the created jobs should automatically be
            assigned to a member. It will choose the nearest member that is available, taking the shift and day-route
            into account.
        :return: Response object
        """

        data = {
            "jobs": job_list,
            "autoassign": auto_assign
        }

        response = self._api_call(method="POST", endpoint=CREATE_JOBS_ENDPOINT, data=data)
        return response

    @staticmethod
    def create_job_object(job_type: int = 0,
                          team_id: int = 0,
                          destination_name: str = None,
                          destination_lat: float = 0,
                          destination_lng: float = 0,
                          destination_text: str = None,
                          destination_url: str = None,
                          text_dispatcher: str = None,
                          text_receiver: str = None,
                          contact_name: str = None,
                          contact_phone: str = None,
                          contact_email: str = None,
                          day: int = None,
                          priority: int = None,
                          number: int = None,
                          on_site_seconds: int = None,
                          window_start: int = None,
                          window_end: int = None,
                          order_id: int = None,
                          dispatcher_uid: str = None,
                          place_uid: str = None,
                          worker: str = None,
                          items_to_dropoff: int = None,
                          items_to_pickup: int = None,
                          custom_attributes: dict = None) -> dict:
        """Create a Job object to be passed on the ``create_jobs`` function.

        :param job_type: Job Type. Defaults to 0. 0=Work, 1=Pickup, 2=Dropoff
        :param team_id: Team Id 0-n. Defaults to 0 (no specific team).
        :param destination_name: Title of the job (1-line description).
        :param destination_lat: Latitude.
        :param destination_lng: Longitude.
        :param destination_text: Location address.
        :param destination_url: Location map URL.
        :param text_dispatcher: Dispatcher additional info text (multi-line).
        :param text_receiver: Worker's reply text.
        :param contact_name: Name of contact at job's location.
        :param contact_phone: Phone number of contact at job's location.
        :param contact_email: Email of contact at job's location.
        :param day: Date for job as YYYYMMDD or 0 (e.g. 20210324).
        :param priority: Priority min:0-max:10.
        :param number: Sequence number for ordering.
        :param on_site_seconds: The assumed onsite-time in seconds (e.g. 10min on site: 600).
        :param window_start: Format: HHMM or 0 (e.g. 704 = 7:04am).
        :param window_end: Format: HHMM or 0 (e.g. 1724 = 5:24pm).
        :param order_id: Optional Order ID as an integer number.
        :param dispatcher_uid: UID of dispatcher account.
        :param place_uid: UID of place to visit or "".
        :param worker: User name of assigned worker.
        :param items_to_dropoff: Number of items to drop off.
        :param items_to_pickup: Number of items to pick up.
        :param custom_attributes: A dictionary containing the custom attributes.
            Example: {"vehicle_id": 1234, "damage": "Broken"}.
        :return: Job object
        """

        job = {
            "type": job_type,
            "teamId": team_id,
            "destinationName": destination_name,
            "destinationLat": destination_lat,
            "destinationLng": destination_lng,
            "destinationText": destination_text,
            "destinationUrl": destination_url,
            "textDispatcher": text_dispatcher,
            "textReceiver": text_receiver,
            "contactName": contact_name,
            "contactPhone": contact_phone,
            "contactEmail": contact_email,
            "day": day,
            "priority": priority,
            "number": number,
            "onSiteSeconds": on_site_seconds,
            "windowStart": window_start,
            "windowEnd": window_end,
            "orderId": order_id,
            "dispatcherUid": dispatcher_uid,
            "placeUid": place_uid,
            "worker": worker,
            "itemsToDropoff": items_to_dropoff,
            "itemsToPickup": items_to_pickup
        }
        job_without_none = {k: v for k, v in job.items() if v is not None}
        job.clear()
        job.update(job_without_none)

        if custom_attributes:
            job.update({f"custom_{k}": v for k, v in custom_attributes.items() if k})

        return job
