import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

def web_scraper_js():
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
	class_PTB = driver.find_elements(By.CLASS_NAME, 'project-text-box')
	class_FCB = driver.find_elements(By.CLASS_NAME, 'flip-card-back')
	class_badge = driver.find_elements(By.CLASS_NAME, 'badge')
	id_mySkills = driver.find_elements(By.ID, 'mySkills')
	class_jobtitle = driver.find_elements(By.CLASS_NAME, 'desire')
	id_brand = driver.find_elements(By.ID, 'brand')

	scraped = [class_PTB, class_FCB, class_badge, id_mySkills, class_jobtitle, id_brand]
	  
	with open('my_cv.txt', 'w') as f:
		for scraped_list in scraped:
			for result in scraped_list:
				f.write(result.text + ' ')
	