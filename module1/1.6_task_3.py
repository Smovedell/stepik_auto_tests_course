from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/huge_form.html'

try:
    browser.get(url)
    time.sleep(5)
    spaces = browser.find_elements(By.CSS_SELECTOR, 'input')
    # print(len(spaces))
    for el in spaces:
        el.send_keys('123')
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(10)
    browser.close()
