from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

driver.get("https://money.rediff.com/indices")
driver.maximize_window()
# output_msg=driver.find_element(By.XPATH,'//*[@id="dataTable"]/tbody/tr[10]/td[1]/a/self::*').text
# print(output_msg)  
# output_msg=driver.find_elements(By.XPATH,'//*[@id="dataTable"]/tbody/tr[10]/child::*')
# print(len(output_msg))

# output_value=driver.find_elements(By.XPATH,'//*[@id="dataTable"]/tbody/tr[7]/td[1]/a/self::a/ancestor::tr')
# print(len(output_value))
# output_val2=driver.find_elements(By.XPATH,'//*[@id="dataTable"]/tbody/tr[7]/td[1]/a/ancestor::tr/child::td').text
# print(output_val2)
sibling_data=driver.find_elements(By.XPATH,'//*[@id="dataTable"]/tbody/tr[7]/td[1]/a/ancestor::tr/child::td')
print(len(sibling_data))
driver.close