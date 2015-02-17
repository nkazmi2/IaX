# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 16:08:55 2015

@author: nova
"""

from __future__ import division
import numpy               as np
import matplotlib.pyplot   as plt
import matplotlib.gridspec as gridspec
import pickle
from matplotlib.ticker  import MultipleLocator 
from matplotlib.ticker  import AutoMinorLocator

#####################################################################
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
########################### PICK THE SN!! ###########################
#####################################################################
#title = 'SN08ge'
#title = 'SN08ha'
title = 'SN10ae'
#title = 'SN10el'

radius = [0,0,500]
#####################################################################

f435f555 = []
f625f814 = []
Abs435 = [] 
Abs555 = [] 
Abs625 = [] 
Abs814 = []
Apn435 = [] 
Apn555 = []
Apn625 = []
Apn814 = [] 
UncXl  = [] 
UncYl  = []
UncXr  = [] 
UncYr  = [] 
SN435  = [] 
SN555  = []
SN625  = [] 
SN814  = []
Radl   = [] 
Radr   = []  
     
if (title == 'SN08ha'):    
    dist       = 20e7
    conver     = (5) 
    f435f555.append(pickle.load(open('SN2008HA/sn2008ha.f435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2008HA/sn2008ha.f625f814.p', 'rb')))    
elif (title == 'SN10ae'):
    dist       = 13.1e7
    conver     = (63.52) 
    f435f555.append(pickle.load(open('SN2010AE/sn2010ae.f435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2010AE/sn2010ae.f625f814.p', 'rb')))    

elif (title == 'SN10el'):
    dist       = 9.97e7
    conver     = (48.33)
    title      = 'SN10el'
    f435f555.append(pickle.load(open('SN2010EL/sn2010el.f435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2010EL/sn2010el.f625f814.p', 'rb')))    
 
elif (title == 'SN08ge'):
    dist     = 17.95e7
    conver   = (4.35)
    f435f555.append(pickle.load(open('SN2008GE/sn2008ge.f435f555.p', 'rb')))  
    f625f814.append(pickle.load(open('SN2008GE/sn2008ge.f625f814.p', 'rb')))  
 
###########################################################################
Abs435 = f435f555[0][0] 
Abs555 = f435f555[0][1] 
Apn435 = f435f555[0][2] 
Apn555 = f435f555[0][3] 
UncXl  = f435f555[0][4] 
UncYl  = f435f555[0][5] 
SN435  = f435f555[0][6] 
SN555  = f435f555[0][7]
Radl   = f435f555[0][8] 

Abs625 = f625f814[0][0] 
Abs814 = f625f814[0][1]
Apn625 = f625f814[0][2]
Apn814 = f625f814[0][3] 
UncXr  = f625f814[0][4] 
UncYr  = f625f814[0][5] 
SN625  = f625f814[0][6] 
SN814  = f625f814[0][7] 
Radr   = f625f814[0][8] 

s2 = np.where(Radl <= radius[2] & ((SN555 >= 10) | (SN435 >= 10)))

r2 = np.where(Radr <= radius[2] & ((SN814 >= 10) | (SN625 >= 10)))

###########################################################################
print "Begin plotting Isochrones..."
h = [2, 4] # height of the plotted figure
fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

fig1.suptitle(title, fontdict = font, size=15)

###########################################################################
c1plt = plt.subplot2grid((2,2), (0,0), rowspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W (mag)",fontdict = font)
plt.ylabel("M$_{F555W}$ (mag)",fontdict = font)

c1plt.xaxis.set_minor_locator(AutoMinorLocator()) 
c1plt.yaxis.set_minor_locator(AutoMinorLocator())

c1plt.yaxis.set_major_locator(MultipleLocator(.5))

###########################################################################
c1plt.scatter(np.subtract(Apn435[s2],   Apn555[s2]),
               Abs555[s2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[2]*conver)),-2)) + " AU",
               c='r',marker='d')           
###########################################################################

c2plt = plt.subplot2grid((2,2), (0,1), rowspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F625W - F814W (mag)",fontdict = font)
plt.ylabel("M$_{F814W}$ (mag)",fontdict = font)

c2plt.tick_params(axis='both',labelbottom = font)
                  
c2plt.xaxis.set_minor_locator(AutoMinorLocator()) 
c2plt.yaxis.set_minor_locator(AutoMinorLocator())

c2plt.yaxis.set_major_locator(MultipleLocator(.5))

###########################################################################

c2plt.scatter(np.subtract(Apn625[r2],   Apn814[r2]),
               Abs814[r2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[2]*conver)),-2)) + " AU",
               c='r',marker='d')           

############################################################################ 
plt.tight_layout()
plt.subplots_adjust(top=0.90)
########################################################################### 
