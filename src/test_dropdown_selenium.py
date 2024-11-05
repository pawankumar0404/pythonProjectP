import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
select_tag = driver.find_element(By.ID, "dropdown")
select_a = Select(select_tag)
select_a.select_by_visible_text("Option 2")

time.sleep(4)
