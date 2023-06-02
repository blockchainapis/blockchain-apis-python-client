from dataclasses import asdict

from BlockchainAPIsTester import BlockchainAPIsTester

class TestInfo(BlockchainAPIsTester):
    """
    Test for the method info of BlockchainAPIs
    """

    async def test_info_only_required(self):
        api_result = await self.api.info(blockchain="ethereum", token="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
        api_call = await self.do_request("/v0/tokens/info", params={
            "blockchain": "ethereum",
            "token": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        })
        self.assertDictEqual(asdict(api_result), api_call)
