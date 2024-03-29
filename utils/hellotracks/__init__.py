"""A Python implementation of the Hellotracks API.

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