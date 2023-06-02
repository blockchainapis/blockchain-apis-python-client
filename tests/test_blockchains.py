from dataclasses import asdict

from BlockchainAPIsTester import BlockchainAPIsTester

class TestBlockchains(BlockchainAPIsTester):
    """
    Test for the method blockchains of BlockchainAPIs
    """

    async def test_blockchains_(self):
        api_result = await self.api.blockchains()
        api_call = await self.do_request("/v0/blockchains/")
        self.assertListEqual([asdict(r) for r in api_result], api_call)
