from . import BlockchainAPIsException

class UnauthorizedException(BlockchainAPIsException):
    """
    Thrown when you are trying to make an API request with an invalid or expired
    API key.
    
    To prevent this exception, you can:
    - Make the request without an API key
    - Update/get a valid API key at: https://dashboard.blockchainapis.io/
    """

    status_code: str
    """The error code returned by the call to the API
    
    For example: 401
    """

    detail: str
    """Some details about the error that occured
    
    For example:
    Unauthorized
    """

    def __init__(self, error_code: int, detail: str):
        super().__init__(error_code, detail)    
