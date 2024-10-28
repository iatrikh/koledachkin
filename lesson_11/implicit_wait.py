import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(10)

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()
