# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 13:51:48 2014

@author: Nova
"""

import numpy as np
import csv
import matplotlib.pyplot as plt

########################################################################

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

########################################################################

layoutfile = open('Template2.txt', 'r')
read  = csv.reader(layoutfile)
LayRows = [line for line in read]
name      = []
Hbeta     = []
Hbetao    = []
Hbetap    = []
layFe5270 = []
Z_2_32 = []
Z_1_71 = []
Z_1_31 = []
Z_0_71 = []
Z_0_40 = []
Z_0_00 = []
Z_0_22 = []
met    = []
age    = []
for j in xrange(len(LayRows)):
    #name.append(LayRows[j][0])
    met.append(LayRows[j][0][:-7])
    age.append(LayRows[j][0][14:])
    Hbeta.append(LayRows[j][18])
    Hbetao.append(LayRows[j][19])
    Hbetap.append(LayRows[j][20])
    layFe5270.append(LayRows[j][28])


metal     = np.array(met)
Hbeta     = np.array(map(float, Hbeta))
Hbetao    = np.array(map(float, Hbetao))
Hbetap    = np.array(map(float, Hbetap))
layFe5270 = np.array(map(float, layFe5270))

#print metal[np.where(metal == 'Mun1.30Zp0.00T')]
Z_2_32 = np.where(metal == 'Mun1.30Zm2.32T')
Z_1_71 = np.where(metal == 'Mun1.30Zm1.71T')
Z_1_31 = np.where(metal == 'Mun1.30Zm1.31T')
Z_0_71 = np.where(metal == 'Mun1.30Zm0.71T')
Z_0_40 = np.where(metal == 'Mun1.30Zm0.40T')
Z_0_00 = np.where(metal == 'Mun1.30Zp0.00T')
Z_0_22 = np.where(metal == 'Mun1.30Zp0.22T')

#print metal[Z_0_22]
#print layFe5270[Z_0_22]

#Z_2_32 = np.where(name[0:6] == '2.32')
#Z_1_71 = np.where(name[0:23] == '1.71')
#Z_1_31 = np.where(name[24:47] == '1.31')
#Z_0_71 = np.where(name[48:72] == '0.71')
#Z_0_40 = np.where(name[73:97] == '0.40')
#Z_0_00 = np.where(name[98:123] == '0.00')
#Z_0_22 = np.where(name[124:147] == '0.22')

#print layFe5270[Z_1_71]
#print layFe5270[Z_1_31]
#print layFe5270[Z_0_71]
#print layFe5270[Z_0_40]
#print layFe5270[Z_0_00]
#print layFe5270[Z_0_22]

#Hbeta     = np.array(map(float, Hbeta))
#Hbetao    = np.array(map(float, Hbetao))
#Hbetap    = np.array(map(float, Hbetap))
#layFe5270 = np.array(map(float, layFe5270))

########################################################################


print "Showin Sesame"
plt.xlabel("Fe 5270")
plt.ylabel("H Beta")
#plt.errorbar(fe5270[real],hydro[real],errfe[real], errhy[real],
#             ecolor="k", marker=None,linestyle="None") 
#plt.scatter(fe5270,hydro,c='k')
#plt.plot(layFe5270,Hbeta,c='k')
plt.plot(layFe5270[Z_2_32],Hbeta[Z_2_32],label = "[M/H] = -2.32", c='k',marker='o')
plt.plot(layFe5270[Z_1_71],Hbeta[Z_1_71],label = "[M/H] = -1.71", c='r',marker='o')
plt.plot(layFe5270[Z_1_31],Hbeta[Z_1_31],label = "[M/H] = -1.31",c='y',marker='o')
plt.plot(layFe5270[Z_0_71],Hbeta[Z_0_71],label = "[M/H] = -0.71",c='g',marker='o')
plt.plot(layFe5270[Z_0_40],Hbeta[Z_0_40],label = "[M/H] = -0.40",c='b',marker='o')
plt.plot(layFe5270[Z_0_00],Hbeta[Z_0_00],label = "[M/H] = 0.00",c='c',marker='o')
plt.plot(layFe5270[Z_0_22],Hbeta[Z_0_22],label = "[M/H] = 0.22",c='m',marker='o')


#plt.plot(layFe5270[0:5],Hbeta[0:5],label = "[M/H] = -2.32", c='k',marker='o')
#plt.plot(layFe5270[6:53],Hbeta[6:53],label = "[M/H] = -1.71", c='r',marker='o')
#plt.plot(layFe5270[54:103],Hbeta[54:103],label = "[M/H] = -1.31",c='y',marker='o')
#plt.plot(layFe5270[104:153],Hbeta[104:153],label = "[M/H] = -0.71",c='g',marker='o')
#plt.plot(layFe5270[154:203],Hbeta[154:203],label = "[M/H] = -0.40",c='b',marker='o')
#plt.plot(layFe5270[204:254],Hbeta[204:254],label = "[M/H] = 0.00",c='c',marker='o')
#plt.plot(layFe5270[255:303],Hbeta[255:303],label = "[M/H] = 0.22",c='m',marker='o')

#plt.plot(layFe5270[0:23],Hbeta[0:23],label = "[M/H] = -1.71", c='r',marker='o')
#plt.plot(layFe5270[24:47],Hbeta[24:47],label = "[M/H] = -1.31",c='y',marker='o')
#plt.plot(layFe5270[48:72],Hbeta[48:72],label = "[M/H] = -0.71",c='g',marker='o')
#plt.plot(layFe5270[73:97],Hbeta[73:97],label = "[M/H] = -0.40",c='b',marker='o')
#plt.plot(layFe5270[98:123],Hbeta[98:123],label = "[M/H] = 0.00",c='c',marker='o')
#plt.plot(layFe5270[124:147],Hbeta[124:147],label = "[M/H] = 0.22",c='m',marker='o')
plt.errorbar(fe5270[109],hydro[109],errfe[109], errhy[109],
             ecolor="k", marker=None,linestyle="None")                 
plt.scatter(fe5270[109],hydro[109],c='k',marker='D')

l = plt.legend(prop = {'family' : 'serif'},loc=1)
l.draw_frame(False)
plt.show()
