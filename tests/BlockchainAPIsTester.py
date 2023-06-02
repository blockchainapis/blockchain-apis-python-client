from unittest import IsolatedAsyncioTestCase
from typing import Any

from aiohttp import ClientSession

from src.blockchainapis import BlockchainAPIs
from secret_config import API_KEY

class BlockchainAPIsTester(IsolatedAsyncioTestCase):
    """
    Helper class to write some test for BlockchainAPIs
    """
    
    _api_key: str
    """The key that we use to make API calls"""
    
    api: BlockchainAPIs
    """The API SDK that we have to test"""
    
    _session: ClientSession
    """The asyncio client session that we use to make manual API
    calls
    
    These API calls are made to compare the results
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._api_key = API_KEY
        self.api = None
        self._session = None
    
    async def asyncSetUp(self):
        """Setup the api instance.
        
        We create a new API instance and session instance for every run
        this way the tests are truly isolated.
        """
        self.api = BlockchainAPIs(api_key=self._api_key)
        self._session = ClientSession("https://api.blockchainapis.io")
        
    async def asyncTearDown(self):
        """Free the resources created from asyncSetUp
        """
        await self.api.close()
        await self._session.close()
    
    async def do_request(self, url: str, params = {}) -> Any:
        """Make a request to the API and return the json
        result

        :param url: The url that we have to fetch (only url after https://api.blockchainapis.io)
        :type url: str
        :param params: The query parameters of the request, defaults to {}
        :type params: dict, optional
        :return: The result of the request from querying directly the API.
                 This result should be compared with the one returned by the SDK.
        :rtype: Any
        """
        async with self._session.get(url, params=params, headers={"api-key": self._api_key}) as response:
            return await response.json()

