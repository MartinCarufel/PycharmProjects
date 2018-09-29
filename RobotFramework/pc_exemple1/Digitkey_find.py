from selenium import webdriver
import requests
import bs4
import re

browser = webdriver.Chrome()
type(browser)

browser.get('https://www.digikey.ca')

champ = browser.find_element_by_id('pagelayout_0_content_2__searchText')
champ.send_keys('7404')
button = browser.find_element_by_id('pagelayout_0_content_2__searchImg')
button.click()
res = requests.get(browser.current_url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
search_result = soup.select('#matching-records-count')


pat = re.compile("(\<.*\>)([0-9]*)(\<.*\>)")
regex = re.split(pat, str(search_result[0]))

print(regex[2])

