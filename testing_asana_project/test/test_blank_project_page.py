import unittest
from logic.login_page import LoginPage
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.base_page_app import BasePageApp
from logic.new_project_page import NewProjectPage
from logic.blank_project_page import BlankProjectPage


class TestNewProjectPage(unittest.TestCase):

    def setUp(self):
        """
        Sets up the testing environment, completes the login process to enter to the main page,
        and creates a new blank project. Works automatically.
        """
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.secret = ConfigProvider.load_secret_json()
        self.driver = self.browser.get_driver(self.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.secret["password"])
        self.base_page_app = BasePageApp(self.driver)
        self.base_page_app.open_new_project()
        self.new_project_page = NewProjectPage(self.driver)
        self.new_project_page.click_on_blank_project_button()

    def tearDown(self):
        """
        Closes the browser after completing the test.
        Works automatically.
        """
        self.driver.quit()

    def test_header_project_name_appears(self):
        """
        This function tests if the project name appears in the project template.
        """
        # Arrange
        blank_project_page = BlankProjectPage(self.driver)
        # Act
        blank_project_page.fill_project_name_field()
        # Assert
        self.assertTrue(blank_project_page.project_name_is_displayed())
