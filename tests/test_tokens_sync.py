from dataclasses import asdict

from BlockchainAPIsSyncTester import BlockchainAPIsSyncTester

class TestTokens(BlockchainAPIsSyncTester):
    """
    Test for the method tokens of BlockchainAPIs
    """

    def test_tokens_only_required(self):
        api_result = self.api.tokens()
        api_call = self.do_request("/v0/tokens/")
        self.assertDictEqual(asdict(api_result), api_call)

    def test_tokens_page(self):
        api_result = self.api.tokens(page=1)
        api_call = self.do_request("/v0/tokens/", params={
            "page": 1
        })
        self.assertDictEqual(asdict(api_result), api_call)

    def test_tokens_blockchain(self):
        api_result = self.api.tokens(blockchain="ethereum")
        api_call = self.do_request("/v0/tokens/", params={
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    def test_tokens_page_blockchain(self):
        api_result = self.api.tokens(page=1, blockchain="ethereum")
        api_call = self.do_request("/v0/tokens/", params={
            "page": 1,
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)
