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
#####################################################################

def AGEinfo(d, rawnum):
    logAGE = np.array(d[:,:,0])
    f435w  = np.array(d[:,:,7])
    f555w  = np.array(d[:,:,10])
    f625w  = np.array(d[:,:,12])
    f814w  = np.array(d[:,:,16])
    #limit  = np.array((logAGE >= (rawnum - .05)) & (logAGE <= (rawnum + .5)))
    age    = np.where(logAGE == rawnum)
    
    return f435w, f555w, f625w, f814w, age, logAGE
  
#####################################################################
  
def met(title):
    d = []
    if (title == 'sn08ha'):
        name = 'Z0060Y26.dat'
    elif (title == 'sn10ae'):
        name = 'Z0096Y26.dat'
    elif (title == 'sn10el'):
        name = 'Z0224Y26.dat'
    elif (title == 'sn08ge'):
        name = 'Z0300Y26.dat'
    d.append(np.loadtxt('Metallicity/'+name))
    d = np.array(d)                
    return d, name
    
#####################################################################
    
def SNinfo(filename):
    fL = []
    fR = []  
    # [dist, conver,                 0, 1,
    # yLmax, yLmin, yRmax, yRmin,    2, 3, 4, 5,
    # xLmax, xLmin, xRmax, xRmin,    6, 7, 8, 9,
    # sn435, sn555, sn625, sn814,    10,11,12,13,
    # age,                           14,   
    # H435,H555,H625,H814,           15,16,17,18,
    # ACS435,ACS555,ACS625,ACS814]   19,20,21,22
    File = []
    if (filename == 'sn08ge'):
        radius = [35,57.47,115]#[114,183,230]#
        File = 'SN2008GE'
        info   = [17.95e7,(4.35), 
               -3.0,-8.5,-4.0,-9.5,
               -0.5,  2.0, -0.5,  2.5, 
               -4.678,-5.388,-5.566,-5.172,
                7.17,
                0.0,0.0,0.0,0.0, 
                0.046,0.036,0.028,0.020] 
    elif (filename == 'sn08ha'):
        radius = [15,30,45]
        File = 'SN2008HA'
        info   = [20e7, (5), 
                -3.50, -6.5, -4.00, -7.0, 
                -0.75,  2.0, -0.75,  2.0,
                -4.04, -4.5, -4.30, -4.5,
                 7.74,
                 0.0,0.0,0.0,0.0,
                 0.284,0.219,0.174,0.120]
    elif (filename == 'sn10ae'):
        radius = [4.73,6.30,9]#[7.9,15.74,23.61]#
        File = 'SN2010AE'        
        info   = [13.1e7, (63.52), 
                -5.0, -8.0, -5.0, -8.5, 
                -0.75,  2.0, -0.75,  2.0,
                -4.036,-4.321,-4.415,-4.651, 
                 7.52,
                 2.052,1.588,1.262,0.867,
                 0.509,0.394,0.313,0.215]
    elif (filename == 'sn10el'):
        radius = [8.3,10.33,15.52]#[10.34,14.48,18.62]#
        File = 'SN2010EL'        
        info   = [9.97e7, (48.33), 
                -5.0, -8.0, -4.0, -8.0, 
                -0.5,  2.0, -0.5,  2.3,
                -6.122,-5.887,-5.497,-4.547, 
                 7.85,
                 3.255,2.517,2.001,1.376,
                 0.033,0.025,0.020,0.014]
                 
    fL.append(pickle.load(open(str(File) + '/' + str(filename) + 'f435f555.p', 'rb')))    
    fR.append(pickle.load(open(str(File) + '/' + str(filename) + 'f625f814.p', 'rb')))  
    
    return info, radius, File, fL, fR      
    
#####################################################################
def main():
    age = []
    num = []
    print 'Which SNe do you wanna plot?'
    print 'sn08ge \nsn08ha \nsn10ae \nsn10el'
    
    SNname = raw_input('Choose a Supernova:')
    
    print ('You picked %s' %(SNname))
    
    check = raw_input('Is this correct? (y/n)')
    if (check == 'y'):
        print "Let's begin!"
    else:
        SNname = []    
        print "Let's try again"
        SNname = raw_input('Choose a Supernova:')
        print ('You picked %s' %(SNname))
    
    SNstuff, Radius, Filename, f435f555, f625f814 = SNinfo(SNname)
    agenum = SNstuff[14]
    
    MetFile, Metname = met(SNname)    
    MetFile = np.array(MetFile)  
    F435W, F555W, F625W, F814W, AGE, LogAge = AGEinfo(MetFile, agenum)
    
    start = agenum - .05
    stop  = agenum + .06 
    
    for i in np.arange(start,stop,0.01):
        age.append(np.where(LogAge == i))
        num.append(round(i,2))
    print num
        
    Abs435 = f435f555[0][0] 
    Abs555 = f435f555[0][1] 
    Apn435 = f435f555[0][2] 
    Apn555 = f435f555[0][3] 
    UncXl  = f435f555[0][4] 
    UncYl  = f435f555[0][5] 
    #SN435  = f435f555[0][6] 
    #SN555  = f435f555[0][7]
    #Radl   = f435f555[0][8] 
    
    Abs625 = f625f814[0][0] 
    Abs814 = f625f814[0][1]
    Apn625 = f625f814[0][2]
    Apn814 = f625f814[0][3] 
    UncXr  = f625f814[0][4] 
    UncYr  = f625f814[0][5] 
    #SN625  = f625f814[0][6] 
    #SN814  = f625f814[0][7] 
    #Radr   = f625f814[0][8] 
    
    """ClosInd = []
    print 'Age 10^' + str(num[0]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[0]],F555W[age[0]]),F555W[age[0]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[0]],F555W[age[0]]),F555W[age[0]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[1]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[1]],F555W[age[1]]),F555W[age[1]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[1]],F555W[age[1]]),F555W[age[1]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[2]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[2]],F555W[age[2]]),F555W[age[2]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[2]],F555W[age[2]]),F555W[age[2]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[3]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[3]],F555W[age[3]]),F555W[age[3]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[3]],F555W[age[3]]),F555W[age[3]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[4]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[4]],F555W[age[4]]),F555W[age[4]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[4]],F555W[age[4]]),F555W[age[4]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[5]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[5]],F555W[age[5]]),F555W[age[5]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[5]],F555W[age[5]]),F555W[age[5]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[6]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[6]],F555W[age[6]]),F555W[age[6]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[6]],F555W[age[6]]),F555W[age[6]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[7]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[7]],F555W[age[7]]),F555W[age[7]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[7]],F555W[age[7]]),F555W[age[7]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[8]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[8]],F555W[age[8]]),F555W[age[8]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[8]],F555W[age[8]]),F555W[age[8]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[9]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[9]],F555W[age[9]]),F555W[age[9]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[9]],F555W[age[9]]),F555W[age[9]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[10]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[10]],F555W[age[10]]),F555W[age[10]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[10]],F555W[age[10]]),F555W[age[10]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[11]) 
    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F435W[age[11]],F555W[age[11]]),F555W[age[11]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F435W[age[11]],F555W[age[11]]),F555W[age[11]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    print '\n\n'
    #for agesInd in xrange(len(age)):
    #    print '\nF435W-F555W'
    #    #print "Age 10^" + str(stupid) + str(agesInd)
    #    print 'Age 10^' + str(num[agesInd])        
    #    ClosIndL = []
    #    for sample in izip(np.subtract(Apn435,Apn555), Abs555):
    #        closestD = -1 
    #        closestIdx = -1
    #        for IdX , val in enumerate(izip(np.subtract(F435W[age[agesInd]],F555W[age[agesInd]]),F555W[age[agesInd]])):
    #            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
    #            if dist < closestD:
    #                closestD = dist
    #                closestIdx = IdX
    #        ClosIndL.append(closestIdx)
    #    ClosIndL = np.array(ClosIndL)
    #    func_vals = np.c_[np.subtract(F435W[age[agesInd]],F555W[age[agesInd]]),F555W[age[agesInd]]]
    #    comp_vals = func_vals[ClosIndL]
    #    print 'Chi^2 of 10^' + str(num[agesInd])  
    #    print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    #    print '\nF625W - F814W'
       
    #for agesIndR in xrange(len(age)):
    #    ClosIndR = []
    #    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
    #        closestD = -1 
    #        closestIdx = -1
    #        for IdX , val in enumerate(izip(np.subtract(F625W[age[agesInd]],F814W[age[agesInd]]),F814W[age[agesInd]])):
    #            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
    #            if dist < closestD:
    #                closestD = dist
    #                closestIdx = IdX
    #        ClosIndR.append(closestIdx)
    #    ClosIndR = np.array(ClosIndR)
    #    func_vals = np.c_[np.subtract(F625W[age[agesInd]],F814W[age[agesInd]]),F814W[age[agesInd]]]
    #    comp_vals = func_vals[ClosIndR]
    #    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    """
    """ClosInd = []
    print 'Age 10^' + str(num[0]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[0]],F814W[age[0]]),F814W[age[0]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[0]],F814W[age[0]]),F814W[age[0]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[1]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[1]],F814W[age[1]]),F814W[age[1]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[1]],F814W[age[1]]),F814W[age[1]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[2]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[2]],F814W[age[2]]),F814W[age[2]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[2]],F814W[age[2]]),F814W[age[2]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    """
    ClosInd = []
    print 'Age 10^' + str(num[3]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[3]],F814W[age[3]]),F814W[age[3]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[3]],F814W[age[3]]),F814W[age[3]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[4]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[4]],F814W[age[4]]),F814W[age[4]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[4]],F814W[age[4]]),F814W[age[4]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[5]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[5]],F814W[age[5]]),F814W[age[5]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[5]],F814W[age[5]]),F814W[age[5]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[6]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[6]],F814W[age[6]]),F814W[age[6]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[6]],F814W[age[6]]),F814W[age[6]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[7]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[7]],F814W[age[7]]),F814W[age[7]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[7]],F814W[age[7]]),F814W[age[7]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[8]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[8]],F814W[age[8]]),F814W[age[8]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[8]],F814W[age[8]]),F814W[age[8]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[9]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[9]],F814W[age[9]]),F814W[age[9]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[9]],F814W[age[9]]),F814W[age[9]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[10]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[10]],F814W[age[10]]),F814W[age[10]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[10]],F814W[age[10]]),F814W[age[10]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #######################
    ClosInd = []
    print 'Age 10^' + str(num[11]) 
    for sample in izip(np.subtract(Apn625,Apn814), Abs814):
        closestD = -1 
        closestIdx = -1
        for IdX , val in enumerate(izip(np.subtract(F625W[age[11]],F814W[age[11]]),F814W[age[11]])):
            dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
            if dist < closestD:
                closestD = dist
                closestIdx = IdX
        ClosInd.append(closestIdx)
    ClosInd = np.array(ClosInd)
    func_vals = np.c_[np.subtract(F625W[age[11]],F814W[age[11]]),F814W[age[11]]]
    comp_vals = func_vals[ClosInd]
    print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)
    #####################################################################
    """
    #title = 'SN10el'
    #title = 'SN08ha'
    title = 'SN10ae'
    #title = 'SN08ge'
    #####################################################################
    
    if (title == 'SN08ha'):
        name   = 'Z0060Y26.dat'
        radius = [450,750,1000,1500,2200] 
        #name = 'Z0384Y26.dat'
    elif (title == 'SN08ge'): 
        name = 'Z0300Y26.dat'
        radius = [2200,4400,6500,7600,8700]
    elif (title == 'SN10el'): 
        name = 'Z0224Y26.dat'
    elif (title == 'SN10ae'): 
        name = 'Z0096Y26.dat'

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
    age731  = np.where((logAGE == 7.31))
    age732  = np.where((logAGE == 7.32))
    age733  = np.where((logAGE == 7.33))
    age734  = np.where((logAGE == 7.34))
    age735  = np.where((logAGE == 7.35))
    age736  = np.where((logAGE == 7.36))
    age737  = np.where((logAGE == 7.37))
    age738  = np.where((logAGE == 7.38))
    age739  = np.where((logAGE == 7.39))
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
    
    age = []
    stupid = 7.3
    age.append([age73,age731,age732,age733,age734,age735,age736,age737,age738,age739])
    #age.append([age74,age741,age742,age743,age744,age745,age746,age747,age748,age749])
    #age.append([age75,age751,age752,age753,age754,age755,age756,age757,age758,age759])
    #age.append([age76,age761,age762,age763,age774,age765,age766,age767,age768,age769])
    #age.append([age77,age771,age772,age773,age774,age775,age776,age777,age778,age779])
    #age.append([age78,age781,age782,age783,age784,age785,age786,age787,age788,age789])
    

    f435f555 = []
    f625f814 = []
    
    if (title == 'SN08ha'):
        for i in range(3,6):
            f435f555.append(pickle.load(open('SN2008HA/sn2008ha_f435f555.p', 'rb')))    
            f625f814.append(pickle.load(open('SN2008HA/sn2008ha_f625f814.p', 'rb'))) 
            ignoring1 = np.where((f435f555[0][8] != f435f555[0][8][0]) & 
                  (f435f555[0][8] != f435f555[0][8][1]) &
                  (f435f555[0][8] != f435f555[0][8][2]) &
                  (f435f555[0][8] != f435f555[0][8][3]) )
            ignoring2 = np.where((f625f814[0][8] != f625f814[0][8][0]) & 
                  (f625f814[0][8] != f625f814[0][8][1]) &
                  (f625f814[0][8] != f625f814[0][8][2]) &
                  (f625f814[0][8] != f625f814[0][8][3]) )
            f435f555 = np.array(f435f555)
            f625f814 = np.array(f625f814) 
    elif (title == 'SN08ge'):
        f435f555.append(pickle.load(open('SN2008GE/sn2008ge.f435f555.p', 'rb')))    
        f625f814.append(pickle.load(open('SN2008GE/sn2008ge.f625f814.p', 'rb')))  
    elif (title == 'SN10el'):
        f435f555.append(pickle.load(open('SN2010EL/sn2010el.f435f555.p', 'rb')))    
        f625f814.append(pickle.load(open('SN2010EL/sn2010el.f625f814.p', 'rb')))     
    elif (title == 'SN10ae'):
        f435f555.append(pickle.load(open('SN2010AE/sn2010ae.f435f555.p', 'rb')))    
        f625f814.append(pickle.load(open('SN2010AE/sn2010ae.f625f814.p', 'rb')))     


    ignoring1 = np.where((f435f555[0][8] != f435f555[0][8][0]) & 
                  (f435f555[0][8] != f435f555[0][8][1]) &
                  (f435f555[0][8] != f435f555[0][8][2]) &
                  (f435f555[0][8] != f435f555[0][8][3]) )
    ignoring2 = np.where((f625f814[0][8] != f625f814[0][8][0]) & 
                  (f625f814[0][8] != f625f814[0][8][1]) &
                  (f625f814[0][8] != f625f814[0][8][2]) &
                  (f625f814[0][8] != f625f814[0][8][3]) )
    f435f555 = np.array(f435f555)
    f625f814 = np.array(f625f814)
    # np.take(f435f555[0][8], bright) useful if I only needed it once

    for agesInd in xrange(len(age[0])):
    print "                "
    print "Age 10^7.4" + str(agesInd)
    print "F435W-F555W"
    ClosInd = []
    for sample in izip(np.subtract(f435f555[0][0][ignoring1],f435f555[0][1][ignoring1]), f435f555[0][1][ignoring1]):
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
    print "Chi^2 of 10^7.4" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f435f555[0][0][ignoring1],f435f555[0][1][ignoring1]), f435f555[0][1][ignoring1]],comp_vals)
   
    
    print "                "
    print "F555W - F814W"
    
    ClosInd = []
    for sample in izip(np.subtract(f625f814[0][0][ignoring2],f625f814[0][1][ignoring2]), f625f814[0][1][ignoring2]):
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
    print "Chi^2 of 10^7.4" + str(agesInd)
    print stats.chisquare(np.c_[np.subtract(f625f814[0][0][ignoring2],f625f814[0][1][ignoring2]), f625f814[0][1][ignoring2]],comp_vals)
       
    ###############################################################################
    ###############################################################################
    ###############################################################################
    ###############################################################################

    for agesInd in xrange(len(age[0])):
    print "                "
    print "Age 10^7.7" + str(agesInd)
    print "F435W-F555W"
    print "                "
    #ClosInd = []
    #for sample in izip(np.subtract(f435f555[0][0],f435f555[0][1]), f435f555[0][1]):
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
    #print stats.chisquare(np.c_[np.subtract(f435f555[0][0],f435f555[0][1]), f435f555[0][1]],comp_vals)
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
    #for sample in izip(np.subtract(f625f814[0][0],f625f814[0][1]), f625f814[0][1]):
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
    #print stats.chisquare(np.c_[np.subtract(f625f814[0][0],f625f814[0][1]), f625f814[0][1]],comp_vals)
       
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
main()