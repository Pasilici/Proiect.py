import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkcalendar import Calendar
import pandas as pd
import re
import os
import numpy
import cv2
from selenium import webdriver


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

BASE_URL = 'http://ro.tntimisoara.com/category/stagiunea_18-19/'


my_headers = {"User-Agent": "Microsoft Edge.Ink"}
page = requests.get(BASE_URL, headers=my_headers)

soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find_all('div', {'class': 'sidebar_content'})

for item in content:
    urluri = soup.find_all('h3', {'class': 'cufon'})

    d = open('links.txt', 'w')
    print(urluri, file=d)
    d = open('links.txt', 'r')

    z = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', d.read())
    g = open('linkuri_piese.txt', 'w')
    print(z, file=g)

for url in 'linkuri_piese.txt':
    my_headers = {"User-Agent": "Microsoft Edge.Ink"}
    page = requests.get(BASE_URL, headers=my_headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    content1 = soup.find_all('div', {'class': 'sidebar_content'})
    content1 = str(content1)
    #for imagine in soup.find_all('img'):
     #   print(imagine['src'])
    #locatia  = re.findall('(?<=(Locația\: )).*(?=\n)', content1)
    #data = re.findall('(?<=(Data premierei\: )).*(?= \n)', content1)
    #print(locatia)
    #print(data)
    #print('labs.txt')

r2 = requests.get("http://ro.tntimisoara.com/category/stagiunea_18-19/")
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

x = soup2.select('img[src^="http://ro.tntimisoara.com/wp-content/uploads"]')

for img in x:
    links.append(img['src'])

#for l in links:
 #   print(l)

os.mkdir('imagini_spectacole')
i=1

for index, img_link in enumerate(links):
    if i<=10:
        img_data = requests.get(img_link).content
        with open("imagini_spectacole/" + str(index+1) + '.jpg', 'wb+') as j:
            j.write(img_data)
        i+=1
    else:
        j.close()

