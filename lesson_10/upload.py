import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(1)

file_input = driver.find_element("xpath", "//input[@type='file']")
file_input.send_keys(f"{os.getcwd()}\\lesson_10\\downloads\\upload-me.txt")

time.sleep(2)

file_submit = driver.find_element("xpath", "//input[@id='file-submit']")
file_submit.click()


time.sleep(2)
