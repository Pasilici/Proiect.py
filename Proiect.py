import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar

BASE_URL = 'http://ro.tntimisoara.com/category/stagiunea_18-19/'


my_headers = {"User-Agent": "Microsoft Edge.Ink"}
page = requests.get(BASE_URL, headers=my_headers)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

labs = re.findall(r'((?<=<h3>)(.+?)(?=</h3>))', soup.prettify())

headings = soup.find_all('h3')

f = open("labs.txt", "w")

for heading in headings:
    f.write(heading.text)

f.close()

root = Tk()

root.geometry("400x400")

cal = Calendar(root, selectmode='day', year=2021, month=5, day=4)
cal.pack(pady=20)


def grad_date():
    date.config(text="Data selectata:" + cal.get_date())


Button(root, text="Selectati data", command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

root.mainloop()

links = re.findall(r'((?<=<a>)(.+?)(?=</a>))', soup.prettify())

x = open("links.txt", "w")

for link in soup.findAll('a'):
    x.write(link.get('href'))

x.close()

images = re.findall(r'((?<=<img>)(.+?)(?=<img>))', soup.prettify())


y = open("images.txt", "w")

for imgtag in soup.findAll('img'):
    y.write(imgtag.get('src'))

y.close()
