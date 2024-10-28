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

driver.get("https://the-internet.herokuapp.com/key_presses")
time.sleep(1)

KEYBOARD_INPUT_LOC = (By.XPATH, "//input[@id='target']")

input_el = driver.find_element(*KEYBOARD_INPUT_LOC)

# input_el.send_keys(Keys.ENTER)
input_el.send_keys("some text")
time.sleep(1)
input_el.send_keys(Keys.CONTROL + "a")
time.sleep(1)
input_el.send_keys(Keys.CONTROL + "v")

time.sleep(1)
