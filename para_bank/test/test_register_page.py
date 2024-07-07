import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.register_page import RegisterPage
from infra.infra_utils import InfraUtils
from logic.successful_register_page import SuccessfulRegisterPage
from logic.logic_utils import LogicUtils, generate_random_value


class TestRegisterPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["base_url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_login_successful(self):
        # Arrange
        self.home_page.click_register_button()
        time.sleep(2)
        infra_utils = InfraUtils()

        register_page = RegisterPage(self.driver)

        # Act
        register_page.fill_first_name_field(generate_random_value(LogicUtils.FIRST_NAME))
        register_page.fill_last_name_field(generate_random_value(LogicUtils.LAST_NAME))
        register_page.fill_address_field(generate_random_value(LogicUtils.ADDRESS))
        register_page.fill_city_field(generate_random_value(LogicUtils.CITY))
        register_page.fill_state_field(generate_random_value(LogicUtils.STATE))
        register_page.fill_zip_code_field(generate_random_value(LogicUtils.ZIP_CODE))
        register_page.fill_phone_field(infra_utils.generate_random_string(10))
        register_page.fill_ssn_field(generate_random_value(LogicUtils.SSN))
        register_page.fill_username_field((infra_utils.generate_random_string(8)))

        generated_password = InfraUtils.generate_random_string(10)
        register_page.fill_password_input(generated_password)
        register_page.fill_confirm_field(generated_password)
        time.sleep(1)

        register_page.click_on_register_button()
        time.sleep(8)

        # Assert
        success = SuccessfulRegisterPage(self.driver)
        self.assertTrue(success.success_text_displayed())