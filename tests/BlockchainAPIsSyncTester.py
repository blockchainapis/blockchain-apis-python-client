
import requests

from unittest import TestCase
from typing import Any
from urllib.parse import urljoin

from src.blockchainapis import BlockchainAPIsSync
from secret_config import API_KEY

class BlockchainAPIsSyncTester(TestCase):
    """
    Helper class to write some test for BlockchainAPIsSync
    
    This test are for the synchronous client only
    """
    
    api: BlockchainAPIsSync | None
    """The API SDK that we have to test"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = None
        self._headers = {
            "api-key": API_KEY  
        }
        self._base_url = "https://api.blockchainapis.io"
    
    def setUp(self):
        self.api = BlockchainAPIsSync(api_key=API_KEY)

    def tearDown(self):
        self.api = None

    def do_request(self, url, params = {}):
        url = urljoin(self._base_url, url)
        response = requests.get(url, params=params, headers=self._headers)
        return response.json()
