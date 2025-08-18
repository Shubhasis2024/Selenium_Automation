from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
querry="Mobiles"
driver.get(f"https://www.amazon.in/s?k={querry}&crid=3LBWSGNEH31X2&sprefix=mobile%2Caps%2C278&ref=nb_sb_noss_2")
elem=driver.find_element(By.CLASS_NAME,"a-link-normal s-no-outline")

time.sleep(15)
driver.close()