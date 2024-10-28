import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 15, poll_frequency=0.2)

SELECT_ONE_INPUT_LOC = (By.XPATH, "//input[@id='react-select-3-input']")
SELECT_ONE_LOC = (By.XPATH, "//div[@id='selectOne']")
SELECT_DR_LOC = (By.XPATH, "//div[@id='react-select-3-option-0-0']")

driver.get("https://demoqa.com/select-menu")
time.sleep(1)


# select_on_el = driver.find_element(*SELECT_ONE_INPUT_LOC)
# select_on_el.send_keys("Ms." + Keys.ENTER)
# driver.refresh()
# driver.find_element(*SELECT_ONE_LOC).click()
# driver.find_element(*SELECT_DR_LOC).click()

MULTISELECT_LOC = (By.XPATH, "//input[@id='react-select-4-input']")

multiselect_el = driver.find_element(*MULTISELECT_LOC)

multiselect_el.send_keys("Green" + Keys.ENTER)
time.sleep(1)
multiselect_el.send_keys("Bla" + Keys.TAB)
time.sleep(2)
