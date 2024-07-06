from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class DynamicContentPage(BasePage):

    DYNAMIC_PARAGRAPH = '(//div[@class="large-10 columns"])[3]'
    DYNAMIC_IMAGE = '(//div[@class="large-2 columns"])[3]//img'
    CLICK_HERE_BUTTON = '//a[text() = "click here"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._click_here_button = self._driver.find_element(By.XPATH, self.CLICK_HERE_BUTTON)

    def get_dynamic_content_text(self):
        content = WebDriverWait(self._driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.DYNAMIC_PARAGRAPH)))
        return content.text

    def click_on_here_button(self):
        self._click_here_button.click()

    def get_image_src(self):
        element = WebDriverWait(self._driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.DYNAMIC_IMAGE)))
        return element.get_attribute("src")