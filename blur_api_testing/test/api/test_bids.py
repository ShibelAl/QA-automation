import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.bids import Bids
from infra.config_provider import ConfigProvider


class TestShuffleTheCards(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by loading the configuration and initializing the API wrapper.
        """
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()

    def test_correct_price_of_first_price_level(self):
        """
        GET request test.
        Test if the price of the first price level is equal to the expected price.
        The querystring and the headers of the bid is in the config.json file.
        """
        # Act
        response = Bids(self._api_request).get_retrieve_executable_bids()
        executable_bids_body = response.json()
        print(executable_bids_body)
        # Assert
        self.assertEqual(response.status_code, 200,
                         "The response did not succeed when retrieving executable bids.")
        self.assertEqual(executable_bids_body["priceLevels"][0]["price"], self._config['expected_price'],
                         "wrong price")

    def test_executable_size_greater_than_or_equal_to_bidders_number(self):
        """
        GET request test.
        Tests that executableSize is always greater than or equal to numberBidders
        for each price level in the response.
        """
        # Act
        executable_bids_body = Bids(self._api_request).get_retrieve_executable_bids().json()
        # Assert
        for price_level in executable_bids_body['priceLevels']:
            executable_size = price_level['executableSize']
            number_bidders = price_level['numberBidders']
            self.assertGreaterEqual(executable_size, number_bidders,
                                    f"Executable size {executable_size} is not greater than or equal to number "
                                    f"of bidders {number_bidders} for price level {price_level['price']}")

    def test_unauthorized_response_retrieve_user_bids(self):
        """
        GET request test.
        Test if given an api request without an authentication key, then the
        response will be a 401 status code, which mean unauthorized.
        """
        # Act
        user_bids_body = Bids(self._api_request).get_retrieve_user_bids().json()
        # Assert
        self.assertEqual(user_bids_body['statusCode'], 401)

    def test_retrieve_authchallenge(self):
        """
        POST request test.
        Test the process of retrieving the authchallenge is correct, and the message contains "Sign in".
        """
        # Act
        authchallenge = Bids(self._api_request).retrieve_authchallenge()
        authchallenge_body = authchallenge.json()
        # Assert
        print(authchallenge_body)
        self.assertTrue(authchallenge.status_code, 201)
        self.assertIn("Sign in", authchallenge_body['message'])
