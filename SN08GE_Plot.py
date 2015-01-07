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
import math
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
print "Grabbing Metallicity files"
print "1"
name = 'Z0300Y26.dat' #'Z0001Y26.dat'

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

IsoAge = 7.29
age    = np.where(logAGE == IsoAge)

#####################################################################
## CHOOSE AGE TO BE PLOTTED 
#####################################################################
print "2"
name2 = 'Z0200Y26.dat' #'Z0001Y26.dat'

d2 = []
d2.append(np.loadtxt('Metallicity/'+name2))
d2 = np.array(d2)

#print d
#print np.shape(d) #(1L, 16776L, 21L)

logAGE2 = []
F435W2  = []
F555W2  = []
F625W2  = []
F814W2  = []

logAGE2 = d2[:,:,0]
F435W2  = d2[:,:,7]
F555W2  = d2[:,:,10]
F625W2  = d2[:,:,12]
F814W2  = d2[:,:,16]

IsoAge2 = 7.3
age2    = np.where(logAGE2 == IsoAge2)

#####################################################################
#####################################################################
"""
print "3"
name3 = 'Z0100Y26.dat' #'Z0001Y26.dat'

d3 = []
d3.append(np.loadtxt('Metallicity/'+name3))
d3 = np.array(d3)

#print d
#print np.shape(d) #(1L, 16776L, 21L)

logAGE3 = []
F435W3  = []
F555W3  = []
F625W3  = []
F814W3  = []

logAGE3 = d3[:,:,0]
F435W3  = d3[:,:,7]
F555W3  = d3[:,:,10]
F625W3  = d3[:,:,12]
F814W3  = d3[:,:,16]

IsoAge3 = 7.44
age3    = np.where(logAGE3 == IsoAge3)
"""
#####################################################################
radius1   = [50,100,200]
radius2   = [38,75 ,100]
dist      = 17.95e7
conver    = (4.35)#(2.5*math.pi)/(50.0*3600*180)
f435f555  = []
f625f814  = []
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

yLmax    = -3.0
yLmin    = -8.0
yRmax    = -4.0
yRmin    = -9.0
     
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

s0 = np.where(Radl <= radius1[0])
s1 = np.where(Radl <= radius1[1])
s2 = np.where(Radl <= radius1[2])
#s3 = np.where(Radl <= radius1[3])
#s4 = np.where(Radl <= radius1[4])

r0 = np.where(Radr <= radius2[0])
r1 = np.where(Radr <= radius2[1])
r2 = np.where(Radr <= radius2[2])
#r3 = np.where(Radr <= radius2[3])
#r4 = np.where(Radr <= radius2[4])

###########################################################################
print "Begin plotting Isochrones..."
h = [2, 4] # height of the plotted figure
fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

#fig1.suptitle('CMD for SN 2008ge',fontdict = font, size=15)

fig1.suptitle(title + ': CMD with S/N >= 3.5,' + ' Z = 0.' + name[2:-9]
            + ' & Z = 0.' + name2[2:-9],
              fontdict = font, size=15)
###########################################################################
c1plt = plt.subplot2grid((2,2), (0,0), rowspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W (mag)",fontdict = font)
plt.ylabel("M$_{F555W}$ (mag)",fontdict = font)

#c1plt.xaxis.set_minor_locator(AutoMinorLocator()) 
#c1plt.yaxis.set_minor_locator(AutoMinorLocator())

#c1plt.yaxis.set_major_locator(MultipleLocator(.5))
 
###########################################################################
c1plt.plot(np.subtract(F435W[age],  F555W[age]),  F555W[age],  
           'g:',  label = 'Age = 10$^{'+ str(IsoAge) +'}$ yrs') #'Z = 0.' + name[1:-7] )#
c1plt.plot(np.subtract(F435W2[age2],  F555W2[age2]),  F555W2[age2],  
           'k--', label = 'Age = 10$^{'+ str(IsoAge2) +'}$ yrs') #'Z = 0.' + name2[1:-7] )#
#c1plt.plot(np.subtract(F435W3[age3],  F555W3[age3]),  F555W3[age3],  
#          'b-.', label = 'Z = 0.' + name3[1:-7] )#'Age = 10$^{'+ str(IsoAge3) +'}$ yrs')
           
           
           
#plt.annotate('', xy=(1.992,-6.1), xycoords = 'data', #(Top of the arrow)
#             xytext = (2, -3.5), textcoords = 'data', # End of the arrow
#                arrowprops = {'arrowstyle':'->'})       # what the arrow looks like
#plt.annotate('A${_v}}$ = 3.6', xy=(0.0,-5.5), xycoords = 'data', # coord of term
#             xytext = (2, 3), textcoords = 'offset points')
"""
c1plt.errorbar(np.subtract(Apn435[s4],   Apn555[s4]),   
               Abs555[s4], UncXl[s4],   UncYl[s4], 
               fmt=None, ecolor="k", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s4],   Apn555[s4]),
               Abs555[s4], label = 'R = ' + str(round(dist*(math.tan(radius1[4]*conver)),-2)) + " AU",
               c='k',marker='d')
"""
#c1plt.errorbar(np.subtract(Apn435[s3],   Apn555[s3]),   
#               Abs555[s3], UncXl[s3],   UncYl[s3], 
               #fmt=None, ecolor="r", marker=None, mew=0 )
#c1plt.scatter(np.subtract(Apn435[s3],   Apn555[s3]),
               #Abs555[s3], label = 'R = ' + str(round(dist*(math.tan(radius1[3]*conver)),-2))+ " AU",
               #c='r',marker='d')       
#c1plt.errorbar(np.subtract(Apn435[s2],   Apn555[s2]),   
               #Abs555[s2], UncXl[s2],   UncYl[s2], 
               #fmt=None, ecolor="g", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s2],   Apn555[s2]),
               Abs555[s2], label = 'R = ' + str(round(radius1[2]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius1[2]*conver)),-2)) + " AU",
               c='r',marker='d')           
#c1plt.errorbar(np.subtract(Apn435[s1],   Apn555[s1]),   
               #Abs555[s1], UncXl[s1],   UncYl[s1], 
               #fmt=None, ecolor="b", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s1],   Apn555[s1]),
               Abs555[s1], label = 'R = ' + str(round(radius1[1]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius1[1]*conver)),-2)) + " AU",
               c='y',marker='d') 
c1plt.errorbar(np.subtract(Apn435[s0],   Apn555[s0]),   
               Abs555[s0], UncXl[s0],   UncYl[s0], 
               fmt=None, ecolor="c", marker=None, mew=0 )
c1plt.scatter(np.subtract(Apn435[s0],   Apn555[s0]),
               Abs555[s0], label = 'R = ' + str(round(radius1[0]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius1[0]*conver)),-2)) + " AU",
               c='c',marker='d')   
"""
c1plt.annotate(str(0), xy=(np.subtract(Apn435[s4][0], Apn555[s4][0]),Abs555[s4][0]), 
               xytext=(np.subtract(Apn435[s4][0], Apn555[s4][0])-.1,Abs555[s4][0]-.1),
                arrowprops=dict(arrowstyle="->",) )
c1plt.annotate(str(11), xy=(np.subtract(Apn435[s4][1], Apn555[s4][1]),Abs555[s4][1]), 
               xytext=(np.subtract(Apn435[s4][1], Apn555[s4][1])-.1,Abs555[s4][1]-.1),
                arrowprops=dict(arrowstyle="->",) )
"""            
"""              
for i in range(len(Apn435[s4])):
    c1plt.annotate(str(i), xy=(np.subtract(Apn435[s4][i], Apn555[s4][i]),Abs555[s4][i]), 
               xytext=(np.subtract(Apn435[s4][i], Apn555[s4][i])+.1,Abs555[s4][i]-.1),
                #textcoords='offset points',
            arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
            )               
"""
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

#c2plt.tick_params(axis='both',labelbottom = font)
                  
#c2plt.xaxis.set_minor_locator(AutoMinorLocator()) 
#c2plt.yaxis.set_minor_locator(AutoMinorLocator())

#c2plt.yaxis.set_major_locator(MultipleLocator(.5))


c2plt.plot(np.subtract(F625W[age],  F814W[age]),  F814W[age],  
           'g:' , label = 'Age = 10$^{'+ str(IsoAge) +'}$ yrs') #'Z = 0.' + name[1:-7] )#
c2plt.plot(np.subtract(F625W2[age2],  F814W2[age2]),  F814W2[age2],  
           'k--', label = 'Age = 10$^{'+ str(IsoAge2) +'}$ yrs') #'Z = 0.' + name2[1:-7] )#
#c2plt.plot(np.subtract(F625W3[age3],  F814W3[age3]),  F814W3[age3],  
#           'b-.', label = 'Z = 0.' + name3[1:-7] )# 'Age = 10$^{'+ str(IsoAge3) +'}$ yrs') 

###########################################################################                         
#plt.annotate('', xy=(1.99,-6), xycoords = 'data',
#             xytext = (2, -3.5), textcoords = 'data',
#                arrowprops = {'arrowstyle':'->'})
#plt.annotate('A${_v}}$ = 2.5', xy=(0.0,-6.5), xycoords = 'data',
#             xytext = (2, 3), textcoords = 'offset points')
"""             
c2plt.errorbar(np.subtract(Apn625[r4],   Apn814[r4]),   
               Abs814[r4], UncXr[r4],   UncYr[r4], 
               fmt=None, ecolor="k", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r4],   Apn814[r4]),
               Abs814[r4], label = 'R = ' + str(round(dist*(math.tan(radius2[4]*conver)),-2)) + " AU",
               c='k',marker='d')
"""
#c2plt.errorbar(np.subtract(Apn625[r3],   Apn814[r3]),   
               #Abs814[r3], UncXr[r3],   UncYr[r3], 
               #fmt=None, ecolor="r", marker=None, mew=0 )
#c2plt.scatter(np.subtract(Apn625[r3],   Apn814[r3]),
               #Abs814[r3], label = 'R = ' + str(round(dist*(math.tan(radius2[3]*conver)),-2)) + " AU",
               #c='r',marker='d')       
#c2plt.errorbar(np.subtract(Apn625[r2],   Apn814[r2]),   
               #Abs814[r2], UncXr[r2],   UncYr[r2], 
               #fmt=None, ecolor="g", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r2],   Apn814[r2]),
               Abs814[r2], label = 'R = ' + str(round(radius2[2]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius2[2]*conver)),-2)) + " AU",
               c='r',marker='d')           
#c2plt.errorbar(np.subtract(Apn625[r1],   Apn814[r1]),   
               #Abs814[r1], UncXr[r1],   UncYr[r1], 
               #fmt=None, ecolor="b", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r1],   Apn814[r1]),
               Abs814[r1], label = 'R = ' + str(round(radius2[1]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius2[1]*conver)),-2)) + " AU",
               c='y',marker='d') 
c2plt.errorbar(np.subtract(Apn625[r0],   Apn814[r0]),   
               Abs814[r0], UncXr[r0],   UncYr[r0], 
               fmt=None, ecolor="c", marker=None, mew=0 )
c2plt.scatter(np.subtract(Apn625[r0],   Apn814[r0]),
               Abs814[r0], label = 'R = ' + str(round(radius2[0]*conver,-1)) + " pc" ,#str(round(dist*(math.tan(radius2[0]*conver)),-2)) + " AU",
               c='c',marker='d')                        

#for k in range(len(Apn814[r4])):
#        c2plt.annotate(str(k), xy=(np.subtract(Apn625[r4][k], Apn814[r4][k]),Abs814[r4][k]), 
#               xytext=(np.subtract(Apn625[r4][k], Apn814[r4][k])-.6,Abs814[r4][k]-.6),
#                arrowprops=dict(arrowstyle="->"),
#                )
   
###########################################################################
sn435 = -4.17#-3.93
sn555 = -4.56#-4.41
sn625 = -5.03#-4.96
sn814 = -5.2#-5.05
#############
s1 = -1 
b1 = -4.0
x2 = 4
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
x4 = 4 
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
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c1plt.set_ylim(bottom=yLmax, top=yLmin)
c1plt.set_xlim(-.75,2.0)
c2plt.set_ylim(bottom=yRmax, top=yRmin)  
c2plt.set_xlim(-.75,2.5)

#redding remove and see what happens
#instead of bad list, make constraints
########################################################################### 
plt.tight_layout()
plt.subplots_adjust(top=0.90)
########################################################################### 
#figname = title + '_' + 'Z' + name[1:-7]+ '.png'
figname = title + '_' + 'we13'+ '.png'
plt.savefig('Figures/'+ figname)
print "Save and show plot : " + figname