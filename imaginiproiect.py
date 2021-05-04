import requests
from bs4 import BeautifulSoup
import re

BASE_URL = 'http://ro.tntimisoara.com/category/stagiunea_18-19/'


my_headers = {"User-Agent":"Microsoft Edge.Ink"}
page = requests.get(BASE_URL, headers = my_headers)

soup = BeautifulSoup(page.content, 'html.parser')


#print(soup.prettify())

#labs = re.findall(r'((?<=<a+img src>)(.+?)(?=<\/a+img src>))', soup.prettify())
headings = soup.find_all("img src")

f = open("lab.txt", "w")

for heading in headings:
    f.write(heading.text)

f.close()
