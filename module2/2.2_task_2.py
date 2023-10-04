from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"


try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    rez = calc(int(x))
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(rez)
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(5)
    browser.quit()