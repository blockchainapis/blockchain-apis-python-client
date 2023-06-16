from . import BlockchainAPIsException

class UnknownBlockchainAPIsException(BlockchainAPIsException):
    """
    Thrown when an unknown exception was returned by the API
    """
    
    status_code: int
    """The status code returned by the API"""
    
    detail: str
    """The details of the exception"""


    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code, detail)    
