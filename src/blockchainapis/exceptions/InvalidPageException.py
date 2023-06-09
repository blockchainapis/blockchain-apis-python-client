from . import BlockchainAPIsException

class InvalidPageException(BlockchainAPIsException):
    """
    Thrown when you given an invalid page index during calls to responses that
    gives paginated results.
    
    An invalid page is:
    * A number lower or equal to 0
    * A page way too high
    
    You should start with 1 as page, and then the response object will give you
    the amount of pages available.
    """

    status_code: str
    """The error code returned by the call to the API
    
    For example: 400
    """

    detail: str
    """Some details about the error that occured
    
    For example:
    -2 is not a valid page number.
    """

    def __init__(self, error_code: int, detail: str):
        super().__init__(error_code, detail)    
