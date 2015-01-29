# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 13:51:48 2014

@author: Nova
"""

import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.optimize    as optimization
from   scipy     import interpolate
from   itertools import izip
from   scipy     import stats
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
hydro  = np.array(map(float, hydro))
errfe  = np.array(map(float, errfe))
errhy  = np.array(map(float, errhy))

########################################################################

layoutfile = open('Template2.txt', 'r')
read       = csv.reader(layoutfile)
LayRows    = [line for line in read]
Hbeta      = []
Hbetao     = []
Hbetap     = []
layFe5270  = []
Z_2_32     = []
Z_1_71     = []
Z_1_31     = []
Z_0_71     = []
Z_0_40     = []
Z_0_00     = []
Z_0_22     = []
met        = []
age        = []
for j in xrange(len(LayRows)):
    met.append(LayRows[j][0][:-7])
    age.append(LayRows[j][0][14:])
    Hbeta.append(LayRows[j][18])
    Hbetao.append(LayRows[j][19])
    Hbetap.append(LayRows[j][20])
    layFe5270.append(LayRows[j][28])

metal     = np.array(met)
AGE       = np.array(age)
Hbeta     = np.array(map(float, Hbeta))
Hbetao    = np.array(map(float, Hbetao))
Hbetap    = np.array(map(float, Hbetap))
layFe5270 = np.array(map(float, layFe5270))

#Z_2_32 = np.where(metal == 'Mun1.30Zm2.32T')
#Z_1_71 = np.where(metal == 'Mun1.30Zm1.71T')
#Z_1_31 = np.where(metal == 'Mun1.30Zm1.31T')
Z_0_71 = np.where(metal == 'Mun1.30Zm0.71T')
Z_0_40 = np.where(metal == 'Mun1.30Zm0.40T')
Z_0_00 = np.where(metal == 'Mun1.30Zp0.00T')
Z_0_22 = np.where(metal == 'Mun1.30Zp0.22T')

#a = np.where(AGE == '00.0631')
#b = np.where(AGE == '00.0708')
#c = np.where(AGE == '00.0794')
#d = np.where(AGE == '00.0891')
#e = np.where(AGE == '00.1000')
#f = np.where(AGE == '00.1122')
#g = np.where(AGE == '00.1259')
#h = np.where(AGE == '00.1413')
#i = np.where(AGE == '00.1585')
#j = np.where(AGE == '00.1778')
#k = np.where(AGE == '00.1995')
#l = np.where(AGE == '00.2239')
#m = np.where(AGE == '00.2512')
#n = np.where(AGE == '00.2818')
#o = np.where(AGE == '00.3162')
#p = np.where(AGE == '00.3548')
#q = np.where(AGE == '00.3981')
#r = np.where(AGE == '00.4467')
#s = np.where(AGE == '00.5012')
#t = np.where(AGE == '00.5623')
#u = np.where(AGE == '00.6310')
#v = np.where(AGE == '00.7079')
#w = np.where(AGE == '00.7943')
#x = np.where(AGE == '00.8913')
#y = np.where(AGE == '01.0000')
#z = np.where(AGE == '01.1220')
#aa = np.where(AGE == '01.2589')
#ba = np.where(AGE == '01.4125')
#ca = np.where(AGE == '01.5849')
#da = np.where(AGE == '01.7783')
#ea = np.where(AGE == '01.9953')
#fa = np.where(AGE == '02.2387')
#ga = np.where(AGE == '02.5119')
#ha = np.where(AGE == '02.8184')
#ia = np.where(AGE == '03.1623')
#ja = np.where(AGE == '03.5481')
#ka = np.where(AGE == '03.9811')
#la = np.where(AGE == '04.4668')
#ma = np.where(AGE == '05.0119')
#na = np.where(AGE == '05.6234')
oa = np.where(AGE == '06.3096')
pa = np.where(AGE == '07.0795')
qa = np.where(AGE == '07.9433')
ra = np.where(AGE == '08.9125')
sa = np.where(AGE == '10.0000')
ta = np.where(AGE == '11.2202')
ua = np.where(AGE == '12.5893')
va = np.where(AGE == '14.1254')
wa = np.where(AGE == '15.8489')
xa = np.where(AGE == '17.7828')
zz = np.where((AGE == '06.3096') | (AGE == '07.0795') | (AGE == '07.9433')
            | (AGE == '08.9125') | (AGE == '10.0000') | (AGE == '11.2202')
            | (AGE == '12.5893') | (AGE == '14.1254') | (AGE == '15.8489')
            | (AGE == '17.7828'))

########################################################################

print "Showin Sesame"
plt.xlabel("Fe 5270")
plt.ylabel("H Beta")

#plt.plot(layFe5270[a],Hbeta[a], c='k',marker='o')
#plt.plot(layFe5270[b],Hbeta[b], c='k',marker='o')
#plt.plot(layFe5270[c],Hbeta[c], c='k',marker='o')
#plt.plot(layFe5270[d],Hbeta[d], c='k',marker='o')
#plt.plot(layFe5270[e],Hbeta[e], c='k',marker='o')
#plt.plot(layFe5270[f],Hbeta[f], c='k',marker='o')
#plt.plot(layFe5270[g],Hbeta[g], c='k',marker='o')
#plt.plot(layFe5270[h],Hbeta[h], c='k',marker='o')
#plt.plot(layFe5270[i],Hbeta[i], c='k',marker='o')
#plt.plot(layFe5270[j],Hbeta[j], c='k',marker='o')
#plt.plot(layFe5270[k],Hbeta[k], c='k',marker='o')
#plt.plot(layFe5270[l],Hbeta[l], c='k',marker='o')
#plt.plot(layFe5270[m],Hbeta[m], c='k',marker='o')
#plt.plot(layFe5270[n],Hbeta[n], c='k',marker='o')
#plt.plot(layFe5270[o],Hbeta[o], c='k',marker='o')
#plt.plot(layFe5270[p],Hbeta[p], c='k',marker='o')
#plt.plot(layFe5270[q],Hbeta[q], c='k',marker='o')
#plt.plot(layFe5270[r],Hbeta[r], c='k',marker='o')
#plt.plot(layFe5270[s],Hbeta[s], c='k',marker='o')
#plt.plot(layFe5270[t],Hbeta[t], c='k',marker='o')
#plt.plot(layFe5270[u],Hbeta[u], c='k',marker='o')
#plt.plot(layFe5270[v],Hbeta[v], c='k',marker='o')
#plt.plot(layFe5270[w],Hbeta[w], c='k',marker='o')
#plt.plot(layFe5270[x],Hbeta[x], c='k',marker='o')
#plt.plot(layFe5270[y],Hbeta[y], c='k',marker='o')
#plt.plot(layFe5270[z],Hbeta[z], c='k',marker='o')
#plt.plot(layFe5270[aa],Hbeta[aa], c='k',marker='o')
#plt.plot(layFe5270[ba],Hbeta[ba], c='k',marker='o')
#plt.plot(layFe5270[ca],Hbeta[ca], c='k',marker='o')
#plt.plot(layFe5270[da],Hbeta[da], c='k',marker='o')
#plt.plot(layFe5270[ea],Hbeta[ea], c='k',marker='o')
#plt.plot(layFe5270[fa],Hbeta[fa], c='k',marker='o')
#plt.plot(layFe5270[ga],Hbeta[ga], c='k',marker='o')
#plt.plot(layFe5270[ha],Hbeta[ha], c='k',marker='o')
#plt.plot(layFe5270[ia],Hbeta[ia], c='k',marker='o')
#plt.plot(layFe5270[ja],Hbeta[ja], c='k',marker='o')
#plt.plot(layFe5270[ka],Hbeta[ka], c='k',marker='o')
#plt.plot(layFe5270[la],Hbeta[la], c='k',marker='o')
#plt.plot(layFe5270[ma],Hbeta[ma], c='k',marker='o')
#plt.plot(layFe5270[na],Hbeta[na], c='k',marker='o')
plt.plot(layFe5270[oa][-4:],Hbeta[oa][-4:], c='k',marker='o')
plt.plot(layFe5270[pa][-4:],Hbeta[pa][-4:], c='k',marker='o')
plt.plot(layFe5270[qa][-4:],Hbeta[qa][-4:], c='k',marker='o')
plt.plot(layFe5270[ra][-4:],Hbeta[ra][-4:], c='k',marker='o')
plt.plot(layFe5270[sa][-4:],Hbeta[sa][-4:], c='k',marker='o')
plt.plot(layFe5270[ta][-4:],Hbeta[ta][-4:], c='k',marker='o')
plt.plot(layFe5270[ua][-4:],Hbeta[ua][-4:], c='k',marker='o')
plt.plot(layFe5270[va][-4:],Hbeta[va][-4:], c='k',marker='o')
plt.plot(layFe5270[wa][-4:],Hbeta[wa][-4:], c='k',marker='o')
plt.plot(layFe5270[xa][-4:],Hbeta[xa][-4:], c='k',marker='o')

#plt.plot(np.sort(layFe5270[zz][-40:]),Hbeta[zz][-40:], c='c',marker='o')
### AGE -> ta ua va wa xa
### met -> Z_0_40, Z_0_00

#plt.plot(layFe5270[Z_2_32],Hbeta[Z_2_32],label = "[M/H] = -2.32", c='k',marker='o')
#plt.plot(layFe5270[Z_1_71],Hbeta[Z_1_71],label = "[M/H] = -1.71", c='r',marker='o')
#plt.plot(layFe5270[Z_1_31],Hbeta[Z_1_31],label = "[M/H] = -1.31",c='y',marker='o')
plt.plot(layFe5270[Z_0_71][-10:],Hbeta[Z_0_71][-10:],label = "[M/H] = -0.71",c='g',marker='o')
plt.plot(layFe5270[Z_0_40][-10:],Hbeta[Z_0_40][-10:],label = "[M/H] = -0.40",c='b',marker='o')
plt.plot(layFe5270[Z_0_00][-10:],Hbeta[Z_0_00][-10:],label = "[M/H] =  0.00",c='c',marker='o')
plt.plot(layFe5270[Z_0_22][-10:],Hbeta[Z_0_22][-10:],label = "[M/H] =  0.22",c='m',marker='o')

plt.errorbar(fe5270[109],hydro[109],errfe[109], errhy[109],
             ecolor="k", marker=None,linestyle="None")                 
plt.scatter(fe5270[109],hydro[109],c='k',marker='D')

l = plt.legend(prop = {'family' : 'serif'},loc=1)
l.draw_frame(False)
#plt.show()

########################################################################
#poly = np.polyfit(layFe5270[zz][-40:], Hbeta[zz][-40:], 4, rcond=None, full=False, w=None, cov=False)
#print poly([fe5270[109],hydro[109]])
"""
AGE   = np.array([11.2202, 12.5893, 14.1254, 15.8489, 17.7828]) 
METAL = np.array([ -0.40, 0.00, 0.22])
Fe = np.array([[ 2.6893,  3.5985,  4.0714], 
               [ 2.7176,  3.6732,  4.1542], 
               [ 2.7539,  3.7121,  4.2214],
               [ 2.7782,  3.7663,  4.2407], 
               [ 2.847,   3.7911,  4.2873]])

# Hbeta is a grid of the line strengths of H_beta
Hbeta = np.array([[ 1.8472,  1.71,    1.6324],
                  [ 1.7714,  1.6365,  1.5464],
                  [ 1.7349,  1.5615,  1.4515],
                  [ 1.6855,  1.5024,  1.3957],
                  [ 1.6596,  1.4307,  1.3054]])
                  
xknots = np.array([0,1,2,3,4]) 
yknots = np.array([0,1,2])                 
                  
LS = interpolate.LSQBivariateSpline(Fe, Hbeta, AGE, xknots, yknots, w=None, kx=2, ky=2, eps=None)
print LS
#Fe    = np.array([[ 2.6893, 2.7176, 2.7539, 2.7782, 2.8470], 
#                  [ 3.5985, 3.6732, 3.7121, 3.7663, 3.7911]])
#Hbeta = np.array([[ 1.8472, 1.7714, 1.7349, 1.6855, 1.6596],  
#                  [ 1.7100, 1.6365, 1.5615, 1.5024, 1.4307]])   
#Fe = np.array([[ 2.6893,  3.5985], 
#               [ 2.7176,  3.6732], 
#               [ 2.7539,  3.7121],
#               [ 2.7782,  3.7663], 
#               [ 2.847,   3.7911]])
               
#Hbeta = np.array([[ 1.8472,  1.7100],
#                  [ 1.7714,  1.6365],
#                  [ 1.7349,  1.5615],
#                  [ 1.6855,  1.5024],
#                  [ 1.6596,  1.4307]])
"""

Fe = np.array([layFe5270[Z_0_40][-5:],layFe5270[Z_0_00][-5:]])
Hb = np.array([Hbeta[Z_0_40][-5:]    ,Hbeta[Z_0_00][-5:]    ])
   
#sigma = np.array([[ 0.0, 0.0, 0.0, 0.0, 0.0], 
#                  [ 0.0, 0.0, 0.0, 0.0, 0.0]])           


#print Fe*Hb

xp = np.linspace(2.5, 4.0, 100)

z = np.polyfit(layFe5270[Z_0_40][-5:],Hbeta[Z_0_40][-5:] , 1)
p = np.poly1d(z)

a = np.polyfit(layFe5270[Z_0_00][-5:],Hbeta[Z_0_00][-5:] , 1)
b = np.poly1d(a)

c = np.polyfit(layFe5270[ta][-3:],Hbeta[ta][-3:], 1)
d = np.poly1d(c)

e = np.polyfit(layFe5270[ua][-3:],Hbeta[ua][-3:], 1)
f = np.poly1d(e)

g = np.polyfit(layFe5270[va][-3:],Hbeta[va][-3:], 1)
h = np.poly1d(g)

i = np.polyfit(layFe5270[wa][-3:],Hbeta[wa][-3:], 1)
j = np.poly1d(i)

k = np.polyfit(layFe5270[xa][-3:],Hbeta[xa][-3:], 1)
l = np.poly1d(k)

plt.plot(Fe, Hb, '.', xp, p(xp))
plt.plot(Fe, Hb, '.', xp, b(xp))
plt.plot(Fe, Hb, '.', xp, d(xp))
#plt.plot(Fe, Hb, '.', xp, f(xp))
#plt.plot(Fe, Hb, '.', xp, h(xp))
#plt.plot(Fe, Hb, '.', xp, j(xp))
plt.plot(Fe, Hb, '.', xp, l(xp))
#xp = np.linspace(2.5, 4.0, 100)
#Fe = np.array([2.6893, 2.7176, 2.7539, 2.7782, 2.8470, 3.5985, 3.6732, 3.7121, 3.7663, 3.7911])
#Hb = np.array([1.8472, 1.7714, 1.7349, 1.6855, 1.6596, 1.7100, 1.6365, 1.5615, 1.5024, 1.4307])
#z  = np.polyfit(Fe, Hb, 4)
#p  = np.poly1d(z)   
#plt.plot(Fe, Hb, '.', xp, p(xp))
plt.show()