import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.bids import Bids
from infra.config_provider import ConfigProvider


class TestShuffleTheCards(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()

    def test_correct_response_after_retrieving_executive_bid(self):
        """
        GET request test.
        Tests if retrieving an executable bid will get us a success response.
        The querystring and the headers of the bid is in the config.json file
        """
        # Act
        executable_bids_body = Bids(self._api_request).get_retrieve_executable_bids().json()
        # Assert
        self.assertTrue(executable_bids_body['success'],
                        "The response did not succeed when retrieving executable bids.")

    def test_executable_size_greater_than_or_equal_to_bidders_number(self):
        """
        GET request test.
        Tests that executableSize is always greater than or equal to numberBidders
        for each price level in the response.
        """
        executable_bids_body = Bids(self._api_request).get_retrieve_executable_bids().json()
        for price_level in executable_bids_body['priceLevels']:
            executable_size = price_level['executableSize']
            number_bidders = price_level['numberBidders']
            self.assertGreaterEqual(executable_size, number_bidders,
                                    f"Executable size {executable_size} is not greater than or equal to number "
                                    f"of bidders {number_bidders} for price level {price_level['price']}")

    def test_unauthorized_response_retrieve_user_bids(self):
        """
        GET request test.
        Tests that if given an api request without an authentication key, then the
        response will be a 401 status code, which mean unauthorized.
        """
        # Act
        user_bids_body = Bids(self._api_request).get_retrieve_user_bids().json()
        # Assert
        self.assertEqual(user_bids_body['statusCode'], 401)
