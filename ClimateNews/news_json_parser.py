# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:10:37 2018

@author: MuthaHarsh
"""

import json
from bs4 import BeautifulSoup


def get_json_output(soup) : 
    
    #get divs and other tags required 
    div1 = soup.find('div',attrs = {'class' :'wire-timeline'})
    inner_div = div1.find_all('div',attrs = {'class':'date-group tc-wire'})
    required_div = inner_div[0]
    articles = required_div.find_all('article',attrs = {'class':'article-block wire'})
    title = inner_div[0].find('h4',attrs = {'class':'section-title'}).text

    arr = {}
    arr["date"] = title
    data = []
    
    for article in articles :
        heading = article.find('h3',attrs = {'class':'article-title'}).text
        h = article.find('h3',attrs = {'class':'article-title'})
        link = h.find('a').get("href")
        content = article.find('div',attrs = {'class':'excerpt'}).find('p').text
        source = article.find('div',attrs = {'class' :'meta tc-link'}).find('a').text
        dict1 = {}
        dict1["heading"] = heading
        dict1["link"] = link
        dict1["content"] = content
        dict1["source"] = source
        data.append(dict1)
        #arr["data"] = dict1

    arr["data"] = data    
    json1 = json.dumps(arr)
    json_response = json.loads(json1)
    
    return json_response
