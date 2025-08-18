from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "You")
elem.clear()
elem.send_keys("seleniumvideo")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(6)
driver.close()