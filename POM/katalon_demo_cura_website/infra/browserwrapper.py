from selenium import webdriver
class BrowserWrapper:

    def getDriver(self, driver):
        temp_driver = webdriver.Chrome()
        temp_driver.get(driver)
        return temp_driver
