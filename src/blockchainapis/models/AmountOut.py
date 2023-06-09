from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AmountOut:
    """The AmountOut model"""

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
    """The amount of tokenIn that you sell

    Example: 1000000000000000000
    """

    amountOut: int
    """The amount of tokenOut that you will get after selling amountIn tokenIn on this exchange

    Example: 11088529
    """
