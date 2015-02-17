# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:14:02 2014

@author: Nova

Read in the data, check which columns are which
"""
import numpy as np
import pandas
# Looking at new.phot.columns files
f = open('../SN2010AE/sn2010ae.phot.columns','r')
#f = open('../SN2008GE/sn2008ge_20141015_final.out.columns','r')
#f = open('../SN2010EL/sn2010el.phot.columns','r')
info = f.read()
f.close()
print info
#print type(info)
#print len(info)
#print info[0:10000]

"""
# Looking at Isochrone files
f   = open('../Metallicity/Z0170Y26.dat')
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