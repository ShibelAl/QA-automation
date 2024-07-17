import unittest
from infra.api.api_wrapper import APIWrapper

class TestApiHarryPotter(unittest.TestCase):
    def test_check_house_by_id(self):
        api_request = APIWrapper()
        api_house = APIHouses(api_request)
