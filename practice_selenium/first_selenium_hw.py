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
    # APjFqb is the id of the search bar
    search_input = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.ID, "APjFqb")))
# search_input = driver.find_element(By.ID, "APjFqb")
    search_input.send_keys("Python programming")
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)
    first_result = driver.find_element(By.TAG_NAME, "h3")  # maybe it picks the first element that has h3 tag
# first_result = driver.find_element(By.XPATH, "")

    print(first_result.text)
    driver.quit()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # infra
    driver.quit()
