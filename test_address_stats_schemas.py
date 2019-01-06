import json
import unittest
from jsonschema import validate
import jsonschema


with open('address_stats_schema.json', 'r') as file:
    address_stats_schema = json.load(file)
file.close()


class addressTest(unittest.TestCase):
    def test_address_stats_schemas_with_valid_data(self):
        validate({'address': 'foo', 'balance': 'bar', 'created_at': 'qux'}, address_stats_schema)

    def test_address_stats_schemas_with_missing_address_data(self):
        msg = "'address' is a required property"
        with self.assertRaisesRegex(jsonschema.exceptions.ValidationError, msg):
            validate({'balance': 'qux'}, address_stats_schema)

    def test_address_stats_schemas_with_invalid_data(self):
        msg = "3 is not of type 'string'"
        with self.assertRaisesRegex(jsonschema.exceptions.ValidationError, msg):
            validate({'address': 3, 'balance': 'qux'}, address_stats_schema)
