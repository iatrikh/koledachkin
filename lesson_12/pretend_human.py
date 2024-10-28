import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=SomeUserAgent")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# driver.implicitly_wait(10)

wait = WebDriverWait(driver, 15, poll_frequency=0.25)

# driver.save_screenshot("screen.png")

# driver.get(
#     "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
# )

driver.get("https://whatismyipaddress.com/")

# driver.save_screenshot("screen.png")
wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))

# time.sleep(5)
