import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
import numpy
import cv2
import os
from selenium import webdriver
import pandas as pd
import urllib.request


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
    print(z)
