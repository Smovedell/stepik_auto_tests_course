from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
import time


url = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(url)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100'))
    button = browser.find_element(By.CSS_SELECTOR, '#book')
    button.click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    ans = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(ans)
    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()
finally:
    time.sleep(10)
    browser.quit()