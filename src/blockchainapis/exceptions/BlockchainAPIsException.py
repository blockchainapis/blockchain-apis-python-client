from abc import ABC

class BlockchainAPIsException(Exception, ABC):
    """Thrown when the API returns us an Exception"""
    
    status_code: int
    """The status code returned by the API"""
    
    detail: str
    """Some details about the error that occured"""
    
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"{self.status_code} - {self.detail}")

