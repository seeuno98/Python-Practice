#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:25:04 2019

@author: seeuno
"""


import matplotlib.pyplot as plt
#%matplotlib inline
plt.show() #non-jupyter we need to keep this line

import numpy as np
x = np.linspace(0,5,11)
y = x**2
x
y

#Functional
plt.plot(x,y,'r')
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

#Subplots
plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()

# OO
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')

#
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
#axes2 = fig.add_axes([0.2,0.15,0.4,0.3])
#axes2 = fig.add_axes([0.8,0.15,0.4,0.3])
axes1.plot(x,y)
axes1.set_title('Larger Plot')
axes2.plot(y,x)
axes2.set_title('Smaller Plot')
plt.show()

#basic
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
plt.show()

############# subplot###########
fig,axes = plt.subplots(nrows=3,ncols=3)
#axes.plot(x,y)
plt.tight_layout()
plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)
for current_ax in axes:
    current_ax.plot(x,y)
plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.tight_layout()
plt.show()

#############Figure Szie & DPI(pixels/inch)###############3
fig = plt.figure(figsize=(3,2),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
plt.show()

############save figure##########################
fig.savefig('my_picture.jpg',dpi=200)


############Legend##############################
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='X Sqaured')
ax.plot(x,x**3,label='X Cubed')
ax.set_title('Title')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(loc=10)
plt.show()

###########Plot Appearance######################
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',linewidth=3, 
        linestyle='--',alpha=0.5)
#ax.plot(x,y,color='purple',linewidth=3, 
        #linestyle=':,step,-.',alpha=0.5)
#ax.plot(x,y,color='purple',linewidth=0.5)
plt.show()
#ax.plot(x,y,color='#FF8C00') #RGB Hex Code

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',linewidth=3, 
        linestyle='-',alpha=0.5,
        marker='o',markersize=10,
        markerfacecolor='yellow',markeredgewidth=3,
        markeredgecolor='green')
#marker = '1','*', '2','+'
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',ls='--')
ax.set_xlim([0,1])
ax.set_ylim([0,2])

#marker = '1','*', '2','+'
plt.show()

#special plot types
