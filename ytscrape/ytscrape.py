from bs4 import BeautifulSoup
import urllib


def SearchVid(search):
    responce = urllib.urlopen('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(responce,'lxml')    
    divs = soup.find_all("div", { "class" : "yt-lockup-content"})

    print(divs)
    for i in divs:
        href= i.find('a', href=True)
        print(href.text,  "\nhttps://www.youtube.com"+href['href'], '\n')
        with open(SearchString.replace("%20", "_")+'.txt', 'a') as writer:
            writer.write("https://www.youtube.com"+href['href']+'\n')

print("What are you looking for?")
SearchString = raw_input()
SearchVid(SearchString.replace(" ", "%20"))
print(SearchString.replace(" ","%20"))
