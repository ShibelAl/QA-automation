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
    search_input.send_keys("ultimate qa")
    search_input.send_keys(Keys.RETURN)

    automation_practice_link = (WebDriverWait(driver, 2).until(
        ec.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Automation Practice')]"))))
    automation_practice_link.click()

    first_item_in_list = (WebDriverWait(driver, 2).until(
        ec.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Big page with many elements')]"))))
    first_item_in_list.click()
    time.sleep(2)
    button_count = len(driver.find_elements(By.XPATH, "//a[text()='Button']"))
    print(button_count)

    for i in range(1, button_count+1):
        driver.find_element(By.XPATH, f"//a[@class='et_pb_button et_pb_button_{i-1} et_pb_bg_layout_light']").click()
        time.sleep(1)

    twitter_button = driver.find_element(By.XPATH, "//li[contains(@class,'et_pb_social_media_follow_network_0')]//a[@class='icon et_pb_with_border' and @title='Follow on Twitter']")
    time.sleep(0.5)
    twitter_button.click()

    time.sleep(10)
    driver.quit()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # infra
    driver.quit()
