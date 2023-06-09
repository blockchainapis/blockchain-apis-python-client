from dataclasses import dataclass
from typing import List
from . import Token


@dataclass(slots=True, frozen=True)
class Tokens:
    """The Tokens model"""

    page: int
    """The page returned by the request

    Example: 1
    """

    total_pages: int
    """The total amount of pages available

    Example: 174
    """

    data: List[Token]
    """100 tokens from our database.

    Example:
    [
        {
            "blockchain": "avalanche",
            "address": "0x130966628846BFd36ff31a822705796e8cb8C18D",
            "decimals": 18,
            "market_cap": 112266645.61161652
        },
        {
            "blockchain": "avalanche",
            "address": "0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB",
            "decimals": 18,
            "market_cap": 110936046.16721554
        },
        {
            "blockchain": "avalanche",
            "address": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
            "decimals": 18,
            "market_cap": 88785441.02623828
        },
        {
            "blockchain": "avalanche",
            "address": "0x6e84a6216eA6dACC71eE8E6b0a5B7322EEbC0fDd",
            "decimals": 18,
            "market_cap": 71669567.812698
        },
        {
            "blockchain": "avalanche",
            "address": "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70",
            "decimals": 18,
            "market_cap": 66925902.344998635
        },
        {
            "blockchain": "avalanche",
            "address": "0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE",
            "decimals": 18,
            "market_cap": 65308840.501452334
        },
        {
            "blockchain": "avalanche",
            "address": "0xc7198437980c041c805A1EDcbA50c1Ce5db95118",
            "decimals": 6,
            "market_cap": 62609470.072472
        }
    ]
    """
