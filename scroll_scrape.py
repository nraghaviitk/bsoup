from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
import lxml

options = Options()
options.headless = True
#driver = webdriver.Chrome(executable_path='/home/raghav/bsoup/chromedriver')
#driver = webdriver.Firefox(executable_path='/home/raghav/bsoup/geckodriver',options=options)
driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver',options=options)
driver.get("https://www.onference.in")

#soupd = BeautifulSoup(driver.page_source, 'html.parser')
soupd = BeautifulSoup(driver.page_source, 'lxml')
data=[]

for a in soupd.find_all("a", class_="course-card-container", href=True,title=True):
    print(a['href'])
    print(a['title'])

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

#sleep(5)

#soupd = BeautifulSoup(driver.page_source, 'lxml')

last_height=driver.execute_script("return document.body.scrollHeight")
#print("last height", last_height)

data=[]
while True:
    last_height=driver.execute_script("return document.body.scrollHeight")
    sleep(12)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height=new_height
    soupd = BeautifulSoup(driver.page_source, 'lxml')
    for a in soupd.find_all("a", class_="course-card-container", href=True,title=True):
        print(a['href'])
        print(a['title'])
driver.quit()
