# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:35:26 2018

@author: MuthaHarsh
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup
import csv

cwd = os.getcwd() #current directory where file is 
chromedriver_path = cwd + "\chromedriver.exe"
#print(chromedriver_path)

cities = """Mumbai,Delhi,Bangalore,Ahmedabad,Chennai,Kolkata,Pune,Lucknow,Kanpur,Nagpur,Visakhapatnam,Indore,Patna,Vadodara,Ludhiana,Coimbatore,Agra,Madurai,Chandigarh,Allahabad"""

items_to_search = cities.split(',')
for item in items_to_search : 
    item = item.strip('\n')
    item = item.strip('\t')
    
#print(items_to_search)
#print(len(items_to_search))
driver = webdriver.Chrome(executable_path = chromedriver_path)
base_url = "https://www.wikipedia.org/"

indices = ["Record high °C (°F)","Average high °C (°F)","Average low °C (°F)","Record low °C (°F)","Average rainfall mm (inches)","Average rainy days"]#,"Average relative humidity (%)","Mean monthly sunshine hours"]
cols = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec","Year"]
size = len(indices) * len(cols)


def climateData(city) : 
    #print(city)
    d = []
    url = base_url + "/wiki/"+city
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,"lxml")
   # print(soup)
    table = soup.find('table',class_="wikitable collapsible mw-collapsible mw-made-collapsible")
    #print(table)
    rows = table.find_all('tr') 
    rows = rows[2:len(indices)+2]
    for row in rows : 
        cells = row.find_all('td')
        for cell in cells : 
            d.append(cell.text.strip('\n'))
    
    data = np.array(d) 
    #print(d[0:size])
    #print(len(d))
    d = d[0:size]
    data = np.array(d)
    data = data.reshape(len(indices),len(cols))
    createDataFrame(data,city) 
    #driver.quit()

def createDataFrame(data,city) : 
    df = pd.DataFrame(data,indices,cols)
    #print(df)
    if os.path.exists('./ClimateData') :
        csv_name = ('ClimateData/'+city+'_climateData.csv')
    else :
        os.mkdir('ClimateData')
        csv_name = ('ClimateData/'+city+'_climateData.csv')
    df.to_csv(csv_name)
    

for city in items_to_search : 
    climateData(city)

driver.quit()
#climateData(items_to_search[0])    