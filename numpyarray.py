#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:07:28 2019

@author: seeuno
"""
import numpy as np
#Numpy Arrays
my_list = [1,2,3]
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat) #create arry using list
np.arange(0,11,2) #from 0 increase by 2 to 11(exclusive 11)
np.zeros(3) 
np.zeros((2,3)) #2x3 matrix with 1
np.ones(4)
np.ones((3,4)) #3x4 matrix with 1
np.linspace(0,5,10) #from 0 to 5 evenly 10 spaced
np.eye(4) #identity matrix (takes 1 parameter cuz I is a square matrix)
np.random.rand(5) #5 random numbers from uniform distribution(0,1)
np.random.randn(2) # 2 random numbers from standard normal distribution
np.random.randn(4,4)  #4x4 matrix of random numbers from N(0,1)
np.random.randint(1,100) # 1 random integer from 1 to 100
np.random.randint(1,100,10) # 10 random integer from 1 to 100
#inclusive lowhand exclusive highhand
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
ranarr
arr.reshape(5,5) #numRows * numCols = #of elements in arr
ranarr.max() #max value in array
ranarr.min() #min value in array
ranarr.argmax() #index of max value
ranarr.argmin() #index of min value
arr.shape 
arr = arr.reshape(5,5) 
arr.shape #return shape of array
arr.dtype #return data type in array

from numpy.random import randint
randint(2,10)
randint(0,50,10)

#3################# Numpy Indexing and Selection ####################
import numpy as np
arr = np.arange(0,11)
arr[8]
arr[1:5] #upto arr[1] to arr[4]
arr[:6] #upto arr[0] to arr[5]
arr[5:] #everything beyond arr[5]
arr[0:5] = 100 #broadcast index[0~4] = 100
arr
arr = np.arange(0,11)
slice_of_arr = arr[0:6] #copy a reference of array
slice_of_arr[:]=99
arr #also arr[0:6] = 99
arr_copy = arr.copy() #actual copy!
arr_copy[:] = 100
arr_copy
arr

#index##################################################################
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d
arr_2d[0][0]
arr_2d[0]
arr_2d[2][1]
arr_2d[2,1]
arr_2d[1,2]

#subsection (2d array slicing)##########################################
arr_2d[:2,1] #:2 slice row 2(last row) grab everything col1
arr_2d[:2,1:]

#
arr = np.arange(0,11)
arr
bool_arr = arr > 5
bool_arr
arr[bool_arr]
arr[arr>5]
arr[arr<3]
arr_2d = np.arange(50).reshape(5,10)
arr_2d[1:3]
arr_2d[1:3,3:5]
