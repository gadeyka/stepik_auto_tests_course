from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_field.send_keys(y)

    check_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    check_box.click()

    check_radio = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_radio)
    check_radio.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(15)
    browser.quit()
