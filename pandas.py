#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:12:00 2019

@author: seeuno
"""
#import
import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

#building series
pd.Series(data = my_data)
pd.Series(data=my_data, index=labels)
pd.Series(my_data,labels)
pd.Series(arr,labels)
pd.Series(d)
pd.Series(data=labels)
pd,series(data=[sum,print,len]) #holding function 

#example
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR', 'Japan'])
ser1
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy', 'Japan'])
ser2
ser1['USA']
ser3 = pd.Series(data=labels)
ser3[0]
ser1
ser2
##add series
ser1 + ser2

#####################Pandas - Data Frames##############################
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df
df['W']
type(df['W']) #series
type(df) #data frames
df.W #not recommended (confused with attributes)

#multiple cols
df[['W','Z']]
type(df[['W','Z']]) #data frames

#df['new'] #error
df['new'] = df['W'] + df['Y']
df
#remove the cols/rows 
df.drop('new',axis=1) #drop a new col
df.drop('new',axis=1,inplace=True) #update "deletion" in df
df.drop('E',axis = 0)
df.shape
df[['Z','X']]

#select rows/cols & cells
df.loc['C'] # RETURNS SERIES index based
df.iloc[2] #integer based
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]

#boolean
df > 0
booldf = df>0
df[booldf]
df[df>0]

df
df['W']>0 #series
df['W']
df[df['W']>0]
df[df['Z']<0]
resultdf = df[df['W']>0]
resultdf['X']
df[df['W']>0]['X']

#simple one line expr
df[df['W']>0][['Y','X']]
#multiple line expr
boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
result[mycols]

#df[multiple booleans]
df[(df['W']>0) and (df['Y'] > 1)] #error cannot use "and" (only single value)
df[(df['W']>0) or (df['Y'] > 1)] #error cannot use "or" (only single value)
df[(df['W']>0) & (df['Y'] > 1)] #use "&"
df[(df['W']>0) | (df['Y'] > 1)] #use "|"

df.reset_index()
df
newind= 'CA NY WY OR CO'.split()
newind
df['States'] = newind
df
df.set_index('States')
df

#Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index
df = pd.DataFrame(randn(6,2,),hier_index,['A','B'])
df.loc['G1']
df
df.index.names = ['Groups','Num']
df
df.loc['G2'].loc[2]['B']
df.loc['G1']
df.xs('G1') #CROSS-SECTION
df.xs(1,level='Num')

#################Missing Data#######################
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df
df.dropna(axis=1) #drop cols
df.dropna()
df.dropna(thresh=2) #row 2 has 2NaN
df.fillna(value='Fill VALUE')
df['A']
df['A'].fillna(value=df['A'].mean())

################Group by############################
#groupby allows you to group together rows based off col
#and perform an aggregate function on them (mean, sum, ...)

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'], 'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df
byComp = df.groupby('Company') #store in memory
byComp.mean() #ignore mean of names (String)
byComp.std()
byComp.sum()
byComp.sum().loc['FB']
df.groupby('Company').sum().loc['FB']
df.groupby('Company').count()
df.groupby('Company').min()
df.groupby('Company').max()
df.groupby('Company').describe().transpose()['FB']

################Merge, Join, Concatenation################
#setup
df1 = pd.DataFrame({'A':['A0','A1','A2','A3'], 'B':['B0','B1','B2','B3'], 'C':['C0','C1','C2','C3'], 'D':['D0','D1','D2','D3']}, index=[0,1,2,3])
df2 = pd.DataFrame({'A':['A4','A5','A6','A7'], 'B':['B4','B5','B6','B7'], 'C':['C4','C5','C6','C7'], 'D':['D4','D5','D6','D7']}, index=[4,5,6,7])
df3 = pd.DataFrame({'A':['A8','A9','A10','A11'], 'B':['B8','B9','B10','B11'], 'C':['C8','C9','C10','C11'], 'D':['D8','D9','D10','D11']}, index=[8,9,10,11])

#Concatenation #choose axis correctly
pd.concat([df1,df2,df3]) #concat rows
pd.concat([df1,df2,df3],axis=1) #concat cols

#setup
left = pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'], 'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'], 'D':['D0','D1','D2','D3']})
left
right
#Merging
pd.merge(left,right,how='inner',on='key') #merge using key col

#setup
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']}) 
#Merging2
pd.merge(left,right,on=['key1','key2'])
pd.merge(left,right,how='outer',on=['key1','key2'])
pd.merge(left,right,how='right',on=['key1','key2'])
pd.merge(left,right,how='left',on=['key1','key2'])

#setup - Joining
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
left
right
#Joining
left.join(right)
left.join(right,how='outer')

#####################operations##########################
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

#unique
len(df['col2'].unique())
df['col2'].nunique()
df['col2'].value_counts()
df
#index
df[(df['col1']>2)&(df['col2']==444)]

#apply
def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len)
df['col2'].apply(lambda x:x*2)

df.drop('col1',axis=1)
df.columns
df.index
df.sort_values('col2')
df.sort_values(by='col2')
df.isnull()
df

#pivot table
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df.pivot_table(values='D', index=['A','B'],columns=['C'])
df

##################Data Input & Output#######################
conda install sqlalchemy
conda install lxml
conda install html5lib
conda install BeautifulSoup4
conda install xlrd

#CSV,EXCEL
df = pd.read_csv("example.csv")
df.to_csv('My_output', index=False)
pd.read_csv('My_output')
pd.read_excel('Excel_sample.xlsx')
df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')

#HTML
data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
type(data)
data[0].head()

#
from sqlalchemy import create_engine
engine = create_engine('splite:///:memory:')
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)
sqldf
