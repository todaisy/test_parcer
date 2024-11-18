from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())  # объект класса Service с установкой драйвера
driver = webdriver.Chrome(service=service)  # создаем объект драйвера и передаем в него хром

# открытие страницы - урок 3
driver.get("https://school.kontur.ru/publications")
time.sleep(5)  # пауза / задержка

driver.back()  # возвращение назад
time.sleep(5)
driver.forward()  # вперед
time.sleep(5)
driver.refresh()  # перезагрузка
driver.close()  # закрыть


# урок 4
cur_url = driver.current_url
print(cur_url, "url")
assert cur_url == "https://school.kontur.ru/publications", "Ошибка в URL"

cur_title = driver.title
print(cur_title, "заголовок")
assert cur_title == "Wikipedia", "Неверный заголовок"

# driver.page_source - весь код сайта
# print(driver.page_source)
time.sleep(3)

# урок 5
from selenium.webdriver.common.by import By
driver.find_element(By.ID, "loginforsubmit")
# эквивалентно
driver.find_element("id", "loginforsubmit")

driver.find_element("id", "loginforsubmit").click()  # нажатие на элемент
