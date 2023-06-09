"""
Contains the Exceptions that can be thrown from
Blockchain APIs

These exceptions are thrown when a call is made to Blockchain APIs
and the response code is not 200 or 201

"""

from .BlockchainAPIsException import BlockchainAPIsException
from .BlockchainNotSupportedException import BlockchainNotSupportedException
from .ExchangeNotSupportedException import ExchangeNotSupportedException
from .InvalidPageException import InvalidPageException
from .TokenNotFoundException import TokenNotFoundException
from .PairNotFoundException import PairNotFoundException
from .TooManyRequestsException import TooManyRequestsException
from .UnauthorizedException import UnauthorizedException

__all__ = [
    "BlockchainNotSupportedException",
    "ExchangeNotSupportedException",
    "InvalidPageException",
    "TokenNotFoundException",
    "PairNotFoundException",
    "TooManyRequestsException",
    "UnauthorizedException"
]
