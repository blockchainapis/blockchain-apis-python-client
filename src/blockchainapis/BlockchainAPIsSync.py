import requests

from typing import Any, Dict, List
from urllib.parse import urljoin

from .models import Blockchain
from .models import Exchanges
from .models import Exchange
from .models import Pairs
from .models import Pair
from .models import Reserve
from .models import AmountOut
from .models import AmountIn
from .models import Tokens
from .models import Token

from .exceptions import BlockchainNotSupportedException
from .exceptions import ExchangeNotSupportedException
from .exceptions import InvalidPageException
from .exceptions import TokenNotFoundException
from .exceptions import PairNotFoundException
from .exceptions import TooManyRequestsException
from .exceptions import UnauthorizedException
from .exceptions import UnknownBlockchainAPIsException


class BlockchainAPIsSync:
    """High-frequency DEX API

    Our API empowers you to access live financial data across multiple blockchains
    (currently supporting 6, with more on the way) with unparalleled speed and efficiency.
    
    What sets our API apart? We've optimized performance to deliver an impressive 1000+
    calls per second per user, with a lightning-fast processing time of less than 2 millisecond
    per request. Compare that to other solutions with a 20-millisecond processing time and fewer
    requests per second, and it's clear why developers choose our API for their trading bots.
    
    Another game-changing feature is our seamless integration across various blockchains and
    protocols. With our API, you can reuse the same code without changing a single line, simplifying
    the development process and saving you valuable time.
    
    Ready to try it out? [Sign up for a free API key here](https://dashboard.blockchainapis.io)
    or start exploring the possibilities on this page. Need support or have questions? Join our
    [Discord community](https://discord.gg/GphRMJXmS5) where our team and fellow developers are
    eager to help you make the most of our powerful API.
    """
    
    def __init__(self, api_key: str | None = None):
        """Creates a BlockchainAPIsSync sync instance that allow you to make API calls
        in a synchronous way.

        The client works without an API key, but for better performance, we advise you
        to get one at: https://dashboard.blockchainapis.io

        :param api_key: Your API key, defaults to None
        :type api_key: str | None, optional
        """
        self._headers = {
            "accept": "application/json"
        }
        if api_key is not None:
            self._headers["api-key"] = api_key
        self._base_url = "https://api.blockchainapis.io"


    def _do_request(self, path: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """Make a raw API request (that return the json result).
        
        It makes the request in a synchronous way and you don't need to close the
        BlockchainAPIs instance.

        :raises BlockchainNotSupportedException: Thrown when an Invalid blockchain id is put during a call to the API.
        :raises ExchangeNotSupportedException: Thrown when an Invalid exchange id is given during a call to the API.
        :raises InvalidPageException: Thrown when you given an invalid page index during calls to responses thatgives paginated results.
        :raises TokenNotFoundException: Thrown when you try to get informations on a token that does not exist inside of our database.
        :raises PairNotFoundException: Thrown when you try to get some data about a pair that does not exist.
        :raises TooManyRequestsException: Thrown when you are doing more request than you are allowed to the API.
        :raises UnauthorizedException: Thrown when you are trying to make an API request with an invalid or expiredAPI key.
        :raises UnknownBlockchainAPIsException: When an unknown exception happens

        :param path: The path of the request
        :type path: str
        :param params: The optional query parameters of the request, defaults to None
        :type params: Dict[str, Any] | None, optional
        :return: The json-formated result
        :rtype: Dict[str, Any]
        """
        url = urljoin(self._base_url, path)
        response = requests.get(url, params=params, headers=self._headers)
        if response.status_code != 200:
            error_data = response.json()
            error_type = error_data["detail"]["error_type"]
            match error_type:
                case "BlockchainNotSupportedException":
                    raise BlockchainNotSupportedException(response.status_code, error_data["detail"]["detail"])
                case "ExchangeNotSupportedException":
                    raise ExchangeNotSupportedException(response.status_code, error_data["detail"]["detail"])
                case "InvalidPageException":
                    raise InvalidPageException(response.status_code, error_data["detail"]["detail"])
                case "TokenNotFoundException":
                    raise TokenNotFoundException(response.status_code, error_data["detail"]["detail"])
                case "PairNotFoundException":
                    raise PairNotFoundException(response.status_code, error_data["detail"]["detail"])
                case "TooManyRequestsException":
                    raise TooManyRequestsException(response.status_code, error_data["detail"]["detail"])
                case "UnauthorizedException":
                    raise UnauthorizedException(response.status_code, error_data["detail"]["detail"])
                case _:
                    raise UnknownBlockchainAPIsException(response.status, f"Unkwnown Exception type: {error_type}.\nGot this exception while handling:\n{error_data} with status code: {response.status}")

        return response.json()

    def blockchains(self) -> List[Blockchain]:
        """Get the list of blockchains supported by the API


        :return: The list of the blockchains supported by the API.
        
        Using this method, you can find the id of the blockchain that you can use for
        other function calls.


        Example response:
        ```json
        [
            {
                "blockchain": "avalanche",
                "name": "Avalanche",
                "chain_id": 43114,
                "explorer": "https://snowtrace.io/"
            }

        ]
        ```
        :rtype: List[Blockchain]
        """
        ret = self._do_request("/v0/blockchains/")
        return [
            Blockchain(
                blockchain=r["blockchain"],
                name=r["name"],
                chain_id=r["chain_id"],
                explorer=r["explorer"]
            )
            for r in ret
        ]

    def exchanges(self, page: int = 1, blockchain: str | None = None) -> Exchanges:
        """Get the list of supported exchanges by the API

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises InvalidPageException: When an invalid page is given

        :param page: You can ignore this value for this version of the API., defaults to 1
        :type page: int, Optional
        :example page: 1
        :param blockchain: The blockchain from which you want to get the exchanges, defaults to None
        :type blockchain: str, Optional
        :example blockchain: ethereum
        :return: The list of all supported exchange of the API.
        
        You can use the exchange id responded from this for other API calls.


        Example response:
        ```json
        {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "exchange": "lydia_finance_avalanche",
                    "blockchain": "avalanche",
                    "name": "Lydia Finance",
                    "url": "https://exchange.lydia.finance/#/swap",
                    "fee": 200
                },
                {
                    "exchange": "oliveswap_avalanche",
                    "blockchain": "avalanche",
                    "name": "Oliveswap",
                    "url": "https://avax.olive.cash/",
                    "fee": 250
                }
            ]
        }

        ```
        :rtype: Exchanges
        """
        params = {}
        params["page"] = page
        if blockchain is not None:
            params["blockchain"] = blockchain
        ret = self._do_request("/v0/exchanges/", params)
        return Exchanges(
            page=ret["page"],
            total_pages=ret["total_pages"],
            data=[
                Exchange(
                    exchange=d["exchange"],
                    blockchain=d["blockchain"],
                    name=d["name"],
                    url=d["url"]
                )
                for d in ret["data"]
            ]
        )

    def info(self, exchange: str) -> Exchange:
        """Get informations on a specific exchange

        :raises ExchangeNotSupportedException: Thrown when an invalid exchange id is given

        :param exchange: The exchange to get the informations from
        :type exchange: str
        :example exchange: uniswapv2_ethereum
        :return: Information on a specific exchange.
        
        These informations includes:
        - The blockchain id of the exchange
        - The id of the exchange
        - The name of the exchange
        - The url to access the exchange


        Example response:
        ```json
        {
            "exchange": "lydia_finance_avalanche",
            "blockchain": "avalanche",
            "name": "Lydia Finance",
            "url": "https://exchange.lydia.finance/#/swap",
            "fee": 200
        }

        ```
        :rtype: Exchange
        """
        params = {}
        params["exchange"] = exchange
        ret = self._do_request("/v0/exchanges/info", params)
        return Exchange(
            exchange=ret["exchange"],
            blockchain=ret["blockchain"],
            name=ret["name"],
            url=ret["url"]
        )

    def pairs(self, page: int = 1, blockchain: str | None = None, exchange: str | None = None) -> Pairs:
        """Get the list of pairs supported by the API

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises ExchangeNotSupportedException: When an invalid Exchange id is given
        :raises InvalidPageException: When you give an invalid page number

        :param page: Each request has a maximum of 100 results separated by page, defaults to 1
        :type page: int, Optional
        :example page: 1
        :param blockchain: The blockchain from which you want to get the pairs, defaults to None
        :type blockchain: str, Optional
        :example blockchain: ethereum
        :param exchange: The exchange from which you want to get the pairs, defaults to None
        :type exchange: str, Optional
        :example exchange: uniswapv2_ethereum
        :return: The list of pairs supported by the API. It returns token addresses,
        blockchain, exchange and the fee that the pair has.
        
        The fee may vary depending on the exchange used.


        Example response:
        ```json
        {
            "page": 1,
            "total_pages": 1804,
            "data": [
                {
                    "blockchain": "ethereum",
                    "exchange": "uniswapv2_ethereum",
                    "token0": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                    "token1": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                    "fee": 300
                },
                {
                    "blockchain": "ethereum",
                    "exchange": "uniswapv2_ethereum",
                    "token0": "0x8E870D67F660D95d5be530380D0eC0bd388289E1",
                    "token1": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                    "fee": 300
                }
            ]
        }

        ```
        :rtype: Pairs
        """
        params = {}
        params["page"] = page
        if blockchain is not None:
            params["blockchain"] = blockchain
        if exchange is not None:
            params["exchange"] = exchange
        ret = self._do_request("/v0/exchanges/pairs", params)
        return Pairs(
            page=ret["page"],
            total_pages=ret["total_pages"],
            data=[
                Pair(
                    blockchain=d["blockchain"],
                    exchange=d["exchange"],
                    token0=d["token0"],
                    token1=d["token1"],
                    fee=d["fee"]
                )
                for d in ret["data"]
            ]
        )

    def reserves(self, blockchain: str, token0: str, token1: str, exchange: str | None = None) -> List[Reserve]:
        """Get the liquidity inside of the reserve of two tokens.

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises ExchangeNotSupportedException: When an invalid exchange id is given
        :raises PairNotFoundException: When a pair is not found for the given blockchain or exchange

        :param blockchain: The id of the blockchain on which the exchange will happen. It is required because some tokens can have same address accross multiple blockchains
        :type blockchain: str
        :example blockchain: ethereum
        :param token0: The address of the first token of the pair
        :type token0: str
        :example token0: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
        :param token1: The address of the second token of the pair
        :type token1: str
        :example token1: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
        :param exchange: The id of the exchange from which you want to get the reserve, defaults to None
        :type exchange: str, Optional
        :example exchange: uniswapv2_ethereum
        :return: The list of all of the reserve for the given pair, blockchain and exchange.
        Can return an empty list if the given pair was not found.


        Example response:
        ```json
        [
            {
                "blockchain": "avalanche",
                "exchange": "lydia_finance_avalanche",
                "token0": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
                "token1": "0xf20d962a6c8f70c731bd838a3a388D7d48fA6e15",
                "reserve0": 11100509297299255000,
                "reserve1": 117592619550992960
            }

        ]
        ```
        :rtype: List[Reserve]
        """
        params = {}
        params["blockchain"] = blockchain
        if exchange is not None:
            params["exchange"] = exchange
        params["token0"] = token0
        params["token1"] = token1
        ret = self._do_request("/v0/exchanges/pairs/reserves", params)
        return [
            Reserve(
                blockchain=r["blockchain"],
                exchange=r["exchange"],
                token0=r["token0"],
                token1=r["token1"],
                reserve0=r["reserve0"],
                reserve1=r["reserve1"]
            )
            for r in ret
        ]

    def amount_out(self, blockchain: str, tokenIn: str, tokenOut: str, amountIn: int, exchange: str | None = None) -> List[AmountOut]:
        """Get the amount of tokenOut that you will get after selling amountIn tokenIn

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises ExchangeNotSupportedException: When an invalid exchange id is given
        :raises PairNotFoundException: When a pair is not found for the given blockchain or exchange

        :param blockchain: The id of the blockchain on which this exchange take place
        :type blockchain: str
        :example blockchain: ethereum
        :param tokenIn: The address of the token that you sell
        :type tokenIn: str
        :example tokenIn: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
        :param tokenOut: The address of the token that you buy
        :type tokenOut: str
        :example tokenOut: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
        :param amountIn: The amount of tokenIn that you sell
        :type amountIn: int
        :example amountIn: 1000000000000000000
        :param exchange: The exchange on which you want to do the trade, defaults to None
        :type exchange: str, Optional
        :example exchange: uniswapv2_ethereum
        :return: The list of the amount out that you will get on all of the exchanges. It can return an empty list if the given pair was not found for the given parameters.


        Example response:
        ```json
        [
            {
                "blockchain": "avalanche",
                "exchange": "lydia_finance_avalanche",
                "tokenIn": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
                "tokenOut": "0xde3A24028580884448a5397872046a019649b084",
                "amountIn": 1000000000000000000,
                "amountOut": 11088529
            }

        ]
        ```
        :rtype: List[AmountOut]
        """
        params = {}
        params["blockchain"] = blockchain
        params["tokenIn"] = tokenIn
        params["tokenOut"] = tokenOut
        params["amountIn"] = amountIn
        if exchange is not None:
            params["exchange"] = exchange
        ret = self._do_request("/v0/exchanges/pairs/amountOut", params)
        return [
            AmountOut(
                blockchain=r["blockchain"],
                exchange=r["exchange"],
                tokenIn=r["tokenIn"],
                tokenOut=r["tokenOut"],
                amountIn=r["amountIn"],
                amountOut=r["amountOut"]
            )
            for r in ret
        ]

    def amount_in(self, blockchain: str, tokenIn: str, tokenOut: str, amountOut: int, exchange: str | None = None) -> List[AmountIn]:
        """Get the amount of tokenIn that you need to sell in order to get amountOut tokenOut

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises ExchangeNotSupportedException: When an invalid exchange id is given
        :raises PairNotFoundException: When a pair is not found for the given blockchain or exchange

        :param blockchain: The id of the blockchain on which this exchange take place
        :type blockchain: str
        :example blockchain: ethereum
        :param tokenIn: The address of the token that you sell
        :type tokenIn: str
        :example tokenIn: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
        :param tokenOut: The address of the token that you buy
        :type tokenOut: str
        :example tokenOut: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
        :param amountOut: The amount of tokenOut that you are trying to get
        :type amountOut: int
        :example amountOut: 1000000000000000000
        :param exchange: The exchange on which you want to do the trade, defaults to None
        :type exchange: str, Optional
        :example exchange: uniswapv2_ethereum
        :return: The list of amount in that you will get on all of the exchanges. It can return an empty list if the given pair was not found.


        Example response:
        ```json
        [
            {
                "blockchain": "avalanche",
                "exchange": "lydia_finance_avalanche",
                "tokenIn": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
                "tokenOut": "0xde3A24028580884448a5397872046a019649b084",
                "amountIn": 843047442340946,
                "amountOut": 10000
            }

        ]
        ```
        :rtype: List[AmountIn]
        """
        params = {}
        params["blockchain"] = blockchain
        params["tokenIn"] = tokenIn
        params["tokenOut"] = tokenOut
        params["amountOut"] = amountOut
        if exchange is not None:
            params["exchange"] = exchange
        ret = self._do_request("/v0/exchanges/pairs/amountIn", params)
        return [
            AmountIn(
                blockchain=r["blockchain"],
                exchange=r["exchange"],
                tokenIn=r["tokenIn"],
                tokenOut=r["tokenOut"],
                amountIn=r["amountIn"],
                amountOut=r["amountOut"]
            )
            for r in ret
        ]

    def tokens(self, page: int = 1, blockchain: str | None = None) -> Tokens:
        """Get the list of supported tokens

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises InvalidPageException: When an invalid page number is given

        :param page: Each request have a limit of 100 data separated per pages, defaults to 1
        :type page: int, Optional
        :example page: 1
        :param blockchain: The blockchain on which you want to get the tokens, defaults to None
        :type blockchain: str, Optional
        :example blockchain: ethereum
        :return: The list of supported tokens ordered by market cap in a descending order.
        
        The market capitalization is in dollars, it can be null if the liquidity available for the given token is lower than 1000$.
        The market capitalization is based on USDT.
        
        The market capitalization of each token is computed as follow:
        average worth of token in liquidity pools * total token supply


        Example response:
        ```json
        {
            "page": 1,
            "total_pages": 174,
            "data": [
                {
                    "blockchain": "avalanche",
                    "address": "0x130966628846BFd36ff31a822705796e8cb8C18D",
                    "decimals": 18,
                    "market_cap": 112266645.61161652
                },
                {
                    "blockchain": "avalanche",
                    "address": "0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB",
                    "decimals": 18,
                    "market_cap": 110936046.16721554
                },
                {
                    "blockchain": "avalanche",
                    "address": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
                    "decimals": 18,
                    "market_cap": 88785441.02623828
                },
                {
                    "blockchain": "avalanche",
                    "address": "0x6e84a6216eA6dACC71eE8E6b0a5B7322EEbC0fDd",
                    "decimals": 18,
                    "market_cap": 71669567.812698
                },
                {
                    "blockchain": "avalanche",
                    "address": "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70",
                    "decimals": 18,
                    "market_cap": 66925902.344998635
                },
                {
                    "blockchain": "avalanche",
                    "address": "0x2b2C81e08f1Af8835a78Bb2A90AE924ACE0eA4bE",
                    "decimals": 18,
                    "market_cap": 65308840.501452334
                },
                {
                    "blockchain": "avalanche",
                    "address": "0xc7198437980c041c805A1EDcbA50c1Ce5db95118",
                    "decimals": 6,
                    "market_cap": 62609470.072472
                }
            ]
        }

        ```
        :rtype: Tokens
        """
        params = {}
        params["page"] = page
        if blockchain is not None:
            params["blockchain"] = blockchain
        ret = self._do_request("/v0/tokens/", params)
        return Tokens(
            page=ret["page"],
            total_pages=ret["total_pages"],
            data=[
                Token(
                    blockchain=d["blockchain"],
                    address=d["address"],
                    decimals=d["decimals"],
                    market_cap=d["market_cap"]
                )
                for d in ret["data"]
            ]
        )

    def info(self, blockchain: str, token: str) -> Token:
        """Get information on a specific token

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises TokenNotFoundException: When the given token is not found

        :param blockchain: The blockchain on which you want to get the information of the token
        :type blockchain: str
        :example blockchain: ethereum
        :param token: The address of the token that you want to get the informations from
        :type token: str
        :example token: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
        :return: Informations on a specific token.
        
        This information includes:
        - The id of the blockchain that this token is
        - The address of the token
        - The decimals of it
        - The market cap


        Example response:
        ```json
        {
            "blockchain": "avalanche",
            "address": "0xc7198437980c041c805A1EDcbA50c1Ce5db95118",
            "decimals": 6,
            "market_cap": 62609470.072472
        }

        ```
        :rtype: Token
        """
        params = {}
        params["blockchain"] = blockchain
        params["token"] = token
        ret = self._do_request("/v0/tokens/info", params)
        return Token(
            blockchain=ret["blockchain"],
            address=ret["address"],
            decimals=ret["decimals"],
            market_cap=ret["market_cap"]
        )

    def decimals(self, blockchain: str, token: str) -> int:
        """Get the decimals of the given token

        :raises BlockchainNotSupportedException: When an invalid blockchain id is given
        :raises TokenNotFoundException: WHen the given token is not found

        :param blockchain: The id of the blockchain of the token
        :type blockchain: str
        :example blockchain: ethereum
        :param token: The address of the token that you want to get the decimals from
        :type token: str
        :example token: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
        :return: The decimals of the specific token


        Example response:
        ```json
        16
        ```
        :rtype: int
        """
        params = {}
        params["blockchain"] = blockchain
        params["token"] = token
        ret = self._do_request("/v0/tokens/decimals", params)
        return int(ret)

    def get_token_decimal_form(self, amount: int, decimals: int) -> str:
        """Convert a token from his unsigned integer form to his decimal form.
        
        This method should be used when you want to display a token to a user.
        
        For highest precision, the implementation is made using only str.

        :param amount: The integer amount that you want to convert
        :type amount: int
        :example amount: 2500000000000000000
        :param decimals: The amount of decimals that the token you are trying to convert
                         has. You can use the [decimals](/docs/python-sdk/blockchain-apis/decimals)
                         method in order to get the amount of decimals.
        :type decimals: int
        :example decimals: 18
        :return: The given amount in a decimal form.
        
        Example response:
        ```json
        2.5
        ```
        :rtype: str
        """
        str_amount = str(amount)

        # special case when decimals is 0
        if decimals == 0:
            return str_amount

        # Check if the string length is less than the decimals
        if len(str_amount) <= decimals:
            # Add leading zeros to the string
            str_amount = '0' * (decimals - len(str_amount) + 1) + str_amount
            
        # Insert the decimal point at the correct position
        str_amount = str_amount[:-decimals] + "." + str_amount[-decimals:]
        
        str_amount = str_amount.rstrip('0').rstrip('.') if '.' in str_amount else str_amount
        return str_amount

    def get_token_unsigned_form(self, amount: str, decimals: int) -> int:
        """Convert a token from his decimal form back to his unsigned integer form (this
        method does the reverse of get_token_decimal_form)
        
        This method should be used when you receive an amount from a user, in order to convert his
        input.

        For the highest precision, the implementation only uses str

        :param amount: The amount in str format that you want to convert
        :type amount: str
        :example amount: 2.5
        :param decimals: The amount of decimals that the token has. You can use the [decimals](/docs/python-sdk/blockchain-apis/decimals)
                         method in order to get the amount of decimals.
        :type decimals: int
        :example decimals: 18
        :return: The amount converted to unsigned integer
        
        Example response:
        ```json
        2500000000000000000
        ```
        :rtype: int
        """
        split = amount.split('.')
        if len(split) >= 2:
            integer_part, fractional_part = split
        else:
            integer_part, fractional_part = split[0], ""

        # Check if the fractional part has less digits than the decimal places
        if len(fractional_part) < decimals:
            # Append zeros to the end of the fractional part
            fractional_part += '0' * (decimals - len(fractional_part))
        else:
            # Trim the fractional part to the number of decimal places
            fractional_part = fractional_part[:decimals]

        # Combine the integer and fractional parts and convert to an integer
        integer_token_amount = int(integer_part + fractional_part)

        return integer_token_amount
