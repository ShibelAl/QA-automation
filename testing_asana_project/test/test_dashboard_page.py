import time
import unittest
from logic.login_page import LoginPage
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.sidebar import SideBar
from logic.reporting_page import ReportingPage
from logic.dashboard_page import DashboardPage


class TestDashboardPage(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.secret = ConfigProvider.load_secret_json()
        self.driver = self.browser.get_driver(self.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.secret["password"])

    def tearDown(self):
        self.driver.quit()

    def test_drag_and_drop_feature(self):
        # Arrange
        self.sidebar = SideBar(self.driver)
        self.sidebar.click_on_reporting_button()
        time.sleep(2)

        self.reporting_page = ReportingPage(self.driver)
        self.reporting_page.go_to_dashboard_page()
        time.sleep(2)

        self.dashboard_page = DashboardPage(self.driver)
        self.dashboard_page.add_two_charts_flow()
        time.sleep(2)

        # Capture initial state
        initial_left_chart_location = self.dashboard_page.get_chart_location('left')
        initial_right_chart_location = self.dashboard_page.get_chart_location('right')

        # Act
        self.dashboard_page.drag_left_chart_to_right()
        time.sleep(2)  # Allow time for the action to complete and UI to update

        # Capture final state
        final_left_chart_location = self.dashboard_page.get_chart_location('right')
        final_right_chart_location = self.dashboard_page.get_chart_location('left')

        # Assert
        assert final_left_chart_location == initial_right_chart_location, ("The left chart was not dragged to the right"
                                                                           " chart's position.")
        assert final_right_chart_location == initial_left_chart_location, ("The right chart was not moved to the left "
                                                                           "chart's position.")

