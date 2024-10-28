import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 15, poll_frequency=0.2)

driver.get("https://www.freeconferencecall.com/global/ru/login")
driver.delete_all_cookies()

cookies_from_file = pickle.load(open(os.getcwd() + "\\cookies\\cookies.pkl", "rb"))

for cookie in cookies_from_file:
    driver.add_cookie(cookie)

time.sleep(2)

driver.refresh()

time.sleep(5)
