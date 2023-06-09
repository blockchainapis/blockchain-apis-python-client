"""
The blockchain-apis package allow you to interact with Blockchain
APIs in a synchronous and asynchronous way.

If you are starting on a new project, it is better to use the async
class, which is called: BlockchainAPIs

If you already have a project and don't want to bother with async,
you can use the BlockchainAPIsSync class.

"""

# Clarensia: https://www.clarensia.com is the company behind
# the development of https://www.blockchainapis.io
__author__ = "Clarensia"
__version__ = "0.1.2"

from .BlockchainAPIs import BlockchainAPIs
from .BlockchainAPIsSync import BlockchainAPIsSync

__all__ = ['BlockchainAPIs']
