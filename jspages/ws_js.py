import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

# start by defining the options 
options = webdriver.ChromeOptions() 
options.headless = True # it's more scalable to work in headless mode 
# normally, selenium waits for all resources to download 
# we don't need it as the page also populated with the running javascript code. 
options.page_load_strategy = 'none' 
# this returns the path web driver downloaded 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 
# pass the defined options and service objects to initialize the web driver 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

url = "https://annwyl21.github.io/" 
 
 
driver.get(url) 
time.sleep(10)

# https://www.selenium.dev/documentation/webdriver/elements/finders/
# use plural to find all elements not just the first one
classPTB = driver.find_elements(By.CLASS_NAME, 'project-text-box')



# for result in classPTB:
# 	print(result.text)
      
with open('my_cv.txt', 'a') as f:
    for result in classPTB:
    	f.write(result.text)
    