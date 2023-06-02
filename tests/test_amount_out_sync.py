from dataclasses import asdict

from BlockchainAPIsSyncTester import BlockchainAPIsSyncTester

class TestAmount_out(BlockchainAPIsSyncTester):
    """
    Test for the method amount_out of BlockchainAPIs
    """

    def test_amount_out_only_required(self):
        api_result = self.api.amount_out(blockchain="ethereum", tokenIn="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", tokenOut="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", amountIn=1000000000000000000)
        api_call = self.do_request("/v0/exchanges/pairs/amountOut", params={
            "blockchain": "ethereum",
            "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "amountIn": 1000000000000000000
        })
        self.assertListEqual([asdict(r) for r in api_result], api_call)

    def test_amount_out_exchange(self):
        api_result = self.api.amount_out(blockchain="ethereum", tokenIn="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", tokenOut="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", amountIn=1000000000000000000, exchange="uniswapv2_ethereum")
        api_call = self.do_request("/v0/exchanges/pairs/amountOut", params={
            "blockchain": "ethereum",
            "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "amountIn": 1000000000000000000,
            "exchange": "uniswapv2_ethereum"
        })
        self.assertListEqual([asdict(r) for r in api_result], api_call)
