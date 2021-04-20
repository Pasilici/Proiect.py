import requests
from bs4 import BeautifulSoup
import re


URL = 'http://ro.tntimisoara.com/informatii-publice/'


my_headers = {"User-Agent":"Microsoft Edge"}
page = requests.get(URL, headers=my_headers)

soup = BeautifulSoup(page.content, 'html.parser')

labs = re.findall(r' (.*manager.*) ', soup.prettify())

f = open("labs.txt", "w")

for lab in labs:
    print(lab)



#print(soup.prettify())

