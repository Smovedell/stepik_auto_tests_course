from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser.get(url)
    
    fname = browser.find_element(By.NAME, 'first_name')
    fname.send_keys('Ivan')
    lname = browser.find_element(By.NAME, 'last_name')
    lname.send_keys('Petrov')
    city = browser.find_element(By.NAME, 'firstname')
    city.send_keys('Smolensk')
    country =  browser.find_element(By.ID, 'country')
    country.send_keys('Russia')
    
    button =  browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    
finally:
    time.sleep(10)
    browser.quit()
    
