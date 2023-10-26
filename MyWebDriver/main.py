# Python program to demonstrate
# selenium

# import webdriver
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)

def login_in():
    driver.get("https://app.myhours.com/#/reports/dashboard")
    driver.maximize_window()
    element = driver.find_element(By.ID, "email")
    element.send_keys("maccam6@gmail.com")
    element = driver.find_element(By.ID, 'password')
    element.send_keys('18,Mac&Amo')
    driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]").click()

def extract_time_work():
    work_time = '0'
    date = driver.find_element(By.XPATH, """/html[1]/body[1]/div[1]/div[1]/div[1]/dashboard[1]/div[1]/div[1]/div[1]/div[1]/
                                                button[2]/span[1]""").get_attribute("innerText")
    while work_time == '0':
        sleep(0.1)
        work_time = driver.find_element(By.XPATH, """/html[1]/body[1]/div[1]/div[1]/div[1]/dashboard[1]/div[1]/div[2]/ 
                                                dashboard-summary[1]/div[1]/report-summary-stat-display[1]/div[1]/div[1]/h4[1]/
                                                span[1]/span[1]/span[1]""").get_attribute("innerText")
    driver.find_element(By.XPATH, """/html[1]/body[1]/div[1]/div[1]/div[1]/dashboard[1]/div[1]/div[1]/div[1]/div[1]
                                         /button[1]/i[1]""").click()
    return (date, work_time)

login_in()
sleep(5)
driver.find_element(By.XPATH, "//span[contains(text(),'Reports')]").click()
driver.find_element(By.ID, "daterange1").click()
# click on month
# driver.find_element(By.XPATH, """/html[1]/body[1]/div[3]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]/select[1]""").click()

# Select element from dropdown list
month_dropdown = Select(driver.find_element(By.CLASS_NAME, "monthselect"))
month_dropdown.select_by_index(0)
sleep(3)
l = driver.find_element(By.XPATH, "//body/div[2]/div[2]/div[1]/table[1]")
# date_dropdown = Select(driver.find_element(By.CLASS_NAME, ))
# select date
# driver.find_element(By.XPATH, """
# /html[1]/body[1]/div[3]/div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]/select[1]/option[1]""").click()
input("Press to continue: ")
driver.find_element(By.XPATH, "//li[contains(text(),'This week')]").click()
# sleep(2)
print(driver.find_element(By.XPATH, """/html[1]/body[1]/div[1]/div[1]/div[1]/dashboard[1]/div[1]/div[2]/ 
                                    dashboard-summary[1]/div[1]/report-summary-stat-display[1]/div[1]/div[1]/h4[1]/
                                    span[1]/span[1]/span[1]""").get_attribute("innerText"))
time_data = ()
test = {}


# for i in range(0, 10):
#     date, work_time = extract_time_work()
#     test[date] = work_time
#
# df = pd.DataFrame(test.items(), columns=["Date Range", "Work Time"])
# print(df)
# print(test)