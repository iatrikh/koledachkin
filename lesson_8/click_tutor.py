import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/ru/login")

# time.sleep(0.5)

# homepage_btn = driver.find_element("xpath", "//a[@title='FreeConferenceCall.com']")

# homepage_btn.click()

# time.sleep(1)

# driver.back()

time.sleep(0.5)


email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("shamoi96@yandex.ru")
print(email_field.get_attribute("value"))
print(email_field.get_attribute("maxlength"))

time.sleep(1)

email_field.clear()
time.sleep(0.5)
email_field.send_keys("thesunlight17@gmail.com")
print(email_field.get_attribute("value"))

time.sleep(1)
