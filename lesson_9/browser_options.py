import time
from unittest import result

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-cache")

# лучше именно тут указывать размер окна
chrome_options.add_argument("--window-size=1280,720")

# chrome_options.page_load_strategy = "normal"
chrome_options.page_load_strategy = "eager"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(chrome_options, service)

# time.sleep(0.5)
# driver.maximize_window()
# driver.set_window_size(600, 600)

start_time = time.time()

driver.get("https://whatismyipaddress.com/")
# driver.get("https://expired.badssl.com/")

end_time = time.time()
result = end_time - start_time

print(result)
