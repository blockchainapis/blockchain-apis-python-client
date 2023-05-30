
from dataclasses import asdict

from BlockchainAPIsTester import BlockchainAPIsTester

class TestPairs(BlockchainAPIsTester):
    """
    Test for the method pairs of BlockchainAPIs
    """

    async def test_pairs_only_required(self):
        api_result = await self.api.pairs()
        api_call = await self.do_request("/v0/exchanges/pairs")
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_page(self):
        api_result = await self.api.pairs(page=1)
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "page": 1
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_blockchain(self):
        api_result = await self.api.pairs(blockchain="ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_exchange(self):
        api_result = await self.api.pairs(exchange="uniswapv2_ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "exchange": "uniswapv2_ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_page_blockchain(self):
        api_result = await self.api.pairs(page=1, blockchain="ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "page": 1,
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_page_exchange(self):
        api_result = await self.api.pairs(page=1, exchange="uniswapv2_ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "page": 1,
            "exchange": "uniswapv2_ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_blockchain_exchange(self):
        api_result = await self.api.pairs(blockchain="ethereum", exchange="uniswapv2_ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "blockchain": "ethereum",
            "exchange": "uniswapv2_ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_pairs_page_blockchain_exchange(self):
        api_result = await self.api.pairs(page=1, blockchain="ethereum", exchange="uniswapv2_ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs", params={
            "page": 1,
            "blockchain": "ethereum",
            "exchange": "uniswapv2_ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)
