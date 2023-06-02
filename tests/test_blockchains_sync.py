from dataclasses import asdict

from BlockchainAPIsSyncTester import BlockchainAPIsSyncTester

class TestBlockchains(BlockchainAPIsSyncTester):
    """
    Test for the method blockchains of BlockchainAPIs
    """

    def test_blockchains_(self):
        api_result = self.api.blockchains()
        api_call = self.do_request("/v0/blockchains/")
        self.assertListEqual([asdict(r) for r in api_result], api_call)
