from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")


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
    check_radio.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()



finally:
    time.sleep(15)
    browser.quit()
