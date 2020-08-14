import pymongo
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


client = pymongo.MongoClient("mongodb+srv://user_27:422sNsIOM0xaqIGp@reportingdata.pgyx6.mongodb.net/covid-19?retryWrites=true&w=majority")
db = client['covid-19']

cases_collection = db['cases']


cases = cases_collection.find()


df = pd.DataFrame(cases)

df2 = df[['TotalDeath', 'TotalCase', 'NewDeath', 'NewCase', 'Date_epicrv']].groupby(['Date_epicrv'], as_index=False).sum()

plt.figure(figsize=(12,8))
plt.ylabel('Infections')
plt.xlabel('Date')
plt.xticks(rotation=90)

#plt.plot(pd.to_datetime(df2['Date_epicrv']), df2['TotalCase'], color='#0000FF', linewidth=2, alpha=0.5, label='Total Cases')
plt.plot(pd.to_datetime(df2['Date_epicrv']), df2['TotalDeath'], color='#FF0000', linewidth=2, alpha=0.5, label='Total Deaths')
plt.plot(pd.to_datetime(df2['Date_epicrv']), df2['NewDeath'], color='#FFAA00', linewidth=2, alpha=0.5, label='New Deaths')
plt.plot(pd.to_datetime(df2['Date_epicrv']), df2['NewCase'], color='#FF00FF', linewidth=2, alpha=0.5, label='New Cases')
plt.legend()

plt.show()


df3 = df[['TotalDeath', 'TotalCase', 'NewDeath', 'NewCase', 'COUNTRY_NAME']].groupby(['COUNTRY_NAME'], as_index=False).sum()

plt.figure(figsize=(12,8))
plt.bar(df3['COUNTRY_NAME'].head(10), df3['TotalDeath'].head(10))
plt.xticks(rotation=90)

plt.show()









