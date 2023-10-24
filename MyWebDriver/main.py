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
driver = webdriver.Chrome(options=options)

driver.get("https://app.myhours.com/#/reports/dashboard")
driver.maximize_window()
element = driver.find_element(By.ID,"email")
element.send_keys("maccam6@gmail.com")
element = driver.find_element(By.ID, 'password')
element.send_keys('18,Mac&Amo')
driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]").click()


