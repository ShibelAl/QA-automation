import unittest
from infra.api_wrapper import APIWrapper
from logic.company import Company
from infra.config_provider import ConfigProvider
from logic.models.company_jobs import CompanyJobs


class TestCompany(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by loading the configuration and initializing the API wrapper.
        """
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()

    def test_company_jobs(self):
        """
        Test if the data structure of the whole response and the data-key value is Dictionary,
        and if the items-key value is a list. If this test failed then the other tests will fail
        because they depend on these data structures, so it's a fundamental test.

        This test will:
        - Create a CompanyJobs object with a list of company IDs and a page number.
        - Use the Company class to send a POST request with the company jobs parameters.
        - Validate the structure of the response to ensure it contains the expected data.
        """
        # Arrange
        payload = self._config['get_company_jobs_payload']
        company_ids = payload['companyIds']
        page = payload['page']
        company_object = CompanyJobs(company_ids, page)

        # Act
        response = Company(self._api_request).get_company_job_by_body(company_object.to_dict())
        company_jobs_body = response.json()

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(company_jobs_body, dict)
        self.assertIsInstance(company_jobs_body['data'], dict)
        self.assertIsInstance(company_jobs_body['data']['items'], list)


if __name__ == '__main__':
    unittest.main()
