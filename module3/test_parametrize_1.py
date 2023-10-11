import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By



def change_url(url):
    return f"/{'/'.join(url.split('/')[3:])}?auth=login"

def auth(browser, url):
    browser.find_element(By.CSS_SELECTOR, f'[href="{change_url(url)}').click()
    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('lcme.nechaev@mail.ru')
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('24861379a')
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn ').click()
    

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
    

urls = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']

# urls = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1']
rez = ''
@pytest.mark.parametrize('choose_urls', urls)
def test_parametrize(browser, choose_urls):
    browser.get(choose_urls)
    auth(browser, choose_urls)
    input = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
    input.send_keys(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    time.sleep(5)
    ans = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    time.sleep(5)
    try:
        assert ans == 'Correct!'
    except:
        rez += ans
        
print(rez)