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
driver = webdriver.Firefox(executable_path='/home/raghav/bsoup/geckodriver',options=options)

def searchvid(search):
    driver.get("https://www.youtube.com/results?search_query=")

    #soupd = BeautifulSoup(driver.page_source, 'html.parser')
    soupd = BeautifulSoup(driver.page_source, 'lxml')
    data=[]
    divs=soupd.find_all("div",class_="yt-lockup-content")
    print(divs)
    for i in divs:
        href=i.find('a',href=True)
        print(href.text,)
        print(a['title'])

print("what are you searching for")
SearchString = raw_input()
searchvid(SearchString.replace(" ","%20"))

