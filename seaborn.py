#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:18:16 2019

@author: seeuno
"""
#setup
import numpy as np
import seaborn as sns
#matplotlib inline
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()
###########Distribution plots#######################
sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False,bins=30)

#joint plot
sns.jointplot(x='total_bill',y='tip',data=tips)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')

sns.pairplot(tips)
sns.pairplot(tips,hue='sex',palette = 'coolwarm') #hue for categorical

sns.rugplot(tips['total_bill']) #actual points
sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False) #Kernel density estimation plot

##########Categorical Plots##########################
sns.barplot(x='sex',y='total_bill',data=tips)
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
sns.countplot(x='sex',data=tips)
sns.boxplot(x='day',y='total_bill',data=tips)
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
sns.violinplot(x='day',y='total_bill',data=tips)
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
sns.stripplot(x='day',y='total_bill',data=tips)
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)
sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',split=True,jitter=True)
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')
sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')

##########Matrix Plots#####################################
flights = sns.load_dataset('flights')
flights.head()

tc = tips.corr()
sns.heatmap(tc,annot=True,cmap='coolwarm')
tc
flights
fp= flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=2)
sns.heatmap(fp,cmap='coolwarm',linecolor='black',linewidths=2)
sns.clustermap(fp)
sns.clustermap(fp,cmap='coolwarm')

#########Grid##############################################
iris = sns.load_dataset('iris')
iris.head()
iris['species'].unique()
sns.pairplot(iris)

g = sns.PairGrid(iris)
#g.map(plt.scatter)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')
tips.head()

g = sns.FacetGrid(data=tips,col='time',row='smoker')
#g.map(sns.distplot,'total_bill')
g.map(plt.scatter,'total_bill','tip')

#########Regresssion Plots####################################
tips = sns.load_dataset('tips')
tips.head()

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',
           markers=['o','v'],scatter_kws={'s':100})

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',row='time',hue='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,
           col='day',row='time',hue='sex',aspect=0.6,size=8)

