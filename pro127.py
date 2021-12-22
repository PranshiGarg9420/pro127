from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd

url= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(url)
soup= BeautifulSoup(page.text, 'html.parser')

info_list=[]
table= soup.find('table')
table_rows= table.find_all('tr')
for tr in table_rows:
    td= tr.find_all('td')
    row= [i.text.rstrip() for i in td]
    info_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
luminosity=[]

for i in range(1, len(info_list)):
    star_names.append(info_list[i][1])
    distance.append(info_list[i][3])
    mass.append(info_list[i][5])
    radius.append(info_list[i][6])
    luminosity.append(info_list[i][7])

df= pd.DataFrame(list(zip(star_names, distance, mass, radius, luminosity)), columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)

df.to_csv('stars.csv')