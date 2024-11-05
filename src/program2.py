from selenium.webdriver.chrome.options import Options
from selenium import webdriver


chrome_options=Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

driver=webdriver.Chrome(chrome_options)
driver.get("https://app.vwo.com/#/login")

