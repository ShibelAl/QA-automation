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
    driver.implicitly_wait(10)
    # go to "ultimate qa"
    search_input = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.ID, "APjFqb")))
    search_input.send_keys("ultimate qa")
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)

    # Go to Automation Practice
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[contains(text(), 'Automation Practice')]").click()

    # Go to Big page with many elements
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Big page with many elements')]").click()

    # Count how many green buttons there
    button_count = len(driver.find_elements(By.XPATH, "//a[text()='Button']"))
    print(button_count)

    # click on each green button
    time.sleep(1)
    for i in range(1, button_count + 1):
        driver.find_element(By.XPATH, f"//a[@class='et_pb_button et_pb_button_{i - 1} et_pb_bg_layout_light']").click()
        time.sleep(1)

    # Enter twitter
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[contains(@class,'et_pb_social_media_follow_network_0')]//a[@class='icon "
                                  "et_pb_with_border' and @title='Follow on Twitter']").click()
    time.sleep(8)

    # If more that one back() is needed
    while driver.current_url != "https://ultimateqa.com/complicated-page":
        driver.back()

    # Enter the name
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='et_pb_contact_name_0']").send_keys("Shibel")

    # Enter the Email
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='et_pb_contact_email_0']").send_keys("Shibel@gmail.com")

    # Enter the Message
    time.sleep(1)
    driver.find_element(By.XPATH, "//textarea[@id='et_pb_contact_message_0']").send_keys("Hello Selenium!")

    # Enter the answer of the equation
    time.sleep(1)
    (driver.find_element(By.XPATH, "//input[@class='input et_pb_contact_captcha' and @name='et_pb_contact_captcha_0']")
     .send_keys("5"))

    # Press on the Submit button
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//button[@name='et_builder_submit_button']").click()

    time.sleep(8)
    driver.quit()

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # infra
    driver.quit()
