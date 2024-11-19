import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
options.add_argument("--window-size=700,700")  # первый вариант изменения окна
options.add_argument("--disable-blink-features=AutomationControlled")  # выключение автоматического контроля
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")  # подмена пользователя

service = Service(executable_path=ChromeDriverManager().install())  # объект класса Service с установкой драйвера
driver = webdriver.Chrome(service=service, options=options)  # создаем объект драйвера и передаем в него хром
wait = WebDriverWait(driver, 5, poll_frequency=1)

# driver.get("https://convertio.co/ru/image-converter/")
# driver.save_screenshot(f'{os.getcwd()}/screenshot/pict.png')
driver.get("https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html")
time.sleep(3)
