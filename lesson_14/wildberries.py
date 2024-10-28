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

driver.get("https://www.wildberries.ru/catalog/154757715/detail.aspx")

time.sleep(4)

ORDER_BTN = (By.XPATH, "//button[@class='order__button btn-main']")

driver.find_element(*ORDER_BTN).click()

# driver.refresh()

time.sleep(3)

# pickle.dump(driver.get_cookies(), open(os.getcwd() + "\\cookies\\cookies.pkl", "wb"))

driver.delete_all_cookies()

driver.refresh()

time.sleep(10)

cookies_from_file = pickle.load(open(os.getcwd() + "\\cookies\\cookies.pkl", "rb"))

for cookie in cookies_from_file:
    driver.add_cookie(cookie)

time.sleep(0.5)

driver.refresh()

time.sleep(4)
