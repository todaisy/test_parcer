import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager"

chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-cache")
# chrome_options.add_argument("--window-size=700,700")  # первый вариант изменения окна

service = Service(executable_path=ChromeDriverManager().install())  # объект класса Service с установкой драйвера
driver = webdriver.Chrome(service=service, options=chrome_options)  # создаем объект драйвера и передаем в него хром
# driver.set_window_size(700, 700)  # второй вариант изменения окна
# driver.maximize_window()  # раскрытие окна на весь экран

start_time = time.time()
driver.get("https://www.freeconference.com")

sign_up = driver.find_element("xpath", '//a[@id="link_text-242-925837"]')
sign_up.click()

# email = driver.find_element("xpath", '//input[@type="email"]')
# email.send_keys("darkey")

end_time = time.time()
print(end_time - start_time)

'''
－Опции из видео:
➖ Безголовый режим "--headless"
➖ Режим инкогнито "--incognito"
➖ Игнорирование ошибок сертификатов "--ignore-certificate-errors"
➖ Размер окна браузера "--window-size=X,Y"
➖ Отключение кеширования "--disable-cache"

－Методы из видео:
➖ Добавление новой опции - add_argument("--имя_опции")
➖ Установка размера окна - driver.set_window_size(1920, 1080)
➖ Развернуть окно браузера на весь экран - driver.maximize_window()

•	Хардкдинг стратегии загрузки:
➖ chrome_options.page_load_strategy = "normal" - дожидается загрузки всех ресурсов
➖ chrome_options.page_load_strategy = "eager" - дожидается загрузки DOM
'''
