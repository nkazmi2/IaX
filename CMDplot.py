# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 09:11:48 2014

@author: Nova
"""

from __future__ import division
import numpy               as np
import matplotlib.pyplot   as plt
import matplotlib.gridspec as gridspec
import pickle
#import math
#import pylab 
from scipy              import stats
#from scipy.optimize     import minimize, rosen, rosen_der
from matplotlib.ticker  import MultipleLocator 
from matplotlib.ticker  import AutoMinorLocator
from matplotlib.patches import Polygon
#import matplotlib.patches  as patches
#import scipy.optimize      as optimization
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
        
        
class Star:
    def _init_(self,f435Abs,f555Abs,uncVert,uncHorz,snr435,snr555,xcoord, ycoord): 
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
#####################################################################
########################### PICK THE SN!! ###########################
#####################################################################
#title = 'SN08ge'
title = 'SN08ha'
#title = 'SN10ae'
#title = 'SN10el'

# Set the plotted point S/N parameters
start      = 0 # start = 0 starts at S/N 3
end        = 1 # end = 2 goes to S/N 4
snt        = 3
snb        = 3
#####################################################################

if (title == 'SN08ha'):
    name = 'Z0046Y26.dat'
    #name = 'Z0384Y26.dat'
elif (title == 'SN10ae'):
    name = 'Z0073Y26.dat'
    #name = 'Z0321Y26.dat'
elif (title == 'SN10el'):
    name = 'Z0170Y26.dat'
    #name = 'Z0217Y26.dat'
elif (title == 'SN08ge'): 
    name = 'Z0170Y26.dat'

d = []
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

age67   = np.where((logAGE == 6.7))
age68   = np.where((logAGE == 6.8))
age69   = np.where((logAGE == 6.9))
age70   = np.where((logAGE == 7.0))
age71   = np.where((logAGE == 7.1))
age72   = np.where((logAGE == 7.2))
age73   = np.where((logAGE == 7.3))
age74   = np.where((logAGE == 7.4))
age75   = np.where((logAGE == 7.5))
age76   = np.where((logAGE == 7.6))
age765  = np.where((logAGE == 7.65))
age77   = np.where((logAGE == 7.7))
age771  = np.where((logAGE == 7.71))
age772  = np.where((logAGE == 7.72))
age773  = np.where((logAGE == 7.73))
age774  = np.where((logAGE == 7.74))
age775  = np.where((logAGE == 7.75))
age776  = np.where((logAGE == 7.76))
age777  = np.where((logAGE == 7.77))
age78   = np.where((logAGE == 7.8))
age785  = np.where((logAGE == 7.85))
age79   = np.where((logAGE == 7.9))
age80   = np.where((logAGE == 8.0))
    
#####################################################################

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


if (title == 'SN08ge'):
    #ytopmax    = -4.0
    #ytopmin    = -9.0
    #ybotmax    = -4.0
    #ybotmin    = -9.0
    ytopmax    = -3.5
    ytopmin    = -6.5
    ybotmax    = -3.5
    ybotmin    = -7.0
    for i in range(3,6):
        f435f555_0.append(pickle.load(open('SN2008GE/sn2008gef435f555_sn3_rad0.p', 'rb')))    
        f625f814_0.append(pickle.load(open('SN2008GE/sn2008gef625f814_sn'+ str(i) +'_rad0.p', 'rb')))    
        f435f555_1.append(pickle.load(open('SN2008GE/sn2008gef435f555_sn'+ str(i) +'_rad1.p', 'rb')))    
        f625f814_1.append(pickle.load(open('SN2008GE/sn2008gef625f814_sn'+ str(i) +'_rad1.p', 'rb')))   
        f435f555_2.append(pickle.load(open('SN2008GE/sn2008gef435f555_sn'+ str(i) +'_rad2.p', 'rb')))    
        f625f814_2.append(pickle.load(open('SN2008GE/sn2008gef625f814_sn'+ str(i) +'_rad2.p', 'rb')))  
        f435f555_3.append(pickle.load(open('SN2008GE/sn2008gef435f555_sn'+ str(i) +'_rad3.p', 'rb')))    
        f625f814_3.append(pickle.load(open('SN2008GE/sn2008gef625f814_sn'+ str(i) +'_rad3.p', 'rb')))
        f435f555_4.append(pickle.load(open('SN2008GE/sn2008gef435f555_sn'+ str(i) +'_rad4.p', 'rb')))    
        f625f814_4.append(pickle.load(open('SN2008GE/sn2008gef625f814_sn'+ str(i) +'_rad4.p', 'rb')))
        
elif (title == 'SN08ha'):
    ytopmax    = -3.5
    ytopmin    = -6.5
    ybotmax    = -3.5
    ybotmin    = -7.0
    #ytopmax    = -4.5
    #ytopmin    = -7.5
    #ybotmax    = -4.0
    #ybotmin    = -7.5
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
        #f435f555_0.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_ext_sn'+ str(i) +'_rad0.p', 'rb')))    
        #f625f814_0.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_ext_sn'+ str(i) +'_rad0.p', 'rb')))    
        #f435f555_1.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_ext_sn'+ str(i) +'_rad1.p', 'rb')))    
        #f625f814_1.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_ext_sn'+ str(i) +'_rad1.p', 'rb')))   
        #f435f555_2.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_ext_sn'+ str(i) +'_rad2.p', 'rb')))    
        #f625f814_2.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_ext_sn'+ str(i) +'_rad2.p', 'rb')))
        #f435f555_3.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_ext_sn'+ str(i) +'_rad3.p', 'rb')))    
        #f625f814_3.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_ext_sn'+ str(i) +'_rad3.p', 'rb')))
        #f435f555_4.append(pickle.load(open('SN2008HA/sn2008ha_f435f555_ext_sn'+ str(i) +'_rad4.p', 'rb')))    
        #f625f814_4.append(pickle.load(open('SN2008HA/sn2008ha_f625f814_ext_sn'+ str(i) +'_rad4.p', 'rb')))
###############################################################################

###############################################################################

elif (title == 'SN10ae'):
    ytopmax    = -2.5
    ytopmin    = -7.0
    ybotmax    = -3.0
    ybotmin    = -7.5
    #ytopmax    = -4.5
    #ytopmin    = -8.0
    #ybotmax    = -4.0
    #ybotmin    = -8.5
    
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
              
        #f435f555_0.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_ext_sn'+ str(i) +'_rad0.p', 'rb')))    
        #f625f814_0.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_ext_sn'+ str(i) +'_rad0.p', 'rb')))    
        #f435f555_1.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_ext_sn'+ str(i) +'_rad1.p', 'rb')))    
        #f625f814_1.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_ext_sn'+ str(i) +'_rad1.p', 'rb')))   
        #f435f555_2.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_ext_sn'+ str(i) +'_rad2.p', 'rb')))    
        #f625f814_2.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_ext_sn'+ str(i) +'_rad2.p', 'rb')))  
        #f435f555_3.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_ext_sn'+ str(i) +'_rad3.p', 'rb')))    
        #f625f814_3.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_ext_sn'+ str(i) +'_rad3.p', 'rb')))
        #f435f555_4.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_ext_sn'+ str(i) +'_rad4.p', 'rb')))    
        #f625f814_4.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_ext_sn'+ str(i) +'_rad4.p', 'rb')))
        
elif (title == 'SN10el'):
    title      = 'SN10el'
    ytopmax    = -1.5
    ytopmin    = -6.0
    ybotmax    = -2.0
    ybotmin    = -6.3

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

#x435555 = f435f555_4[0][6] # Max radius, min s/n 
#y435555 = f435f555_4[0][7]
#x625814 = f625f814_4[0][6]
#y625814 = f625f814_4[0][7]
#overlapL = np.where(list(np.any(x in f625f814_4[0][6] for x in f435f555_4[0][6]) and np.any(y in f625f814_4[0][7] for y in f435f555_4[0][7])))
#overlapR = np.where(list(np.any(x in f435f555_4[0][6] for x in f625f814_4[0][6]) and np.any(y in f435f555_4[0][7] for y in f625f814_4[0][7])))


#
#def func(x, a, b, c):
#    return a + b*x + c*x*x
#
#print optimization.curve_fit(func, xdata, ydata, x0, sigma)


###########################################################################
print "Begin plotting Isochrones..."
h = [2, 4] # height of the plotted figure
fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

fig1.suptitle(title + ': CMD for Z = 0.' + name[1:-7] + ', Y = 0.' + name[6:-4] + ' S/N >= 3',
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
    print "Continue"
    """
    c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
           'y-', label = 'Age = 10$^{7.1}$ yrs')
    c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
           'g:', label = 'Age = 10$^{7.2}$ yrs')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Age = 10$^{7.3}$ yrs')
    """
elif (title == 'SN08ha'):          
    #plt.annotate('', xy=(.74, -5.876), xycoords = 'data', #(Top of the arrow)
    #xytext = (1.0, -5), textcoords = 'data', # End of the arrow
    #arrowprops = {'arrowstyle':'->'}) # what the arrow looks like
    #plt.annotate('A${_v}}$ = .9137', xy=(1.0,-4.8), xycoords = 'data', # coord of term
    #xytext = (2, 3), textcoords = 'offset points')
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
    #           'c-', label = 'Age = 10$^{7.3}$ yrs')
    #c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c1plt.plot(np.subtract(F435W[age765],  F555W[age765]),  F555W[age765],  
    #       'b--', label = 'Age = 10$^{7.6}$ yrs')
    #c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
    #c1plt.plot(np.subtract(F435W[age771], F555W[age771]), F555W[age771],  
    #       'y-' , label = 'Age = 10$^{7.71}$ yrs')
    c1plt.plot(np.subtract(F435W[age773], F555W[age773]), F555W[age773],  
           'r--' , label = 'Age = 10$^{7.73}$ yrs')
    #c1plt.plot(np.subtract(F435W[age774], F555W[age774]), F555W[age774],  
    #       'g-' , label = 'Age = 10$^{7.74}$ yrs')
    #c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
    #       'g:' , label = 'Age = 10$^{7.8}$ yrs')
elif (title == 'SN10ae'):  
    #plt.annotate('', xy=(.536, -6.588), xycoords = 'data', #(Top of the arrow)
    #xytext = (1.0, -5), textcoords = 'data', # End of the arrow
    #arrowprops = {'arrowstyle':'->'}) # what the arrow looks like
    #plt.annotate('A${_v}}$ = .708', xy=(1.0,-5.8), xycoords = 'data', # coord of term
    #xytext = (2, 3), textcoords = 'offset points')
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    #c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
    #       'r--', label = 'Age = 10$^{7.6}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
    #c1plt.plot(np.subtract(F435W[age774], F555W[age774]), F555W[age774],  
    #       'g:' , label = 'Age = 10$^{7.74}$ yrs')
elif (title == 'SN10el'):  
    #plt.annotate('A${_v}}$ = ' + str(A435555), xy=(0.5, -6.5), xytext=(1.1, -5.0),
    #         arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="arc3"),)
    plt.annotate('', xy=(1.062, -5.717), xycoords = 'data',
    xytext = (1.8, -3.2), textcoords = 'data',
    arrowprops = {'arrowstyle':'->'})
    plt.annotate('A${_v}}$ = 3.4105', xy=(0.2,-5.5), xycoords = 'data',
    xytext = (2, 3), textcoords = 'offset points')
    
    #c1plt.plot(np.subtract(F435W[age70],  F555W[age70]),  F555W[age70],  
    #       'r--', label = 'Age = 10$^{7.0}$ yrs')
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    #c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
    #       'r--', label = 'Age = 10$^{7.6}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
    #c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
    #       'g:' , label = 'Age = 10$^{7.8}$ yrs')
    c1plt.plot(np.subtract(F435W[age785], F555W[age785]), F555W[age785],  
           'r--' , label = 'Age = 10$^{7.85}$ yrs')
    #c1plt.plot(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  
    #       'c-.', label = 'Age = 10$^{7.9}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  
    #       'b:' , label = 'Age = 10$^{8.0}$ yrs')  
###########################################################################
#c1plt.scatter(np.subtract(f435f555_4[0][0][overlapL],   f435f555_4[0][1][overlapL]),
#              f435f555_4[0][1][overlapL],label = "Shared Points",  
#                        c='r',marker="D")

for i in range(start,end):
        c1plt.errorbar(np.subtract(f435f555_4[i][8],   f435f555_4[i][9]),   
                       f435f555_4[i][1], f435f555_4[i][2],   f435f555_4[i][3], 
                        fmt=None, ecolor="c",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_4[i][8],   f435f555_4[i][9]),   
                      f435f555_4[i][1], label = 'R = ' + str(radius[4]) + " PC",  
                        c='c',marker='d')
        c1plt.errorbar(np.subtract(f435f555_3[i][8],   f435f555_3[i][9]),   
                       f435f555_3[i][1], f435f555_3[i][2],   f435f555_3[i][3], 
                        fmt=None, ecolor="y",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_3[i][8],   f435f555_3[i][9]),   
                      f435f555_3[i][1], label = 'R = ' + str(radius[3]) + " PC",  
                        c='y',marker='d')
        c1plt.errorbar(np.subtract(f435f555_2[i][8],   f435f555_2[i][9]),   
                       f435f555_2[i][1], f435f555_2[i][2],   f435f555_2[i][3], 
                        fmt=None, ecolor="b",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_2[i][8],   f435f555_2[i][9]),   
                      f435f555_2[i][1], label = 'R = ' + str(radius[2]) + " PC",  
                        c='b',marker='d')
        c1plt.errorbar(np.subtract(f435f555_1[i][8],   f435f555_1[i][9]),  
                       f435f555_1[i][1], f435f555_1[i][2],   f435f555_1[i][3],
                         fmt=None, ecolor="r", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_1[i][8],   f435f555_1[i][9]),   
                      f435f555_1[i][1], label = 'R = ' + str(radius[1]) + " PC",  
                        c='r',marker='d')        
        c1plt.errorbar(np.subtract(f435f555_0[i][8],   f435f555_0[i][9]),  
                       f435f555_0[i][1], f435f555_0[i][2],   f435f555_0[i][3],
                         fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_0[i][8],   f435f555_0[i][9]),   
                      f435f555_0[i][1], label = 'R = ' + str(radius[0]) + " PC",  
                        c='k',marker='d')
        snt += 1

########################################################################### 
###########################################################################
#pts = np.array([[-1,ybotmax],[-1,-4.6],[.4,-4.6],[2.5,-7],[2.5,ybotmax]])
#poly = Polygon(pts, color='grey', alpha=0.15,closed = True)

#c1plt.add_patch(poly)
###########################################################################  
l = plt.legend(prop = {'family' : 'serif'},loc=4)
#l = plt.legend(prop = {'family' : 'serif'},loc=1)
l.draw_frame(False)
########################################################################### 
c1plt.set_ylim(bottom=ytopmax, top=ytopmin)
#c1plt.set_xlim(-1.5, 2.5) 
#p = plt.axhspan(ytopmax, -4, facecolor='g', alpha=0.2)
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
    print "Continue"
    """
    c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
           'y-', label = 'Age = 10$^{7.1}$ yrs')
    c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
           'g:', label = 'Age = 10$^{7.2}$ yrs')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Age = 10$^{7.3}$ yrs')
    """
elif (title == 'SN08ha'):   
    #plt.annotate('', xy=(1.216, -5.48), xycoords = 'data', #(Top of the arrow)
    #xytext = (1.0, -5), textcoords = 'data', # End of the arrow
    #arrowprops = {'arrowstyle':'->'}) # what the arrow looks like
    #plt.annotate('A${_v}}$ = .5263', xy=(1.0,-4.8), xycoords = 'data', # coord of term
    #xytext = (2, 3), textcoords = 'offset points')
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    #c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c2plt.plot(np.subtract(F625W[age765],  F814W[age765]),  F814W[age765],  
    #       'b--', label = 'Age = 10$^{7.65}$ yrs')
    #c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
           #'y-' , label = 'Age = 10$^{7.7}$ yrs')   
    #c2plt.plot(np.subtract(F625W[age771],  F814W[age771]),  F814W[age771],  
    #       'y-' , label = 'Age = 10$^{7.71}$ yrs')  
    c2plt.plot(np.subtract(F625W[age773],  F814W[age773]),  F814W[age773],  
           'r--' , label = 'Age = 10$^{7.73}$ yrs')  
    #c2plt.plot(np.subtract(F625W[age774],  F814W[age774]),  F814W[age774],  
    #       'g-' , label = 'Age = 10$^{7.74}$ yrs')
    #c2plt.plot(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  
    #       'g:' , label = 'Age = 10$^{7.8}$ yrs')
elif (title == 'SN10ae'):
    #plt.annotate('', xy=(1.114, -6.867), xycoords = 'data', #(Top of the arrow)
    #xytext = (1.5, -6), textcoords = 'data', # End of the arrow
    #arrowprops = {'arrowstyle':'->'}) # what the arrow looks like
    #plt.annotate('A${_v}}$ = .949', xy=(1.25,-6.5), xycoords = 'data', # coord of term
    #xytext = (2, 3), textcoords = 'offset points')
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    #c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
    #       'r--', label = 'Age = 10$^{7.6}$ yrs')
    #c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
    #c2plt.plot(np.subtract(F625W[age774],  F814W[age774]),  F814W[age774],  
    #       'g:' , label = 'Age = 10$^{7.74}$ yrs')
elif (title == 'SN10el'): 
    #plt.annotate('A${_v}}$ = ' + str(A625814) , xy=(0.5, -7.0), xytext=(1.1, -5.5),
    #         arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="arc3"),)
    plt.annotate('', xy=(1.375, -5.376), xycoords = 'data',
    xytext = (2.0, -4), textcoords = 'data',
    arrowprops = {'arrowstyle':'->'})
    plt.annotate('A${_v}}$ = 2.2016', xy=(1.2,-3.8), xycoords = 'data',
    xytext = (2, 3), textcoords = 'offset points')
    #c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
    #       'r--', label = 'Age = 10$^{7.0}$ yrs')
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
    #       'c-', label = 'Age = 10$^{7.3}$ yrs')
    #c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
    #       'r--', label = 'Age = 10$^{7.6}$ yrs')
    #c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
    #c2plt.plot(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  
    #       'g:' , label = 'Age = 10$^{7.8}$ yrs')
    c2plt.plot(np.subtract(F625W[age785], F814W[age785]), F814W[age785],  
           'r--' , label = 'Age = 10$^{7.85}$ yrs')
    #c2plt.plot(np.subtract(F625W[age79],  F814W[age79]),  F814W[age79],  
    #       'c-.', label = 'Age = 10$^{7.9}$ yrs') 
    #c2plt.plot(np.subtract(F625W[age80],  F814W[age80]),  F814W[age80],  
    #       'b:' , label = 'Age = 10$^{8.0}$ yrs')  

###########################################################################
#c2plt.scatter(np.subtract(f625f814_4[0][0][overlapR],   f625f814_4[0][1][overlapR]),
#              f625f814_4[0][1][overlapR],label = "Shared Points",  
#                        c='r',marker="D")

for k in range(start,end):
        c2plt.errorbar(np.subtract(f625f814_4[k][8],   f625f814_4[k][9]),   
                       f625f814_4[k][1], f625f814_4[k][2],   f625f814_4[k][3], 
                        fmt=None, ecolor="c", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_4[k][8],   f625f814_4[k][9]),   f625f814_4[k][1],
                      label = 'R = ' + str(radius[4]) + " PC",  #'S/N >= ' + str(snb) +
                        c='c',marker='d')
        c2plt.errorbar(np.subtract(f625f814_3[k][8],   f625f814_3[k][9]),   
                       f625f814_3[k][1], f625f814_3[k][2],   f625f814_3[k][3], 
                        fmt=None, ecolor="y", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_3[k][8],   f625f814_3[k][9]),   f625f814_3[k][1],
                      label = 'R = ' + str(radius[3]) + " PC",   #'S/N >= ' + str(snb) +
                        c='y',marker='d')
        c2plt.errorbar(np.subtract(f625f814_2[k][8],   f625f814_2[k][9]),   
                       f625f814_2[k][1], f625f814_2[k][2],   f625f814_2[k][3], 
                        fmt=None, ecolor="b", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_2[k][8],   f625f814_2[k][9]),   f625f814_2[k][1],
                      label = 'R = ' + str(radius[2]) + " PC",   #'S/N >= ' + str(snb) +
                        c='b',marker='d')
        c2plt.errorbar(np.subtract(f625f814_1[k][8],   f625f814_1[k][9]),   
                       f625f814_1[k][1], f625f814_1[k][2],   f625f814_1[k][3], 
                        fmt=None, ecolor="r", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_1[k][8],   f625f814_1[k][9]),   f625f814_1[k][1],  #'S/N >= ' + str(snb) +   
                      label ='R = ' + str(radius[1]) + " PC",  
                        c='r',marker='d')
        c2plt.errorbar(np.subtract(f625f814_0[k][8],   f625f814_0[k][9]),   
                       f625f814_0[k][1], f625f814_0[k][2],   f625f814_0[k][3], 
                        fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_0[k][8],   f625f814_0[k][9]),   f625f814_0[k][1],   
                      label = 'R = ' + str(radius[0]) + " PC",   #'S/N >= ' + str(snb) +
                        c='k',marker='d')
        snb += 1
#c2plt.fill([3,4,4,3], [2,2,4,4], 'b', alpha=0.2, edgecolor='r')

###########################################################################

#This was an iffy move,using the sn =3 of a point that's not plotted, I don't like it

f555min3    = -4.4110 #555
#f555min3 this has to be changed
f555min3435 = -4.6930 
f435min3    = -4.5320 #-3.8880  #commented out is sn 435 = 3.0
f435min3555 = -4.4810 #-2.7340 #555

s1 = -1 #np.subtract(f435min3555,f555min3 ) / np.subtract(np.subtract(f435min3 ,f435min3555),np.subtract(f555min3435,f555min3 ))
horz1 = -4.4 #f555min3 
b1 = horz1 - (s1*(np.subtract(horz1 ,f555min3435)))

ptsR = np.array([[-2,ytopmax],
                 [-2,horz1],
                 [np.subtract(f555min3,b1)/s1,horz1], #need the x value
                 [2.0,((2.0*s1)+b1)],           
                 [2.0,ytopmax]])
polyR = Polygon(ptsR, color='grey', alpha=0.15,closed = True)

c1plt.add_patch(polyR)
#############
min3l       = np.where(f625f814_4[0][5] == 3.0)
#f625f814_4[0][1][min3l] This is what I have to change
f625min3    = -3.9410#-4.2860 #SN 625 == 3
f625min3814 = -4.8030#-4.5880
horz = -4.4#f625f814_4[0][1][min3l]
s4 = -1 # np.subtract(f625min3814,f625f814_4[0][1][min3l])/np.subtract(np.subtract(f625min3,f625min3814),np.subtract(f625f814_4[0][0][min3l] ,f625f814_4[0][1][min3l]))
b4 = np.subtract(horz,s4*(np.subtract(f625f814_4[0][0][min3l],horz)))
y4 = (s4*2.5) + b4
x4 = np.subtract(horz,b4)/s4

pts = np.array([[-2,ybotmax],
                [-2,horz],
                [x4,horz], 
                [2.5,y4],           
                [2.5,ybotmax]])
poly = Polygon(pts, color='grey', alpha=0.15,closed = True)

c2plt.add_patch(poly)

###########################################################################
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c2plt.set_ylim(bottom=ybotmax, top=ybotmin) 
#c2plt.set_xlim(-1.5, 2.5) 
#gs.tight_layout(w_pad = .5)
#p = plt.axhspan(ybotmax, -4, facecolor='g', alpha=0.2)
########################################################################### 
plt.tight_layout()
plt.subplots_adjust(top=0.90)
########################################################################### 
#figname = title + '_' + 'Z' + name[1:-7]+ '.png'
figname = title + '_' + 'delete' + '.png'
plt.savefig('Figures/'+ figname)
print "Save and show plot : " + figname
