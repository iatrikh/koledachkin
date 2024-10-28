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

# cookie = driver.get_cookie("country_code")
# all_cookies = driver.get_cookies()
# driver.add_cookie({"name": "example", "value": "kukushka"})
# driver.delete_cookie("split")
# driver.add_cookie({"name": "split", "value": "qwerty"})
# # driver.delete_all_cookies()

EMAIL_FIELD = (By.XPATH, "//input[@id='login_email']")
PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
SUBMIT_BTN = (By.XPATH, "//button[@id='loginformsubmit']")

driver.get("https://www.freeconferencecall.com/global/ru/login")

time.sleep(1.5)

driver.find_element(*EMAIL_FIELD).send_keys("thesunlight17@gmail.com")
driver.find_element(*PASSWORD_FIELD).send_keys("shamoi96")

time.sleep(1)

driver.find_element(*SUBMIT_BTN).click()

time.sleep(2)

pickle.dump(driver.get_cookies(), open(os.getcwd() + "\\cookies\\cookies.pkl", "wb"))
