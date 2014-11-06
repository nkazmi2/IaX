# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 15:07:49 2014

@author: Nova
"""

import numpy     as     np
from   scipy     import stats
from   itertools import izip
import pickle
#####################################################################
########################### PICK THE SN!! ###########################
title = 'SN08ge'
#title = 'SN08ha'
#####################################################################

if (title == 'SN08ha'):
    name = 'Z0046Y26.dat'
    #name = 'Z0384Y26.dat'
elif (title == 'SN08ge'): 
    name = 'Z0170Y26.dat'
    
d = []
d.append(np.loadtxt('Metallicity/'+name))
d = np.array(d)

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
age761  = np.where((logAGE == 7.61))
age762  = np.where((logAGE == 7.62))
age763  = np.where((logAGE == 7.63))
age764  = np.where((logAGE == 7.64))
age765  = np.where((logAGE == 7.65))
age766  = np.where((logAGE == 7.66))
age767  = np.where((logAGE == 7.67))
age768  = np.where((logAGE == 7.68))
age769  = np.where((logAGE == 7.69))
age77   = np.where((logAGE == 7.7))
age771  = np.where((logAGE == 7.71))
age772  = np.where((logAGE == 7.72))
age773  = np.where((logAGE == 7.73))
age774  = np.where((logAGE == 7.74))
age775  = np.where((logAGE == 7.75))
age776  = np.where((logAGE == 7.76))
age777  = np.where((logAGE == 7.77))
age778  = np.where((logAGE == 7.78))
age779  = np.where((logAGE == 7.79))
age78   = np.where((logAGE == 7.8))
age785  = np.where((logAGE == 7.85))
age79   = np.where((logAGE == 7.9))
age80   = np.where((logAGE == 8.0))

age = []
#age.append([age76,age761,age762,age763,age774,age765,age766,age767,age768,age769])
age.append([age77,age771,age772,age773,age774,age775,age776,age777,age778,age779])

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

if (title == 'SN08ha'):
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
elif (title == 'SN08ge'):
        f435f555_0.append(pickle.load(open('SN2008GE/sn2008ge_f435f555.p', 'rb')))    
        f625f814_0.append(pickle.load(open('SN2008GE/sn2008ge_f625f814.p', 'rb')))    


for agesInd in xrange(len(age[0])):
    print "                "
    print "Age 10^7.7" + str(agesInd)
    print "F435W-F555W"
    ClosInd = []
    for sample in izip(np.subtract(f435f555_0[0][0],f435f555_0[0][1]), f435f555_0[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f435f555_0[0][0],f435f555_0[0][1]), f435f555_0[0][1]],comp_vals)
   
    
    print "                "
    print "F555W - F814W"
    
    ClosInd = []
    for sample in izip(np.subtract(f625f814_0[0][0],f625f814_0[0][1]), f625f814_0[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f625f814_0[0][0],f625f814_0[0][1]), f625f814_0[0][1]],comp_vals)
           
###############################################################################
###############################################################################
###############################################################################
###############################################################################
"""
for agesInd in xrange(len(age[0])):
    print "                "
    print "Age 10^7.7" + str(agesInd)
    print "F435W-F555W"
    print "                "
    #ClosInd = []
    #for sample in izip(np.subtract(f435f555_0[0][0],f435f555_0[0][1]), f435f555_0[0][1]):
    #    closestD = -1 
    #    closestIdx = -1
    #    for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
    #        dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
    #        if dist < closestD:
    #            closestD = dist
    #            closestIdx = IdX
    #    ClosInd.append(closestIdx)
    #ClosInd = np.array(ClosInd)
    #func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    #comp_vals = func_vals[ClosInd]
    
    #print "Radius 450pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    #print stats.chisquare(np.c_[np.subtract(f435f555_0[0][0],f435f555_0[0][1]), f435f555_0[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f435f555_1[0][0],f435f555_1[0][1]), f435f555_1[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Radius 750pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f435f555_1[0][0],f435f555_1[0][1]), f435f555_1[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f435f555_2[0][0],f435f555_2[0][1]), f435f555_2[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Radius 1000pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f435f555_2[0][0],f435f555_2[0][1]), f435f555_2[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f435f555_3[0][0],f435f555_3[0][1]), f435f555_3[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Radius 1500pc"
    ##print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f435f555_3[0][0],f435f555_3[0][1]), f435f555_3[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f435f555_4[0][0],f435f555_4[0][1]), f435f555_4[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    #print "Radius 2200pc"
    #print stats.chisquare(np.c_[np.subtract(f435f555_4[0][0],f435f555_4[0][1]), f435f555_4[0][1]],comp_vals)

    print "                "
    print "F555W - F814W"
    print "                "
    #ClosInd = []
    #for sample in izip(np.subtract(f625f814_0[0][0],f625f814_0[0][1]), f625f814_0[0][1]):
    #    closestD = -1 
    #    closestIdx = -1
    #    for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
    #        dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
    #        if dist < closestD:
    #            closestD = dist
    #            closestIdx = IdX
    #    ClosInd.append(closestIdx)
    #ClosInd = np.array(ClosInd)
    #func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    #comp_vals = func_vals[ClosInd]
    #print "Radius 450pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    #print stats.chisquare(np.c_[np.subtract(f625f814_0[0][0],f625f814_0[0][1]), f625f814_0[0][1]],comp_vals)
       
    ######
    ClosInd = []
    for sample in izip(np.subtract(f625f814_1[0][0],f625f814_1[0][1]), f625f814_1[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Radius 750pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f625f814_1[0][0],f625f814_1[0][1]), f625f814_1[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f625f814_2[0][0],f625f814_2[0][1]), f625f814_2[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Radius 1000pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f625f814_2[0][0],f625f814_2[0][1]), f625f814_2[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f625f814_3[0][0],f625f814_3[0][1]), f625f814_3[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    print "Radius 1500pc"
    #print "Chi^2 of 10^7.7" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f625f814_3[0][0],f625f814_3[0][1]), f625f814_3[0][1]],comp_vals)
    ######
    ClosInd = []
    for sample in izip(np.subtract(f625f814_4[0][0],f625f814_4[0][1]),f625f814_4[0][1]):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0][agesInd]],F555W[age[0][agesInd]]),F555W[age[0][agesInd]]]
    comp_vals = func_vals[ClosInd]
    #print "Radius 2200pc"
    #print stats.chisquare(np.c_[np.subtract(f625f814_4[0][0],f625f814_4[0][1]), f625f814_4[0][1]],comp_vals)
"""