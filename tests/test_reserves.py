
from dataclasses import asdict

from BlockchainAPIsTester import BlockchainAPIsTester

class TestReserves(BlockchainAPIsTester):
    """
    Test for the method reserves of BlockchainAPIs
    """

    async def test_reserves_only_required(self):
        api_result = await self.api.reserves(blockchain="ethereum", token0="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", token1="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
        api_call = await self.do_request("/v0/exchanges/pairs/reserves", params={
            "blockchain": "ethereum",
            "token0": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "token1": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
        })
        self.assertListEqual([asdict(r) for r in api_result], api_call)

    async def test_reserves_exchange(self):
        api_result = await self.api.reserves(blockchain="ethereum", token0="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", token1="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", exchange="uniswapv2_ethereum")
        api_call = await self.do_request("/v0/exchanges/pairs/reserves", params={
            "blockchain": "ethereum",
            "token0": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "token1": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "exchange": "uniswapv2_ethereum"
        })
        self.assertListEqual([asdict(r) for r in api_result], api_call)
