import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/ru/login")

submit_butt = driver.find_element("id", "loginformsubmit")

submit_butt.click()

time.sleep(2)
