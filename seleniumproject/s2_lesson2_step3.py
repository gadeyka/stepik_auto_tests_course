from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(a1, b2):
        return str(int(a) + int(b))


    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text

    b_element = browser.find_element(By.ID, "num2")
    b = b_element.text

    y = calc(a, b)

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
