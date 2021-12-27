#Hello!
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.dominos.co.uk/')
sleep(4)

with open('creds.json') as json_file:
    data = json.load(json_file)

print(email)
print(password)

driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
sleep(1)

driver.find_element_by_xpath('//*[@id="account-overlay"]/ul/li[1]/a').click()
sleep(1)

driver.find_element_by_xpath('//*[@id="formulate--login-1"]/input').send_keys(email)
sleep(1)

driver.find_element_by_xpath('//*[@id="formulate--login-2"]/input').send_keys(password)
sleep(1)

driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/form/div[4]/button/div').click()
sleep(5.5)

driver.find_element_by_xpath('//*[@id="menu-selector"]').click()
sleep(1)

driver.execute_script("window.scrollTo(0, 300)")
sleep(1)

driver.find_element_by_xpath('//*[@id="1677"]/div/div[1]/div/img').click()
sleep(1)

driver.find_element_by_xpath('//*[@id="add-to-order"]').click()
sleep(1)

driver.find_element_by_xpath('//*[@id="main-nav"]/div/ul/li[4]/a').click()
sleep(1)

driver.find_element_by_xpath('//*[@id="upsell-overlay-container"]/div[2]/button[2]').click()
sleep(1)

driver.execute_script("window.scrollTo(0, 600)")
sleep(1)

driver.find_element_by_xpath('//*[@id="checkoutButtonBottom"]').click()
# sleep(1)
