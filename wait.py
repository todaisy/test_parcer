# явные и неявные ожидания
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.implicitly_wait(10)  # неявное ожидания, ждет каждый элемент 10 секунд

driver.get("https://convertio.co/ru/image-converter/")
button = ("xpath", "//a[text()='Вход']")
email = ("xpath", "//input[@type='email']")
# driver.find_element(*button).click()
# time.sleep(3)


# явные ожидания
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10, poll_frequency=1)

# wait_button = wait.until(EC.visibility_of_element_located(button))  # жди пока...
wait.until(EC.element_to_be_clickable(button)).click()
wait.until(EC.element_to_be_clickable(email)).send_keys('Hello')
wait.until(EC.text_to_be_present_in_element_value(email, 'Hello'))
print('Done')

