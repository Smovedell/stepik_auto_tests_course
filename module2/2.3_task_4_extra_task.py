from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
import time

stepik_url = 'https://stepik.org/lesson/236205/step/2?unit=208637'
browser = webdriver.Chrome()

def auth(driver):
    enter_button = driver.find_element(By.CSS_SELECTOR, '[href="/course/575/promo?auth=login"]')
    enter_button.click()
    time.sleep(1)

    email = driver.find_element(By.ID, 'id_login_email')
    email.send_keys('lcme.nechaev@mail.ru')
    # time.sleep(5)
    password = driver.find_element(By.ID, 'id_login_password')
    password.send_keys('24861379a')
    # time.sleep(5)
    enter_button = driver.find_element(By.CSS_SELECTOR, '.sign-form__btn')
    enter_button.click()

try:
    browser.get(stepik_url)
    browser.implicitly_wait(30)
    auth(browser)
    browser.find_element(By.CSS_SELECTOR, '[href="/lesson/236205/step/1?unit=208637"]').click()
    browser.find_elements(By.CSS_SELECTOR, '.step-pin-icon')[1].click()
    
    # button = browser.find_element(By.CSS_SELECTOR, '.again-btn')
    # button.click()
    labels = browser.find_elements(By.CSS_SELECTOR, '.s-checkbox')
    # print(len(labels), labels)
    for label in labels:
        if 'явными' in label.text or 'списками' in label.text or 'html' in label.text or 'браузера' in label.text:
            print(label.text)
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.s-checkbox')))
            label.click()
    # labels = browser.find_element(By.CSS_SELECTOR, '.s-checkbox')
    # print(labels.text)
    # labels.click()
    button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()