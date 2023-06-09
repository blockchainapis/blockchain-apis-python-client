from dataclasses import dataclass
from typing import List
from . import Exchange


@dataclass(slots=True, frozen=True)
class Exchanges:
    """The Exchanges model"""

    page: int
    """The page returned by the request

    Example: 1
    """

    total_pages: int
    """The total amount of pages available

    Example: 1
    """

    data: List[Exchange]
    """The list of exchanges

    Example:
    [
        {
            "exchange": "lydia_finance_avalanche",
            "blockchain": "avalanche",
            "name": "Lydia Finance",
            "url": "https://exchange.lydia.finance/#/swap",
            "fee": 200
        },
        {
            "exchange": "oliveswap_avalanche",
            "blockchain": "avalanche",
            "name": "Oliveswap",
            "url": "https://avax.olive.cash/",
            "fee": 250
        }
    ]
    """
