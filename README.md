# Blockchain APIs

## Introduction

The fastest and easiest way to interact with DeFi.

With this SDK you can:
- Get the price of any pair across all marketplaces in one API call
- Get the current reserves of any pair
- Use the same code to gather data from many blockchains and exchanges

Since DeFi is volatile and fast moving space, you need an SDK that is highly performant. Here are the capabilities of **Blockchain APIs**:
- Make async API calls for more than 1000 requests per second
- Processing time 20 times faster than the blockchain

Examples of project that you can make with **Blockchain APIs**:
- Arbitrage trading bot
- Aggregator
- Application to track cryptocurrency prices

To get any help, feel free to join [our discord](https://discord.gg/GphRMJXmS5)
Documentation link: [https://api.blockchainapis.io/docs](https://api.blockchainapis.io/docs)

## Quickstart

### Install the package

`pip install blockchain-apis`

### Get the current price of ethereum accross all blockchains

```python
import asyncio

from blockchainapis import BlockchainAPIs

async def print_eth_price():
    blockchain_apis = BlockchainAPIs()
    # Get the price of selling 1 ETH to USDT in Ethereum
    eth_price = await blockchain_apis.amount_out(
        blockchain="ethereum",
        amountIn=1000000000000000000,
        tokenIn="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        tokenOut="0xdAC17F958D2ee523a2206206994597C13D831ec7"
    )

    print(eth_price)
    await blockchain_apis.close()

asyncio.run(print_eth_price())
```

#### Example response:

```json
[
  {
    "blockchain": "ethereum",
    "exchange": "elk_finance_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "amountIn": 1000000000000000000,
    "amountOut": 149342441
  },
  {
    "blockchain": "ethereum",
    "exchange": "pancakeswap_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "amountIn": 1000000000000000000,
    "amountOut": 1873655816
  },
  {
    "blockchain": "ethereum",
    "exchange": "plasmafinance_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "amountIn": 1000000000000000000,
    "amountOut": 8710340
  },
  {
    "blockchain": "ethereum",
    "exchange": "shibaswap_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "amountIn": 1000000000000000000,
    "amountOut": 1897543149
  },
  {
    "blockchain": "ethereum",
    "exchange": "sushiswap_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "amountIn": 1000000000000000000,
    "amountOut": 1905389353
  },
  {
    "blockchain": "ethereum",
    "exchange": "uniswapv2_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "amountIn": 1000000000000000000,
    "amountOut": 1904261651
  }
]
```
