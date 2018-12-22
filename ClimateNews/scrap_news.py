
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import os
import news_json_parser as njp
import jsonify

#code to scrape data from website 
url = "https://insideclimatenews.org/todaysclimate"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
soup = BeautifulSoup(response,"lxml")

output=njp.get_json_output(soup)


