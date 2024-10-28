import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/")

nav_links = driver.find_elements("class name", "nav-link")

time.sleep(1.5)

nav_links[1].click()

time.sleep(1.5)
