# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 13:51:48 2014

@author: Nova
"""

from __future__ import division
import numpy               as np
import matplotlib.pyplot   as plt
import matplotlib.gridspec as gridspec
import pickle
from matplotlib.ticker  import MultipleLocator 
from matplotlib.ticker  import AutoMinorLocator
from matplotlib.patches import Polygon

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
title = 'SN08ge'

# Set the plotted point S/N parameters
start      = 0 # start = 0 starts at S/N 3
end        = 1 # end = 2 goes to S/N 4
snt        = 3
snb        = 3
#####################################################################

name = 'Z0170Y26.dat' #'Z0001Y26.dat'

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
age763   = np.where((logAGE == 7.63))
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

radius   = [10,17,23,34,50]#[10,50,100,150,200]
#radius     = [200]
f435f555   = []
f625f814   = []

if (title == 'SN08ge'):
    yLmax    = -2.0
    yLmin    = -6.5
    yRmax    = -3.0
    yRmin    = -8.0
    f435f555.append(pickle.load(open('SN2008GE/sn2008ge_f435f555.p', 'rb')))    
    f625f814.append(pickle.load(open('SN2008GE/sn2008ge_f625f814.p', 'rb')))    
    
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
s3 = np.where(Radl <= radius[3])
s4 = np.where(Radl <= radius[4])

r0 = np.where(Radr <= radius[0])
r1 = np.where(Radr <= radius[1])
r2 = np.where(Radr <= radius[2])
r3 = np.where(Radr <= radius[3])
r4 = np.where(Radr <= radius[4])

###########################################################################
print "Begin plotting Isochrones..."
h = [2, 4] # height of the plotted figure
fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

fig1.suptitle('CMD for SN 2008ge',fontdict = font, size=15)

###########################################################################
c1plt = plt.subplot2grid((2,2), (0,0), rowspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W (mag)",fontdict = font)
plt.ylabel("M$_{F555W}$ (mag)",fontdict = font)

c1plt.xaxis.set_minor_locator(AutoMinorLocator()) 
c1plt.yaxis.set_minor_locator(AutoMinorLocator())

c1plt.yaxis.set_major_locator(MultipleLocator(.5))

###########################################################################
#if (title == 'SN08ge'):
#    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
#           'b:', label = 'Age = 10$^{7.6}$ yrs')
#    c1plt.plot(np.subtract(F435W[age765],  F555W[age765]),  F555W[age765],  
#           'g:', label = 'Age = 10$^{7.65}$ yrs')
    #c1plt.plot(np.subtract(F435W[age773],  F555W[age773]),  F555W[age773],  
           #'r--', label = 'Age = 10$^{7.73}$ yrs')

#plt.annotate('', xy=(1.992,-6.1), xycoords = 'data', #(Top of the arrow)
#             xytext = (2, -3.5), textcoords = 'data', # End of the arrow
#                arrowprops = {'arrowstyle':'->'})       # what the arrow looks like
#plt.annotate('A${_v}}$ = 3.6', xy=(0.0,-5.5), xycoords = 'data', # coord of term
#             xytext = (2, 3), textcoords = 'offset points')

c1plt.errorbar(np.subtract(Apn435[r4],   Apn555[r4]),   
               Abs555[r4], UncXl[r4],   UncYl[r4], 
               fmt=None, ecolor="k", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[r4],   Apn555[r4]),
               Abs555[r4], label = 'R = ' + str(radius[4]) + " Pc",
               c='k',marker='d')
c1plt.errorbar(np.subtract(Apn435[r3],   Apn555[r3]),   
               Abs555[r3], UncXl[r3],   UncYl[r3], 
               fmt=None, ecolor="r", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[r3],   Apn555[r3]),
               Abs555[r3], label = 'R = ' + str(radius[3]) + " Pc",
               c='r',marker='d')       
c1plt.errorbar(np.subtract(Apn435[r2],   Apn555[r2]),   
               Abs555[r2], UncXl[r2],   UncYl[r2], 
               fmt=None, ecolor="g", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[r2],   Apn555[r2]),
               Abs555[r2], label = 'R = ' + str(radius[2]) + " Pc",
               c='g',marker='d')           
c1plt.errorbar(np.subtract(Apn435[r1],   Apn555[r1]),   
               Abs555[r1], UncXl[r1],   UncYl[r1], 
               fmt=None, ecolor="b", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[r1],   Apn555[r1]),
               Abs555[r1], label = 'R = ' + str(radius[1]) + " Pc",
               c='b',marker='d') 
c1plt.errorbar(np.subtract(Apn435[r0],   Apn555[r0]),   
               Abs555[r0], UncXl[r0],   UncYl[r0], 
               fmt=None, ecolor="c", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[r0],   Apn555[r0]),
               Abs555[r0], label = 'R = ' + str(radius[0]) + " Pc",
               c='c',marker='d')   
               
########################################################################### 
###########################################################################
###########################################################################  
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
#c1plt.set_ylim(bottom=yLmax, top=yLmin)
#c1plt.set_xlim(-2,2)
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
#if (title == 'SN08ge'):    
#    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
#           'b:', label = 'Age = 10$^{7.6}$ yrs')
#    c2plt.plot(np.subtract(F625W[age765],  F814W[age765]),  F814W[age765],
#           'g:' , label = 'Age = 10$^{7.65}$ yrs')
    #c2plt.plot(np.subtract(F625W[age773],  F814W[age773]),  F814W[age773],  
    #       'r--' , label = 'Age = 10$^{7.73}$ yrs')  
                              
#plt.annotate('', xy=(1.99,-6), xycoords = 'data',
#             xytext = (2, -3.5), textcoords = 'data',
#                arrowprops = {'arrowstyle':'->'})
#plt.annotate('A${_v}}$ = 2.5', xy=(0.0,-6.5), xycoords = 'data',
#             xytext = (2, 3), textcoords = 'offset points')
             
c2plt.errorbar(np.subtract(Apn625[r4],   Apn814[r4]),   
               Abs814[r4], UncXr[r4],   UncYr[r4], 
               fmt=None, ecolor="k", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r4],   Apn814[r4]),
               Abs814[r4], label = 'R = ' + str(radius[4]) + " Pc",
               c='k',marker='d')
c2plt.errorbar(np.subtract(Apn625[r3],   Apn814[r3]),   
               Abs814[r3], UncXr[r3],   UncYr[r3], 
               fmt=None, ecolor="r", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r3],   Apn814[r3]),
               Abs814[r3], label = 'R = ' + str(radius[3]) + " Pc",
               c='r',marker='d')       
c2plt.errorbar(np.subtract(Apn625[r2],   Apn814[r2]),   
               Abs814[r2], UncXr[r2],   UncYr[r2], 
               fmt=None, ecolor="g", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r2],   Apn814[r2]),
               Abs814[r2], label = 'R = ' + str(radius[2]) + " Pc",
               c='g',marker='d')           
c2plt.errorbar(np.subtract(Apn625[r1],   Apn814[r1]),   
               Abs814[r1], UncXr[r1],   UncYr[r1], 
               fmt=None, ecolor="b", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r1],   Apn814[r1]),
               Abs814[r1], label = 'R = ' + str(radius[1]) + " Pc",
               c='b',marker='d') 
c2plt.errorbar(np.subtract(Apn625[r0],   Apn814[r0]),   
               Abs814[r0], UncXr[r0],   UncYr[r0], 
               fmt=None, ecolor="c", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r0],   Apn814[r0]),
               Abs814[r0], label = 'R = ' + str(radius[0]) + " Pc",
               c='c',marker='d')                        

###########################################################################

c1plt.set_xlim(-1, 3)
c2plt.set_xlim(-.8, 1.2)
s1 = -1 
horz1 = -4.4 
b1 = -4.0
x2 = 4
y1 = (s1*x2) + b1
x1 = .48# np.subtract(horz1,b1)/s1


ptsR = np.array([[-3,yLmax],
                 [-3,horz1],
                 [x1,horz1], #need the x value
                 [x2,y1],           
                 [x2,yLmax]])
polyR = Polygon(ptsR, color='grey', alpha=0.15,closed = True)

c1plt.add_patch(polyR)
#############
horz = -5.3
s4 = -1 
b4 = -5.0
x4 = 4 
y4 = (s4*x4) + b4
x3 = .1#np.subtract(horz,b4)/s4


pts = np.array([[-3,yRmax],
                [-3,horz],
                [x3,horz], 
                [x4,y4],           
                [x4,yRmax]])
poly = Polygon(pts, color='grey', alpha=0.15,closed = True)

c2plt.add_patch(poly)

###########################################################################
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c1plt.set_ylim(bottom=yLmax, top=yLmin)
c1plt.set_xlim(-2,3.3)
#12Z
#14dt
#redding remove and see what happens
#instead of bad list, make constraints
c2plt.set_ylim(bottom=yRmax, top=yRmin)  
c2plt.set_xlim(-1,3)
########################################################################### 
plt.tight_layout()
plt.subplots_adjust(top=0.90)
########################################################################### 
#figname = title + '_' + 'Z' + name[1:-7]+ '.png'
figname = title + '_' + 'rnd3'+ '.png'
plt.savefig('Figures/'+ figname)
print "Save and show plot : " + figname