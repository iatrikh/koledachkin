import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://dzen.ru/")

time.sleep(8)

driver.back()

time.sleep(2)

driver.forward()

time.sleep(2)

driver.refresh()()

time.sleep(1)
