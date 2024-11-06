import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# def test_webtable2():
driver = webdriver.Chrome()
driver.get("https://awesomeqa.com/webtable1.html")

select_cell = driver.find_element(By.XPATH,
                                  "//table[contains(@class,'tsc_table_s13')]/tbody/tr[2]/td[1]/following-sibling::td")
print(select_cell.text)

time.sleep(4)
