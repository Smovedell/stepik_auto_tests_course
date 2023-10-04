import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12?unit=196192")
time.sleep(15)

enter_button = driver.find_element(By.ID, 'ember128')
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
time.sleep(20)
# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".ember-text-area")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(15)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()