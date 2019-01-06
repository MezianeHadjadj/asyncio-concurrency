import json
import dataset
from jsonschema import validate


with open('address_stats_schema.json', 'r') as file:
    address_stats_schema = json.load(file)
file.close()

db = dataset.connect('sqlite:///:memory:')
table = db['eth_addresses']


class StorageAdapter:
    async def insert_address_stats(self, stats):
        validate(stats, address_stats_schema)
        print(stats)
        return table.insert(stats)
