from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    spaces = browser.find_elements(By.CSS_SELECTOR, '.form-group input')
    spaces[0].send_keys('Test_name')
    spaces[1].send_keys('Test_surname')
    spaces[2].send_keys('Test_email@mail.ru')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'test_file.txt') 
    file = browser.find_element(By.CSS_SELECTOR, '#file')
    file.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
