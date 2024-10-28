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

# driver.get("https://the-internet.herokuapp.com/checkboxes")

# CHECKBOX_1 = (By.XPATH, "(//input[@type='checkbox'])[1]")

# first_check = driver.find_element(*CHECKBOX_1)
# print(first_check.get_attribute("checked"))
# print(first_check.is_selected())
# first_check.click()
# print(first_check.get_attribute("checked"))
# print(first_check.is_selected())

# driver.get("https://demoqa.com/checkbox")
# CHECKBOX_HOME_STATUS = (By.XPATH, "//input[@id='tree-node-home']")
# CHECKBOX_HOME_SPAN = (By.XPATH, "//span[@class='rct-checkbox']")
# home_chckbx_el = driver.find_element(*CHECKBOX_HOME_STATUS)
# home_chckbx_span = driver.find_element(*CHECKBOX_HOME_SPAN)
# print(home_chckbx_el.is_selected())
# home_chckbx_span.click()
# print(home_chckbx_el.is_selected())

# driver.get("https://demoqa.com/selectable")
# ELEMENT_ONE_LOC = (By.XPATH, "//li[text()='Cras justo odio']")
# elem_one = driver.find_element(*ELEMENT_ONE_LOC)
# is_active = "active" in elem_one.get_attribute("class")
# print(is_active)
# elem_one.click()
# is_active = "active" in elem_one.get_attribute("class")
# print(is_active)

driver.get("https://demoqa.com/radio-button")
time.sleep(1)

YES_RADIO_LOC = (By.XPATH, "//input[@id='yesRadio']")
YES_LABEL_LOC = (By.XPATH, "//label[@for='yesRadio']")

IMPRESS_RADIO_LOC = (By.XPATH, "//input[@id='impressiveRadio']")
IMPRESS_LABEL_LOC = (By.XPATH, "//label[@for='impressiveRadio']")

NO_RADIO_LOC = (By.XPATH, "//input[@id='noRadio']")
NO_LABEL_LOC = (By.XPATH, "//label[@for='noRadio']")

yes_radio_el = driver.find_element(*YES_RADIO_LOC)
yes_label_el = driver.find_element(*YES_LABEL_LOC)

impress_radio_el = driver.find_element(*IMPRESS_RADIO_LOC)
impress_label_el = driver.find_element(*IMPRESS_LABEL_LOC)

no_radio_el = driver.find_element(*NO_RADIO_LOC)
no_label_el = driver.find_element(*NO_LABEL_LOC)


for x in range(8):
    yes_label_el.click()
    time.sleep(0.2)
    impress_label_el.click()
    time.sleep(0.2)

print(no_radio_el.is_enabled())

time.sleep(1)
