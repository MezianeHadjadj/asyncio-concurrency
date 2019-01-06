import aiohttp
import asyncio
import json
import random
import os
import datetime


class Address(object):
    async def number_of_transactions(self):
        # etherscan api dosen't provide number of transactions for now we generate a random number.
        return random.randint(0, 1000)

    async def fetch_balance(self, address):
        async with aiohttp.ClientSession() as session:
            eth_balance_api_url = 'https://api.etherscan.io/api?module=account&action=balance&tag=latest&apikey='
            os.environ['ETHERSCAN_API_KEY'] + '&address=' + address
            async with session.get(eth_balance_api_url) as response:
                return await response.text()

    async def get_stats(self, address):
        tasks = [
            asyncio.ensure_future(self.fetch_balance(address)),
            asyncio.ensure_future(self.number_of_transactions())
        ]
        results = await asyncio.gather(*tasks)
        return {'address': address, 'balance': json.loads(results[0])['result'], 'number_of_transactions': results[1],
                'created_at': str(datetime.datetime.now())}
