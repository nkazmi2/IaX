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
f435f555_5 = []
f625f814_5 = []
f435f555_6 = []
f625f814_6 = []
f435f555_7 = []
f625f814_7 = []
f435f555_8 = []
f625f814_8 = []



if (title == 'SN08ge'):
    #ytopmax    = -4.0
    #ytopmin    = -9.0
    #ybotmax    = -4.0
    #ybotmin    = -9.0
    ytopmax    = -3.0
    ytopmin    = -5.5
    ybotmax    = -3.0
    ybotmin    = -7.0
    f435f555_0.append(pickle.load(open('SN2008GE/sn2008ge_f435f555_sn3_rad0.p', 'rb')))    
    f625f814_0.append(pickle.load(open('SN2008GE/sn2008ge_f625f814_sn3_rad0.p', 'rb')))    
    #f435f555_1.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad1.p', 'rb')))    
    #f625f814_1.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad1.p', 'rb')))   
    #f435f555_2.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad2.p', 'rb')))    
    #f625f814_2.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad2.p', 'rb')))  
    #f435f555_3.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad3.p', 'rb')))    
    #f625f814_3.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad3.p', 'rb')))
    #f435f555_4.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad4.p', 'rb')))    
    #f625f814_4.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad4.p', 'rb')))
    """
    f435f555_5.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad5.p', 'rb')))    
    f625f814_5.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad5.p', 'rb')))   
    f435f555_6.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad6.p', 'rb')))    
    f625f814_6.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad6.p', 'rb')))  
    f435f555_7.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad7.p', 'rb')))    
    f625f814_7.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad7.p', 'rb')))
    f435f555_8.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff435f555_sn3_rad8.p', 'rb')))    
    f625f814_8.append(pickle.load(open('SN2008GE/sn2008ge_20141015_ff625f814_sn3_rad8.p', 'rb')))
    """
 

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
"""if (title == 'SN08ge'):
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'b:', label = 'Age = 10$^{7.6}$ yrs')
    #c1plt.plot(np.subtract(F435W[age765],  F555W[age765]),  F555W[age765],  
    #       'g:', label = 'Age = 10$^{7.65}$ yrs')
    #c1plt.plot(np.subtract(F435W[age773],  F555W[age773]),  F555W[age773],  
    #       'r--', label = 'Age = 10$^{7.73}$ yrs')
"""    
for i in range(start,end):
        """
        c1plt.errorbar(np.subtract(f435f555_4[i][8],   f435f555_4[i][9]),   
                       f435f555_4[i][1], f435f555_4[i][2],   f435f555_4[i][3], 
                        fmt=None, ecolor="c",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_4[i][8],   f435f555_4[i][9]),   
                      f435f555_4[i][1], label = 'R = ' + str(radius[4]) + " Pix",  
                        c='c',marker='d')
        c1plt.errorbar(np.subtract(f435f555_3[i][8],   f435f555_3[i][9]),   
                       f435f555_3[i][1], f435f555_3[i][2],   f435f555_3[i][3], 
                        fmt=None, ecolor="y",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_3[i][8],   f435f555_3[i][9]),   
                      f435f555_3[i][1], label = 'R = ' + str(radius[3]) + " Pix",  
                        c='y',marker='d')
        c1plt.errorbar(np.subtract(f435f555_2[i][8],   f435f555_2[i][9]),   
                       f435f555_2[i][1], f435f555_2[i][2],   f435f555_2[i][3], 
                        fmt=None, ecolor="b",  marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_2[i][8],   f435f555_2[i][9]),   
                      f435f555_2[i][1], label = 'R = ' + str(radius[2]) + " Pix",  
                        c='b',marker='d')
        c1plt.errorbar(np.subtract(f435f555_1[i][8],   f435f555_1[i][9]),  
                       f435f555_1[i][1], f435f555_1[i][2],   f435f555_1[i][3],
                         fmt=None, ecolor="r", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_1[i][8],   f435f555_1[i][9]),   
                      f435f555_1[i][1], label = 'R = ' + str(radius[1]) + " Pix",  
                        c='r',marker='d')        
        c1plt.errorbar(np.subtract(f435f555_0[i][8],   f435f555_0[i][9]),  
                       f435f555_0[i][1], f435f555_0[i][2],   f435f555_0[i][3],
                         fmt=None, ecolor="k", marker=None, mew=0 )
        """
        c1plt.scatter(np.subtract(f435f555_0[i][8],   f435f555_0[i][9]),   
                      f435f555_0[i][1], label = 'R = ' + str(radius[0]) + " Pix",  
                        c='k',marker='d')
        snt += 1

########################################################################### 
###########################################################################
###########################################################################  
#l = plt.legend(prop = {'family' : 'serif'},loc=4)
#l.draw_frame(False)
########################################################################### 
#c1plt.set_ylim(bottom=ytopmax, top=ytopmin)
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
"""if (title == 'SN08ge'):    
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'b:', label = 'Age = 10$^{7.6}$ yrs')
    #c2plt.plot(np.subtract(F625W[age765],  F814W[age765]),  F814W[age765],
    #       'g:' , label = 'Age = 10$^{7.65}$ yrs')
    #c2plt.plot(np.subtract(F625W[age773],  F814W[age773]),  F814W[age773],  
    #       'r--' , label = 'Age = 10$^{7.73}$ yrs')  
"""

for k in range(start,end):
        """
        c2plt.errorbar(np.subtract(f625f814_4[k][8],   f625f814_4[k][9]),   
                       f625f814_4[k][1], f625f814_4[k][2],   f625f814_4[k][3], 
                        fmt=None, ecolor="c", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_4[k][8],   f625f814_4[k][9]),   f625f814_4[k][1],
                      label = 'R = ' + str(radius[4]) + " Pix",  #'S/N >= ' + str(snb) +
                        c='c',marker='d')
        c2plt.errorbar(np.subtract(f625f814_3[k][8],   f625f814_3[k][9]),   
                       f625f814_3[k][1], f625f814_3[k][2],   f625f814_3[k][3], 
                        fmt=None, ecolor="y", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_3[k][8],   f625f814_3[k][9]),   f625f814_3[k][1],
                      label = 'R = ' + str(radius[3]) + " Pix",   #'S/N >= ' + str(snb) +
                        c='y',marker='d')
        c2plt.errorbar(np.subtract(f625f814_2[k][8],   f625f814_2[k][9]),   
                       f625f814_2[k][1], f625f814_2[k][2],   f625f814_2[k][3], 
                        fmt=None, ecolor="b", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_2[k][8],   f625f814_2[k][9]),   f625f814_2[k][1],
                      label = 'R = ' + str(radius[2]) + " Pix",   #'S/N >= ' + str(snb) +
                        c='b',marker='d')
        c2plt.errorbar(np.subtract(f625f814_1[k][8],   f625f814_1[k][9]),   
                       f625f814_1[k][1], f625f814_1[k][2],   f625f814_1[k][3], 
                        fmt=None, ecolor="r", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_1[k][8],   f625f814_1[k][9]),   f625f814_1[k][1],  #'S/N >= ' + str(snb) +   
                      label ='R = ' + str(radius[1]) + " Pix",  
                        c='r',marker='d')
        c2plt.errorbar(np.subtract(f625f814_0[k][8],   f625f814_0[k][9]),   
                       f625f814_0[k][1], f625f814_0[k][2],   f625f814_0[k][3], 
                        fmt=None, ecolor="k", marker=None, mew=0 )
        """
        c2plt.scatter(np.subtract(f625f814_0[k][8],   f625f814_0[k][9]),   f625f814_0[k][1],   
                      label = 'R = ' + str(radius[0]) + " Pix",   #'S/N >= ' + str(snb) +
                        c='k',marker='d')
        snb += 1

###########################################################################
#This was an iffy move,using the sn =3 of a point that's not plotted, I don't like it
"""
c1plt.set_xlim(-1, 3)
c2plt.set_xlim(-.8, 1.2)
s1 = -1 
horz1 = -4.0 
b1 = -4.0
x2 = 4
y1 = (s1*x2) + b1
x1 = 1.5# np.subtract(horz1,b1)/s1


ptsR = np.array([[-4,ytopmax],
                 [-4,horz1],
                 [x1,horz1], #need the x value
                 [x2,y1],           
                 [x2,ytopmax]])
polyR = Polygon(ptsR, color='grey', alpha=0.15,closed = True)

c1plt.add_patch(polyR)
#############
horz = -4.0
s4 = -1 
b4 = -4.0
x4 = 1.5 
y4 = (s4*x4) + b4
x3 = np.subtract(horz,b4)/s4


pts = np.array([[-2,ybotmax],
                [-2,horz],
                [x3,horz], 
                [x4,y4],           
                [x4,ybotmax]])
poly = Polygon(pts, color='grey', alpha=0.15,closed = True)

c2plt.add_patch(poly)
"""

###########################################################################
#l = plt.legend(prop = {'family' : 'serif'},loc=4)
#l.draw_frame(False)
########################################################################### 
#c2plt.set_ylim(bottom=ybotmax, top=ybotmin) 
########################################################################### 
plt.tight_layout()
plt.subplots_adjust(top=0.90)
########################################################################### 
#figname = title + '_' + 'Z' + name[1:-7]+ '.png'
figname = title + '_' + 'total'+ '.png'
plt.savefig('Figures/'+ figname)
print "Save and show plot : " + figname
