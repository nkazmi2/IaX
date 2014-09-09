# -*- coding: utf-8 -*-
"""
Created on Wed Aug 06 11:34:01 2014

@author: Nova
"""
import numpy as np

A = np.matrix([[1,2,3,4],[2,2,4,3],[3,5,2,2],[4,4,2,1]])
B = np.matrix([[1,2,3,4],[2,1,3,2],[3,4,1,2],[4,3,2,1]])

#print A
#print B
#print "Center", A[cent1,cent2]

a = []
b = []
for n in range(4):
    for p in range(4):
        a.append(A[3-n,0+p])
        b.append(B[0+n,3-p])
      
bo = np.reshape( b  , (4,4))
ao = np.reshape( a  , (4,4))
print np.matrix( ao - bo)

cent1 = 2
cent2 = 1
#A[2,1] = 0
c = []
d = []
for n in range(4):
    for p in range(4):
        d.append(A[n,p])
        c.append(B[n,p])
        #d.append(A[n,p-1])
        #c.append(B[n-1,p])

co = np.reshape( c  , (4,4))
do = np.reshape( d  , (4,4))
imp = np.matrix( do - co)
print imp


