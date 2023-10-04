from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/find_link_text'

try:
    browser.get(url)
    link = browser.find_element(By.PARTIAL_LINK_TEXT, link_text)
    link.click()
    fname = browser.find_element(By.NAME, 'first_name')
    fname.send_keys('Ivan')
    lname = browser.find_element(By.NAME, 'last_name')
    lname.send_keys('Petrov')
    city = browser.find_element(By.NAME, 'firstname')
    city.send_keys('Smolensk')
    country =  browser.find_element(By.ID, 'country')
    country.send_keys('Russia')
    
    button =  browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
