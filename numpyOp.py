#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:32:39 2019

@author: seeuno
"""

import numpy as np
arr = np.arrange(0,11)
arr
#adding arrays together
arr + arr 
#multiply arrays 
arr * arr
#add # to every elements in array
arr + 100
arr - 100
#numpy division
1/0 #>> gives error
arr / arr #outputs "nan" (warning)
1 / arr #outputs "inf" (warining)

#square
arr **2
#square root
np.sqrt(arr)
#exponential
np.exp(arr)

#maximum
np.max(arr)
arr.max()

#sin, log
np.sin(arr)
np.log(arr)

#more operations - docs.scipy.org/dpoc/numpy/reference/ufuncs.html
