# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 13:51:48 2014

@author: Nova
"""

import numpy as np
import csv
import matplotlib.pyplot as plt


crimefile = open('Abundances.txt', 'r')
reader  = csv.reader(crimefile)
allRows = [row for row in reader]
#print np.shape(allRows)#(509L)
print "Open Sesame!"
galax  = []
hydro  = []
fe5270 = []
errhy  = []
errfe  = []
real   = []
for i in xrange(len(allRows)):
    galax.append( allRows[i][0])
    hydro.append( allRows[i][1])
    fe5270.append(allRows[i][6])
    errhy.append( allRows[i][12])
    errfe.append( allRows[i][17])
    
fe5270 = np.array(fe5270)
hydro = np.array(hydro)
errfe = np.array(errfe)
errhy = np.array(errhy) 

real = np.where(( errfe != ' nan  ') & (errhy != ' nan  ') )   

fe5270 = np.array(map(float, fe5270))
hydro = np.array(map(float, hydro))
errfe = np.array(map(float, errfe))
errhy = np.array(map(float, errhy))

#print errfe[468] 
#print type(errfe[468])
#print type(np.float64('nan'))
#print (errfe[468] == errfe[468])
#print errfe[468]
#print errhy
#real = np.where(( errfe == float('nan')) & (errhy == float('nan')) )
#real = np.where(( errfe != ' nan  ') & (errhy != ' nan  ') )
#print len(fe5270)
#print len(fe5270[real])

print "Showin Sesame"
plt.xlabel("Fe 5270")
plt.ylabel("H")
plt.errorbar(fe5270[real],hydro[real],errfe[real], errhy[real],
             ecolor="k", marker=None,linestyle="None") 
plt.scatter(fe5270,hydro,c='k')
plt.errorbar(fe5270[109],hydro[109],errfe[109], errhy[109],
             ecolor="r", marker=None,linestyle="None")                 
plt.scatter(fe5270[109],hydro[109],c='r')
plt.show()
