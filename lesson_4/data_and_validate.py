import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# url = driver.current_url
# print("URL of page is", url)
# assert url == "https://www.wikipedia.org/", "URL error. Wrong page requested."

# current_title = driver.title
# print("Current title of page is", current_title)
# assert current_title == "Wikipedia", "Title error. Wrong title of page."


print(driver.page_source)

time.sleep(0.5)
