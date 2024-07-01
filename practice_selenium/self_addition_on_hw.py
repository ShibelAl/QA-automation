import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# infra
driver = webdriver.Chrome()

# logic
driver.get("https://www.google.com/")

try:
    # search_input = WebDriverWait(driver, 2).until(ec.presence_of_element _located((By.ID, "APjFqb")))  # search bar id
    # search_input = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
    search_input = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH,
                                                                                  "//textarea[@class='gLFyf']")))
    search_input.send_keys("Python programming")
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)  # wait for 2 seconds.
    first_result = driver.find_element(By.TAG_NAME, "h3")  # maybe it picks the first element that has h3 tag

    print(first_result.text)

    link = driver.find_element(By.LINK_TEXT, "Python For Beginners")
    link.click()
    driver.implicitly_wait(2)  # only waits as long as necessary. If the element appears before the timeout, the
    # execution proceeds immediately, that makes it more efficient than a fixed wait time.
    driver.back()
    search_input = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.ID, "APjFqb")))
    search_input.send_keys(" it appends the text!!")  # to show that we should clear the input field
    time.sleep(2)

    search_input.clear()  # so we should put clear after every input insertion
    time.sleep(2)

    driver.forward()
    time.sleep(2)

    driver.quit()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # infra
    driver.quit()
