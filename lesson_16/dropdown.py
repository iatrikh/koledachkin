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

SELECT_LOC = (By.XPATH, "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(1)

dropdown_el = Select(driver.find_element(*SELECT_LOC))

# dropdown_el.select_by_visible_text("Option 1")
# dropdown_el.select_by_value("2")
# dropdown_el.select_by_index(1)

all_options = dropdown_el.options

for option in all_options:
    # dropdown_el.select_by_visible_text(option.text)
    # dropdown_el.select_by_index(all_options.index(option))
    dropdown_el.select_by_value(option.get_attribute("value"))
    time.sleep(1)
