from dataclasses import asdict

from BlockchainAPIsSyncTester import BlockchainAPIsSyncTester

class TestInfo(BlockchainAPIsSyncTester):
    """
    Test for the method info of BlockchainAPIs
    """

    def test_info_only_required(self):
        api_result = self.api.info(blockchain="ethereum", token="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
        api_call = self.do_request("/v0/tokens/info", params={
            "blockchain": "ethereum",
            "token": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        })
        self.assertDictEqual(asdict(api_result), api_call)
