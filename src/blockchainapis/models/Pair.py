from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Pair:
    """The Pair model"""

    blockchain: str
    """The blockchain id on which the pair is

    Example: "ethereum"
    """

    exchange: str
    """The exchange id on which the pair is

    Example: "uniswapv2_ethereum"
    """

    token0: str
    """The first token of the exchange

    Example: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    """

    token1: str
    """The second token of the exchange

    Example: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    """

    fee: int
    """The fee of the pair in 100000 of percents (for example: 1000 is 1%)

    Example: 300
    """
