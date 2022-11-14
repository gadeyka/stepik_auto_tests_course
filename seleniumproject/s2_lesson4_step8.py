from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.wait import WebDriverWait

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(15)
    browser.quit()
