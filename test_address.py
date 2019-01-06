import asyncio
from aioresponses import aioresponses
import unittest
import re
from address import Address
import random
import datetime


class NewDate(datetime.datetime):
    @classmethod
    def now(cls):
        return cls(2018, 11, 1, 4, 5, 6)


datetime.datetime = NewDate


class addressTest(unittest.TestCase):
    @unittest.mock.patch('random.randint')
    def test_get_stats(self, randint_mock):
        randint_mock.return_value = 232
        address = Address()
        with aioresponses() as aioresponse:
            pattern = re.compile(r'^https://api.etherscan.io/api/?.*$')
            aioresponse.get(pattern, payload={'status': '1', 'message': 'OK', 'result': '323'})

            loop = asyncio.get_event_loop()
            resp = loop.run_until_complete(address.get_stats('address_id'))
            assert {'address': 'address_id', 'balance': "323", 'number_of_transactions': 232, 'created_at': '2018-11-01 04:05:06'} == resp
