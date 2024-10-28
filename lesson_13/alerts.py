import time

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

driver.get("https://demoqa.com/alerts")

SIMPLE_ALERT_BTN = (By.XPATH, "//button[@id='alertButton']")
CANCEL_ALERT_BTN = (By.XPATH, "//button[@id='confirmButton']")
PROMPT_ALERT_BTN = (By.XPATH, "//button[@id='promtButton']")

time.sleep(2)

wait.until(EC.element_to_be_clickable(PROMPT_ALERT_BTN)).click()

alert = wait.until(EC.alert_is_present())

time.sleep(2)

driver.switch_to.alert
# print(alert.text)

# alert.accept()
# alert.dismiss()
alert.send_keys("Hello")
time.sleep(3)
alert.accept()

time.sleep(2)
