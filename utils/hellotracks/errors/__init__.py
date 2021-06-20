"""Errors that can be raised by this SDK"""


class HellotracksClientError(Exception):
    """Base class for Hellotracks Client errors."""


class HellotracksRequestError(HellotracksClientError):
    """Error raised when there's a problem with the request that's being submitted."""


class HellotracksApiError(HellotracksClientError):
    """Error raised when Hellotracks does not send the expected response.

    Attributes:
        response (HellotracksResponse): The HellotracksResponse object containing all of the data sent back from the
        API.
    Note:
        The message (str) passed into the exception is used when
        a user converts the exception to a str.
        i.e. str(HellotracksApiError("This text will be sent as a string."))
    """

    def __init__(self, message, response):
        msg = f"{message}\nThe server responded with: {response}"
        self.response = response
        super(HellotracksApiError, self).__init__(msg)


class HellotracksInternalServerError(HellotracksClientError):
    """Used for Hellotracks API responses where response code is of type 5XX suggesting Hellotracks
    side server errors.
    """


