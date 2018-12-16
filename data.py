import requests
from pprint import pprint

city=input('Enter city: ')
url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44'.format(city)
res=requests.get(url)
data=res.json()
pprint(data)