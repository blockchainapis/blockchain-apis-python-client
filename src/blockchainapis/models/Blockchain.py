from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Blockchain:
    """The Blockchain model"""

    blockchain: str
    """The blockchain id that should be used for other calls

    Example: "avalanche"
    """

    name: str
    """The name of the blockchain

    Example: "Avalanche"
    """

    chain_id: int
    """The chain id of the blockchain that is used to add the blockchain in wallets like Metamask

    Example: 43114
    """

    explorer: str
    """The url to the explorer of the blockchain

    Example: "https://snowtrace.io/"
    """
