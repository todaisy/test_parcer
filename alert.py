from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())  # объект класса Service с установкой драйвера
driver = webdriver.Chrome(service=service)  # создаем объект драйвера и передаем в него хром
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

button_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(button_1)).click()

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
text_alert = alert.text
print(text_alert)
alert.accept()  # принять
# alert.dismiss()  # отклонить
# alert.send_keys('Hello')  # ввод текста
