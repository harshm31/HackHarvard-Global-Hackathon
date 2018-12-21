
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import shutil
import news_json_parser as njp

#code to scrape data from website 
url = "https://insideclimatenews.org/todaysclimate"
req = requests.get(url , verify = False)
soup = BeautifulSoup(req.content,"lxml")

try :
    output=njp.get_json_output(soup)
    print(output)
except Exception as e :
    print(e)


