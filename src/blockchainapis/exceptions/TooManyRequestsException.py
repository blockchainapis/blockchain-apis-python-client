from . import BlockchainAPIsException

class TooManyRequestsException(BlockchainAPIsException):
    """
    Thrown when you are doing more request than you are allowed to the API.
    
    To prevent this exception you can:
    - Lower the amount of requests that you make to the API per second
    - Upgrade your subscription at: https://dashboard.blockchainapis.io/
    """

    status_code: str
    """The error code returned by the call to the API
    
    For example: 429
    """

    detail: str
    """Some details about the error that occured
    
    For example:
    Too many requests
    """

    def __init__(self, error_code: int, detail: str):
        super().__init__(error_code, detail)    
