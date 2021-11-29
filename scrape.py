import requests
from bs4 import BeautifulSoup
from selenium import webdriver

data = requests.get('https://www.onference.in')
print("prinitng onfe html")
#print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')

data=[]

#for course-card-container in soup.find_all('course-card-container'):
 #     print(course-card-container)
for a in soup.find_all("a", class_="course-card-container", href=True,title=True):
    print(a['href'])
    print(a['title'])
for a in soup.find_all("a", class_="event-card-container", href=True,title=True):
    print(a['href'])
    print(a['title'])
    

