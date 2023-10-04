from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/registration1.html"

try:
    browser.get(url)
    
    fname = browser.find_element(By.CSS_SELECTOR, '.first')
    fname.send_keys('Ivan')
    lname = browser.find_element(By.CSS_SELECTOR, '.second')
    lname.send_keys('Petrov')
    email = browser.find_element(By.CSS_SELECTOR, '.third')
    email.send_keys('test@mail.ru')
    # country =  browser.find_element(By.ID, 'country')
    # country.send_keys('Russia')
    
    button =  browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    assert welcome_text_elt.text == "Congratulations! You have successfully registered!"
    
    
finally:
    time.sleep(10)
    browser.quit()
    