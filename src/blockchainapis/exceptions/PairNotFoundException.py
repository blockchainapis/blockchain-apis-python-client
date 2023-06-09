from . import BlockchainAPIsException

class PairNotFoundException(BlockchainAPIsException):
    """
    Thrown when you try to get some data about a pair that does not exist.
    
    To avoid getting this error, you can get the list of available pairs for
    the blockchain and exchange that you are interested in by calling `/exchanges/pairs`
    """

    status_code: str
    """The error code returned by the call to the API
    
    For example: 422
    """

    detail: str
    """Some details about the error that occured
    
    For example:
    Pair 0x8E870D67F660D95d5be530380D0eC0bd388289E1->0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2 not found in blockchain Arbitrum
    """

    def __init__(self, error_code: int, detail: str):
        super().__init__(error_code, detail)    
