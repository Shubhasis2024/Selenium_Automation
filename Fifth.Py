from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://hilarious-moonbeam-5957f8.netlify.app/")
driver.maximize_window()
value1=driver.find_element(By.CSS_SELECTOR,"textarea#Myboxarea")
value2=driver.find_element(By.CLASS_NAME,"btn")

value1.clear()
value1.send_keys("Hello")
value2.click()

realtitile=driver.title
expectitle="Enter text to Analyze Below"
if realtitile == expectitle:
 print("Testcase pass")
else:
    print("Test case fail ")
time.sleep(15)
driver.close
