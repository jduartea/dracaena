class WunderClientError(Exception):
    """
    Represents any Wunder Client Error.
    """


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
    Used for Wunder API responses where response code is of type 5XX suggesting WunderMobility side server errors.
    """