# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:14:02 2014

@author: Nova

Read in the data, check which columns are which
"""
import numpy as np
#"""
# Looking at new.phot.columns files
f = open('sn2010el_new.phot.columns','r')
info = f.read()
f.close()
print info
#"""
"""
# Looking at Isochrone files
f   = open('Z017Y26.dat')
row = []
row = [f.readline().strip().split() for i in range(16776)]
row = np.array(row)

print row[:][0]
print row[:][1]
print row[:][2]
print row[:][3]
print row[:][4]
print row[:][5]
print row[:][6]
print row[:][7]
print row[:][8]
print row[:][9]
print row[:][10]
"""