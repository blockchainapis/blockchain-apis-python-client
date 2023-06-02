from dataclasses import asdict

from BlockchainAPIsSyncTester import BlockchainAPIsSyncTester

class TestExchanges(BlockchainAPIsSyncTester):
    """
    Test for the method exchanges of BlockchainAPIs
    """

    def test_exchanges_only_required(self):
        api_result = self.api.exchanges()
        api_call = self.do_request("/v0/exchanges/")
        self.assertDictEqual(asdict(api_result), api_call)

    def test_exchanges_page(self):
        api_result = self.api.exchanges(page=1)
        api_call = self.do_request("/v0/exchanges/", params={
            "page": 1
        })
        self.assertDictEqual(asdict(api_result), api_call)

    def test_exchanges_blockchain(self):
        api_result = self.api.exchanges(blockchain="ethereum")
        api_call = self.do_request("/v0/exchanges/", params={
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)

    def test_exchanges_page_blockchain(self):
        api_result = self.api.exchanges(page=1, blockchain="ethereum")
        api_call = self.do_request("/v0/exchanges/", params={
            "page": 1,
            "blockchain": "ethereum"
        })
        self.assertDictEqual(asdict(api_result), api_call)
