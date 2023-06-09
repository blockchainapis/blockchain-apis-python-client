from dataclasses import dataclass
from typing import List
from . import Pair


@dataclass(slots=True, frozen=True)
class Pairs:
    """The Pairs model"""

    page: int
    """The page returned by the request

    Example: 1
    """

    total_pages: int
    """The total amount of pages available

    Example: 1804
    """

    data: List[Pair]
    """The list of pairs

    Example:
    [
        {
            "blockchain": "ethereum",
            "exchange": "uniswapv2_ethereum",
            "token0": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "token1": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "fee": 300
        },
        {
            "blockchain": "ethereum",
            "exchange": "uniswapv2_ethereum",
            "token0": "0x8E870D67F660D95d5be530380D0eC0bd388289E1",
            "token1": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "fee": 300
        }
    ]
    """
