import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

browser = webdriver.Chrome()
url_reg1 = "http://suninjuly.github.io/registration1.html"
url_reg2 = "http://suninjuly.github.io/registration2.html"

def try_to_reg(url):
    browser.get(url)        
    fname = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    fname.send_keys('Ivan')
    lname = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    lname.send_keys('Petrov')
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email.send_keys('test@mail.ru')
    # country =  browser.find_element(By.ID, 'country')
    # country.send_keys('Russia')

    button =  browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    return welcome_text_elt.text
    # assert welcome_text_elt.text == "Congratulations! You have successfully registered!"


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(try_to_reg(url_reg1), "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(try_to_reg(url_reg2), "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()