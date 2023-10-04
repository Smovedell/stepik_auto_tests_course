from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


url = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(url)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    print(x)
    ans = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(ans)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()