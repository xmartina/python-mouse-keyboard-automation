from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="C:\\Users\\HP\\seleniumChromesDrive\\chromedriver")
driver = webdriver.Chrome(service=service)

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="C:/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('https://matagram.com/wp-login.php')
    #find element by partial link text
    myLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Privacy Policy')
    myLink.click()

