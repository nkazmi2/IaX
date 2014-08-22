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
#import random 

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
ytopmin    = -8.0
ybotmax    = -2.0
ybotmin    = -9.0
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
ytopmax    = -1.0
ytopmin    = -11.0
ybotmax    = -4.0
ybotmin    = -9.0
for i in range(3,6):
    f435f555_0.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad0.p', 'rb')))    
    f625f814_0.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad0.p', 'rb')))    
    f435f555_1.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad1.p', 'rb')))    
    f625f814_1.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad1.p', 'rb')))   
    f435f555_2.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad2.p', 'rb')))    
    f625f814_2.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad2.p', 'rb')))  
    f435f555_3.append(pickle.load(open('SN2010AE/sn2010ae_f435f555_sn'+ str(i) +'_rad3.p', 'rb')))    
    f625f814_3.append(pickle.load(open('SN2010AE/sn2010ae_f625f814_sn'+ str(i) +'_rad3.p', 'rb')))

"""
""" 7.7 -> 8.0
title      = 'SN10el'

ytopmax    = -2.0
ytopmin    = -8.0
ybotmax    = -2.0
ybotmin    = -8.0

#ytopmax    = -5.0
#ytopmin    = -9.0
#ybotmax    = -5.0
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
    
#    f435f555_0.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad0.p', 'rb')))    
#    f625f814_0.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad0.p', 'rb')))    
#    f435f555_1.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad1.p', 'rb')))    
#    f625f814_1.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad1.p', 'rb')))   
#    f435f555_2.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad2.p', 'rb')))    
#    f625f814_2.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad2.p', 'rb')))  
#    f435f555_3.append(pickle.load(open('SN2010EL/sn2010el_f435f555_sn'+ str(i) +'_red_rad3.p', 'rb')))    
#    f625f814_3.append(pickle.load(open('SN2010EL/sn2010el_f625f814_sn'+ str(i) +'_red_rad3.p', 'rb')))

"""
#####################################################################

print "Begin plotting Isochrones..."
h = [2, 5] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)
#plots = plt.subplot(gs[0])

c1plt = plt.subplot2grid((2,2), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W (mag)",fontdict = font)
plt.ylabel("M$_{F555W}$ (mag)",fontdict = font)
    

if (title == 'SN08ge'):
    c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
           'y-', label = 'Log(Age) = 7.1')
    c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
           'g:', label = 'Log(Age) = 7.2')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Log(Age) = 7.3')
elif (title == 'SN08ha'):          
    #c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
    #       'y-', label = 'Log(Age) = 7.1')
    #c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
    #       'g:', label = 'Log(Age) = 7.2')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Log(Age) = 7.3')
    c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
    c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Log(Age) = 7.6')
elif (title == 'SN10ae'):  
    c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
           'y-', label = 'Log(Age) = 7.1')
    c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
           'g:', label = 'Log(Age) = 7.2')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Log(Age) = 7.3')
    c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
    c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Log(Age) = 7.6') 
elif (title == 'SN10el'):  
    """
    c1plt.plot(np.subtract(F435W[age70],  F555W[age70]),  F555W[age70],  
           'r--', label = 'Log(Age) = 7.0')
    c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
           'y-', label = 'Log(Age) = 7.1')
    c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
           'g:', label = 'Log(Age) = 7.2')
    c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
           'c-', label = 'Log(Age) = 7.3')
    """
    c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
    c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
    c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
           'r--', label = 'Log(Age) = 7.6') 
    c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
           'y-' , label = 'Log(Age) = 7.7')
    c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
           'g:' , label = 'Log(Age) = 7.8')

    #c1plt.plot(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  
    #       'c-.', label = 'Log(Age) = 7.9') 
    #c1plt.plot(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  
    #       'b:' , label = 'Log(Age) = 8.0')  
###########################################################################

for i in range(start,end):
        #c1plt.errorbar(np.subtract(f435f555_4[i][0],   f435f555_4[i][1]),   
        #               f435f555_4[i][1], f435f555_4[i][2],   f435f555_4[i][3], 
        #                fmt=None, marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_4[i][0],   f435f555_4[i][1]),   
                      f435f555_4[i][1], label = 'S/N >= ' + str(snt) +' Radius ' + str(radius[4]) + " PC",  
                        c='c',marker='D')
        #c1plt.errorbar(np.subtract(f435f555_3[i][0],   f435f555_3[i][1]),   
        #               f435f555_3[i][1], f435f555_3[i][2],   f435f555_3[i][3], 
        #                fmt=None, marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_3[i][0],   f435f555_3[i][1]),   
                      f435f555_3[i][1], label = 'S/N >= ' + str(snt) +' Radius ' + str(radius[3]) + " PC",  
                        c='y',marker='D')
        #c1plt.errorbar(np.subtract(f435f555_2[i][0],   f435f555_2[i][1]),   
        #               f435f555_2[i][1], f435f555_2[i][2],   f435f555_2[i][3], 
        #                fmt=None, marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_2[i][0],   f435f555_2[i][1]),   
                      f435f555_2[i][1], label = 'S/N >= ' + str(snt) +' Radius ' + str(radius[2]) + " PC",  
                        c='b',marker='D')
        #c1plt.errorbar(np.subtract(f435f555_1[i][0],   f435f555_1[i][1]),  
        #               f435f555_1[i][1], f435f555_1[i][2],   f435f555_1[i][3],
        #                 fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_1[i][0],   f435f555_1[i][1]),   
                      f435f555_1[i][1], label = 'S/N >= ' + str(snt) +' Radius ' + str(radius[1]) + " PC",  
                        c='r',marker='D')        
        #c1plt.errorbar(np.subtract(f435f555_0[i][0],   f435f555_0[i][1]),  
        #               f435f555_0[i][1], f435f555_0[i][2],   f435f555_0[i][3],
        #                 fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(f435f555_0[i][0],   f435f555_0[i][1]),   
                      f435f555_0[i][1], label = 'S/N >= ' + str(snt) +' Radius ' + str(radius[0]) + " PC",  
                        c='k',marker='D')
        snt += 1

#c1plt.fill([3,4,4,3], [2,2,4,4], 'b', alpha=0.2, edgecolor='r')
###########################################################################      
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
plt.xlabel("F625W - F814W (mag)",fontdict = font)
plt.ylabel("M$_{F814W}$ (mag)",fontdict = font)
#c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
#           'r--', label = 'Log(Age) = 7.0')
if (title == 'SN08ge'):
    c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
           'y-', label = 'Log(Age) = 7.1')
    c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
           'g:', label = 'Log(Age) = 7.2')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Log(Age) = 7.3')
elif (title == 'SN08ha'):   
    #c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
    #       'y-', label = 'Log(Age) = 7.1')
    #c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
    #       'g:', label = 'Log(Age) = 7.2')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Log(Age) = 7.3')
    c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
    c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Log(Age) = 7.6')
elif (title == 'SN10ae'):
    c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
           'y-', label = 'Log(Age) = 7.1')
    c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
           'g:', label = 'Log(Age) = 7.2')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Log(Age) = 7.3')
    c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
    c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Log(Age) = 7.6')
elif (title == 'SN10el'): 
    """
    c2plt.plot(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  
           'r--', label = 'Log(Age) = 7.0')
    c2plt.plot(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  
           'y-', label = 'Log(Age) = 7.1')
    c2plt.plot(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  
           'g:', label = 'Log(Age) = 7.2')
    c2plt.plot(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  
           'c-', label = 'Log(Age) = 7.3')
    """
    c2plt.plot(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  
           'b:' , label = 'Log(Age) = 7.4')
    c2plt.plot(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  
           'c-.', label = 'Log(Age) = 7.5')
    c2plt.plot(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  
           'r--', label = 'Log(Age) = 7.6')
    c2plt.plot(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  
           'y-' , label = 'Log(Age) = 7.7')
    c2plt.plot(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  
           'g:' , label = 'Log(Age) = 7.8')
    
    #c2plt.plot(np.subtract(F625W[age79],  F814W[age79]),  F814W[age79],  
    #       'c-.', label = 'Log(Age) = 7.9') 
    #c2plt.plot(np.subtract(F625W[age80],  F814W[age80]),  F814W[age80],  
    #       'b:' , label = 'Log(Age) = 8.0')  

###########################################################################
           
for k in range(start,end):
        #c2plt.errorbar(np.subtract(f625f814_4[k][0],   f625f814_4[k][1]),   
        #               f625f814_4[k][1], f625f814_4[k][2],   f625f814_4[k][3], 
        #                fmt=None, marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_4[k][0],   f625f814_4[k][1]),   f625f814_4[k][1],
                      label = 'S/N >= ' + str(snb) +' Radius ' + str(radius[4]) + " PC",  
                        c='c',marker='D')
        #c2plt.errorbar(np.subtract(f625f814_3[k][0],   f625f814_3[k][1]),   
        #               f625f814_3[k][1], f625f814_3[k][2],   f625f814_3[k][3], 
        #                fmt=None, marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_3[k][0],   f625f814_3[k][1]),   f625f814_3[k][1],
                      label = 'S/N >= ' + str(snb) +' Radius ' + str(radius[3]) + " PC",  
                        c='y',marker='D')
        #c2plt.errorbar(np.subtract(f625f814_2[k][0],   f625f814_2[k][1]),   
        #               f625f814_2[k][1], f625f814_2[k][2],   f625f814_2[k][3], 
        #                fmt=None, marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_2[k][0],   f625f814_2[k][1]),   f625f814_2[k][1],
                      label = 'S/N >= ' + str(snb) +' Radius ' + str(radius[2]) + " PC",  
                        c='b',marker='D')
        #c2plt.errorbar(np.subtract(f625f814_1[k][0],   f625f814_1[k][1]),   
        #               f625f814_1[k][1], f625f814_1[k][2],   f625f814_1[k][3], 
        #                fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_1[k][0],   f625f814_1[k][1]),   f625f814_1[k][1],   
                      label = 'S/N >= ' + str(snb) +' Radius ' + str(radius[1]) + " PC",  
                        c='r',marker='D')
        #c2plt.errorbar(np.subtract(f625f814_0[k][0],   f625f814_0[k][1]),   
        #               f625f814_0[k][1], f625f814_0[k][2],   f625f814_0[k][3], 
        #                fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(f625f814_0[k][0],   f625f814_0[k][1]),   f625f814_0[k][1],   
                      label = 'S/N >= ' + str(snb) +' Radius ' + str(radius[0]) + " PC",  
                        c='k',marker='D')
        snb += 1
#c2plt.fill([3,4,4,3], [2,2,4,4], 'b', alpha=0.2, edgecolor='r')
###########################################################################
l = plt.legend(prop = {'family' : 'serif'},loc=4)
l.draw_frame(False)
########################################################################### 
c2plt.set_ylim(bottom=ybotmax, top=ybotmin) 
########################################################################### 

print "Save and show plot : " + title + '_' + 'Z' + name[1:-7]+ '_Comparison.png'

plt.savefig('Figures/'+title + '_' + 'Z' + name[1:-7]+ '_Comparison.png')
