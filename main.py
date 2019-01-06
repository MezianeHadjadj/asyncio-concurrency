import json
import asyncio
import aiohttp
from address import Address
from storage_adapter import StorageAdapter


addresses = tuple(open('addresses.txt', 'r'))


async def main():
    tasks = []
    addressInstance = Address()
    storageAdapter = StorageAdapter()
    for address in addresses:
        # fetch stats for each address
        result = await addressInstance.get_stats(address.rstrip('\n'))
        # insert stats for each address
        task = asyncio.ensure_future(storageAdapter.insert_address_stats(result))
        tasks.append(task)
    results = await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
loop.run_until_complete(future)
