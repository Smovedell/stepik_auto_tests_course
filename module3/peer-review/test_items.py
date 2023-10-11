import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button(browser):
    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')




'''Код чтобы спарсить возможные варианты языков (писал для себя)'''
# rez = []
# try:
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(10)
#     link = 'http://selenium1py.pythonanywhere.com/ar/catalogue/coders-at-work_207/'
#     browser.get(link)
#     select = Select(browser.find_element(By.CSS_SELECTOR, '.form-control'))
#     select_len = len(select.options)
#     for i in range(select_len):
#         WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-default[type="submit"]')))
#         select = Select(browser.find_element(By.CSS_SELECTOR, '.form-control'))
#         select.select_by_index(i)
#         browser.find_element(By.CSS_SELECTOR, '.btn-default[type="submit"]').click()
#         # time.sleep(5)
#         cur = browser.current_url
#         rez.append(cur.split('/')[3])

# finally:
#     browser.quit()
# print(rez)
