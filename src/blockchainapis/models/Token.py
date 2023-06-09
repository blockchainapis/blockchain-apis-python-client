from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class Token:
    """The Token model"""

    blockchain: str
    """The blockchain on which the token is

    Example: "avalanche"
    """

    address: str
    """The address of the token on the blockchain

    Example: "0xc7198437980c041c805A1EDcbA50c1Ce5db95118"
    """

    decimals: int
    """The decimals of the token

    Example: 6
    """

    market_cap: Decimal
    """Total supply of the token multiplied by the worth of one token in liquidity pools.

The value is in dollars, it can be None if the liquidity of the token in pools is lower than 1000$

This value is in Decimal, and is based on USDT.

    Example: Decimal(62609470.072472)
    """
