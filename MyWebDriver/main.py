# Python program to demonstrate
# selenium

# import webdriver
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# create webdriver object
driver = webdriver.Chrome(options=options)

# get google.co.in
# driver.get("https://google.com")
driver.get("https://app.myhours.com/#/reports/dashboard")
# element = driver.find_element(By.ID,"email")
element = driver.find_element(By.ID,"email")
element.send_keys("maccam6@gmail.com")
# element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]")
element.send_keys(Keys.TAB)
sleep(1)
ActionChains(driver).send_keys("18,Mac&Amo").perform()
sleep(2)

# element.find_element(By.XPATH, r"//span[contains(text(),'Sign in')]")
# element.click()
# element.send_keys(Keys.ENTER)



