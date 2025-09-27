from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("xxxxxxxxxxx")
driver.find_element(By.NAME,"pass").send_keys("xxxxxxxxxxxx")
Button=driver.find_element(By.NAME,"login")
Button.click()

time.sleep(10)
print("All Test cases are passed succesfully")
driver.close