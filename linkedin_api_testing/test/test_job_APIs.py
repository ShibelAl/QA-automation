import unittest
from infra.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.job_APIs import JobAPIs


class TestCompany(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by loading the configuration and initializing the API wrapper.
        """
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()
        self.job = JobAPIs(self._api_request)

    def test_unique_job_ids(self):
        """
        Tests that all job IDs in the job search response are unique.

        - Asserts that the response status code is 200.
        - Asserts that all job IDs are unique by comparing the number of IDs with
          the number of unique IDs (using a set).
        """
        # Act
        response = self.job.search_jobs()
        response_body = response.json()
        job_ids_list = self.job.list_of_job_ids(response_body)
        print(response_body)
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(job_ids_list), len(set(job_ids_list)))
