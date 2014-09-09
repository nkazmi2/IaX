# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 09:11:48 2014

@author: Nova
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle
from matplotlib.ticker import MultipleLocator 
from matplotlib.ticker import AutoMinorLocator
#import pylab as pl
#import glob
#import random 
#minL     = MultipleLocator(5)

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
name = 'Z020Y26.dat'
d.append(np.loadtxt('Metallicity/'+name))
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

age67   = np.where((d[:,:,0] == 6.7))
age68   = np.where((d[:,:,0] == 6.8))
age69   = np.where((d[:,:,0] == 6.9))
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

#####################################################################
start      = 0 # start = 0 starts at S/N 3
end        = 1 # end = 2 goes to S/N 4
snt        = 3
snb        = 3
radius     = [450,750,1000,1500,2200] 
f435f555_0 = []
f625f814_0 = []
f435f555_1 = []
f625f814_1 = []
f435f555_2 = []
f625f814_2 = []
f435f555_3 = []
f625f814_3 = []
f435f555_4 = []
f625f814_4 = []

""" 7.1 - > 7.4
title      = 'SN08ge'
ytopmax    = -4.0
ytopmin    = -9.0
ybotmax    = -4.0
ybotmin    = -9.0
for i in range(3,6):
    f435f555_0.append(pickle.load(open('SN2008GE/sn2008ge_f435f555_sn'+ str(i) +'_rad0.p', 'rb')))    
    f625f814_0.append(pickle.load(open('SN2008GE/sn2008ge_f625f814_sn'+ str(i) +'_rad0.p', 'rb')))    
    f435f555_1.append(pickle.load(open('SN2008GE/sn2008ge_f435f555_sn'+ str(i) +'_rad1.p', 'rb')))    
    f625f814_1.append(pickle.load(open('SN2008GE/sn2008ge_f625f814_sn'+ str(i) +'_rad1.p', 'rb')))   
    f435f555_2.append(pickle.load(open('SN2008GE/sn2008ge_f435f555_sn'+ str(i) +'_rad2.p', 'rb')))    
    f625f814_2.append(pickle.load(open('SN2008GE/sn2008ge_f625f814_sn'+ str(i) +'_rad2.p', 'rb')))  
    f435f555_3.append(pickle.load(open('SN2008GE/sn2008ge_f435f555_sn'+ str(i) +'_rad3.p', 'rb')))    
    f625f814_3.append(pickle.load(open('SN2008GE/sn2008ge_f625f814_sn'+ str(i) +'_rad3.p', 'rb')))
"""
#""" 7.4 -> 7.6
title      = 'SN08ha'
ytopmax    = -2.0
ytopmin    = -6.5
ybotmax    = -3.0
ybotmin    = -7.0
for i in range(3,6):
    f435f555_0.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_sn'+ str(i) +'_rad0.p', 'rb')))    
    f625f814_0.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_sn'+ str(i) +'_rad0.p', 'rb')))    
    f435f555_1.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_sn'+ str(i) +'_rad1.p', 'rb')))    
    f625f814_1.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_sn'+ str(i) +'_rad1.p', 'rb')))   
    f435f555_2.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_sn'+ str(i) +'_rad2.p', 'rb')))    
    f625f814_2.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_sn'+ str(i) +'_rad2.p', 'rb')))
    f435f555_3.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_sn'+ str(i) +'_rad3.p', 'rb')))    
    f625f814_3.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_sn'+ str(i) +'_rad3.p', 'rb')))
    f435f555_4.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_sn'+ str(i) +'_rad4.p', 'rb')))    
    f625f814_4.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_sn'+ str(i) +'_rad4.p', 'rb')))
#"""
""" 7.3 -> 7.7
title      = 'SN10ae'
ytopmax    = -2.5
ytopmin    = -7.0
ybotmax    = -3.0
ybotmin    = -7.5
for i in range(3,6):
    f435f555_0.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad0.p', 'rb')))    
    f625f814_0.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad0.p', 'rb')))    
    f435f555_1.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad1.p', 'rb')))    
    f625f814_1.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad1.p', 'rb')))   
    f435f555_2.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad2.p', 'rb')))    
    f625f814_2.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad2.p', 'rb')))  
    f435f555_3.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad3.p', 'rb')))    
    f625f814_3.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad3.p', 'rb')))
    f435f555_4.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad4.p', 'rb')))    
    f625f814_4.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad4.p', 'rb')))

"""
""" 7.7 -> 8.0
title      = 'SN10el'

ytopmax    = -1.5
ytopmin    = -7.0
ybotmax    = -2.0
ybotmin    = -7.5

#ytopmax    = 0.0
#ytopmin    = -9.0
#ybotmax    = -2.0
#ybotmin    = -9.0

for i in range(3,6):
    
    f435f555_0.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_rad0.p', 'rb')))    
    f625f814_0.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_rad0.p', 'rb')))    
    f435f555_1.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_rad1.p', 'rb')))    
    f625f814_1.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_rad1.p', 'rb')))   
    f435f555_2.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_rad2.p', 'rb')))    
    f625f814_2.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_rad2.p', 'rb')))
    f435f555_3.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_rad3.p', 'rb')))     
    f625f814_3.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_rad3.p', 'rb')))   
    f435f555_4.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_rad4.p', 'rb')))     
    f625f814_4.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_rad4.p', 'rb')))   
    
    #f435f555_0.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad0.p', 'rb')))    
    #f625f814_0.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad0.p', 'rb')))    
    #f435f555_1.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad1.p', 'rb')))    
    #f625f814_1.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad1.p', 'rb')))   
    #f435f555_2.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad2.p', 'rb')))    
    #f625f814_2.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad2.p', 'rb')))  
    #f435f555_3.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad3.p', 'rb')))    
    #f625f814_3.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad3.p', 'rb')))
    #f435f555_4.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad4.p', 'rb')))     
    #f625f814_4.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad4.p', 'rb')))   

#radius435555 = []
#radius625814 = []
#radius435555.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn3_red_rad4.p', 'rb')))     
#radius625814.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn3_red_rad4.p', 'rb')))   

#A435555 = (round(np.mean((radius435555[start][1]- f435f555_4[start][1])/(radius435555[start][0]-np.subtract(f435f555_4[start][0],f435f555_4[start][1]))),3))
#A625814 = (round(np.mean((radius625814[start][1]- f625f814_4[start][1])/(radius625814[start][0]-np.subtract(f625f814_4[start][0],f625f814_4[start][1]))),3))

"""

###########################################################################
print "Begin plotting Isochrones..."
h = [2, 4] # height of the plotted figure
fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

fig1.suptitle(title + ': CMD for Z = 0.' + name[1:-7] + ', Y = 0.' + name[5:-4] + ' S/N >= 3',
          fontdict = font, size=15)

###########################################################################
#plots = plt.subplot(gs[0])

#c1plt = plt.subplot2grid((2,2), (0,0), colspan = 2)
c1plt = plt.subplot2grid((2,2), (0,0), rowspan = 2)
#c1plt = plt.subplot2grid((1,1), (0,0), colspan = 1)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W (mag)",fontdict = font)
plt.ylabel("M$_{F555W}$ (mag)",fontdict = font)

c1plt.xaxis.set_minor_locator(AutoMinorLocator()) 
c1plt.yaxis.set_minor_locator(AutoMinorLocator())

c1plt.yaxis.set_major_locator(MultipleLocator(.5))

###########################################################################
if (title == 'SN08ge'):
    c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
           'y-', label = 'Age = 10$^{7.1}$ yrs')
    c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
           'g:', label = 'Age = 10$^{7.2}$ yrs')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Age = 10$^{7.3}$ yrs')
elif (title == 'SN08ha'):          
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
           'b:' , label = 'Age = 10$^{7.4}$ yrs')
    c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Age = 10$^{7.5}$ yrs')
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Age = 10$^{7.6}$ yrs')
elif (title == 'SN10ae'):  
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
           'b:' , label = 'Age = 10$^{7.4}$ yrs')
    c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Age = 10$^{7.5}$ yrs')
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Age = 10$^{7.6}$ yrs') 
elif (title == 'SN10el'):  
    #plt.annotate('A${_v}}$ = ' + str(A435555), xy=(0.5, -6.5), xytext=(1.1, -5.0),
    #         arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="arc3"),)
    """
    c1plt.plot(np.subtract(F435W[age70],  F555W[age70]),  F555W[age70],  
           'r--', label = 'Age = 10$^{7.0}$ yrs')
    c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
           'y-', label = 'Age = 10$^{7.1}$ yrs')
    c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
           'g:', label = 'Age = 10$^{7.2}$ yrs')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Age = 10$^{7.3}$ yrs')
    """
    #c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Age = 10$^{7.6}$ yrs') 
    c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
           'y-' , label = 'Age = 10$^{7.7}$ yrs')
    c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
           'g:' , label = 'Age = 10$^{7.8}$ yrs')

    #c1plt.plot(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  
    #       'c-.', label = 'Age = 10$^{7.9}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  
    #       'b:' , label = 'Age = 10$^{8.0}$ yrs')  
###########################################################################

for i in range(start,end):
        c1plt.errorbar(np.subtract(f435f555_4[i][0],   f435f555_4[i][1]),   
                       f435f555_4[i][1], f435f555_4[i][2],   f435f555_4[i][3], 
                        fmt=None, ecolor="c",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_4[i][0],   f435f555_4[i][1]),   
                      f435f555_4[i][1], label = 'R = ' + str(radius[4]) + " PC",  
                        c='c',marker='D')
        c1plt.errorbar(np.subtract(f435f555_3[i][0],   f435f555_3[i][1]),   
                       f435f555_3[i][1], f435f555_3[i][2],   f435f555_3[i][3], 
                        fmt=None, ecolor="y",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_3[i][0],   f435f555_3[i][1]),   
                      f435f555_3[i][1], label = 'R = ' + str(radius[3]) + " PC",  
                        c='y',marker='D')
        c1plt.errorbar(np.subtract(f435f555_2[i][0],   f435f555_2[i][1]),   
                       f435f555_2[i][1], f435f555_2[i][2],   f435f555_2[i][3], 
                        fmt=None, ecolor="b",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_2[i][0],   f435f555_2[i][1]),   
                      f435f555_2[i][1], label = 'R = ' + str(radius[2]) + " PC",  
                        c='b',marker='D')
        c1plt.errorbar(np.subtract(f435f555_1[i][0],   f435f555_1[i][1]),  
                       f435f555_1[i][1], f435f555_1[i][2],   f435f555_1[i][3],
                         fmt=None, ecolor="r", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_1[i][0],   f435f555_1[i][1]),   
                      f435f555_1[i][1], label = 'R = ' + str(radius[1]) + " PC",  
                        c='r',marker='D')        
        c1plt.errorbar(np.subtract(f435f555_0[i][0],   f435f555_0[i][1]),  
                       f435f555_0[i][1], f435f555_0[i][2],   f435f555_0[i][3],
                         fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_0[i][0],   f435f555_0[i][1]),   
                      f435f555_0[i][1], label = 'R = ' + str(radius[0]) + " PC",  
                        c='k',marker='D')
        snt += 1

#c1plt.fill([3,4,4,3], [2,2,4,4], 'b', alpha=0.2, edgecolor='r')
###########################################################################  
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c1plt.set_ylim(bottom=ytopmax, top=ytopmin)
#c1plt.set_xlim(-1.5, 2.5) 
###########################################################################

#c2plt = plt.subplot2grid((2,2), (1,0), colspan = 2)
c2plt = plt.subplot2grid((2,2), (0,1), rowspan = 2)
#c2plt = plt.subplot2grid((0,0), (1,1), colspan = 1)
plt.gca().invert_yaxis()
plt.xlabel("F625W - F814W (mag)",fontdict = font)
plt.ylabel("M$_{F814W}$ (mag)",fontdict = font)

c2plt.tick_params(axis='both',labelbottom = font)
                  
c2plt.xaxis.set_minor_locator(AutoMinorLocator()) 
c2plt.yaxis.set_minor_locator(AutoMinorLocator())

c2plt.yaxis.set_major_locator(MultipleLocator(.5))

###########################################################################
#c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
#           'r--', label = 'Age = 10$^{7.0}$ yrs')
if (title == 'SN08ge'):
    c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
           'y-', label = 'Age = 10$^{7.1}$ yrs')
    c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
           'g:', label = 'Age = 10$^{7.2}$ yrs')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Age = 10$^{7.3}$ yrs')
elif (title == 'SN08ha'):   
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
           'b:' , label = 'Age = 10$^{7.4}$ yrs')
    c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Age = 10$^{7.5}$ yrs')
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Age = 10$^{7.6}$ yrs')
elif (title == 'SN10ae'):
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
           'b:' , label = 'Age = 10$^{7.4}$ yrs')
    c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Age = 10$^{7.5}$ yrs')
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Age = 10$^{7.6}$ yrs')
elif (title == 'SN10el'): 
    #plt.annotate('A${_v}}$ = ' + str(A625814) , xy=(0.5, -7.0), xytext=(1.1, -5.5),
    #         arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="arc3"),)
    """
    c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
           'r--', label = 'Age = 10$^{7.0}$ yrs')
    c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
           'y-', label = 'Age = 10$^{7.1}$ yrs')
    c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
           'g:', label = 'Age = 10$^{7.2}$ yrs')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Age = 10$^{7.3}$ yrs')
    """
    #c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Age = 10$^{7.6}$ yrs')
    c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
           'y-' , label = 'Age = 10$^{7.7}$ yrs')
    c2plt.plot(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  
           'g:' , label = 'Age = 10$^{7.8}$ yrs')
    
    #c2plt.plot(np.subtract(F625W[age79],  F814W[age79]),  F814W[age79],  
    #       'c-.', label = 'Age = 10$^{7.9}$ yrs') 
    #c2plt.plot(np.subtract(F625W[age80],  F814W[age80]),  F814W[age80],  
    #       'b:' , label = 'Age = 10$^{8.0}$ yrs')  

###########################################################################
           
for k in range(start,end):
        c2plt.errorbar(np.subtract(f625f814_4[k][0],   f625f814_4[k][1]),   
                       f625f814_4[k][1], f625f814_4[k][2],   f625f814_4[k][3], 
                        fmt=None, ecolor="c", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_4[k][0],   f625f814_4[k][1]),   f625f814_4[k][1],
                      label = 'R = ' + str(radius[4]) + " PC",  #'S/N >= ' + str(snb) +
                        c='c',marker='D')
        c2plt.errorbar(np.subtract(f625f814_3[k][0],   f625f814_3[k][1]),   
                       f625f814_3[k][1], f625f814_3[k][2],   f625f814_3[k][3], 
                        fmt=None, ecolor="y", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_3[k][0],   f625f814_3[k][1]),   f625f814_3[k][1],
                      label = 'R = ' + str(radius[3]) + " PC",   #'S/N >= ' + str(snb) +
                        c='y',marker='D')
        c2plt.errorbar(np.subtract(f625f814_2[k][0],   f625f814_2[k][1]),   
                       f625f814_2[k][1], f625f814_2[k][2],   f625f814_2[k][3], 
                        fmt=None, ecolor="b", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_2[k][0],   f625f814_2[k][1]),   f625f814_2[k][1],
                      label = 'R = ' + str(radius[2]) + " PC",   #'S/N >= ' + str(snb) +
                        c='b',marker='D')
        c2plt.errorbar(np.subtract(f625f814_1[k][0],   f625f814_1[k][1]),   
                       f625f814_1[k][1], f625f814_1[k][2],   f625f814_1[k][3], 
                        fmt=None, ecolor="r", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_1[k][0],   f625f814_1[k][1]),   f625f814_1[k][1],  #'S/N >= ' + str(snb) +   
                      label ='R = ' + str(radius[1]) + " PC",  
                        c='r',marker='D')
        c2plt.errorbar(np.subtract(f625f814_0[k][0],   f625f814_0[k][1]),   
                       f625f814_0[k][1], f625f814_0[k][2],   f625f814_0[k][3], 
                        fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_0[k][0],   f625f814_0[k][1]),   f625f814_0[k][1],   
                      label = 'R = ' + str(radius[0]) + " PC",   #'S/N >= ' + str(snb) +
                        c='k',marker='D')
        snb += 1
#c2plt.fill([3,4,4,3], [2,2,4,4], 'b', alpha=0.2, edgecolor='r')
###########################################################################
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c2plt.set_ylim(bottom=ybotmax, top=ybotmin) 
#c2plt.set_xlim(-1.5, 2.5) 
#gs.tight_layout(w_pad = .5)
########################################################################### 
figname = title + '_' + 'Z' + name[1:-7]+ 'nobadlist_morethan50.png'

plt.savefig('Figures/'+ figname)
print "Save and show plot : " + figname