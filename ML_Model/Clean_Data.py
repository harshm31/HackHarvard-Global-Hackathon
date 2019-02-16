#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd 
import numpy as np 
from sklearn.utils import shuffle


# In[2]:


df = pd.read_csv("Toronto_temp.csv")
#dataset.head(10)


# In[3]:


#clean data in year column
df["Year"] = df["Year"].astype(str)
df["Year"] = df["Year"].str.replace(",","")


# In[4]:


df.season.unique()


# In[5]:


no_rows = df.shape[0]
print(no_rows)


# In[6]:


#adding columns for each season and storing particular value 0 or 1 accordingly

df["Winter"] = pd.Series(index=df.index)
df["Summer"] = pd.Series(index=df.index)
df["Spring"] = pd.Series(index=df.index)
df["Fall"] = pd.Series(index=df.index)

df["Winter"] = df["Winter"].fillna(0)
df["Summer"] = df["Summer"].fillna(0)
df["Spring"] = df["Spring"].fillna(0)
df["Fall"] = df["Fall"].fillna(0)
#df.head(10)

df.loc[df["season"]=="Winter","Winter"] = 1
df.loc[df["season"]=="Summer","Summer"] = 1
df.loc[df["season"]=="Spring","Spring"] = 1
df.loc[df["season"]=="Fall","Fall"] = 1


# In[7]:


#remove unnecessary columns 
columns = ["Max Temp (C)","Min Temp (C)","Date/Time","season"]
df = df.drop(columns=columns,axis=1)


# In[8]:


df.head(10)


# In[9]:


#convert cm to mm in Total Snow column 
type(df["Total Snow (cm)"][0])
df.loc[df["Total Snow (cm)"]!=0.0,"Total Snow (cm)"] *= 10

df.rename(columns={"Total Snow (cm)" : "Total Snow (mm)"},inplace=True)


# In[10]:


df.head(10)


# In[11]:


df.dropna(axis=0,inplace=True)


# In[12]:


count_nan = len(df)-df.count()
print(count_nan)


# In[13]:


df.head(10)


# In[15]:


df = shuffle(df)
df.head(10)


# In[16]:


df.to_csv("clean_weather.csv")


# In[ ]:




