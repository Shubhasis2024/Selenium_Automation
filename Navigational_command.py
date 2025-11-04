from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.myntra.com/jabong")

driver.back()#Navgational commands in selenium 
driver.forward()#Navgational commands in selenium 
driver.back()#Navgational commands in selenium 
driver.refresh()#Navgational commands in selenium 
searchbox=driver.find_elements(By.XPATH,'//*[@id="inputValEnter"]')
print(len(searchbox))
searchbox[0].send_keys("Mens shirt")
searchbtn=driver.find_element(By.XPATH,'//*[@id="sdHeader"]/div[4]/div[2]/div/div[2]/button/span')
searchbtn.click()
# print("The text data is:",searchbtn.text)
# print("the text data is ",searchbox[0].text) #iner text of html will come if avilable 
# print("The attribte is ",searchbox[0].get_attribute('value')) #user enter data will come here 
time.sleep(5)
driver.quit()