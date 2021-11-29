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
driver.get("https://www.onference.in")

try:
    myElem_1 = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,'course-card-container')))
    print(myElem_1)
    sleep(5)
except TimeoutException:
    print("no element found")
#html = driver.execute_script("return document.getElementsByTagname('html')[0].innerHTML")
#print(html)

#soupd = BeautifulSoup(driver.page_source, 'html.parser')
soupd = BeautifulSoup(driver.page_source, 'lxml')
data=[]

for a in soupd.find_all("a", class_="course-card-container", href=True,title=True):
    print(a['href'])
    print(a['title'])


driver.quit()
