import pandas as pd
import os
import pymongo
from glob import glob
monthDict={'Mar': 3, 'Feb': 2, 'Aug': 8, 'Apr': 4, 'June': 6, 'Jan': 1, 'May': 5, 'Nov': 11, 'July': 7, 'Dec': 12, 'Sept': 9, 'Oct': 10, 'Year':-1}
client = pymongo.MongoClient("localhost", 27017) 
db = client.climatedb

csv_files = glob('./ClimateData_cleaned/*.csv')
allObjects = []
for f in csv_files:
    city = f.split('_')[0][2:].lower()
    print('Processing '+ city)
    df = pd.read_csv(f)
    months = df.columns.values[:]
    df = df.transpose()
    rows, cols = df.shape
    for i in range(1, rows):
        obj = {}
        obj['city'] = city
        obj['month_no'] = monthDict[months[i]] 
        for j in range(0, cols):
            cell = df.iloc[i,j]
            header = df.iloc[0, j]
            obj[header] = cell
        allObjects.append(obj)

print(db.climate.insert(allObjects))

