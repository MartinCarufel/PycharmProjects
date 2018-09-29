from selenium import webdriver

driver = webdriver.Chrome()
browser = webdriver.Chrome()
type(browser)

browser.get('https://www.webpagetest.org/easy.php')

champ = browser.find_element_by_id('url')
champ.send_keys('https://www.digikey.ca')
button = browser.find_element_by_name('submit')
button.click()
