from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
sleep(2)
l = len(driver.find_elements(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/div[1]/table[1]/tbody[1]/tr[1]/th[1]"))
print(l)


