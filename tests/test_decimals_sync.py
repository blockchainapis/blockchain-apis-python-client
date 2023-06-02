from BlockchainAPIsSyncTester import BlockchainAPIsSyncTester

class TestDecimals(BlockchainAPIsSyncTester):
    """
    Test for the method decimals of BlockchainAPIs
    """

    def test_decimals_only_required(self):
        api_result = self.api.decimals(blockchain="ethereum", token="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
        api_call = self.do_request("/v0/tokens/decimals", params={
            "blockchain": "ethereum",
            "token": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        })
        self.assertEqual(api_result, api_call)
