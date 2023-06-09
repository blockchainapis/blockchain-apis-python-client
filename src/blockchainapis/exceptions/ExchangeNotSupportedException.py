from . import BlockchainAPIsException

class ExchangeNotSupportedException(BlockchainAPIsException):
    """
    Thrown when an Invalid exchange id is given during a call to the API.
    
    To get the list of supported exchange ids, call `/exchanges`
    """

    status_code: str
    """The error code returned by the call to the API
    
    For example: 422
    """

    detail: str
    """Some details about the error that occured
    
    For example:
    Exchange with id "test" is not supported. You can get the list of valid exchange ids in /exchanges
    """

    def __init__(self, error_code: int, detail: str):
        super().__init__(error_code, detail)    
