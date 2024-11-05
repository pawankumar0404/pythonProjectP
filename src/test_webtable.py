from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://awesomeqa.com/webtable1.html")
tr_count=driver.find_element(By.XPATH,"//table[contains(@class,'tsc_table_s13')]/tbody/tr[2]")


print(tr_count.text)
