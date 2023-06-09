from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Reserve:
    """The Reserve model"""

    blockchain: str
    """The blockchain on which the reserve is

    Example: "avalanche"
    """

    exchange: str
    """The id of the exchange on which this reserve is

    Example: "lydia_finance_avalanche"
    """

    token0: str
    """The address of the token0

    Example: "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"
    """

    token1: str
    """The address of the token1

    Example: "0xf20d962a6c8f70c731bd838a3a388D7d48fA6e15"
    """

    reserve0: int
    """The amount of token0 inside of the reserve

    Example: 11100509297299255000
    """

    reserve1: int
    """The amount of token1 inside of the reserve

    Example: 117592619550992960
    """
