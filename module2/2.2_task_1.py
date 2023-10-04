from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


url = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    rez = int(num1) + int(num2)
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_visible_text(str(rez))
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()