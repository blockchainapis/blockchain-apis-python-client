from dataclasses import asdict

from BlockchainAPIsTester import BlockchainAPIsTester

class TestExchanges(BlockchainAPIsTester):
    """
    Test for the method exchanges of BlockchainAPIs
    """

    async def test_exchanges_only_required(self):
        api_result = await self.api.exchanges()
        api_call = await self.do_request("/v0/exchanges/")
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_exchanges_page(self):
        api_result = await self.api.exchanges(page=1)
        api_call = await self.do_request("/v0/exchanges/", params={
            "page": 1
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_exchanges_blockchain(self):
        api_result = await self.api.exchanges(blockchain="ethereum")
        api_call = await self.do_request("/v0/exchanges/", params={
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_exchanges_page_blockchain(self):
        api_result = await self.api.exchanges(page=1, blockchain="ethereum")
        api_call = await self.do_request("/v0/exchanges/", params={
            "page": 1,
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)
