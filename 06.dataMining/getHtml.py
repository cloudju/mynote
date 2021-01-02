#import requests
#from lxml import html
#url='https://www.google.com/search?q=python+%E7%88%AC%E8%99%AB&sxsrf=ACYBGNRQE-2fAKipBm4DpT-GWYmEDJf0tg:1579490542685&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiF5OPlnJHnAhUsyIsBHblnAeYQ_AUoAnoECAwQBA&biw=1440&bih=789' #需要爬数据的网址
#page=requests.Session().get(url)
#print(page.text)

import re

from bs4 import BeautifulSoup

abc = open("./2.html", mode='r')
html_doc = abc.read()

soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")

links = soup.find_all('p')
for link in links:
    print(link)
    #print(link['href'])
