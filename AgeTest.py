# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 15:07:49 2014

@author: Nova
"""
import numpy     as     np
from   scipy     import stats
from   scipy     import interpolate
from   itertools import izip
import pickle
import statsmodels.formula.api as sm
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
                -6.088,-5.910,-5.677,-5.518,#-4.036,-4.321,-4.415,-4.651,
                 7.2,
                 2.052,1.588,1.262,0.867,
                 0.509,0.394,0.313,0.215]
    elif (filename == 'sn10el'):
        radius = [8.3,10.33,15.52]#[10.34,14.48,18.62]#
        File = 'SN2010EL'        
        info   = [9.97e7, (48.33), 
                -5.0, -8.0, -4.0, -8.0, 
                -0.5,  2.0, -0.5,  2.3,
                -6.122,-5.887,-5.497,-4.547, 
                 7.3,
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
    
    H435   = SNstuff[15]
    H555   = SNstuff[16]
    H625   = SNstuff[17]
    H814   = SNstuff[18]
    
    ACS435 = SNstuff[19]
    ACS555 = SNstuff[20]
    ACS625 = SNstuff[21]
    ACS814 = SNstuff[22]
    
    MetFile, Metname = met(SNname)    
    MetFile = np.array(MetFile)  
    F435W, F555W, F625W, F814W, AGE, LogAge = AGEinfo(MetFile, agenum)
          
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
    
    start = agenum - .05
    stop  = agenum + .06 
        
    for i in np.arange(start,stop,0.01):
        #age.append(np.where(LogAge == i))
        num.append(round(i,2))       
        
    age0    = np.where(LogAge == num[0])
    age1    = np.where(LogAge == num[1])
    age2    = np.where(LogAge == num[2])
    age3    = np.where(LogAge == num[3])
    age4    = np.where(LogAge == num[4])
    age5    = np.where(LogAge == num[5])
    age6    = np.where(LogAge == num[6])
    age7    = np.where(LogAge == num[7])
    age8    = np.where(LogAge == num[8])
    age9    = np.where(LogAge == num[9])
    age10   = np.where(LogAge == num[10])
    
    age = [age0,age1,age2,age3,age4,age5,age6,age7,age8,age9,age10]
    
    for ageInd in xrange(len(age)):
        ClosInd = []
        print 'F435w-F555W \nAge 10^' + str(num[ageInd]) 
        for sample in izip(np.subtract(Apn435,Apn555), Abs555):
            closestD = -1 
            closestIdx = -1
            for IdX , val in enumerate(izip(np.subtract(F435W[age[ageInd]],F555W[age[ageInd]]),F555W[age[ageInd]])):
                dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
                if dist < closestD:
                    closestD = dist
                    closestIdx = IdX
            ClosInd.append(closestIdx)
        ClosInd = np.array(ClosInd)
        func_vals = np.c_[np.subtract(F435W[age[ageInd]],F555W[age[ageInd]]),F555W[age[ageInd]]]
        comp_vals = func_vals[ClosInd]
        print stats.chisquare(np.c_[np.subtract(Apn435,Apn555), Abs555],comp_vals)
    
        ClosInd = []
        print 'F625W-F814W \nAge 10^' + str(num[ageInd]) 
        for sample in izip(np.subtract(Apn625,Apn814), Abs814):
            closestD = -1 
            closestIdx = -1
            for IdX , val in enumerate(izip(np.subtract(F625W[age[ageInd]],F814W[age[ageInd]]),F814W[age[ageInd]])):
                dist = (sample[0] - val[0])**2 + (sample[1] - val[1])**2 
                if dist < closestD:
                    closestD = dist
                    closestIdx = IdX
            ClosInd.append(closestIdx)
        ClosInd = np.array(ClosInd)
        func_vals = np.c_[np.subtract(F625W[age[ageInd]],F814W[age[ageInd]]),F814W[age[ageInd]]]
        comp_vals = func_vals[ClosInd]
        print stats.chisquare(np.c_[np.subtract(Apn625,Apn814), Abs814],comp_vals)

main()