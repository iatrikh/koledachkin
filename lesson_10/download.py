import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()

prefs = {"download.default_directory": f"{os.getcwd()}\\lesson_10\\downloads"}
chrome_options.add_experimental_option("prefs", prefs)

chrome_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(1)
driver.find_elements("xpath", "//a")[1].click()
time.sleep(7)