from abc import ABC

class BlockchainAPIsException(Exception, ABC):
    """Thrown when the API returns us an Exception"""
    
    error_code: int
    """The error code returned by the API"""
    
    detail: str
    """Some details about the error that occured"""
    
    def __init__(self, error_code: int, detail: str):
        self.error_code = error_code
        self.detail = detail
        super().__init__(f"{self.error_code} - {self.detail}")

