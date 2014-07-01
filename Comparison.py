# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 09:11:48 2014

@author: Nova
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#import glob
import pickle
import random 

params = {'legend.fontsize': 10, 
          'legend.linewidth': 2,
          'legend.font': 'serif',
          'mathtext.default': 'regular', 
          'xtick.labelsize': 10, 
          'ytick.labelsize': 10} # changes font size in the plot legend

plt.rcParams.update(params) # reset the plot parameters

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 10,
        } 
#####################################################################

d = []
name = 'Z017Y26.dat'
d.append(np.loadtxt(name))
d = np.array(d)

#print d
#print np.shape(d) #(1L, 16776L, 21L)

logAGE = []
F435W  = []
F555W  = []
F625W  = []
F814W  = []

logAGE = d[:,:,0]
F435W  = d[:,:,7]
F555W  = d[:,:,10]
F625W  = d[:,:,12]
F814W  = d[:,:,16]

age70   = np.where((d[:,:,0] == 7.0))
age71   = np.where((d[:,:,0] == 7.1))
age72   = np.where((d[:,:,0] == 7.2))
age73   = np.where((d[:,:,0] == 7.3))
age74   = np.where((d[:,:,0] == 7.4))
age75   = np.where((d[:,:,0] == 7.5))
age76   = np.where((d[:,:,0] == 7.6))
age77   = np.where((d[:,:,0] == 7.7))
age78   = np.where((d[:,:,0] == 7.8))
age79   = np.where((d[:,:,0] == 7.9))
age80   = np.where((d[:,:,0] == 8.0))

age7    = np.where((d[:,:,0] >= 7.0)  & (d[:,:,0] < 8.5))
age758  = np.where((d[:,:,0] >= 7.5)  & (d[:,:,0] < 8.0))
age8    = np.where((d[:,:,0] >= 8.0)  & (d[:,:,0] < 9.0))
age9    = np.where((d[:,:,0] >= 9.0)  & (d[:,:,0] < 10.0))
age10   = np.where((d[:,:,0] >= 10.0) & (d[:,:,0] < 10.3))
age103  = np.where((d[:,:,0] == 10.3))

#####################################################################
start      = 0 # starts at S/N 4
end        = 2 # ends at S/N 5
snt        = 4
snb        = 4
f435f555_1 = []
f625f814_1 = []
f435f555_2 = []
f625f814_2 = []

"""
title      = 'SN08ge'
radius     = [36.1008,46.0927]
ytopmax    = -2.0
ytopmin    = -9.0
ybotmax    = -3.0
ybotmin    = -9.0
for i in range(4,9):
    f435f555_1.append(pickle.load(open('sn2008ge_f435f555_r1_'+ str(i) +'.p', 'rb')))    
    f625f814_1.append(pickle.load(open('sn2008ge_f625f814_r1_'+ str(i) +'.p', 'rb')))    
    f435f555_2.append(pickle.load(open('sn2008ge_f435f555_r2_'+ str(i) +'.p', 'rb')))    
    f625f814_2.append(pickle.load(open('sn2008ge_f625f814_r2_'+ str(i) +'.p', 'rb')))

"""
#"""

title      = 'SN08ha'
radius     = [32.4, 41.25]
ytopmax    = -2.0
ytopmin    = -8.0
ybotmax    = -2.0
ybotmin    = -9.0
for i in range(4,9):
    f435f555_1.append(pickle.load(open('sn2008ha_f435f555_r1_'+ str(i) +'.p', 'rb')))    
    f625f814_1.append(pickle.load(open('sn2008ha_f625f814_r1_'+ str(i) +'.p', 'rb')))    
    f435f555_2.append(pickle.load(open('sn2008ha_f435f555_r2_'+ str(i) +'.p', 'rb')))    
    f625f814_2.append(pickle.load(open('sn2008ha_f625f814_r2_'+ str(i) +'.p', 'rb')))
#"""
"""  
f435f555_4   = pickle.load(open( "sn2008ha_f435f555_r1_4.p", "rb" ))
f625f814_4   = pickle.load(open( "sn2008ha_f625f814_r1_4.p", "rb" ))
f435f555_5   = pickle.load(open( "sn2008ha_f435f555_r1_5.p", "rb" ))
f625f814_5   = pickle.load(open( "sn2008ha_f625f814_r1_5.p", "rb" ))
f435f555_4_2 = pickle.load(open( "sn2008ha_f435f555_r2_4.p", "rb" ))
f625f814_4_2 = pickle.load(open( "sn2008ha_f625f814_r2_4.p", "rb" ))
f435f555_5_2 = pickle.load(open( "sn2008ha_f435f555_r2_5.p", "rb" ))
f625f814_5_2 = pickle.load(open( "sn2008ha_f625f814_r2_5.p", "rb" ))  
#f435f555_3 = pickle.load(open( "sn2008ha_f435f555.p"  , "rb" ))
#f625f814_3 = pickle.load(open( "sn2008ha_f625f814.p"  , "rb" ))
f435f555_4 = pickle.load(open( "sn2008ha_f435f555_r1_4.p", "rb" ))
f625f814_4 = pickle.load(open( "sn2008ha_f625f814_r1_4.p", "rb" ))
f435f555_5 = pickle.load(open( "sn2008ha_f435f555_r1_5.p", "rb" ))
f625f814_5 = pickle.load(open( "sn2008ha_f625f814_r1_5.p", "rb" ))
f435f555_6 = pickle.load(open( "sn2008ha_f435f555_r1_6.p", "rb" ))
f625f814_6 = pickle.load(open( "sn2008ha_f625f814_r1_6.p", "rb" ))
f435f555_7 = pickle.load(open( "sn2008ha_f435f555_r1_7.p", "rb" ))
f625f814_7 = pickle.load(open( "sn2008ha_f625f814_r1_7.p", "rb" ))
f435f555_8 = pickle.load(open( "sn2008ha_f435f555_r1_8.p", "rb" ))
f625f814_8 = pickle.load(open( "sn2008ha_f625f814_r1_8.p", "rb" ))


f435f555_4_2 = pickle.load(open( "sn2008ha_f435f555_r2_4.p", "rb" ))
f625f814_4_2 = pickle.load(open( "sn2008ha_f625f814_r2_4.p", "rb" ))
f435f555_5_2 = pickle.load(open( "sn2008ha_f435f555_r2_5.p", "rb" ))
f625f814_5_2 = pickle.load(open( "sn2008ha_f625f814_r2_5.p", "rb" ))
f435f555_6_2 = pickle.load(open( "sn2008ha_f435f555_r2_6.p", "rb" ))
f625f814_6_2 = pickle.load(open( "sn2008ha_f625f814_r2_6.p", "rb" ))
f435f555_7_2 = pickle.load(open( "sn2008ha_f435f555_r2_7.p", "rb" ))
f625f814_7_2 = pickle.load(open( "sn2008ha_f625f814_r2_7.p", "rb" ))
f435f555_8_2 = pickle.load(open( "sn2008ha_f435f555_r2_8.p", "rb" ))
f625f814_8_2 = pickle.load(open( "sn2008ha_f625f814_r2_8.p", "rb" ))
"""

"""
title      = 'SN10ae'
radius     = [49.4712,62.9816]
ytopmax    = -1.0
ytopmin    = -11.0
ybotmax    = -4.0
ybotmin    = -9.0
for i in range(4,9):
    f435f555_1.append(pickle.load(open('sn2010ae_f435f555_r1_'+ str(i) +'.p', 'rb')))    
    f625f814_1.append(pickle.load(open('sn2010ae_f625f814_r1_'+ str(i) +'.p', 'rb')))    
    f435f555_2.append(pickle.load(open('sn2010ae_f435f555_r2_'+ str(i) +'.p', 'rb')))    
    f625f814_2.append(pickle.load(open('sn2010ae_f625f814_r2_'+ str(i) +'.p', 'rb')))

"""
"""
title      = 'SN10el'
radius     = [65.0016,82.7545]
ytopmax    = -1.0
ytopmin    = -6.0
ybotmax    = -1.0
ybotmin    = -6.0
for i in range(4,9):
    f435f555_1.append(pickle.load(open('sn2010el_f435f555_r1_'+ str(i) +'.p', 'rb')))    
    f625f814_1.append(pickle.load(open('sn2010el_f625f814_r1_'+ str(i) +'.p', 'rb')))    
    f435f555_2.append(pickle.load(open('sn2010el_f435f555_r2_'+ str(i) +'.p', 'rb')))    
    f625f814_2.append(pickle.load(open('sn2010el_f625f814_r2_'+ str(i) +'.p', 'rb')))
"""
#####################################################################

print "Begin plotting Isochrones..."
h = [2, 5] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)
#plots = plt.subplot(gs[0])

c1plt = plt.subplot2grid((2,2), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W",fontdict = font)
plt.ylabel("F555W",fontdict = font)
    
#c1plt.plot(np.subtract(F435W[age70],  F555W[age70]),  F555W[age70],  
#           'r--', label = 'Log(Age) = 7.0')
#c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
#           'y-', label = 'Log(Age) = 7.1')
#c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
#           'g:', label = 'Log(Age) = 7.2')
#c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
#           'c-', label = 'Log(Age) = 7.3')
c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Log(Age) = 7.6')
#c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
#           'y-' , label = 'Log(Age) = 7.7')
#c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
#           'g:' , label = 'Log(Age) = 7.8')
#c1plt.plot(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  
#           'c-.', label = 'Log(Age) = 7.9') 
#c1plt.plot(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  
#           'b:' , label = 'Log(Age) = 8.0')  
#c1plt.plot(np.subtract(F435W[age10],  F555W[age10]),  F555W[age10],  
#           label = 'Log(Age) >= 10.0 & < 10.3',c="y")#,marker='o')
#c1plt.plot(np.subtract(F435W[age103], F555W[age103]), F555W[age103], 
#           label = 'Log(Age) == 10.3 & < 7.5', c="r")#,marker='o')
###########################################################################

for i in range(start,end):
        c1plt.errorbar(np.subtract(f435f555_1[i][0],   f435f555_1[i][1]),   f435f555_1[i][1], 
                       f435f555_1[i][2],   f435f555_1[i][3], fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_1[i][0],   f435f555_1[i][1]),   f435f555_1[i][1],   
                      label = 'S/N ' + str(snt) +' Radius ' + str(radius[0]),  c=random.choice(['w','g', 'r', 'c', 'm', 'b', 'k']),marker='D')
        c1plt.errorbar(np.subtract(f435f555_2[i][0],   f435f555_2[i][1]),   f435f555_2[i][1], 
                      f435f555_2[i][2],   f435f555_2[i][3], fmt=None, marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_2[i][0],   f435f555_2[i][1]),   f435f555_2[i][1],
                      label = 'S/N ' + str(snt) +' Radius ' + str(radius[1]),  c=random.choice(['w','g', 'r', 'c', 'm', 'b', 'k']),marker='D')
        snt += 1


"""
print np.shape(f435f555_1)
print np.shape(f435f555_1[0])
print np.shape(f435f555_1[1])
print np.shape(f435f555_1[2])
print np.shape(f435f555_1[3])
print np.shape(f435f555_1[4])
print np.shape(f435f555_2)
print np.shape(f435f555_2[0])
print np.shape(f435f555_2[1][0])
print np.shape(f435f555_2[1])
print np.shape(f435f555_2[2])
print np.shape(f435f555_2[3])
print np.shape(f435f555_2[4])
c1plt.errorbar(np.subtract(f435f555_1[0][0],   f435f555_1[0][1]),   f435f555_1[0][1], 
              f435f555_1[0][2],   f435f555_1[0][3], fmt=None, ecolor="b", marker=None, mew=0 )
c1plt.scatter(np.subtract(f435f555_1[0][0],   f435f555_1[0][1]),   f435f555_1[0][1],   
              label = 'S/N 4, Radius ' + str(radius[0]),  c="w",marker='D')
c1plt.errorbar(np.subtract(f435f555_1[1][0],   f435f555_1[1][1]),   f435f555_1[1][1], 
              f435f555_1[1][2],   f435f555_1[1][3], fmt=None, ecolor="b", marker=None, mew=0 )
c1plt.scatter(np.subtract(f435f555_1[1][0],   f435f555_1[1][1]),   f435f555_1[1][1],   
              label = 'S/N 5, Radius ' + str(radius[0]),  c="b",marker='D')

c1plt.errorbar(np.subtract(f435f555_2[0][0],   f435f555_2[0][1]),   f435f555_2[0][1], 
              f435f555_2[0][2],   f435f555_2[0][3], fmt=None, ecolor="k", marker=None, mew=0 )
c1plt.scatter(np.subtract(f435f555_2[0][0],   f435f555_2[0][1]),   f435f555_2[0][1],   
              label = 'S/N 4, Radius ' + str(radius[1]),  c="w",marker='D')
c1plt.errorbar(np.subtract(f435f555_2[1][0],   f435f555_2[1][1]),   f435f555_2[1][1], 
              f435f555_2[1][2],   f435f555_2[1][3], fmt=None, ecolor="k", marker=None, mew=0 )
c1plt.scatter(np.subtract(f435f555_2[1][0],   f435f555_2[1][1]),   f435f555_2[1][1],   
              label = 'S/N 5, Radius ' + str(radius[1]),  c="b",marker='D')
"""
#c1plt.errorbar(np.subtract(f435f555_8[0],   f435f555_8[1]),   f435f555_8[1], 
#              f435f555_8[2],   f435f555_8[3], fmt=None, ecolor="b", marker=None, mew=0 )
#c1plt.scatter(np.subtract(f435f555_8[0],   f435f555_8[1]),   f435f555_8[1],   
#              label = 'S/N 8, Radius ' + radius,  c="w",marker='D')
###########################################################################              
#####c1plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.1)
#c1plt.legend(loc=4, borderaxespad=0.)
#c1plt.legend(bbox_to_anchor=(.85, .7), loc=2, borderaxespad=0.)
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c1plt.set_ylim(bottom=ytopmax, top=ytopmin)
###########################################################################

plt.title(title + ': CMD for Z = 0.' + name[1:-7] + ', Y = 0.' + name[5:-4],
          fontdict = font)

###########################################################################
c2plt = plt.subplot2grid((2,2), (1,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F625W - F814W",fontdict = font)
plt.ylabel("F625W",fontdict = font)
#c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
#           'r--', label = 'Log(Age) = 7.0')
#c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
#           'y-', label = 'Log(Age) = 7.1')
#c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
#           'g:', label = 'Log(Age) = 7.2')
#c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
#           'c-', label = 'Log(Age) = 7.3')
c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Log(Age) = 7.6')
#c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
#           'y-' , label = 'Log(Age) = 7.7')
#c2plt.plot(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  
#           'g:' , label = 'Log(Age) = 7.8')
#c2plt.plot(np.subtract(F625W[age79],  F814W[age79]),  F814W[age79],  
#           'c-.', label = 'Log(Age) = 7.9') 
#c2plt.plot(np.subtract(F625W[age80],  F814W[age80]),  F814W[age80],  
#           'b:' , label = 'Log(Age) = 8.0')  
###########################################################################
           
for k in range(start,end):
        c2plt.errorbar(np.subtract(f625f814_1[k][0],   f625f814_1[k][1]),   f625f814_1[k][1], 
                       f625f814_1[k][2],   f625f814_1[k][3], fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_1[k][0],   f625f814_1[k][1]),   f625f814_1[k][1],   
                      label = 'S/N ' + str(snb) +' Radius ' + str(radius[0]),  c=random.choice(['w','g', 'r', 'c', 'm', 'b', 'k']),marker='D')
        c2plt.errorbar(np.subtract(f625f814_2[k][0],   f625f814_2[k][1]),   f625f814_2[k][1], 
                      f625f814_2[k][2],   f625f814_2[k][3], fmt=None, marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_2[k][0],   f625f814_2[k][1]),   f625f814_2[k][1],
                      label = 'S/N ' + str(snb) +' Radius ' + str(radius[1]),  c=random.choice(['w','g', 'r', 'c', 'm', 'b', 'k']),marker='D')
        snb += 1
"""
c2plt.errorbar(np.subtract(f625f814_4_2[0],   f625f814_4_2[1]),   f625f814_4_2[1], 
              f625f814_4_2[2],   f625f814_4_2[3], fmt=None, ecolor="b", marker=None, mew=0 )
c2plt.scatter(np.subtract(f625f814_4[0],   f625f814_4[1]),   f625f814_4[1],   
              label = 'S/N 4, Radius ' + str(radius),  c="w",marker='D')
c2plt.errorbar(np.subtract(f625f814_5_2[0],   f625f814_5_2[1]),   f625f814_5_2[1], 
              f625f814_5_2[2],   f625f814_5_2[3], fmt=None, marker=None, mew=0 )
c2plt.scatter(np.subtract(f625f814_5_2[0],   f625f814_5_2[1]),   f625f814_5_2[1], 
              label = 'S/N 5, Radius ' + str(radius),  c="b",marker='D')
"""
#c2plt.errorbar(np.subtract(f625f814_6[0],   f625f814_6[1]),   f625f814_6[1], 
#              f625f814_6[2],   f625f814_6[3], fmt=None, marker=None, mew=0 )
#c2plt.scatter(np.subtract(f625f814_6[0],   f625f814_6[1]),   f625f814_6[1],   
#              label = 'S/N 6, Radius ' + radius,  c="w",marker='D')
#c2plt.errorbar(np.subtract(f625f814_7[0],   f625f814_7[1]),   f625f814_7[1], 
#              f625f814_7[2],   f625f814_7[3], fmt=None, marker=None, mew=0 )
#c2plt.scatter(np.subtract(f625f814_7[0],   f625f814_7[1]),   f625f814_7[1],   
#              label = 'S/N 7, Radius ' + radius,  c="w",marker='D')
#c2plt.errorbar(np.subtract(f625f814_8[0],   f625f814_8[1]),   f625f814_8[1], 
#              f625f814_8[2],   f625f814_8[3], fmt=None, marker=None, mew=0 )
#c2plt.scatter(np.subtract(f625f814_8[0],   f625f814_8[1]),   f625f814_8[1],   
#              label = 'S/N 8, Radius ' + radius,  c="w",marker='D')
###########################################################################
#c2plt.plot(np.subtract(F625W[age7],   F814W[age7]),   F814W[age7],   
#              label = 'Log(Age) >= 7.0 & < 7.5',  c="w")#,marker='o')
#c2plt.plot(np.subtract(F625W[age758],  F814W[age758]),  F814W[age758],  
#              label = 'Log(Age) >= 7.5 & < 8.0',  c="m",marker='o' )
#c2plt.plot(np.subtract(F625W[age8],   F814W[age8]),   F814W[age8],   
#              label = 'Log(Age) >= 8.0 & < 9.0',  c="b")#,marker='o')
#c2plt.plot(np.subtract(F625W[age9],   F814W[age9]),   F814W[age9],   
#              label = 'Log(Age) >= 9.0 & < 10.0', c="g")#,marker='o')
#c2plt.plot(np.subtract(F625W[age10],  F814W[age10]),  F814W[age10],  
#              label = 'Log(Age) >= 10.0 & < 10.3',c="y")#,marker='o')
#c2plt.plot(np.subtract(F625W[age103], F814W[age103]), F814W[age103], 
#              label = 'Log(Age) == 10.3 & < 7.5', c="r")#,marker='o')
###########################################################################
#c2plt.legend(loc=4, borderaxespad=0.)
#c2plt.legend(bbox_to_anchor=(.85, .7), loc=2, borderaxespad=0.)
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c2plt.set_ylim(bottom=ybotmax, top=ybotmin) 
########################################################################### 

print "Save and show plot : " + title + '_' + 'Z' + name[1:-7]+ '_Comparison.png'

plt.savefig(title + '_' + 'Z' + name[1:-7]+ '_Comparisonip.png')
