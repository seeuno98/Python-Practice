#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:42:17 2019

@author: seeuno
"""

#https://www.kaggle.com/mchirico/montcoalert
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv('911.csv')
df.info()
df.head()

#TOP 5 Zipcodes for 911
df["zip"].value_counts().head()
#TOP 5 townships(twp) for 911
df["twp"].value_counts().head()
#how many unique title codes
df["title"].nunique()

#create a new column for Reasons
types = ['EMS','Fire','Traffic']
def createReason(title):
    if 'ems' in title.lower():
        return 'EMS'
    elif 'fire' in title.lower():
        return 'Fire'
    else:
        return 'Traffic'
    
df['Reasons'] = df['title'].apply(lambda x : createReason(x))

#Most Common Reason
df['Reasons'].value_counts() 
#EMS is the most common reason for 911 calls

#countplot of 911 calls by Reason
sns.countplot(x='Reasons',data=df)

#create new columns to separate timeStamp to Hour,Month,Day of Week
df['timeStamp']
type(df['timeStamp'][0]) #str

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
time = df['timeStamp'].iloc[0]
time.hour
time.month
time.dayofweek

df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

#make 0-6 value in Day of Week to string names to the week
daymap = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',
          4:'Friday',5:'Saturaday',6:'Sunday'}
df['Day of Week'] = df['Day of Week'].map(daymap)

#Countplot (Day of Week col with hue based off of the Reason col)
sns.countplot(x="Day of Week", data = df, hue = 'Reasons')
plt.legend(bbox_to_anchor=(1.25, 1), loc='upper right')

#make 1-12 value in Month to string names to the month
#monthmap = {1: 'January', 2: 'February', 3:'March', 4:'April', 5:'May',
#            6: 'June', 7: 'July', 8: 'August', 9: 'September', 
#            10: 'October', 11: 'November', 12: 'December'}
#df['Month'] = df['Month'].map(monthmap)

#Countplot (Month col with hue based off of the Reason col)
sns.countplot(x='Month',data = df,hue='Reasons')
plt.legend(bbox_to_anchor=(1.25,1), loc='upper right')

#Create an object(byMonth) to group data frame by the month use count for aggregation 
byMonth = df.groupby('Month').count()
byMonth.head()

#A simple plot representing the count of calls per month
byMonth['addr'].plot()

#create a linear fit on # of calls per month
sns.lmplot(x='Month', y='addr', data = byMonth.reset_index())

#create a new column "Date"
df['Date'] = df['timeStamp'].apply(lambda x:x.date())

#Groupby this Date column with count() aggregate
byDate = df.groupby('Date').count()
byDate['addr'].plot()
plt.tight_layout()

#create 3 separate plots with each plot representing a Reason
df[df['Reasons']=='EMS'].groupby('Date').count()['addr'].plot()
plt.tight_layout()
df[df['Reasons']=='Fire'].groupby('Date').count()['addr'].plot()
plt.tight_layout()
df[df['Reasons']=='Traffic'].groupby('Date').count()['addr'].plot()
plt.tight_layout()

#create new data frames (col = hours, ind = day of week)
dayWeekHours = df.groupby(by=["Day of Week","Hour"]).count()['addr'].unstack()
dayWeekHours.head()
#create HeatMap using df
plt.figure(figsize=(12,6))
sns.heatmap(x=")
