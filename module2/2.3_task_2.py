from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


url = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(url)
    button = browser.find_element(By.CSS_SELECTOR,  '.btn')
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    ans = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(ans)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()    

finally:
    time.sleep(10)
    browser.quit()