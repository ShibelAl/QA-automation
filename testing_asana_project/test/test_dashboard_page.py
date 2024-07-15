import logging
import unittest
from logic.login_page import LoginPage
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.sidebar import SideBar
from logic.reporting_page import ReportingPage
from logic.dashboard_page import DashboardPage
from logic.chart_location_options import ChartLocationOptions
from infra.logging_setup import LoggingSetup  # it appears not used, without it logging fails


class TestDashboardPage(unittest.TestCase):

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
        self.sidebar = SideBar(self.driver)
        self.sidebar.click_on_reporting_button()
        self.reporting_page = ReportingPage(self.driver)
        self.reporting_page.go_to_dashboard_page()

    def tearDown(self):
        """
        Closes the browser after completing the test.
        Works automatically.
        """
        self.driver.quit()

    def test_drag_and_drop_feature(self):
        """
        This function tests the drag and drop feature in the dashboard
        page, it uses the "get_chart_location" function that returns the
        location of the element (chart) in the page.
        """
        logging.info("Test drag and drop feature - test started")
        # Arrange
        self.dashboard_page = DashboardPage(self.driver)
        self.dashboard_page.add_two_charts_flow()

        # Capture initial state
        initial_left_chart_location = self.dashboard_page.get_chart_location(ChartLocationOptions.LEFT.value)
        initial_right_chart_location = self.dashboard_page.get_chart_location(ChartLocationOptions.RIGHT.value)

        # Act
        self.dashboard_page.drag_left_chart_to_right()

        # Capture final state
        final_left_chart_location = self.dashboard_page.get_chart_location(ChartLocationOptions.LEFT.value)
        final_right_chart_location = self.dashboard_page.get_chart_location(ChartLocationOptions.RIGHT.value)

        # Assert
        self.assertDictEqual(final_left_chart_location, initial_right_chart_location)
        self.assertDictEqual(final_right_chart_location, initial_left_chart_location)
