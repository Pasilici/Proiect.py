import csv

import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from urllib.request import urlopen as uReq








filepath = '/Users/passy/PycharmProjects/Book1.csv'

file = open(filepath)
reader = csv.reader(file)
data= list(reader)
del(data[0])


list_of_date = []
for x in list(range(0, len(data))):
    list_of_date.append(data[x][0])

root = Tk()
root.geometry('500x300')
listbox1 = Listbox(root)
for x, y in enumerate(list_of_date):
    listbox1.insert(x, y)
var = StringVar(value= list_of_date)
listbox1 = Listbox(root,width=70, height=10, listvariable = var)
listbox1.grid(row = 0, column=0)

def eveniment():
    index = listbox1.curselection()[0]
    datapremiereilabel2.config(text = data[index[0]])
    linkurilabel2.config(text = data[index[1]])
    locatialabel2.config(text = data[index[3]])
    return None

button1 = Button(root , text = "eveniment", command = eveniment)
button1.grid(row=5, column=0)

datapremiereilabel= Label(root, text="data premierei").grid(row=1, column=0,sticky="w")
linkurilabel= Label(root, text="linkuri").grid(row=2, column=0,sticky="w")
locatialabel= Label(root, text="locatia").grid(row=3, column=0,sticky="w")

datapremiereilabel2= Label(root, text="")
datapremiereilabel2.grid(row=1, column=1,sticky="w")
linkurilabel2= Label(root, text="")
linkurilabel2.grid(row=2, column=1,sticky="w")
locatialabel2= Label(root, text="")
locatialabel2.grid(row=3, column=1,sticky="w")

root.mainloop()
