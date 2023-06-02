from dataclasses import asdict

from BlockchainAPIsTester import BlockchainAPIsTester

class TestTokens(BlockchainAPIsTester):
    """
    Test for the method tokens of BlockchainAPIs
    """

    async def test_tokens_only_required(self):
        api_result = await self.api.tokens()
        api_call = await self.do_request("/v0/tokens/")
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_tokens_page(self):
        api_result = await self.api.tokens(page=1)
        api_call = await self.do_request("/v0/tokens/", params={
            "page": 1
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_tokens_blockchain(self):
        api_result = await self.api.tokens(blockchain="ethereum")
        api_call = await self.do_request("/v0/tokens/", params={
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    async def test_tokens_page_blockchain(self):
        api_result = await self.api.tokens(page=1, blockchain="ethereum")
        api_call = await self.do_request("/v0/tokens/", params={
            "page": 1,
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)
