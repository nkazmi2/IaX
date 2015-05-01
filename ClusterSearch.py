# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:59:35 2015

@author: nova
"""
from __future__ import division
import numpy               as np
import matplotlib.pyplot   as plt
import matplotlib.gridspec as gridspec
import pickle
import pandas
import pyregion
from   matplotlib.ticker  import MultipleLocator 
from   matplotlib.ticker  import AutoMinorLocator
from   matplotlib.patches import Polygon
from   itertools          import cycle

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
        
###############################################################################
def AGEinfo(d, rawnum):
    logAGE = np.array(d[:,:,0])
    f435w  = np.array(d[:,:,7])
    f555w  = np.array(d[:,:,10])
    f625w  = np.array(d[:,:,12])
    f814w  = np.array(d[:,:,16])
    #limit  = np.array((logAGE >= (rawnum - .05)) & (logAGE <= (rawnum + .5)))
    age    = np.where(logAGE == rawnum)
    
    return f435w, f555w, f625w, f814w, age, logAGE
###############################################################################
def cutdata(SNname, sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn, ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            f435Abs, f555Abs, f625Abs, f814Abs,
            xcoord, ycoord,
            srp435,srp555,srp625,srp814,
            rnd435,rnd555,rnd625,rnd814,
            crd435,crd555,crd625,crd814,
            chi435,chi555,chi625,chi814,
            qf435 ,qf555 ,qf625 ,qf814,
            TotalSigN):
    print "Make final cuts for", SNname 
    cutL = []
    cutR = []
    cuteverything = []
    cutL.append(np.where((star <= 2) 
                & ((qf435 < 3.0) & (qf555 < 3.0) & (qf625 < 3.0) & (qf814 < 3.0))
                & (TotalSigN >= 3)
                & ((snr435 >= 3) | (snr555 >= 3)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <=  1000)
                & (sharp < sharpmax) 
                & (sharp > sharpmin)
                & (roond < roundmax)
                & (crowd < crowdmax)
                ))
    cutR.append(np.where((star <= 2) 
                & ((qf435 < 3.0) & (qf555 < 3.0) & (qf625 < 3.0) & (qf814 < 3.0))
                & (TotalSigN >= 3)
                & ((snr625 >= 3) | (snr814 >= 3)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <=  1000)
                & (sharp < sharpmax) 
                & (sharp > sharpmin)
                & (roond < roundmax)
                & (crowd < crowdmax)     
                ))
    cuteverything.append(np.where((star <= 2) 
                & ((qf435 < 3.0) & (qf555 < 3.0) & (qf625 < 3.0) & (qf814 < 3.0))
                & (TotalSigN >= 3)
                & ((snr435 >= 3) | (snr555 >= 3) | (snr625 >= 3) | (snr814 >= 3)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <=  1000)
                & (sharp < sharpmax) 
                & (sharp > sharpmin)
                & (roond < roundmax)
                & (crowd < crowdmax)

                ))
    return cutL, cutR, cuteverything
###############################################################################
def regfile(folder, bluecuts, redcuts,xsn,ysn,xcoord,ycoord,allcuts):      
    print "Save into region file"
    circ      = []
    comm      = []
    clos      = [] 
    for i in range(len(xcoord[allcuts])):
            circ.append('circle(')
            comm.append(',')
            clos.append(',5)')#Field_Sharp.48_50
    np.savetxt(folder +'/Cluster.reg', np.c_[circ,xcoord[allcuts]+.5,comm,ycoord[allcuts]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=green dashlist=8 3 width=1' \
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1'\
               '\nimage;' )
###############################################################################             
def iso(c1plt,c2plt,supname,isoAGE,isonum,f435,f555,f625,f814,h435,h555,h625,h814,a435,a555,a625,a814,isoall,decredhost,decrange,deccol): 
                
    print "Begin Plotting Isochrone..."
    if (decrange == 'y'):
        num = []
        start = isonum - .05
        stop  = isonum + .06 
    
        for i in np.arange(start,stop,0.01):
            #age.append(np.where(LogAge == i))
            num.append(round(i,2))       
        
        # assigning age arrays to one array so that I can loop through it
        age0    = np.where(isoall == num[0])
        age1    = np.where(isoall == num[1])
        age2    = np.where(isoall == num[2])
        age3    = np.where(isoall == num[3])
        age4    = np.where(isoall == num[4])
        age5    = np.where(isoall == num[5])
        age6    = np.where(isoall == num[6])
        age7    = np.where(isoall == num[7])
        age8    = np.where(isoall == num[8])
        age9    = np.where(isoall == num[9])
        age10   = np.where(isoall == num[10])
    
        age = [age0,age1,age2,age3,age4,age5,age6,age7,age8,age9,age10]
        if (decredhost == 'y'):
            for ageInd in xrange(len(age)):
                colors = np.random.rand(4,1)
                c1plt.plot(np.subtract((np.add(f435[age[ageInd]],h435)), (np.add(f555[age[ageInd]],h555))), 
                           (np.add(f555[age[ageInd]],h555)), 
                            c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
                c2plt.plot(np.subtract((np.add(f625[age[ageInd]],h625)), (np.add(f814[age[ageInd]],h814))),
                           (np.add(f814[age[ageInd]],h814)), 
                            c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
        else:
            for ageInd in xrange(len(age)):
                colors = np.random.rand(4,1)
                c1plt.plot(np.subtract(f435[age[ageInd]],f555[age[ageInd]]), 
                       f555[age[ageInd]], c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
                c2plt.plot(np.subtract(f625[age[ageInd]],f814[age[ageInd]]),
                       f814[age[ageInd]], c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
    else:
        print "No age range" 
        
    if (decredhost == 'y'):
        print "Reddening by the host galaxy"
        c1plt.plot(np.subtract((np.add(f435[isoAGE],h435)), (np.add(f555[isoAGE],h555))), 
             (np.add(f555[isoAGE],h555)),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#'Age = 10$^{' + str(isonum) + '}$ yrs')
        c2plt.plot(np.subtract((np.add(f625[isoAGE],h625)), (np.add(f814[isoAGE],h814))),
             (np.add(f814[isoAGE],h814)),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#''Age = 10$^{' + str(isonum) + '}$ yrs')
    elif (deccol == 'y'):
        print "Isochrone for Color-Color"
        c1plt.plot(np.subtract((f435[isoAGE]), (f555[isoAGE])),np.subtract((f625[isoAGE]), (f814[isoAGE])),  #np.subtract((f435[isoAGE]), (f555[isoAGE])),np.subtract((f625[isoAGE]), (f814[isoAGE])),  
             'k-' )#, lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs') 
        c2plt.plot(np.subtract((f625[isoAGE]), (f814[isoAGE])),np.subtract((f435[isoAGE]), (f555[isoAGE])),#np.subtract((f625[isoAGE]), (f814[isoAGE])),np.subtract((f435[isoAGE]), (f555[isoAGE])),  
             'k-')#, lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')
    else:
        print "Single Isochrone"
        c1plt.plot(np.subtract((f435[isoAGE]), (f555[isoAGE])),(f555[isoAGE]),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#'Age = 10$^{' + str(isonum) + '}$ yrs')
        c2plt.plot(np.subtract((f625[isoAGE]), (f814[isoAGE])),(f814[isoAGE]),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#''Age = 10$^{' + str(isonum) + '}$ yrs')
###############################################################################
def met(title):
    d = []
    if (title == 'sn08ha'):
        name = 'Z0060Y26.dat'
    elif (title == 'sn10ae'):
        name = 'Z0096Y26.dat'
    elif (title == 'sn10el'):
        name = 'Z0224Y26.dat'
    elif (title == 'sn08ge'):
        name = 'Z0314Y26.dat'
    d.append(np.loadtxt('Metallicity/'+name))
    d = np.array(d)                
    return d, name
###############################################################################
def SNinfo(SNname):
        ##### Things that change for each sn ######
        #[folder, file,                    0,1
        #ACS435,ACS555,ACS625,ACS814,      2,3,4,5,
        #MW,Host,                          6,7,
        #H435,H555,H625,H814,              8,9,10,11
        #dmod,xsn,ysn,                     12,13,14,
        #sharpmax, sharpmin, round, crowd, 15,16,17,18
        #dist, conver,                     19,10,
        #yLmax, yLmin, yRmax, yRmin,       21,22,23,24
        #xLmax, xLmin, xRmax, xRmin,       25,26,27,28
        #sn435, sn555, sn625, sn814,       29,30,31,32
        #age]                              33
    Info   = []
    #File   = []
    radius = []
    if (SNname == "sn08ge"):
      #File = 'SN2008GE'
      radius = [16.09,34.47,50.56]
      Info = ['SN2008GE', 'sn2008ge.phot.out', 
                0.046,0.036,0.028,0.020,
                0.011,0.0,
                0.0,0.0,0.0,0.0,
                31.33,3249.22,3421.6611,
                .62,-.65,0.35,0.7,
                17.95e6,(4.3512), 
                -3.5, -6.8,-5.5,-7.7,  #-3.0,-14,-3.0,-14,   #-1.0,-8.5,-3.0,-9.5,   #          
                -1.0,  3.0, -0.25,  3.0, #-3.0,  5.0, -3.0,  5.0,#
                -4.5,-5.25,-5.41,-5.8,# sn2.8-3.2#-4.644,-5.205,-5.50,-5.9,#sn3.0##-4.59,-5.37,-4.50,-5.13,#sn3-3.5#-4.678,-5.388,-5.566,-5.172, SN3-4.0
                7.28]
    elif (SNname == "sn08ha"):
       #File = 'SN2008HA'
       radius = [15,30,45]
       Info = ['SN2008HA', 'sn2008ha_new.phot',
                0.284,0.219,0.174,0.120,
                0.07,0.0,
                0.0,0.0,0.0,0.0,
                31.64,1736.199,3171.792,50,
                .55,-.65,2.0,0.6,#.55,-.65,2.0,1.5
                20e6, (4.8414), 
                -3.50, -6.5, -4.00, -7.0, 
                -0.75,  2.0, -0.75,  2.0,
                -4.04, -4.5, -4.30, -4.5,
                 7.74]
    elif (SNname == "sn10ae"):
       #File = 'SN2010AE'        
       radius = [200,500,1000]
       Info = ['SN2010AE', 'sn2010ae.phot.out',
                0.509,0.394,0.313,0.215,
                0.124,0.5,
                2.052,1.588,1.262,0.867,
                30.9,1783.3953,1923.19955,70,
                0.45,-0.65,0.6,0.6,
                13.1e6, (3.17553), 
                -5.50, -8.5, -5.00, -9.0,#-4.0, -7.0, -4.5, -7.5,
                -0.5,  1.8, -0.5,  1.6,#-0.75,  3.5, -0.75,  4.0,
                -6.088,-5.910,-5.677,-5.518,#-4.036,-4.321,-4.415,-4.651, 
                 9.00]#7.15,
    elif (SNname == "sn10el"):
        #File = 'SN2010EL'        
        radius = [29,62,90]
        Info = ['SN2010EL', 'sn2010el.phot.out',
                0.033,0.025,0.020,0.014,
                0.008,0.8,
                3.255,2.517,2.001,1.376,
                30.09,2419.791,1563.517,92,
                0.45,-0.65,0.8,0.6,#0.45,-0.65,0.8,1.7
                9.97e6, (2.4168), 
                -4.0, -8.5, -4.0, -8.0, 
                -0.5,  2.0, -0.75,  2.3,
                -6.122,-5.887,-5.497,-4.547,#-2.867,-3.370,-3.496,-3.171
                 7.29]
    
    return Info, radius
###############################################################################
def textfile(folder, name, star, bluecuts, redcuts, allcuts ,xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd,TotalSigN,
             srp435,srp555,srp625,srp814,
             rnd435,rnd555,rnd625,rnd814,
             crd435,crd555,crd625,crd814,
             chi435,chi555,chi625,chi814,
             qf435 ,qf555 ,qf625 ,qf814): 
     
    print "Save into text file"
    dataOut_1 = []
    dataOut_2 = []
    
    dataOut_1 = np.array(np.c_[star[bluecuts]  ,
        xcoord[bluecuts]+.5 ,ycoord[bluecuts]+.5 ,
        (((xsn - xcoord[bluecuts])**2 + (ysn - ycoord[bluecuts])**2)**.5),
        (f435mag[bluecuts] - f555mag[bluecuts]),
        TotalSigN[bluecuts],
        snr435[bluecuts] ,snr555[bluecuts] ,
        snr625[bluecuts] ,snr814[bluecuts] ,
        f435Abs[bluecuts],f555Abs[bluecuts],
        f625Abs[bluecuts],f814Abs[bluecuts],
        sharp[bluecuts],
        roond[bluecuts],
        crowd[bluecuts],
        srp435[bluecuts],srp555[bluecuts],srp625[bluecuts],srp814[bluecuts],
        rnd435[bluecuts],rnd555[bluecuts],rnd625[bluecuts],rnd814[bluecuts],
        crd435[bluecuts],crd555[bluecuts],crd625[bluecuts],crd814[bluecuts],
        chi435[bluecuts],chi555[bluecuts],chi625[bluecuts],chi814[bluecuts],
        qf435[bluecuts] ,qf555[bluecuts] ,qf625[bluecuts] ,qf814[bluecuts]
        ])
        
    dataOut_2 = np.array(np.c_[star[redcuts] ,
        xcoord[redcuts]+.5 ,ycoord[redcuts]+.5,
        (((xsn - xcoord[redcuts])**2 + (ysn - ycoord[redcuts])**2)**.5),
        (f625mag[redcuts] - f814mag[redcuts]),
        TotalSigN[redcuts],
        snr435[redcuts] ,snr555[redcuts] ,
        snr625[redcuts] ,snr814[redcuts] ,
        f435Abs[redcuts],f555Abs[redcuts],
        f625Abs[redcuts],f814Abs[redcuts],
        sharp[redcuts],
        roond[redcuts],
        crowd[redcuts],
        srp435[redcuts],srp555[redcuts],srp625[redcuts],srp814[redcuts],
        rnd435[redcuts],rnd555[redcuts],rnd625[redcuts],rnd814[redcuts],
        crd435[redcuts],crd555[redcuts],crd625[redcuts],crd814[redcuts],
        chi435[redcuts],chi555[redcuts],chi625[redcuts],chi814[redcuts],
        qf435[redcuts] ,qf555[redcuts] ,qf625[redcuts] ,qf814[redcuts]
        ])
        
    dataOut_all = np.array(np.c_[star[allcuts] ,
        xcoord[allcuts]+.5 ,ycoord[allcuts]+.5,
        (((xsn - xcoord[allcuts])**2 + (ysn - ycoord[allcuts])**2)**.5),
        (f435mag[allcuts] - f555mag[allcuts]),
        (f625mag[allcuts] - f814mag[allcuts]),
        TotalSigN[allcuts],
        snr435[allcuts] ,snr555[allcuts] ,
        snr625[allcuts] ,snr814[allcuts] ,
        f435Abs[allcuts],f555Abs[allcuts],
        f625Abs[allcuts],f814Abs[allcuts],
        sharp[allcuts],
        roond[allcuts],
        crowd[allcuts],
        srp435[allcuts],srp555[allcuts],srp625[allcuts],srp814[allcuts],
        rnd435[allcuts],rnd555[allcuts],rnd625[allcuts],rnd814[allcuts],
        crd435[allcuts],crd555[allcuts],crd625[allcuts],crd814[allcuts],
        chi435[allcuts],chi555[allcuts],chi625[allcuts],chi814[allcuts],
        qf435[allcuts] ,qf555[allcuts] ,qf625[allcuts] ,qf814[allcuts]
        ])
    
    np.savetxt(folder +'/'+ name + 'clust435555.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub      '\
               'S/N     S/N 435   S/N 555   S/N 625   S/N 814  '\
               'AbsMag435  AbsMag555 AbsMag625 AbsMag814  '\
               'Sharp    Round    Crowd   '\
               'Sharp 435    555        625      814    '\
               'Round 435  555       625      814    '\
               'Crowd 435  555       625      814    '\
               'CHI435     555      625     814   '\
               'QualFlag435  555       625     814')
    
    np.savetxt(folder +'/'+ name + 'clust625814.txt', dataOut_2 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub      '\
               'S/N     S/N 435   S/N 555   S/N 625   S/N 814  '\
               'AbsMag435  AbsMag555 AbsMag625 AbsMag814  '\
               'Sharp    Round    Crowd   '\
               'Sharp 435    555        625      814    '\
               'Round 435  555       625      814    '\
               'Crowd 435  555       625      814    '\
               'CHI435     555      625     814   '\
               'QualFlag435  555       625     814')
               
    f_handle = file(folder +'/'+'cluster.txt', 'a')
    np.savetxt(f_handle, dataOut_all,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix       DisFromSN  Sub-4-5  Sub-6-8    '\
               'S/N     S/N 435   S/N 555   S/N 625   S/N 814  '\
               'AbsMag435  AbsMag555 AbsMag625 AbsMag814  '\
               'Sharp    Round    Crowd   '\
               'Sharp 435    555        625      814    '\
               'Round 435  555       625      814    '\
               'Crowd 435  555       625      814    '\
               'CHI435     555      625     814   '\
               'QualFlag435  555       625     814')
    f_handle.close()

    print "Text files " + name + ".cut435555.txt & "+ name + '.cut625814.txt made'
    
###############################################################################
##################### Open and read in the data file ########################## 
###############################################################################
def main():
    ########################################################################### 
    ########################## declared variables #############################
    ########################################################################### 
    data    = []
    SigN    = []
    star    = [] # Column 11 the object type
    xcoord  = [] # Column 03 the x pix coordinate
    ycoord  = [] # Column 04 the y pix coordinate

    chi435  = [] 
    chi555  = []
    chi625  = [] 
    chi814  = []
    
    qf435  = [] 
    qf555  = []
    qf625  = [] 
    qf814  = []
    
    unc435  = [] # Column 18 SNR for F435W
    unc555  = [] # Column 31 SNR for F555W
    unc625  = [] # Column 44 SNR for F625W
    unc814  = [] # Column 57 SNR for F814W

    snr435  = [] # Column 20 SNR for F435W
    snr555  = [] # Column 33 SNR for F555W
    snr625  = [] # Column 46 SNR for F625W
    snr814  = [] # Column 59 SNR for F814W
    
    sharp   = []
    crowd   = []
    roond   = [] 
       
    radius  = []

    # arrays after the respective cuts

    f435mag = [] # Column 16 F435W Apparent Magnitude
    f555mag = [] # Column 29 F555W Apparent Magnitude
    f625mag = [] # Column 42 F625W Apparent Magnitude
    f814mag = [] # Column 55 F814W Apparent Magnitude
    
    f435Abs = [] # Absolute F435W Magnitudes
    f555Abs = [] # Absolute F555W Magnitudes
    f625Abs = [] # Absolute F625W Magnitudes
    f814Abs = [] # Absolute F814W Magnitudes
    ####################
    
    #Abs435 = [] 
    Abs555 = [] 
    #Abs625 = [] 
    Abs814 = []
    Apn435 = [] 
    Apn555 = []
    Apn625 = []
    Apn814 = [] 
    UncXl  = [] 
    UncYl  = []
    UncXr  = [] 
    UncYr  = [] 
    #SN435  = [] 
    #SN555  = []
    #SN625  = [] 
    #SN814  = []
    Radl   = [] 
    Radr   = []   
    ########################################################################### 
    print 'Choose a Supernova! Available SNe:'
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
    
    dectxt  = raw_input('Do you want make a text file            (y/n):')
    decreg  = raw_input('Do you want make a region file          (y/n):')
    decrange= raw_input('Do you want to plot age range?          (y/n):')
    decerrb = raw_input('Plot: Do you want to see errorbars      (y/n):')
    decmet  = raw_input('Plot: Do you want to plot the isochrone (y/n):')
    dechost = raw_input('Plot: Isochrone reddening, Host Galaxy  (y/n):')
    deccol  = raw_input('Plot: Would you rather make a Col-Col?  (y/n):')
    print "Get Supernova information"
    SNstuff, radius = SNinfo(SNname)
    
    folder  = SNstuff[0] #[folder, file,                    0,1
    name    = SNstuff[1] 
    ACS435  = SNstuff[2]  #ACS435,ACS555,ACS625,ACS814,      2,3,4,5, 
    ACS555  = SNstuff[3]  
    ACS625  = SNstuff[4]
    ACS814  = SNstuff[5]
    #MW      = SNstuff[6] #MW,Host,                          6,7,
    #Host    = SNstuff[7]
    H435    = SNstuff[8] #H435,H555,H625,H814,              8,9,10,11
    H555    = SNstuff[9]
    H625    = SNstuff[10]
    H814    = SNstuff[11]
    dmod    = SNstuff[12] #dmod,xsn,ysn,                     12,13,14,
    xsn     = SNstuff[13]
    ysn     = SNstuff[14]
    
    sharpmax = SNstuff[15] #sharpmax, sharpmin, round, crowd, 15,16,17,18
    sharpmin = SNstuff[16]
    roundmax = SNstuff[17]
    crowdmax = SNstuff[18]
    
    #dist   = SNstuff[19] #dist, conver,                     19,10,
    conver = SNstuff[20]
    
    yLmax  = SNstuff[21] #yLmax, yLmin, yRmax, yRmin,       21,22,23,24
    yLmin  = SNstuff[22]
    yRmax  = SNstuff[23]
    yRmin  = SNstuff[24]
    
    xLmax  = SNstuff[25] #xLmax, xLmin, xRmax, xRmin,       25,26,27,28
    xLmin  = SNstuff[26]
    xRmax  = SNstuff[27]
    xRmin  = SNstuff[28]
    
    sn435 = SNstuff[29]  #sn435, sn555, sn625, sn814,       29,30,31,32
    sn555 = SNstuff[30]
    sn625 = SNstuff[31]
    sn814 = SNstuff[32]
    iag   = SNstuff[33] #age]                              33
    
    
    s0 = np.where(Radl <= radius[0])
    s1 = np.where(Radl <= radius[1])
    s2 = np.where(Radl <= radius[2])
    
    r0 = np.where(Radr <= radius[0])
    r1 = np.where(Radr <= radius[1])
    r2 = np.where(Radr <= radius[2])
    
    print "Opening file: ",name
    print "Extracting ", name, " information..."
    
    data = pandas.read_csv(str(folder) + '/' + name,delim_whitespace=True, header=None)

    print "Organizing ", name, " information..."

    data    = np.array(data)
    data    = data.astype(float)

    star    = data[:,10] # object type
    SigN    = data[:, 5] # total Signal to noise
    
    sharp   = data[:, 6]
    roond   = data[:, 7] # round is already a special word
    crowd   = data[:, 9]
    
    f435mag = data[:,15] # instramental VEGAMAG magnitude
    f555mag = data[:,28]
    f625mag = data[:,41]
    f814mag = data[:,55]
    
    #unc435  = data[:,17] # uncertainty 
    #unc555  = data[:,30]
    #unc625  = data[:,43]
    #unc814  = data[:,56]
      
    snr435  = data[:,19] # signal to noise
    snr555  = data[:,32]
    snr625  = data[:,45]
    snr814  = data[:,58]

    srp435  = data[:,20] # Column 21 Sharp for F435W
    srp555  = data[:,33] # Column 34 Sharp for F555W
    srp625  = data[:,46] # Column 47 Sharp for F625W
    srp814  = data[:,59] # Column 60 Sharp for F814W
    
    rnd435  = data[:,21] # Column 22 Round for F435W
    rnd555  = data[:,34] # Column 35 Round for F555W
    rnd625  = data[:,47] # Column 48 Round for F625W
    rnd814  = data[:,60] # Column 61 Round for F814W
    
    crd435  = data[:,22] # Column 23 Crowd for F435W
    crd555  = data[:,35] # Column 36 Crowd for F555W
    crd625  = data[:,48] # Column 49 Crowd for F625W
    crd814  = data[:,61] # Column 62 Crowd for F814W
    
    qf435  = data[:,23] 
    qf555  = data[:,36] 
    qf625  = data[:,49] 
    qf814  = data[:,62]   
    
    xcoord = data[:, 2]
    ycoord = data[:, 3]
    ########################################################################### 
    ####################### Calculate Absolute Magnitude ######################
    ########################################################################### 
    print "Calculating Absolute Magnitude..."
    #dmod = 5*log(D(pc)) - 5
    f435Abs = f435mag - dmod - ACS435 - H435
    f555Abs = f555mag - dmod - ACS555 - H555
    f625Abs = f625mag - dmod - ACS625 - H625
    f814Abs = f814mag - dmod - ACS814 - H814
    ########################################################################### 
    ######################### Make  filters ###################################
    ###########################################################################       
    bluecuts = []
    redcuts  = []
    all_cuts = []
    bluecuts, redcuts, all_cuts = cutdata(SNname,sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn,ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            f435Abs, f555Abs, f625Abs, f814Abs,
            xcoord, ycoord,
            srp435,srp555,srp625,srp814,
            rnd435,rnd555,rnd625,rnd814,
            crd435,crd555,crd625,crd814,
            chi435,chi555,chi625,chi814,
            qf435 ,qf555 ,qf625 ,qf814,
            SigN)
    ###########################################################################
    ############################ Save as Text #################################
    ###########################################################################   
    if (dectxt == 'y'):
        print "I miss the era of stone tablets"
        textfile(folder,SNname,star,bluecuts[0],redcuts[0],all_cuts[0],xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd,
             SigN,
             srp435,srp555,srp625,srp814,
             rnd435,rnd555,rnd625,rnd814,
             crd435,crd555,crd625,crd814,
             chi435,chi555,chi625,chi814,
             qf435 ,qf555 ,qf625 ,qf814)
    else:
        print "Papyrus is going to come back in style."
    ########################################################################### 
    ############################ Save as Region################################
    ###########################################################################
    if (decreg == 'y'):
        regfile(folder,bluecuts[0],redcuts[0],xsn,ysn,xcoord,ycoord,all_cuts[0])
    else:
        print "Moving along"   
    ########################################################################### 
    ########################## Make Isochrone #################################
    ########################################################################### 
    MetFile = []
    F435W   = []
    F555W   = []
    F625W   = []
    F814W   = []
    AGE     = []
    Metname = []
    ISOALL  = []
    
    if (decmet  == 'y'):
        MetFile, Metname = met(SNname)    
        MetFile = np.array(MetFile)  
        #print d
        #print np.shape(d) #(1L, 16776L, 21L)
        F435W, F555W, F625W, F814W, AGE, ISOALL = AGEinfo(MetFile, iag)
    else:    
        print "No isochrone"
    ########################################################################### 
    #if (decmet  == 'y'):
    #    iso(c1plt,c2plt,SNname,AGE,iag,F435W,F555W,F625W,F814W,H435,H555,H625,H814,ACS435,ACS555,ACS625,ACS814,ISOALL,dechost,decrange,deccol)   
    #else:
    #    print "Moving along"
    ########################################################################### 
    print "Begin plotting Isochrones..."
    h = [4, 4] # height of the plotted figure
    fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
    gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

    fig1.suptitle('SN 20' + SNname[2:] + ': CMD for Z = 0.' + Metname[1:-7] + ', Y = 0.' + Metname[6:-4], 
            fontdict = font, size=15)
    ########################################################################### 
            
    cmd45 = plt.subplot2grid((2,2), (0,0), colspan = 2)
    plt.gca().invert_yaxis()
    plt.xlabel("F625W - F814W (mag)",fontdict = font)
    plt.ylabel("M$_{F814W}$ (mag)",fontdict = font)
    if (dechost == 'y'):
        cmd45.scatter(np.subtract(np.add(Apn435[s2],H435),   np.add(Apn555[s2],H555)),
               np.add(Abs555[s2],H555), label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)          
        cmd45.scatter(np.subtract(np.add(Apn435[s1],H435),   np.add(Apn555[s1],H555)),
               np.add(Abs555[s1],H555), label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)  
        cmd45.errorbar(np.subtract(np.add(Apn435[s0],H435),  np.add(Apn555[s0],H555)),   
               np.add(Abs555[s0],H555), UncXl[s0],   UncYl[s0], 
               fmt=None, ecolor="k", marker=None, mew=0 )
        cmd45.scatter(np.subtract(np.add(Apn435[s0],H435),   np.add(Apn555[s0],H555)),
               np.add(Abs555[s0],H555), label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
               c='k',marker='o',s = 25.0)  
    elif (deccol == 'y'):
        cmd45.scatter(np.subtract(Abs435_all[s2],Abs555_all[s2]),np.subtract(Abs625_all[s2],Abs814_all[s2]),
                      label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)          
        c1plt.scatter(np.subtract(Abs435_all[s1],Abs555_all[s1]),
                      np.subtract(Abs625_all[s1],Abs814_all[s1]), label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)  
        cmd45.scatter(np.subtract(Abs435_all[s0],Abs555_all[s0]),
                      np.subtract(Abs625_all[s0],Abs814_all[s0]), label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
                      c='k',marker='o',s = 25.0)
    elif (decerrb == 'y'):  
        cmd45.errorbar(np.subtract(Apn435[s2],Apn555[s2]),Abs555[s2], UncXl[s2],   UncYl[s2], 
               fmt=None, ecolor="k", marker=None, mew=0 )              
        cmd45.scatter(np.subtract(Apn435[s2],Apn555[s2]),Abs555[s2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)       

        cmd45.errorbar(np.subtract(Apn435[s1],Apn555[s1]),Abs555[s1], UncXl[s1],   UncYl[s1], 
               fmt=None, ecolor="k", marker=None, mew=0 )               
        cmd45.scatter(np.subtract(Apn435[s1],Apn555[s1]),Abs555[s1], label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)  

        cmd45.errorbar(np.subtract(Apn435[s0],Apn555[s0]),Abs555[s0], UncXl[s0],   UncYl[s0], 
               fmt=None, ecolor="k", marker=None, mew=0 )
        cmd45.scatter(np.subtract(Apn435[s0],Apn555[s0]),Abs555[s0], label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
               c='k',marker='o',s = 25.0)  
    else:              
        cmd45.scatter(np.subtract(Apn435[s2],Apn555[s2]),Abs555[s2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)                 
        cmd45.scatter(np.subtract(Apn435[s1],Apn555[s1]),Abs555[s1], label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)
        cmd45.scatter(np.subtract(Apn435[s0],Apn555[s0]),Abs555[s0], label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
               c='k',marker='o',s = 25.0)  
    cmd45.tick_params(axis='both',labelbottom = font)
    
    cmd68 = plt.subplot2grid((2,2), (0,1), colspan = 2)
    plt.gca().invert_yaxis()
    plt.xlabel('Sharp F435W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    cmd68.hist(srp435[cut1],bins=50,color='c')
    cmd68.tick_params(axis='both',labelbottom = font)

    col45 = plt.subplot2grid((2,2), (0,2), colspan = 2)
    plt.gca().invert_yaxis()
    plt.xlabel("F435W - F555W (mag)",fontdict = font)
    plt.ylabel("F625W - F814W (mag)",fontdict = font)
    col45.hist(srp555[cut1],bins=50,color='c')
    col45.tick_params(axis='both',labelbottom = font)

    col68 = plt.subplot2grid((2,2), (0,3), colspan = 2)
    plt.gca().invert_yaxis()
    plt.xlabel("F625W - F814W (mag)",fontdict = font)
    plt.ylabel("F435W - F555W (mag)",fontdict = font)
    col68.hist(srp625[cut1],bins=50,color='c')
    col68.tick_params(axis='both',labelbottom = font)

    ###########################################################################

    
    ###########################################################################
    if (dechost == 'y'):
        c2plt.scatter(np.subtract(np.add(Apn625[r2],H625),   np.add(Apn814[r2],H814)),
               np.add(Abs814[r2],H814), label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)          
        c2plt.scatter(np.subtract(np.add(Apn625[r1],H625),   np.add(Apn814[r1],H814)),
               np.add(Abs814[r1],H814), label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)
        c2plt.errorbar(np.subtract(np.add(Apn625[r0],H625),  np.add(Apn814[r0],H814)),   
               np.add(Abs814[r0],H814), UncXr[r0],   UncYr[r0], 
               fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(np.add(Apn625[r0],H625),   np.add(Apn814[r0],H814)),
               np.add(Abs814[r0],H814), label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 25.0)  
    elif (deccol == 'y'):
        c2plt.scatter(np.subtract(Abs625_all[r2],Abs814_all[r2]),
                      np.subtract(Abs435_all[r2],Abs555_all[r2]), 
                      label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)          
        c2plt.scatter(np.subtract(Abs625_all[r1],Abs814_all[r1]),
                      np.subtract(Abs435_all[r1],Abs555_all[r1]),
                      label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)
        c2plt.scatter(np.subtract(Abs625_all[r0],Abs814_all[r0]),
                      np.subtract(Abs435_all[r0],Abs555_all[r0]), 
                      label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 25.0) 
    elif (decerrb == 'y'):
        c2plt.errorbar(np.subtract(Apn625[r2],Apn814[r2]),Abs814[r2], 
                       UncXr[r2],   UncYr[r2], fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(Apn625[r2],Apn814[r2]),Abs814[r2], 
                      label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)   

        c2plt.errorbar(np.subtract(Apn625[r1],Apn814[r1]),Abs814[r1], 
                       UncXr[r1],   UncYr[r1], fmt=None, ecolor="k", marker=None, mew=0 )        
        c2plt.scatter(np.subtract(Apn625[r1],Apn814[r1]),Abs814[r1], 
                      label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)

        c2plt.errorbar(np.subtract(Apn625[r0],Apn814[r0]),Abs814[r0], 
                       UncXr[r0],   UncYr[r0], fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(Apn625[r0],Apn814[r0]),Abs814[r0], 
                      label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 25.0)
    else:
        c2plt.scatter(np.subtract(Apn625[r2],Apn814[r2]),Abs814[r2], 
                      label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)   
        c2plt.scatter(np.subtract(Apn625[r1],Apn814[r1]),Abs814[r1], 
                      label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)
        c2plt.scatter(np.subtract(Apn625[r0],Apn814[r0]),Abs814[r0], 
                      label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 25.0)  
    

    ########################################################################### 
    #lL = c1plt.legend(prop = {'family' : 'serif'},loc=4)
    #lL.draw_frame(False)

    #lR = c2plt.legend(prop = {'family' : 'serif'},loc=4)
    #lR.draw_frame(False)
    ########################################################################### 
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)    

main() 