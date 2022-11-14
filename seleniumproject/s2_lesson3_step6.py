from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()

finally:
    time.sleep(15)
    browser.quit()
