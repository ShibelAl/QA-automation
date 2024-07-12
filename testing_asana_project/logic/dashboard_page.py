import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class DashboardPage(BasePage):
    INCOMPLETE_TASKS_GREEN_CHART = '//h5[contains(text(), "Incomplete tasks")]'
    CREATE_BUTTON_IN_ADD_CHART_POPUP = '//div[text() = "Create"]'
    PROJECTS_BY_STATUS = '(//div[@class = "CardGalleryCategory-card"][3])'
    ADD_CHART_BUTTON = '//div[contains(@class, "PageToolbarStructure")]//div[@role = "button"]'
    LEFT_CHART_HEADER_TITLE_WRAPPER = '(//div[@class = "BaseChartHeader-titleWrapper"])[1]'
    RIGHT_CHART_HEADER_TITLE_WRAPPER = '(//div[@class = "BaseChartHeader-titleWrapper"])[2]'

    def __init__(self, driver):
        super().__init__(driver)
        self._left_chart_header = None
        self._right_chart_header = None

    def click_on_incomplete_tasks_green_chart(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.INCOMPLETE_TASKS_GREEN_CHART))
        ).click()

    def click_on_create_button_in_add_chart_popup(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON_IN_ADD_CHART_POPUP))
        ).click()

    def click_on_add_chart_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_CHART_BUTTON))
        ).click()

    def click_on_projects_by_status(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROJECTS_BY_STATUS))
        ).click()

    def add_two_charts_flow(self):
        self.click_on_incomplete_tasks_green_chart()
        time.sleep(2)
        self.click_on_create_button_in_add_chart_popup()
        time.sleep(2)
        self.click_on_add_chart_button()
        time.sleep(2)
        self.click_on_projects_by_status()
        time.sleep(2)
        self.click_on_create_button_in_add_chart_popup()

    def drag_left_chart_to_right(self):
        self._left_chart_header = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LEFT_CHART_HEADER_TITLE_WRAPPER))
        )
        self._right_chart_header = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.RIGHT_CHART_HEADER_TITLE_WRAPPER))
        )
        ac = ActionChains(self._driver)
        ac.drag_and_drop(self._left_chart_header, self._right_chart_header).perform()
        time.sleep(5)

    def get_chart_location(self, chart_position):
        if chart_position == 'left':
            chart_element = self._driver.find_element(By.XPATH, self.LEFT_CHART_HEADER_TITLE_WRAPPER)
        elif chart_position == 'right':
            chart_element = self._driver.find_element(By.XPATH, self.RIGHT_CHART_HEADER_TITLE_WRAPPER)
        else:
            raise ValueError("Invalid chart position specified. Use 'left' or 'right'.")

        return chart_element.location