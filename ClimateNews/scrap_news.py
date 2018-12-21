
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import shutil
import news_json_parser as njp

cwd = os.getcwd()
#get today's date 
date1 = str(datetime.now()).split(' ')[0]
dt = datetime.strptime(date1, '%Y-%m-%d')
yr = dt.year%100
m = dt.month
d = dt.day
folder_name = str(d)+str(m)+str(yr)
print(folder_name)

#code to scrape data from website 
url = "https://insideclimatenews.org/todaysclimate"
req = requests.get(url , verify = False)
soup = BeautifulSoup(req.content,"lxml")
print(soup)

try :
    output=njp.get_json_output(soup)
    print(output)
except Exception as e :
    print(e)


