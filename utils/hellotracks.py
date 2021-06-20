"""
    A Python implementation of the Hellotracks API.


    **Job API Object**

    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | Attribute       |  Type | R/W | Description                                                             |
    +=================+=======+=====+=========================================================================+
    | id              |  str  |  R  | Job unique ID                                                           |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | type            |  int  |  RW | Job Type: 0=Work, 1=Pickup, 2=Dropoff                                   |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | teamId          |  int  |  RW | Team Id 0-n (the number of the team). Defaults to 0 (no specific team). |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | destinationName |  str  |  RW | Title of this job (1-line description)                                  |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | destinationLat  | float |  RW | Latitude                                                                |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | destinationLng  | float |  RW | Longitude                                                               |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | destinationText |  str  |  RW | Location Address                                                        |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | destinationUrl  |  str  |  RW | Location map URL                                                        |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | textDispatcher  |  str  |  RW | Dispatcher additional info text (multi-line)                            |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | textReceiver    |  str  |  RW | Worker’s reply text                                                     |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | contactName     |  str  |  RW | Name of contact at job’s location                                       |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | contactPhone    |  str  |  RW | Phone number of contact at job’s location                               |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | contactEmail    |  str  |  RW | Email of contact at job’s location                                      |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | day             |  int  |  RW | Date for job as YYYYMMDD or 0 (e.g. 20210324)                           |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | priority        |  int  |  RW | Priority min:0-max:10                                                   |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | number          |  int  |  RW | Sequence number for ordering                                            |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | onSiteSeconds   |  int  |  RW | The assumed onsite-time in seconds (e.g. 10min on site: 600)            |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | windowStart     |  int  |  RW | Format: HHMM or 0 (e.g 704 = 7:04am)                                    |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | windowEnd       |  int  |  RW | Format: HHMM or 0 (e.g 1724 = 5:24pm)                                   |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | orderId         |  int  |  RW | Optional Order ID as an integer number                                  |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | dispatcherUid   |  str  |  RW | UID of dispatcher account                                               |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | dispatcherName  |  str  |  R  | Name of Dispatcher                                                      |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | dispatcherUrl   |  str  |  R  | URL for dispatcher icon image                                           |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | placeUid        |  str  |  RW | UID of place to visit or “”                                             |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | placeName       |  str  |  R  | Name of place/location                                                  |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | placeUrl        |  str  |  R  | URL for place icon image                                                |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | radius          |  int  |  R  | Radius for check-in/out in meter (place-radius or default-radius)       |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | worker          |  str  |  RW | User name of assigned worker                                            |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | workerName      |  str  |  R  | Full name of assigned worker                                            |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | itemsToDropoff  |  int  |  RW | Number of items to drop off                                             |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | itemsToPickup   |  int  |  RW | Number of items to pick up                                              |
    +-----------------+-------+-----+-------------------------------------------------------------------------+
    | status          |  str  |  R  | Set to archived if job is archived, omitted otherwise                   |
    +-----------------+-------+-----+-------------------------------------------------------------------------+


    **Job Status attributes (progress)**

    The job status attributes hold the timestamp when an event has occurred or 0 if it does not apply.

    Note: Timestamps are milliseconds, between the current time and midnight, January 1, 1970 UTC (Java timestamps)

    E.g.: ``1430580377000 = Sat, 02 May 2015 15:26:17 GMT``

    +---------------+-------+-----+---------------------------------------------------------+
    | Attribute     | Type  | R/W | Description                                             |
    +===============+=======+=====+=========================================================+
    | tsCreated     | float |  RW | Timestamp in millis for job creation                    |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsAssigned    | float |  R  | Timestamp in millis for job assigned to worker          |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsAccepted    | float |  RW | Timestamp in millis for job accepted by worker          |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsRejected    | float |  RW | Timestamp in millis for job rejected by worker          |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsDoneSuccess | float |  RW | Timestamp in millis for job marked as success by worker |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsDoneFailed  | float |  RW | Timestamp in millis for job marked as issue by worker   |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsCheckIn     | float |  RW | Timestamp in millis for auto check-in by worker         |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsCheckOut    | float |  RW | Timestamp in millis for auto check-out by worker        |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsCheckNFC1   | float |  RW | Timestamp in millis for first check with NFC            |
    +---------------+-------+-----+---------------------------------------------------------+
    | tsCheckNFC2   | float |  RW | Timestamp in millis for second check with NFC           |
    +---------------+-------+-----+---------------------------------------------------------+


    **Customizable Attributes**

    +----------------------+------+-----+-----------------------------------------------------+
    | Attributes           | Type | R/W | Description                                         |
    +======================+======+=====+=====================================================+
    | custom_{text}        | str  |  RW | Custom field where {text} is the desired field name |
    +----------------------+------+-----+-----------------------------------------------------+
    | extra_number_{x}_key | str  |  R  | Worker input number field where {x} is 1-4          |
    +----------------------+------+-----+-----------------------------------------------------+
    | extra_number_{x}_val | int  |  RW | Worker input number value where {x} is 1-4          |
    +----------------------+------+-----+-----------------------------------------------------+
    | extra_text_{x}_key   | str  |  R  | Worker input text field where {x} is 1-4            |
    +----------------------+------+-----+-----------------------------------------------------+
    | extra_text_{x}_val   | str  |  RW | Worker input text value where {x} is 1-4            |
    +----------------------+------+-----+-----------------------------------------------------+

"""
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

ht_user = os.getenv("HELLOTRACKS_USER")
ht_key = os.getenv("HELLOTRACKS_API")


def send_hellotracks_call(endpoint, data: dict):
    """
    Call Hellotracks API using POST request.

    :param endpoint: Hellotracks endpoint
    :param data: Data to be sent to Hellotracks
    :return: requests.Response
    """
    response = requests.post(url="https://hellotracks.com/api/" + endpoint,
                             headers={
                                 "Content-Type": "text/plain; charset=uft-8"
                             },
                             data=json.dumps(data))
    return response


def get_all_jobs_for_day(worker: str = "*", **kwargs):
    """
    Get jobs from Hellotracks.

    :param worker: Worker value (email). To retrieve jobs that are not assigned to a worker, set worker:"". To request all jobs for all workers for a specific date, set worker:"*" (default).
    :key day: (optional) Day in YYYYMMDD format as int. Defaults to today. To retrieve jobs with no date assigned, set day:0.
    :key team: (optional) Filter to only request jobs for a specific team.
    :key int order_id: (optional) Filter to request a specific job.
    :key order_ids: (optional) Filter to request multiple specific jobs.
    :key progress_success: (optional) Filter to only retrieve jobs that are marked as successfully completed. For this, set the value to 1, else set it either to 0 or do not set the field at all.
    :return: Response object
    :rtype: requests.Response
    """

    endpoint = "getjobs"
    data = {
        "worker": worker
    }

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

    payload = {
        "auth": {"usr": ht_user, "key": ht_key},
        "data": data
    }

    response = send_hellotracks_call(endpoint, payload)
    return response


def delete_jobs(job_id_list: list, notify=True):
    """
    Delete jobs from Hellotracks. Deleted jobs will be deleted entirely, this action cannot be undone.

    Consider archiving jobs if you want to keep related data in the system.

    :param job_id_list: A list that contains job_id to be deleted
    :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress
        |  status of this job changed. To omit creating notifications for this job modification, set notify: False.
    :return: Response 0bject
    :rtype: requests.Response
    """

    endpoint = "deletejobs"
    data = {
        "jobs": {job_id: {} for job_id in job_id_list},
        "notify": notify
    }
    payload = {
        "auth": {"usr": ht_user, "key": ht_key},
        "data": data
    }
    response = send_hellotracks_call(endpoint, payload)
    return response


def archive_jobs(job_id_list: list, notify=True):
    """
    Archive jobs from Hellotracks.

    Archived jobs can easily be restored in the Hellotracks Dashboard or via the /restorejobs endpoint.

    :param job_id_list: A list that contains job_id to be deleted
    :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress
        |  status of this job changed. To omit creating notifications for this job modification, set notify: False.
    :return: Response 0bject
    :rtype: requests.Response
    """

    endpoint = "archivejobs"
    data = {
        "jobs": {job_id: {} for job_id in job_id_list},
        "notify": notify
    }
    payload = {
        "auth": {"usr": ht_user, "key": ht_key},
        "data": data
    }
    response = send_hellotracks_call(endpoint, payload)
    return response


def restore_jobs(job_id_list: list, notify=True):
    """
    Restore previously archived jobs from Hellotracks.

    :param job_id_list: A list that contains job_id to be deleted
    :param notify: (optional) Set to True (default) if you want to generate a notification in case the progress
        |  status of this job changed. To omit creating notifications for this job modification, set notify: False.
    :return: Response 0bject
    :rtype: requests.Response
    """

    endpoint = "restorejobs"
    data = {
        "jobs": {job_id: {} for job_id in job_id_list},
        "notify": notify
    }
    payload = {
        "auth": {"usr": ht_user, "key": ht_key},
        "data": data
    }
    response = send_hellotracks_call(endpoint, payload)
    return response


def edit_jobs(modified_jobs: dict, notify=True):
    """
    Edit jobs in Hellotracks. You can change job properties and update job status/progress.

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
    :rtype: requests.Response
    """

    endpoint = "editjobs"
    data = {
        "jobs": modified_jobs,
        "notify": notify
    }
    payload = {
        "auth": {"usr": ht_user, "key": ht_key},
        "data": data
    }
    response = send_hellotracks_call(endpoint, payload)
    return response


def create_jobs(job_list: list, auto_assign=False):
    """
    Create jobs in Hellotracks.

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
    :rtype: requests.Response
    """

    endpoint = "createjobs"
    data = {
        "jobs": job_list,
        "autoassign": auto_assign
    }
    payload = {
        "auth": {"usr": ht_user, "key": ht_key},
        "data": data
    }

    response = send_hellotracks_call(endpoint, payload)
    return response


def create_job_object(
        job_type: int = 0,
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
        custom_attributes: dict = {}):
    """
    Create a Job object to be passed on the ``create_jobs`` function.

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
    :rtype: dict
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
