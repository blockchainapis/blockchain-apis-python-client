from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Exchange:
    """The Exchange model"""

    exchange: str
    """The exchange unique id that should be put in other calls

    Example: "lydia_finance_avalanche"
    """

    blockchain: str
    """The blockchain on which the exchange is done

    Example: "avalanche"
    """

    name: str
    """The name of the exchange

    Example: "Lydia Finance"
    """

    url: str
    """The url to the exchange

    Example: "https://exchange.lydia.finance/#/swap"
    """
