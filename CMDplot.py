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
import math
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
####################################################################

#title = 'SN08ha'
title = 'SN10ae'
#title = 'SN10el'
#####################################################################

if (title == 'SN08ha'):
    name = 'Z0060Y26.dat'
elif (title == 'SN10ae'):
    name = 'Z0096Y26.dat'
elif (title == 'SN10el'):
    name = 'Z0224Y26.dat'
elif (title == 'SN08ge'):
    name = 'Z0300Y26.dat'

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

age70   = np.where((logAGE == 7.0))
age71   = np.where((logAGE == 7.1))
age711  = np.where((logAGE == 7.11))
age712  = np.where((logAGE == 7.12))
age713  = np.where((logAGE == 7.13))
age714  = np.where((logAGE == 7.14))
age715  = np.where((logAGE == 7.15))
age716  = np.where((logAGE == 7.16))
age717  = np.where((logAGE == 7.17))
age718  = np.where((logAGE == 7.18))
age719  = np.where((logAGE == 7.19))
age72   = np.where((logAGE == 7.2))
age721  = np.where((logAGE == 7.21))
age722  = np.where((logAGE == 7.22))
age723  = np.where((logAGE == 7.23))
age724  = np.where((logAGE == 7.24))
age725  = np.where((logAGE == 7.25))
age726  = np.where((logAGE == 7.26))
age727  = np.where((logAGE == 7.27))
age728  = np.where((logAGE == 7.28))
age729  = np.where((logAGE == 7.29))
age73   = np.where((logAGE == 7.3))
age731  = np.where((logAGE == 7.31))
age732  = np.where((logAGE == 7.32))
age733  = np.where((logAGE == 7.33))
age734  = np.where((logAGE == 7.34))
age735  = np.where((logAGE == 7.35))
age736  = np.where((logAGE == 7.36))
age737  = np.where((logAGE == 7.37))
age738  = np.where((logAGE == 7.38))
age739   = np.where((logAGE == 7.39))
age74   = np.where((logAGE == 7.4))
age741  = np.where((logAGE == 7.41))
age742  = np.where((logAGE == 7.42))
age743  = np.where((logAGE == 7.43))
age744  = np.where((logAGE == 7.44))
age745  = np.where((logAGE == 7.45))
age746  = np.where((logAGE == 7.46))
age747  = np.where((logAGE == 7.47))
age748  = np.where((logAGE == 7.48))
age749  = np.where((logAGE == 7.49))
age75   = np.where((logAGE == 7.5))
age751  = np.where((logAGE == 7.51))
age752  = np.where((logAGE == 7.52))
age753  = np.where((logAGE == 7.53))
age754  = np.where((logAGE == 7.54))
age755  = np.where((logAGE == 7.55))
age756  = np.where((logAGE == 7.56))
age757  = np.where((logAGE == 7.57))
age758  = np.where((logAGE == 7.58))
age759  = np.where((logAGE == 7.59))
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
age778  = np.where((logAGE == 7.78))
age78   = np.where((logAGE == 7.8))
age781  = np.where((logAGE == 7.81))
age782  = np.where((logAGE == 7.82))
age783  = np.where((logAGE == 7.83))
age784  = np.where((logAGE == 7.84))
age785  = np.where((logAGE == 7.85))
age786  = np.where((logAGE == 7.86))
age787  = np.where((logAGE == 7.87))
age788  = np.where((logAGE == 7.88))
age789  = np.where((logAGE == 7.89))
age79   = np.where((logAGE == 7.9))
age80   = np.where((logAGE == 8.0))
    
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
    radius     = [15,30,45]
    dist       = 20e7
    conver     = (5) #(2.5*math.pi)/(50.0*3600*180)
    yLmax      = -3.5
    yLmin      = -6.5
    yRmax      = -4.0
    yRmin      = -7.0
    xLmax    = -0.75
    xLmin    =  2.0
    xRmax    = -0.75
    xRmin    =  2.0
    
    #Mean f435w Abs Mag at S/N = 3 :  -4.0062
    #Mean f555w Abs Mag at S/N = 3 :  -4.36564102564
    #Mean f625w Abs Mag at S/N = 3 :  -4.37502222222
    #Mean f814w Abs Mag at S/N = 3 :  -4.46459459459
    #f435f555.append(pickle.load(open('SN2008HA/sn2008ha_f435f555.p', 'rb')))    
    #f625f814.append(pickle.load(open('SN2008HA/sn2008ha_f625f814.p', 'rb'))) 
    f435f555.append(pickle.load(open('SN2008HA/sn08haf435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2008HA/sn08haf625f814.p', 'rb')))    
###############################################################################

###############################################################################

elif (title == 'SN10ae'):
    radius     = [7.8,9.5,11]#[7.8,11,18.85]
    dist       = 13.1e7
    conver     = (63.52) #(2.5*math.pi)/(50.0*3600*180)
    
    yLmax      = -3.9
    yLmin      = -7.0
    yRmax      = -5.0
    yRmin      = -7.5
    
    xLmax      = -0.75
    xLmin      =  2.0
    xRmax      = -0.75
    xRmin      =  2.0
    
    f435f555.append(pickle.load(open('SN2010AE/sn10aef435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2010AE/sn10aef625f814.p', 'rb')))    
    #f435f555.append(pickle.load(open('SN2010AE/sn2010ae.f435f555.p', 'rb')))    
    #f625f814.append(pickle.load(open('SN2010AE/sn2010ae.f625f814.p', 'rb')))    

elif (title == 'SN10el'):
    radius     = [10.34,18.62,20.74]#[16.55,18.62,19.65]#
    dist       = 9.97e7
    conver     = (48.33) #(2.5*math.pi)/(50.0*3600*180)
    title      = 'SN10el'
    yLmax    = -2.0
    yLmin    = -5.5
    yRmax    = -3.0
    yRmin    = -6.0
    
    xLmax    = -0.5
    xLmin    =  2.0
    xRmax    = -0.5
    xRmin    =  2.3
    
    f435f555.append(pickle.load(open('SN2010EL/sn10elf435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2010EL/sn10elf625f814.p', 'rb')))    
 

elif (title == 'SN08ge'):
    radius   = [38,75,100]
    dist     = 17.95e7
    conver   = (4.35)
    yLmax    = -3.0
    yLmin    = -8.0
    yRmax    = -4.0
    yRmin    = -9.0
    
    xLmax    = -0.5
    xLmin    =  2.0
    xRmax    = -0.5
    xRmin    =  1.7
    
    f435f555.append(pickle.load(open('SN2008GE/sn08gef435f555.p', 'rb')))  
    f625f814.append(pickle.load(open('SN2008GE/sn08gef625f814.p', 'rb')))  
 
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

s0 = np.where(Radl <= radius[0])
s1 = np.where(Radl <= radius[1])
s2 = np.where(Radl <= radius[2])
#s3 = np.where(Radl <= radius[3])
#s4 = np.where(Radl <= radius[4])

r0 = np.where(Radr <= radius[0])
r1 = np.where(Radr <= radius[1])
r2 = np.where(Radr <= radius[2])
#r3 = np.where(Radr <= radius[3])
#r4 = np.where(Radr <= radius[4])

###########################################################################
print "Begin plotting Isochrones..."
h = [2, 4] # height of the plotted figure
fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

fig1.suptitle(title + ': CMD for Z = 0.' + name[1:-7] + ', Y = 0.' + name[6:-4], 
              #+ ' S/N >= 10',
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
c1plt.xaxis.set_major_locator(MultipleLocator(.5))

###########################################################################
if (title == 'SN08ha'):          
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
    c1plt.plot(np.subtract(F435W[age772], F555W[age772]), F555W[age772],  
           'k--' , label = 'Age = 10$^{7.72}$ yrs')
    #c1plt.plot(np.subtract(F435W[age773], F555W[age773]), F555W[age773],  
    #       'k--' , label = 'Age = 10$^{7.73}$ yrs')
    #c1plt.plot(np.subtract(F435W[age774], F555W[age774]), F555W[age774],  
    #       'g-' , label = 'Age = 10$^{7.74}$ yrs')
    #c1plt.plot(np.subtract(F435W[age775], F555W[age775]), F555W[age775],  
    #       'b-' , label = 'Age = 10$^{7.75}$ yrs')
    #c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
    #       'g:' , label = 'Age = 10$^{7.8}$ yrs')
elif (title == 'SN10ae'):  
    #plt.annotate('', xy=(.536, -6.588), xycoords = 'data', #(Top of the arrow)
    #xytext = (1.0, -5), textcoords = 'data', # End of the arrow
    #arrowprops = {'arrowstyle':'->'}) # what the arrow looks like
    #plt.annotate('A${_v}}$ = .708', xy=(1.0,-5.8), xycoords = 'data', # coord of term
    #xytext = (2, 3), textcoords = 'offset points')
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
    #c1plt.plot(np.subtract(F435W[age731], F555W[age731]), F555W[age731],  
    #       'k--' , label = 'Age = 10$^{7.31}$ yrs')
    #c1plt.plot(np.subtract(F435W[age732], F555W[age732]), F555W[age732],  
    #       'k--' , label = 'Age = 10$^{7.32}$ yrs')
    #c1plt.plot(np.subtract(F435W[age733], F555W[age733]), F555W[age733],  
    #       'g-' , label = 'Age = 10$^{7.33}$ yrs')
    #c1plt.plot(np.subtract(F435W[age734], F555W[age734]), F555W[age734],  
    #       'k--' , label = 'Age = 10$^{7.34}$ yrs')
    c1plt.plot(np.subtract(F435W[age735], F555W[age735]), F555W[age735],  
           'k--' , label = 'Age = 10$^{7.35}$ yrs')
    #c1plt.plot(np.subtract(F435W[age736], F555W[age736]), F555W[age736],  
    #       'm--' , label = 'Age = 10$^{7.36}$ yrs')
    #c1plt.plot(np.subtract(F435W[age737], F555W[age737]), F555W[age737],  
    #       'g-' , label = 'Age = 10$^{7.37}$ yrs')
    #c1plt.plot(np.subtract(F435W[age738], F555W[age738]), F555W[age738],  
    #       'b-' , label = 'Age = 10$^{7.38}$ yrs')
    #c1plt.plot(np.subtract(F435W[age739],  F555W[age739]),  F555W[age739],  
    #       'c-', label = 'Age = 10$^{7.39}$ yrs')
    #c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c1plt.plot(np.subtract(F435W[age741], F555W[age741]), F555W[age741],  
    #       'k--' , label = 'Age = 10$^{7.41}$ yrs')
    #c1plt.plot(np.subtract(F435W[age742], F555W[age742]), F555W[age742],  
    #       'k--' , label = 'Age = 10$^{7.42}$ yrs')
    #c1plt.plot(np.subtract(F435W[age743], F555W[age743]), F555W[age743],  
           #'g-' , label = 'Age = 10$^{7.43}$ yrs')
    #c1plt.plot(np.subtract(F435W[age744], F555W[age744]), F555W[age744],  
    #      'y-' , label = 'Age = 10$^{7.44}$ yrs')
    #c1plt.plot(np.subtract(F435W[age745], F555W[age745]), F555W[age745],  
    #       'r:' , label = 'Age = 10$^{7.45}$ yrs')
    #c1plt.plot(np.subtract(F435W[age746], F555W[age746]), F555W[age746],  
           #'m--' , label = 'Age = 10$^{7.46}$ yrs')
    #c1plt.plot(np.subtract(F435W[age747], F555W[age747]), F555W[age747],  
           #'g-' , label = 'Age = 10$^{7.47}$ yrs')
    #c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
    #       'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
    #       'r--', label = 'Age = 10$^{7.6}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age765], F555W[age765]), F555W[age765],  
    #       'g-' , label = 'Age = 10$^{7.65}$ yrs')
    #c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
    #c1plt.plot(np.subtract(F435W[age747], F555W[age747]), F555W[age747],  
           #'g-' , label = 'Age = 10$^{7.747}$ yrs')
elif (title == 'SN10el'):  
    #plt.annotate('A${_v}}$ = ' + str(A435555), xy=(0.5, -6.5), xytext=(1.1, -5.0),
    #         arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="arc3"),)
    
    plt.annotate('', xy=(1.1, -5.417), xycoords = 'data',
                 xytext = (1.838, -2.9), textcoords = 'data',
                    arrowprops = {'arrowstyle':'->'})
    plt.annotate('A${_v}}$ = 3.4105', xy=(0.3,-5.2), xycoords = 'data',
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
    c1plt.plot(np.subtract(F435W[age781], F555W[age781]), F555W[age781],  
           'k--' , label = 'Age = 10$^{7.81}$ yrs')
    #c1plt.plot(np.subtract(F435W[age782], F555W[age782]), F555W[age782],  
    #       'y--', label = 'Age = 10$^{7.82}$ yrs')
    #c1plt.plot(np.subtract(F435W[age783], F555W[age783]), F555W[age783],  
    #       'g--', label = 'Age = 10$^{7.83}$ yrs')
    #c1plt.plot(np.subtract(F435W[age784], F555W[age784]), F555W[age784],  
    #       'b--' , label = 'Age = 10$^{7.84}$ yrs')
    #c1plt.plot(np.subtract(F435W[age785], F555W[age785]), F555W[age785],  
    #       'm--' , label = 'Age = 10$^{7.85}$ yrs')
    #c1plt.plot(np.subtract(F435W[age786], F555W[age786]), F555W[age786],  
    #       'r--' , label = 'Age = 10$^{7.86}$ yrs')
    #c1plt.plot(np.subtract(F435W[age787], F555W[age787]), F555W[age787],  
    #       'k--' , label = 'Age = 10$^{7.87}$ yrs')
    #c1plt.plot(np.subtract(F435W[age788], F555W[age788]), F555W[age788],  
    #       'g--', label = 'Age = 10$^{7.88}$ yrs')
    #c1plt.plot(np.subtract(F435W[age789], F555W[age789]), F555W[age789],  
    #       'b--' , label = 'Age = 10$^{7.89}$ yrs')
    #c1plt.plot(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  
    #       'c-.', label = 'Age = 10$^{7.9}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  
    #       'b:' , label = 'Age = 10$^{8.0}$ yrs')  
elif (title == 'SN08ge'):  
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Age = 10$^{7.1}$ yrs')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c1plt.plot(np.subtract(F435W[age725],  F555W[age725]),  F555W[age725],  
    #       'r:', label = 'Age = 10$^{7.25}$ yrs')
    #c1plt.plot(np.subtract(F435W[age728],  F555W[age728]),  F555W[age728],  
    #       'g--', label = 'Age = 10$^{7.28}$ yrs')
    c1plt.plot(np.subtract(F435W[age729],  F555W[age729]),  F555W[age729],  
           'g--', label = 'Age = 10$^{7.29}$ yrs')
    #c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
    #       'k--', label = 'Age = 10$^{7.3}$ yrs')
    #c1plt.plot(np.subtract(F435W[age731], F555W[age731]), F555W[age731],  
    #       'k--', label = 'Age = 10$^{7.31}$ yrs')
    #c1plt.plot(np.subtract(F435W[age732], F555W[age732]), F555W[age732],  
    #       'c-' , label = 'Age = 10$^{7.32}$ yrs')
    #c1plt.plot(np.subtract(F435W[age733], F555W[age733]), F555W[age733],  
    #       'g-' , label = 'Age = 10$^{7.33}$ yrs')
    #c1plt.plot(np.subtract(F435W[age734], F555W[age734]), F555W[age734],  
    #       'y-' , label = 'Age = 10$^{7.34}$ yrs')
    #c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
    #       'b:', label = 'Age = 10$^{7.4}$ yrs')
    #c1plt.plot(np.subtract(F435W[age741],  F555W[age741]),  F555W[age741],  
    #       'y-', label = 'Age = 10$^{7.41}$ yrs')
    #c1plt.plot(np.subtract(F435W[age742],  F555W[age742]),  F555W[age742],  
    #       'g:', label = 'Age = 10$^{7.42}$ yrs')
    #c1plt.plot(np.subtract(F435W[age743],  F555W[age743]),  F555W[age743],  
    #       'g--', label = 'Age = 10$^{7.43}$ yrs')
    #c1plt.plot(np.subtract(F435W[age744],  F555W[age744]),  F555W[age744],  
    #       'b:' , label = 'Age = 10$^{7.44}$ yrs')
    #c1plt.plot(np.subtract(F435W[age745],  F555W[age745]),  F555W[age745],  
    #       'c-.', label = 'Age = 10$^{7.45}$ yrs')
    #c1plt.plot(np.subtract(F435W[age746],  F555W[age746]),  F555W[age746],  
    #       'r--', label = 'Age = 10$^{7.46}$ yrs') 
    #c1plt.plot(np.subtract(F435W[age747],  F555W[age747]),  F555W[age747],  
    #       'y-' , label = 'Age = 10$^{7.47}$ yrs')
    #c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
    #       'y-', label = 'Age = 10$^{7.5}$ yrs')
    #c1plt.plot(np.subtract(F435W[age758],  F555W[age758]),  F555W[age758],  
    #       'b--', label = 'Age = 10$^{7.58}$ yrs')
###########################################################################
#c1plt.scatter(np.subtract(f435f555_4[0][0][overlapL],   f435f555_4[0][1][overlapL]),
#              f435f555_4[0][1][overlapL],label = "Shared Points",  
                        #c='r',marker="D")
#c1plt.errorbar(np.subtract(Apn435[s4],   Apn555[s4]),   
#               Abs555[s4], UncXl[s4],   UncYl[s4], 
#               fmt=None, ecolor="k", marker=None, mew=0 )
#c1plt.scatter(np.subtract(Apn435[s4],   Apn555[s4]),
#               Abs555[s4], label = 'R = ' + str(round(dist*(math.tan(radius[4]*conver)),-2)) + " AU",
#               c='k',marker='d')
#c1plt.errorbar(np.subtract(Apn435[s3],   Apn555[s3]),   
#               Abs555[s3], UncXl[s3],   UncYl[s3], 
#               fmt=None, ecolor="r", marker=None, mew=0 )
#c1plt.scatter(np.subtract(Apn435[s3],   Apn555[s3]),
#               Abs555[s3], label = 'R = ' + str(round(dist*(math.tan(radius[3]*conver)),-2)) + " AU",
#               c='r',marker='d')       
#c1plt.errorbar(np.subtract(Apn435[s2],   Apn555[s2]),   
#               Abs555[s2], UncXl[s2],   UncYl[s2], 
#               fmt=None, ecolor="g", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s2],   Apn555[s2]),
               Abs555[s2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[2]*conver)),-2)) + " AU",
               c='r',marker='d')           
#c1plt.errorbar(np.subtract(Apn435[s1],   Apn555[s1]),   
               #Abs555[s1], UncXl[s1],   UncYl[s1], 
               #fmt=None, ecolor="b", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s1],   Apn555[s1]),
               Abs555[s1], label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[1]*conver)),-2)) + " AU",
               c='y',marker='d') 
c1plt.errorbar(np.subtract(Apn435[s0],   Apn555[s0]),   
               Abs555[s0], UncXl[s0],   UncYl[s0], 
               fmt=None, ecolor="c", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s0],   Apn555[s0]),
               Abs555[s0], label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,#str(round(dist*(math.tan(radius[0]*conver)),-2))+ " AU",
               c='c',marker='d')   
###########################################################################
"""for i in range(len(f435f555[0][0])):
    c1plt.annotate('', xy=(np.subtract(f435f555[0][2][i],   f435f555[0][3][i]),f435f555[0][3][i]), 
            xycoords = 'data', #(Top of the arrow)
            xytext = (np.subtract(f435f555[0][2][i],   f435f555[0][3][i])+.5,f435f555[0][3][i]+.5), textcoords = 'data', # End of the arrow
           arrowprops = {'arrowstyle':'->'})
    #c1plt.annotate('S'+str(i+1), xy=(0.2,-5.2), xycoords = 'data',
    #             xytext = (np.subtract(f435f555[0][2][i],   f435f555[0][3][i]),f435f555[0][3][i]), 
    #            textcoords = 'offset points')
                
   
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
"""
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
c2plt.xaxis.set_major_locator(MultipleLocator(.5))

###########################################################################
#c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
#           'r--', label = 'Age = 10$^{7.0}$ yrs')
if (title == 'SN08ha'):   
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
    c2plt.plot(np.subtract(F625W[age772],  F814W[age772]),  F814W[age772],  
           'k--' , label = 'Age = 10$^{7.72}$ yrs')   
    #c2plt.plot(np.subtract(F625W[age773],  F814W[age773]),  F814W[age773],  
    #       'k--' , label = 'Age = 10$^{7.73}$ yrs')  
    #c2plt.plot(np.subtract(F625W[age774],  F814W[age774]),  F814W[age774],  
    #       'g-' , label = 'Age = 10$^{7.74}$ yrs')
    #c2plt.plot(np.subtract(F625W[age775],  F814W[age775]),  F814W[age775],  
    #       'b-' , label = 'Age = 10$^{7.75}$ yrs')
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
    #c2plt.plot(np.subtract(F625W[age731],  F814W[age731]),  F814W[age731],  
    #       'k--' , label = 'Age = 10$^{7.31}$ yrs')
    #c2plt.plot(np.subtract(F625W[age732],  F814W[age732]),  F814W[age732],  
    #       'k--' , label = 'Age = 10$^{7.32}$ yrs')
    #c2plt.plot(np.subtract(F625W[age733],  F814W[age733]),  F814W[age733],  
    #       'g-' , label = 'Age = 10$^{7.33}$ yrs')
    #c2plt.plot(np.subtract(F625W[age734],  F814W[age734]),  F814W[age734],  
    #       'y-' , label = 'Age = 10$^{7.34}$ yrs')
    c2plt.plot(np.subtract(F625W[age735],  F814W[age735]),  F814W[age735],  
           'k--' , label = 'Age = 10$^{7.35}$ yrs')
    #c2plt.plot(np.subtract(F625W[age736],  F814W[age736]),  F814W[age736],  
    #       'm-' , label = 'Age = 10$^{7.36}$ yrs')
    #c2plt.plot(np.subtract(F625W[age737],  F814W[age737]),  F814W[age737],  
    #       'g--' , label = 'Age = 10$^{7.37}$ yrs')
    #c2plt.plot(np.subtract(F625W[age738],  F814W[age738]),  F814W[age738],  
    #       'b-' , label = 'Age = 10$^{7.38}$ yrs')
    #c2plt.plot(np.subtract(F625W[age739],  F814W[age739]),  F814W[age739],  
    #       'c-', label = 'Age = 10$^{7.39}$ yrs')
    #c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
    #       'b:' , label = 'Age = 10$^{7.4}$ yrs')
    #c2plt.plot(np.subtract(F625W[age741],  F814W[age741]),  F814W[age741],  
    #       'k--' , label = 'Age = 10$^{7.41}$ yrs')
    #c2plt.plot(np.subtract(F625W[age742],  F814W[age742]),  F814W[age742],  
    #       'k--' , label = 'Age = 10$^{7.42}$ yrs')
    #c2plt.plot(np.subtract(F625W[age743],  F814W[age743]),  F814W[age743],  
    #       'g-' , label = 'Age = 10$^{7.43}$ yrs')
    #c2plt.plot(np.subtract(F625W[age744],  F814W[age744]),  F814W[age744],  
    #       'y-' , label = 'Age = 10$^{7.44}$ yrs')
    #c2plt.plot(np.subtract(F625W[age745],  F814W[age745]),  F814W[age745],  
    #       'r:' , label = 'Age = 10$^{7.45}$ yrs')
    #c2plt.plot(np.subtract(F625W[age746],  F814W[age746]),  F814W[age746],  
    #       'm-' , label = 'Age = 10$^{7.46}$ yrs')
    #c2plt.plot(np.subtract(F625W[age747],  F814W[age747]),  F814W[age747],  
    #       'g--' , label = 'Age = 10$^{7.47}$ yrs')
    #c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
    #      'c-.', label = 'Age = 10$^{7.5}$ yrs')
    #c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
    #       'r--', label = 'Age = 10$^{7.6}$ yrs')
    #c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
    #       'y-' , label = 'Age = 10$^{7.7}$ yrs')
elif (title == 'SN10el'): 
    #plt.annotate('A${_v}}$ = ' + str(A625814) , xy=(0.5, -7.0), xytext=(1.1, -5.5),
    #         arrowprops=dict(arrowstyle="->",
    #                        connectionstyle="arc3"),)
    
    plt.annotate('', xy=(1.0, -5.376), xycoords = 'data',
                 xytext = (1.625, -4), textcoords = 'data',
                    arrowprops = {'arrowstyle':'->'})
    plt.annotate('A${_v}}$ = 2.2016', xy=(.9,-3.8), xycoords = 'data',
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
    c2plt.plot(np.subtract(F625W[age781], F814W[age781]), F814W[age781],  
           'k--' , label = 'Age = 10$^{7.81}$ yrs')    
    #c2plt.plot(np.subtract(F625W[age782], F814W[age782]), F814W[age782],  
    #       'y--', label = 'Age = 10$^{7.82}$ yrs')
    #c2plt.plot(np.subtract(F625W[age783], F814W[age783]), F814W[age783],  
    #       'g--', label = 'Age = 10$^{7.83}$ yrs')
    #c2plt.plot(np.subtract(F625W[age784], F814W[age784]), F814W[age784],  
    #       'b--' , label = 'Age = 10$^{7.84}$ yrs')
    #c2plt.plot(np.subtract(F625W[age785], F814W[age785]), F814W[age785],  
    #       'm--' , label = 'Age = 10$^{7.85}$ yrs')
    #c2plt.plot(np.subtract(F625W[age786], F814W[age786]), F814W[age786],  
    #       'r--' , label = 'Age = 10$^{7.86}$ yrs')
    #c2plt.plot(np.subtract(F625W[age787], F814W[age787]), F814W[age787],  
    #       'k--' , label = 'Age = 10$^{7.87}$ yrs')    
    #c2plt.plot(np.subtract(F625W[age788], F814W[age788]), F814W[age788],  
    #       'g--', label = 'Age = 10$^{7.88}$ yrs')
    #c2plt.plot(np.subtract(F625W[age789], F814W[age789]), F814W[age789],  
    #       'b--' , label = 'Age = 10$^{7.89}$ yrs')
    #c2plt.plot(np.subtract(F625W[age79], F814W[age79]), F814W[age79],  
    #       'm--' , label = 'Age = 10$^{7.9}$ yrs')
    #c2plt.plot(np.subtract(F625W[age80],  F814W[age80]),  F814W[age80],  
    #       'b:' , label = 'Age = 10$^{8.0}$ yrs')  
elif (title == 'SN08ge'): 
    #c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
    #       'y-', label = 'Age = 10$^{7.0}$ yrs')
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'm-', label = 'Age = 10$^{7.1}$ yrs')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Age = 10$^{7.2}$ yrs')
    #c2plt.plot(np.subtract(F625W[age721],  F814W[age721]),  F814W[age721],  
    #       'k--' , label = 'Age = 10$^{7.21}$ yrs')
    #c2plt.plot(np.subtract(F625W[age722],  F814W[age722]),  F814W[age722],  
    #       'c--' , label = 'Age = 10$^{7.22}$ yrs')
    #c2plt.plot(np.subtract(F625W[age723],  F814W[age723]),  F814W[age723],  
    #       'g--' , label = 'Age = 10$^{7.23}$ yrs')
    #c2plt.plot(np.subtract(F625W[age724],  F814W[age724]),  F814W[age724],  
    #       'y-' , label = 'Age = 10$^{7.24}$ yrs')
    #c2plt.plot(np.subtract(F625W[age725],  F814W[age725]),  F814W[age725],  
    #       'r:' , label = 'Age = 10$^{7.25}$ yrs')
    #c2plt.plot(np.subtract(F625W[age726],  F814W[age726]),  F814W[age726],  
    #       'y-' , label = 'Age = 10$^{7.26}$ yrs')
    #c2plt.plot(np.subtract(F625W[age727],  F814W[age727]),  F814W[age727],  
    #       'y-' , label = 'Age = 10$^{7.27}$ yrs')
    #c2plt.plot(np.subtract(F625W[age728],  F814W[age728]),  F814W[age728],  
    #       'g--' , label = 'Age = 10$^{7.28}$ yrs')
    c2plt.plot(np.subtract(F625W[age729],  F814W[age729]),  F814W[age729],  
           'c-', label = 'Age = 10$^{7.29}$ yrs')
    #c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
    #       'k--', label = 'Age = 10$^{7.3}$ yrs')
    #c2plt.plot(np.subtract(F625W[age731],  F814W[age731]),  F814W[age731],  
    #       'k--' , label = 'Age = 10$^{7.31}$ yrs')
    #c2plt.plot(np.subtract(F625W[age732],  F814W[age732]),  F814W[age732],  
    #       'c--' , label = 'Age = 10$^{7.32}$ yrs')
    #c2plt.plot(np.subtract(F625W[age733],  F814W[age733]),  F814W[age733],  
    #       'g--' , label = 'Age = 10$^{7.33}$ yrs')
    c2plt.plot(np.subtract(F625W[age734],  F814W[age734]),  F814W[age734],  
           'y-' , label = 'Age = 10$^{7.34}$ yrs')
    #c2plt.plot(np.subtract(F625W[age735],  F814W[age735]),  F814W[age735],  
    #       'y--' , label = 'Age = 10$^{7.35}$ yrs')
    #c2plt.plot(np.subtract(F625W[age736],  F814W[age736]),  F814W[age736],  
    #       'y-' , label = 'Age = 10$^{7.36}$ yrs')
    #c2plt.plot(np.subtract(F625W[age737],  F814W[age737]),  F814W[age737],  
    #       'y-' , label = 'Age = 10$^{7.37}$ yrs')
    #c2plt.plot(np.subtract(F625W[age738],  F814W[age738]),  F814W[age738],  
    #       'y-' , label = 'Age = 10$^{7.38}$ yrs')
    #c2plt.plot(np.subtract(F625W[age739],  F814W[age739]),  F814W[age739],  
    #       'c-', label = 'Age = 10$^{7.39}$ yrs')
    #c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
    #       'b:', label = 'Age = 10$^{7.4}$ yrs')
    #c2plt.plot(np.subtract(F625W[age741],  F814W[age741]),  F814W[age741],  
    #       'k--' , label = 'Age = 10$^{7.41}$ yrs')
    #c2plt.plot(np.subtract(F625W[age742],  F814W[age742]),  F814W[age742],  
    #       'c--' , label = 'Age = 10$^{7.42}$ yrs')
    #c2plt.plot(np.subtract(F625W[age743],  F814W[age743]),  F814W[age743],  
    #      'g--' , label = 'Age = 10$^{7.43}$ yrs')
    #c2plt.plot(np.subtract(F625W[age744],  F814W[age744]),  F814W[age744],  
    #       'k--' , label = 'Age = 10$^{7.44}$ yrs')
    #c2plt.plot(np.subtract(F625W[age745],  F814W[age745]),  F814W[age745],  
    #       'r:' , label = 'Age = 10$^{7.45}$ yrs')
    #c2plt.plot(np.subtract(F625W[age746],  F814W[age746]),  F814W[age746],  
    #       'm--' , label = 'Age = 10$^{7.46}$ yrs')
    #c2plt.plot(np.subtract(F625W[age747],  F814W[age747]),  F814W[age747],  
    #       'g--' , label = 'Age = 10$^{7.47}$ yrs')
    #c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
    #       'y--', label = 'Age = 10$^{7.5}$ yrs')
    #c2plt.plot(np.subtract(F625W[age751],  F814W[age751]),  F814W[age751],  
    #       'k--', label = 'Age = 10$^{7.51}$ yrs')
    #c2plt.plot(np.subtract(F625W[age752],  F814W[age752]),  F814W[age752],  
    #       'c--', label = 'Age = 10$^{7.52}$ yrs')
    #c2plt.plot(np.subtract(F625W[age753],  F814W[age753]),  F814W[age753],  
    #       'g--', label = 'Age = 10$^{7.53}$ yrs')
    #c2plt.plot(np.subtract(F625W[age754],  F814W[age754]),  F814W[age754],  
    #       'y-', label = 'Age = 10$^{7.54}$ yrs')
    #c2plt.plot(np.subtract(F625W[age755],  F814W[age755]),  F814W[age755],  
    #       'r:', label = 'Age = 10$^{7.55}$ yrs')
    #c2plt.plot(np.subtract(F625W[age756],  F814W[age756]),  F814W[age756],  
    #       'm--', label = 'Age = 10$^{7.56}$ yrs')
    #c2plt.plot(np.subtract(F625W[age757],  F814W[age757]),  F814W[age757],  
    #       'g--', label = 'Age = 10$^{7.57}$ yrs')
    #c2plt.plot(np.subtract(F625W[age758],  F814W[age758]),  F814W[age758],  
    #       'b--', label = 'Age = 10$^{7.58}$ yrs')
    #c2plt.plot(np.subtract(F625W[age759],  F814W[age759]),  F814W[age759],  
    #       'r--', label = 'Age = 10$^{7.59}$ yrs')
    #c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
    #       'g:', label = 'Age = 10$^{7.6}$ yrs')
    #c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
    #       'c-', label = 'Age = 10$^{7.7}$ yrs')
    #c2plt.plot(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  
    #       'b:', label = 'Age = 10$^{7.8}$ yrs')
###########################################################################
#c2plt.scatter(np.subtract(f625f814_4[0][0][overlapR],   f625f814_4[0][1][overlapR]),
#              f625f814_4[0][1][overlapR],label = "Shared Points",  
#                        c='r',marker="D")
             
#c2plt.errorbar(np.subtract(Apn625[r4],   Apn814[r4]),   
#               Abs814[r4], UncXr[r4],   UncYr[r4], 
#               fmt=None, ecolor="k", marker=None, mew=0 )
#c2plt.scatter(np.subtract(Apn625[r4],   Apn814[r4]),
#               Abs814[r4], label = 'R = ' + str(round(dist*(math.tan(radius[4]*conver)),-2)) + " AU",
#               c='k',marker='d')
#c2plt.errorbar(np.subtract(Apn625[r3],   Apn814[r3]),   
#               Abs814[r3], UncXr[r3],   UncYr[r3], 
#               fmt=None, ecolor="r", marker=None, mew=0 )
#c2plt.scatter(np.subtract(Apn625[r3],   Apn814[r3]),
#               Abs814[r3], label = 'R = ' + str(round(dist*(math.tan(radius[3]*conver)),-2)) + " AU",
#               c='r',marker='d')       
#c2plt.errorbar(np.subtract(Apn625[r2],   Apn814[r2]),   
#               Abs814[r2], UncXr[r2],   UncYr[r2], 
#               fmt=None, ecolor="g", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r2],   Apn814[r2]),
               Abs814[r2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[2]*conver)),-2)) + " AU",
               c='r',marker='d')           
#c2plt.errorbar(np.subtract(Apn625[r1],   Apn814[r1]),   
               #Abs814[r1], UncXr[r1],   UncYr[r1], 
               #fmt=None, ecolor="b", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r1],   Apn814[r1]),
               Abs814[r1], label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[1]*conver)),-2)) + " AU",
               c='y',marker='d') 
c2plt.errorbar(np.subtract(Apn625[r0],   Apn814[r0]),   
               Abs814[r0], UncXr[r0],   UncYr[r0], 
               fmt=None, ecolor="c", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r0],   Apn814[r0]),
               Abs814[r0], label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius[0]*conver)),-2)) + " AU",
               c='c',marker='d')                        


###########################################################################

if (title == 'SN08ha'): 
    sn435 = -4.04 #-4.09376
    sn555 = -4.5  #-4.48311864407
    sn625 = -4.3  #-4.50531617647
    sn814 = -4.5  #-3.37183193277
elif (title == 'SN10ae'):
    sn435 = -4.04249230769#-3.62
    sn555 = -4.32949019608#-4.0#3.78
    sn625 = -4.42041580756#-4.2#4.10
    sn814 = -4.66327731092#-3.83
elif (title == 'SN10el'):
    sn435 = -2.86694202899
    sn555 = -3.3699483871
    sn625 = -3.49584816754
    sn814 = -3.171453125
elif (title == 'SN08ge'):
    sn435 = -4.65271111111#-4.17#-3.93
    sn555 = -5.37180645161#-4.56#-4.41
    sn625 = -5.56276436782#-5.03#-4.96
    sn814 = -5.16993814433#-5.2#-5.05
#############
s1 = -1 
b1 = -4.0
x2 = 3
y1 = (s1*x2) + b1
x1 = sn435 - sn555 #.48# np.subtract(horz1,b1)/s1

ptsR = np.array([[-3,yLmax],
                 [-3,sn555],
                 [x1,sn555], #need the x value
                 [x2,y1],           
                 [x2,yLmax]])
polyR = Polygon(ptsR, color='grey', alpha=0.15,closed = True)

c1plt.add_patch(polyR)
#############
s4 = -1 
b4 = -5.0
x4 = 3 
y4 = (s4*x4) + b4
x3 = sn625 - sn814  #.1#np.subtract(horz,b4)/s4

pts = np.array([[-3,yRmax],
                [-3,sn814],
                [x3,sn814], 
                [x4,y4],           
                [x4,yRmax]])
poly = Polygon(pts, color='grey', alpha=0.15,closed = True)

c2plt.add_patch(poly)

###########################################################################
"""
#Annotate!
for i in range(len(Apn435[s2])-1):
    c1plt.annotate(str(i+1), xy=(np.subtract(Apn435[s2][i], Apn555[s2][i]),Abs555[s2][i]), 
               xytext=(np.subtract(Apn435[s2][i], Apn555[s2][i])+.2,Abs555[s2][i]-.2),
                #textcoords='offset points',
            arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
            )               

c1plt.annotate(str(7), xy=(np.subtract(Apn435[s2][5], Apn555[s2][5]),Abs555[s2][5]), 
     xytext=(np.subtract(Apn435[s2][5], Apn555[s2][5])+.2,Abs555[s2][5]-.2),
     #textcoords='offset points',
     arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
     )   
              
for i in range(len(Apn625[r2])):
    c2plt.annotate(str(i+1), xy=(np.subtract(Apn625[r2][i], Apn814[r2][i]),Abs814[r2][i]), 
               xytext=(np.subtract(Apn625[r2][i], Apn814[r2][i])+.2,Abs814[r2][i]-.2),
                #textcoords='offset points',
            arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
            ) 
"""
###########################################################################
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c1plt.set_ylim(bottom=yLmax, top=yLmin)
c1plt.set_xlim(xLmax,xLmin)
c2plt.set_ylim(bottom=yRmax, top=yRmin)  
c2plt.set_xlim(xRmax,xRmin)
########################################################################### 
plt.tight_layout()
plt.subplots_adjust(top=0.90)
########################################################################### 
#figname = title + '_' + 'Z' + name[1:-7]+ '.png'
figname = title + '_' + 'test' + '.png'
plt.savefig('Figures/'+ figname)
print "Save and show plot : " + figname
