from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome(executable_path='/home/raghav/bsoup/chromedriver')
driver.get("https://www.onference.in")
sleep(5)
html = driver.execute_script("return document.getElementsByTagname('html')[0].innerHTML")
print(html)

soupd = BeautifulSoup(driver.page_source, 'html.parser')
data=[]

for a in soupd.find_all("a", class_="course-card-container", href=True,title=True):
    print(a['href'])
    print(a['title'])
