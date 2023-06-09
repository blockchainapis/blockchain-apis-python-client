from . import BlockchainAPIsException

class BlockchainNotSupportedException(BlockchainAPIsException):
    """
    Thrown when an Invalid blockchain id is put during a call to the API.
    
    To get the list of valid blockchain ids, call `/blockchains`
    """

    status_code: str
    """The error code returned by the call to the API
    
    For example: 422
    """

    detail: str
    """Some details about the error that occured
    
    For example:
    Blockchain with id "test" is not supported. You can find a list of valid blockchain ids in /blockchains
    """

    def __init__(self, error_code: int, detail: str):
        super().__init__(error_code, detail)    
