import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
import pandas as pd



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
    print(z)
listatab = []
f = open('output.txt', "w", encoding="utf-8")
for i in z[:10]:
        URL = i
        my_headers = {"User-Agent": "Chrome/90"}
        page = requests.get(URL, headers=my_headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        # print(text)


        data = r'Data premierei.*'
        locatie = r'Locația.*'

        data_f = re.findall(data, text)
        locatie_f=re.findall(locatie,text)


        print(i)
        print(data_f)
        print(locatie_f)
        print("---------------------------------------")
        Info_link = [i, data_f, locatie_f]
        listatab.append(Info_link)
f.write(tabulate(listatab, headers='firstrow', tablefmt='fancy_grid'))
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


 #   ele = 0
   # top = Tk()
   # top.geometry("400x225")
   # L1 = Label(top, text="Data(yyyy-mm-dd)",font="arial 12 bold")
   # L1.place(x=125, y=50)
   # E1 = Entry(top, bd =5, font="arial 10 bold", )
   # E1.place(x=125, y=100)
   # button2=tkinter.Button(top, text="CAUTA",font="belltm 10 bold",command = mapa)
   # button2.place(x=175, y=175)
   # top.mainloop()













