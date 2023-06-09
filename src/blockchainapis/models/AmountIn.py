from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AmountIn:
    """The AmountIn model"""

    blockchain: str
    """The id of blockchain on which the exchange is taking place

    Example: "avalanche"
    """

    exchange: str
    """The id of the exchange used for this trade

    Example: "lydia_finance_avalanche"
    """

    tokenIn: str
    """The address of the token that you sell

    Example: "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"
    """

    tokenOut: str
    """The address of the token that you buy

    Example: "0xde3A24028580884448a5397872046a019649b084"
    """

    amountIn: int
    """The amount of tokenIn that you have to sell in order to get amountOut tokenOut

    Example: 843047442340946
    """

    amountOut: int
    """The amount of tokenOut that you wish to buy

    Example: 10000
    """
