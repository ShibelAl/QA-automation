import unittest
from infra.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.profile_APIs import ProfileAPIs


class TestProfileAPIs(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by loading the configuration and initializing the API wrapper,
        and then making a JobAPIs object, its API response and its json body.
        """
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()
        self.profile = ProfileAPIs(self._api_request)
        self.response = self.profile.get_profile_data_by_url()

    def test_if_user_data_is_correct(self):
        """
        Test if the user data is correct.

        - Asserts that the response status code is 200.
        - Asserts that the user data is equal to the expected data
        """
        # Act
        response_body = self.response.json()
        # Assert
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(response_body['username'], self._config['username'])
        self.assertEqual(response_body['firstName'], self._config['firstName'])
        self.assertEqual(response_body['lastName'], self._config['lastName'])
        self.assertEqual(response_body['isCreator'], self._config['isCreator'])
        self.assertEqual(response_body['isOpenToWork'], self._config['isOpenToWork'])
        self.assertEqual(response_body['isHiring'], self._config['isHiring'])
        self.assertEqual(response_body['profilePicture'], self._config['profilePicture'])
        self.assertEqual(response_body['backgroundImage'], self._config['backgroundImage'])
        self.assertEqual(response_body['summary'], self._config['summary'])
        self.assertEqual(response_body['headline'], self._config['headline'])

    def test_specific_fields_in_the_API_response(self):
        """
        Tests specific fields in the JSON response:
        username, fieldOfStudy and degree.

        Uses the function "get_profile_data_and_connections_follower_count" in logic-profile_APIs.
        """
        # Act
        response_body = self.response.json()
        # Assert
        self.assertEqual(response_body['username'], self._config['username'])
        self.assertEqual(response_body['educations'][0]['fieldOfStudy'], self._config['fieldOfStudy'])
        self.assertEqual(response_body['educations'][0]['degree'], self._config['degree'])