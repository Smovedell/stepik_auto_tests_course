from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


url = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


print(calc(970))
try:
    browser.get(url)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    print(x)
    ans = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(ans)
    time.sleep(3)
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()
    time.sleep(1)
    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    alert = browser.switch_to.alert
    print(alert.text)
finally:
    time.sleep(15)
    browser.quit()
    
#28.90365769590374
#28.903657713001966
#28.903657739533696
#28.903657761938266
# 2.1039326902403084