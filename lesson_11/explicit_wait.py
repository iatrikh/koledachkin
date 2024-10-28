import time
from tkinter import DISABLED

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(10)

wait = WebDriverWait(driver, 15, poll_frequency=0.25)

# driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")
ENABLE_AFTER_BUTTON = (By.XPATH, "//button[@id='enableAfter']")

# wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()
# wait.until(EC.element_to_be_clickable(ENABLE_AFTER_BUTTON)).click()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BTN = (By.XPATH, "//button[text()='Remove']")

# driver.find_element(*REMOVE_BTN).click()
# wait.until(EC.invisibility_of_element_located(REMOVE_BTN))

ENABLE_BTN = (By.XPATH, "//button[text()='Enable']")
DISABLED_INPUT = (By.XPATH, "//form[@id='input-example']//input")

driver.find_element(*ENABLE_BTN).click()
wait.until(EC.element_to_be_clickable(DISABLED_INPUT)).send_keys("some text")
wait.until(EC.text_to_be_present_in_element_value(DISABLED_INPUT, "some text"))

time.sleep(2)
