# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 09:43:26 2014

@author: Nova
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv
from itertools import izip
import pickle
import glob


filename = open('sn2008ge_F435W_F555W_snr3.csv')
data = np.recfromcsv(filename, names=['a','a','a'])
newxcoord = []
newycoord = []
for i in range(len(data)):
    newxcoord.append(data[i][0] - 3200)
    newycoord.append(data[i][1] - 3370)

with open('test.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(newxcoord,newycoord))
"""
f = []
data = []
coord = []
f = glob.glob('sn2008ge_*.csv')
for i in range(len(f)):
    coord = np.genfromtxt(f[i], delimiter = ',')
print coord

for i in range(len(f)):
    photfile = open(f[i],'r')
    print photfile
    
    for line in photfile:
        columns = line.split()
        data.append(columns)
    print data
"""