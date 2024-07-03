from katalon_demo_cura_website.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class BasePageApp(BasePage):
    MENU_BUTTON = "//i[@class='fa fa-bars']"
    HOME_IN_MENU = "//li//a[text()='Home']"
    LOGIN_IN_MENU = "//li//a[text()='Login']"

    def __init__(self, driver):
        super().__init__(driver)
        # self._driver.get("https://katalon-demo-cura.herokuapp.com/#")
        self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
        self._home_in_menu = self._driver.find_element(By.XPATH, self.HOME_IN_MENU)
        self._login_in_menu = self._driver.find_element(By.XPATH, self.LOGIN_IN_MENU)

    def click_on_menu_button(self):
        self._menu_button.click()

    def click_on_home_in_the_menu(self):
        self._home_in_menu.click()

    def click_on_login_in_the_menu(self):
        self._login_in_menu.click()

