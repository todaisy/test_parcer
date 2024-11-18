import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# chrome_options.page_load_strategy = "eager"

prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}

chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--window-size=500, 500")  # первый вариант изменения окна

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

'''
driver.get("https://rutube.ru/video/4521aa88b24d5fbbcfe0668fc56e6113/")
time.sleep(10)
my_object = driver.find_element("xpath", '//video[@scr="blob:https://rutube.ru/2ccedd99-fb56-44b5-94ab-8c4d64aa5929"]')
my_object.click()
time.sleep(5)
'''

# upload
driver.get("https://convertio.co/ru/image-converter/")
time.sleep(3)
name = driver.find_element("xpath", "//input[@class='file-input']")  # работает!!!!
name.send_keys(f"{os.getcwd()}/downloads/picture.png")
time.sleep(3)

