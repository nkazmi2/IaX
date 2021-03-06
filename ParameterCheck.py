# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 17:59:51 2015

@author: nova
"""

###################################################  
############# Mag vs Sig/Noise ####################
################################################### 

import numpy as np
import pandas
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pyregion
################################################### 

params = {'legend.fontsize': 10, 
          'legend.linewidth': 2,
          'legend.font': 'serif',
          'mathtext.default': 'regular', 
          'xtick.labelsize': 10, 
          'ytick.labelsize': 10} # changes font size in the plot legend

plt.rcParams.update(params)                             # reset the plot parameters

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 10,
        } 
        
################################################### 
######### Things that change for each sn ##########
################################################### 
def cutdata(SNname, sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn, ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord,
            badX, badY,
            badXL, badYL,srp435,srp555,srp625,srp814,
            rnd435,rnd555,rnd625,rnd814,
            crd435,crd555,crd625,crd814):
    print "Make final cuts for", SNname 
    cut435555 = []
    cut625814 = []
    if (SNname == 'sn08ha'):
       cut1  = (np.where((star <= 2) 
                & (((snr625 >= 3) & (snr814 >= 3)) 
                | (( snr435 >= 3) & (snr555 >= 3)))                 
                & (crowd <= crowdmax)  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)               
                & ((((1716.4613  - xcoord)**2 + (3163.7546 - ycoord)**2)**.5) >= 7) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)))
    elif (SNname == 'sn08ge'):    
       cut1  = (np.where((star <= 2)
                #& (crd814 <= 2)
                #& (((snr625 >= 3) & (snr814 >= 3)) | (( snr435 >= 3) & (snr555 >= 3)))  
                #& (((snr625 >= 0) & (snr814 >= 0)) | (( snr435 >= 0) & (snr555 >= 0)))    
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25)
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)))
    else:
        cut435555.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)    
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((f435mag <= 90) & (f555mag <= 90)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cut625814.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)    
                & ((snr625 >= 3) & (snr814 >= 3))  
                & ((f625mag <= 90) & (f814mag <= 90))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    return cut1

###################################################     
def removBad(folder, good_list, coord_list):    
    print "Filter bad sources...."
    save = []
    pixX = []
    pixY = []
    fix  = []
    k    = []
    l    = []
    pixXL = []
    pixYL = []

    if (folder == "SN2008HA"):
        saveL = []
        fixL  = []
        i = []
        j = []
        identify  = pyregion.open(str(folder) + '/sn08ha_right.reg')
        r         = pyregion.open(str(folder) + '/sn2008ha_coord.reg')  
        identifyL = pyregion.open(str(folder) + '/sn08ha_left.reg') 
        origcoord = pyregion.open(str(folder) + '/sn2008ha_coord.reg') 
        
        for i in xrange(len(identifyL)):
            if (pyregion.ShapeList(identifyL[i].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
                fixL.append(i)
                #yellow is good
                #cyan is bad

        for i in xrange(len(fixL)):
            origcoord[fixL[i]].attr[1]["color"] = 'yellow'
            

        for i in xrange(len(origcoord)):
            p1 = pyregion.ShapeList(origcoord[i].attr[1].get("color"))
            if (p1[0] == 'c'):
                saveL.append(i) 

        for j in xrange(len(saveL)): 
            pixXL.append(origcoord[saveL[j]].coord_list[0] - 0.5)
            pixYL.append(origcoord[saveL[j]].coord_list[1] - 0.5)
    else:
        identify = pyregion.open(str(folder) + '/' + str(good_list))
        r        = pyregion.open(str(folder)+ '/'  + str(coord_list))  
    ############################### 
    for k in xrange(len(identify)):
        if (pyregion.ShapeList(identify[k].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
            fix.append(k)
            #yellow is good
            #cyan is bad

    for k in xrange(len(fix)):
        r[fix[k]].attr[1]["color"] = 'yellow'
        
    for k in xrange(len(r)):
        r1 = pyregion.ShapeList(r[k].attr[1].get("color"))
        if (r1[0] == 'c'):
            save.append(k) 
 
    for l in xrange(len(save)): 
        pixX.append(r[save[l]].coord_list[0] - 0.5)
        pixY.append(r[save[l]].coord_list[1] - 0.5)

    return pixX, pixY, pixXL, pixYL
###################################################     
def SNinfo(SNname):
        ##### Things that change for each sn ######
        #[folder, file,
        #dist, conv
        #ACS435,ACS555,ACS625,ACS814,
        #MW,Host,
        #H435,H555,H625,H814,
        #dmod,xsn,ysn,radius,
        #coordlist, good/bad source list,
        #sharpmax, sharpmin, round, crowd]
    Info = []
    if (SNname == "sn08ge"):
        Info = ['SN2008GE', 'sn2008ge.phot.out', 
                17.95e7,(4.35), 
                0.046,0.036,0.028,0.020,
                0.011,0.0,
                0.0,0.0,0.0,0.0,
                31.33,3249.22,3421.6611,52,
                'NewCat.reg','NewCatCoord.reg',
                0.6,-0.6,3,2]#0.06,-0.35,1.5,0.2]#1.0,-1.0,1.5,1.0]#0.06,-0.35,1.5,0.2]
    elif (SNname == "sn08ha"):
        Info = ['SN2008HA', 'sn2008ha_new.phot',
                20e7, (5),
                0.284,0.219,0.174,0.120,
                0.07,0.0,
                0.0,0.0,0.0,0.0,
                31.64,1736.199,3171.792,50,
                'sn2008ha_coord.reg', 'sn08ha_right.reg',
                .55,-.44,2.7,1.7]
    elif (SNname == "sn10ae"):
        Info = ['SN2010AE', 'sn2010ae.phot.out',
                13.1e7, (63.52), 
                0.509,0.394,0.313,0.215,
                0.124,0.5,
                2.052,1.588,1.262,0.867,
                30.9,1783.3953,1923.19955,70,
                'NewCat.reg','NewCatCoord.reg', 
                0.55,-0.44,3,2]#.4,-.5,.45,0.5]#0.5,-0.9,1.0,0.8]#9.0,-9.0,9.0,9.0]#
    elif (SNname == "sn10el"):
        Info = ['SN2010EL', 'sn2010el.phot.out',
                9.97e7, (48.33), 
                0.033,0.025,0.020,0.014,
                0.008,0.8,
                3.255,2.517,2.001,1.376,
                30.09,2419.791,1563.517,93,
                'NewCat.reg','NewCatCoord.reg',
                0.55,-0.44,3,2]#0.66,-0.40,0.62,0.4]
    return Info
    
###################################################
def save(name):
    #figname = title + '_' + 'Z' + name[1:-7]+ '.png'
    figname = name + '_' + 'Params_3' + '.png'
    plt.savefig('Figures/'+ figname)
    print "Save and show plot : " + figname
    
###################################################    
    
def textfile(folder, name, cuts, star, xsn, ysn,
             #unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd,
             srp435,srp555,srp625,srp814,
             rnd435,rnd555,rnd625,rnd814,
             crd435,crd555,crd625,crd814): 
     
    print "Save into text file"
    dataOut = []
    dataOut = np.array(np.c_[star[cuts]  ,
        xcoord[cuts]+.5 ,ycoord[cuts]+.5 ,
        (((xsn - xcoord[cuts])**2 + (ysn - ycoord[cuts])**2)**.5),
        snr435[cuts],snr555[cuts],snr625[cuts],snr814[cuts],
        sharp[cuts],
        srp435[cuts],srp555[cuts],srp625[cuts],srp814[cuts],
        roond[cuts],
        rnd435[cuts],rnd555[cuts],rnd625[cuts],rnd814[cuts],
        crowd[cuts],
        crd435[cuts],crd555[cuts],crd625[cuts],crd814[cuts]
        ])
        
    np.savetxt(folder +'/'+ name[:8] + '.CRS4.txt', dataOut ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN  '\
               'S/N 435  S/N 555  S/N 625  S/N 814 ' \
               #'  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
               'Sharp  435   555   625   814 Round 435   555  625   814 Crowd 435  555  625  814')


    print "Text files " + name + ".CRS.txt "
    
###################################################
def main():
    ################################################### 
    ############### declared variables ################
    data    = []
    star    = [] # Column 11 the object type
    xcoord  = [] # Column 03 the x pix coordinate
    ycoord  = [] # Column 04 the y pix coordinate

    #unc435  = [] # Column 18 SNR for F435W
    #unc555  = [] # Column 31 SNR for F555W
    #unc625  = [] # Column 44 SNR for F625W
    #unc814  = [] # Column 57 SNR for F814W

    snr435  = [] # Column 20 SNR for F435W
    snr555  = [] # Column 33 SNR for F555W
    snr625  = [] # Column 46 SNR for F625W
    snr814  = [] # Column 59 SNR for F814W
    
    sharp   = []
    crowd   = []
    roond   = [] 
       
    radius  = []

    # arrays after the respective cuts

    #f435mag = [] # Column 16 F435W Apparent Magnitude
    #f555mag = [] # Column 29 F555W Apparent Magnitude
    #f625mag = [] # Column 42 F625W Apparent Magnitude
    #f814mag = [] # Column 55 F814W Apparent Magnitude
    
    #f435Abs = [] # Absolute F435W Magnitudes
    #f555Abs = [] # Absolute F555W Magnitudes
    #f625Abs = [] # Absolute F625W Magnitudes
    #f814Abs = [] # Absolute F814W Magnitudes
    
    #################################################################
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
    
    
    decsave = raw_input('Do you want to save the figure (y/n):')
    dectext = raw_input('Make a text file               (y/n):')
    SNstuff = SNinfo(SNname)
        #[folder, file,
        #dist, conv
        #ACS435,ACS555,ACS625,ACS814,
        #MW,Host,
        #H435,H555,H625,H814,
        #dmod,xsn,ysn,radius,
        #coordlist, good/bad source list,
        #sharpmax, sharpmin, round, crowd]
    folder  = SNstuff[0] 
    name    = SNstuff[1] 
    dist    = SNstuff[2] 
    conv    = SNstuff[3] 
    ACS435  = SNstuff[4]  
    ACS555  = SNstuff[5]  
    ACS625  = SNstuff[6]
    ACS814  = SNstuff[7]
    #MW      = SNstuff[8]
    #Host    = SNstuff[9]
    H435    = SNstuff[10]
    H555    = SNstuff[11]
    H625    = SNstuff[12]
    H814    = SNstuff[13]
    dmod    = SNstuff[14]
    xsn     = SNstuff[15]
    ysn     = SNstuff[16]
    radius  = SNstuff[17]
    
    good_list = SNstuff[18]
    coor_list = SNstuff[19]
    
    sharpmax = SNstuff[20]
    sharpmin = SNstuff[21]
    roundmax = SNstuff[22]
    crowdmax = SNstuff[23]

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

    xcoord  = data[:, 2]
    ycoord  = data[:, 3]
    
    ###################################################
    badX  = []
    badY  = []  
    badXL = []
    badYL = []  
    #badX, badY, badXL, badYL = removBad(folder, good_list,coor_list)
    ###################################################
    """cut1 = cutdata(SNname,sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn,ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord,
            badX, badY,
            badXL, badYL,
            srp435,srp555,srp625,srp814,
            rnd435,rnd555,rnd625,rnd814,
            crd435,crd555,crd625,crd814)
    """
    cut1 = (np.where((star <= 2)           
                #& (SigN >= 3)
                #& ((snr625 >= 3) | (snr814 >= 3) | (snr435 >= 3) | (snr555 >= 3))
                #& ((((3817 - xcoord)**2 + (2967 - ycoord)**2)**.5) <= 200) 
                #& (snr625 >= 5) & (snr814 >= 5) & (snr435 >= 5) & (snr555 >= 5)   
                & (SigN >= 8)
                & ((snr625 >= 8) | (snr814 >= 8) | (snr435 >= 8) | (snr555 >= 8))
                #& (roond < .25)
                & (np.abs(sharp) < .6)
                #& (crowd <=.25)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #& ((f435mag <= 23) | (f555mag <= 23) | (f625mag <= 23) | (f814mag <= 23))             
                #& (roond <=3)
                #& (crowd <=3)
                #& (sharp <= .60) & (sharp >= -.60)
                #& ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                #& (crowd <= crowdmax ) 
                #& (snr625 >= 10) & (snr814 >= 10) & (snr435 >= 10) & (snr555 >= 10)     
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #& (srp435 <=  10) & (srp555 <= 5)
                #& (srp625 <= .8) & (srp814 <= .8)
                #& (roond <= roundmax)
                #& (crd435 <= 5) & (crd555 <= 5)
                #& (crd625 <= .5) & (crd814 <= .75)
                #& (srp435 <=  10) & (srp555 <= 4.5)
                #& (srp625 <= .73) & (srp814 <=  .4)
                #& (srp435 >= -2.55) & (srp555 >= -1.09)
                #& (srp625 >= -.53) & (srp814 >= -.47)
                #& (srp435 <=  10) & (srp555 <= 5)
                #& (srp625 <= .8) & (srp814 <= .8)
                #& ((rnd435 <= 4.2) & (rnd555 <= 4.2) & (rnd625 <= 4.2) & (rnd814 <= 4.2))
                #& ((crd435 <= 6.0) & (crd555 <= 6.0) & (crd625 <= 6.0) & (crd814 <= 6.0))
                #& (((snr625 >= 3) & (snr814 >= 3)) | ((snr435 >= 3) & (snr555 >= 3)))                  
                #& ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                ))
    """sn10ae = (np.where((star <= 2) 
                & (SigN <= 70)
                & (crowd <= crowdmax) 
                & (crd435 <= .6) & (crd555 <= .6)
                & (crd625 <= .6) & (crd814 <= .6)
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (srp435 <= .5) & (srp555 <= .5)
                & (srp625 <= .5) & (srp814 <= .5)
                & (srp435 >= -.5) & (srp555 >= -.5)
                & (srp625 >= -.5) & (srp814 >= -.5)
                & (roond <= roundmax) 
                & (rnd435 <=  .4) & (rnd555 <=  .4)
                & (rnd625 <=  .4) & (rnd814 <=  .4)
                & (rnd435 >= 0.0) & (rnd555 >= 0.0)
                & (rnd625 >= 0.0) & (rnd814 >= 0.0)
                #& (rnd435 >= -.1) & (rnd555 >= -.1)
                #& (rnd625 >= -.1) & (rnd814 >= -.1)
                & (np.subtract(f435mag,f555mag) <= 50)
                & (np.subtract(f435mag,f555mag) >= -50)
                & (np.subtract(f625mag,f814mag) <= 50)  
                & (np.subtract(f625mag,f814mag) >= -50) 
                & ((f435mag <= 90) & (f555mag <= 90))  
                & ((f625mag <= 90) & (f814mag <= 90))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)))
   sn10el -  
                & (SigN <= 70)
                & (crowd <= crowdmax) 
                & (crd435 <= 1) & (crd555 <= 1)
                & (crd625 <= 1) & (crd814 <= 1)
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (srp435 <= .5) & (srp555 <= .5)
                & (srp625 <= .5) & (srp814 <= .5)
                & (srp435 >= -.6) & (srp555 >= -.6)
                & (srp625 >= -.4) & (srp814 >= -.6)
                & (roond <= roundmax) 
                & (rnd435 <= .6) & (rnd555 <= .6)
                & (rnd625 <= .6) & (rnd814 <= .6)
                & (rnd435 >= -.3) & (rnd555 >= -.3)
                & (rnd625 >= -.3) & (rnd814 >= -.3)
                & (np.subtract(f435mag,f555mag) <=  50)
                & (np.subtract(f435mag,f555mag) >= -50)
                & (np.subtract(f625mag,f814mag) <=  50)  
                & (np.subtract(f625mag,f814mag) >= -50) 
                & ((f435mag <= 90) & (f555mag <= 90))  
                & ((f625mag <= 90) & (f814mag <= 90))     
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)))
    cut4  = (np.where((star <= 2) 
                #& (crowd <= .43 ) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)))
    
    cut435555  = []
    cut625814  = []
    
    cut435555, cut625814 = cutdata(SNname,sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn,ysn,
            snr435, snr555, snr625, snr814,
            #f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord)
    
    """
    
    print "Sharp Max: ", np.max( sharp[cut1])
    print "Sharp Min: ", np.min( sharp[cut1])
    print "SharpMean: ", np.mean(sharp[cut1]) 
    print "Round Max: ", np.max( roond[cut1])
    print "RoundMean: ", np.mean(roond[cut1])
    print "Crowd Max: ", np.max( crowd[cut1])
    print "CrowdMean: ", np.mean(crowd[cut1])

    print "435 values"
    print "Sharp Max: ", np.max( srp435[cut1])
    print "Sharp Min: ", np.min( srp435[cut1])
    print "SharpMean: ", np.mean(srp435[cut1]) 
    print "Round Max: ", np.max( rnd435[cut1])
    print "RoundMean: ", np.mean(rnd435[cut1])
    print "Crowd Max: ", np.max( crd435[cut1])
    print "CrowdMean: ", np.mean(crd435[cut1])

    print "555 values"
    print "Sharp Max: ", np.max( srp555[cut1])
    print "Sharp Min: ", np.min( srp555[cut1])
    print "SharpMean: ", np.mean(srp555[cut1]) 
    print "Round Max: ", np.max( rnd555[cut1])
    print "RoundMean: ", np.mean(rnd555[cut1])
    print "Crowd Max: ", np.max( crd555[cut1])
    print "CrowdMean: ", np.mean(crd555[cut1])

    print "625 values"
    print "Sharp Max: ", np.max( srp625[cut1])
    print "Sharp Min: ", np.min( srp625[cut1])
    print "SharpMean: ", np.mean(srp625[cut1]) 
    print "Round Max: ", np.max( rnd625[cut1])
    print "RoundMean: ", np.mean(rnd625[cut1])
    print "Crowd Max: ", np.max( crd625[cut1])
    print "CrowdMean: ", np.mean(crd625[cut1])

    print "814 values"
    print "Sharp Max: ", np.max( srp814[cut1])
    print "Sharp Min: ", np.min( srp814[cut1])
    print "SharpMean: ", np.mean(srp814[cut1]) 
    print "Round Max: ", np.max( rnd814[cut1])
    print "RoundMean: ", np.mean(rnd814[cut1])
    print "Crowd Max: ", np.max( crd814[cut1])
    print "CrowdMean: ", np.mean(crd814[cut1])
    
    
    
    h = [6, 6] # height of the plotted figure
    fig = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
    gs = gridspec.GridSpec(1, 1, height_ratios = h, hspace = 0.005)
    fig.suptitle('SN 20' + SNname[2:] + ' SRC Parameters', fontdict = font)#, size=15)
            
    srp1 = plt.subplot2grid((3,5), (0,0), colspan = 1)
    plt.xlabel('Sharp',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    srp1.hist(sharp[cut1],bins=50,color='c')
    
    srp4 = plt.subplot2grid((3,5), (0,1), colspan = 1)
    plt.xlabel('Sharp F435W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    srp4.hist(srp435[cut1],bins=50,color='c')

    srp5 = plt.subplot2grid((3,5), (0,2), colspan = 1)
    plt.xlabel('Sharp F555W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    srp5.hist(srp555[cut1],bins=50,color='c')

    srp6 = plt.subplot2grid((3,5), (0,3), colspan = 1)
    plt.xlabel('Sharp F625W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    srp6.hist(srp625[cut1],bins=50,color='c')
    
    srp8 = plt.subplot2grid((3,5), (0,4), colspan = 1)
    plt.xlabel('Sharp F814W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    srp8.hist(srp814[cut1],bins=50,color='c')
        
    ###################################################
    
    rnd  = plt.subplot2grid((3,5), (1,0), colspan = 1)
    plt.xlabel('Round',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    rnd.hist(roond[cut1],bins=50,color='c')
    
    rnd4 = plt.subplot2grid((3,5), (1,1), colspan = 1)
    plt.xlabel('Round F435W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    rnd4.hist(rnd435[cut1],bins=50,color='c')

    rnd5 = plt.subplot2grid((3,5), (1,2), colspan = 1)
    plt.xlabel('Round F555W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    rnd5.hist(rnd555[cut1],bins=50,color='c')

    rnd6 = plt.subplot2grid((3,5), (1,3), colspan = 1)
    plt.xlabel('Round F625W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    rnd6.hist(rnd625[cut1],bins=50,color='c')
    
    rnd8 = plt.subplot2grid((3,5), (1,4), colspan = 1)
    plt.xlabel('Round F814W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    rnd8.hist(rnd814[cut1],bins=50,color='c')
    ###################################################
    
    crd  = plt.subplot2grid((3,5), (2,0), colspan = 1)
    plt.xlabel('Crowd',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    crd.hist(crowd[cut1],bins=50,color='c')
    
    crd4 = plt.subplot2grid((3,5), (2,1), colspan = 1)
    plt.xlabel('Crowd F435W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    crd4.hist(crd435[cut1],bins=50,color='c')

    crd5 = plt.subplot2grid((3,5), (2,2), colspan = 1)
    plt.xlabel('Crowd F555W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    crd5.hist(crd555[cut1],bins=50,color='c')

    crd6 = plt.subplot2grid((3,5), (2,3), colspan = 1)
    plt.xlabel('Crowd F625W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    crd6.hist(crd625[cut1],bins=50,color='c')
    
    crd8 = plt.subplot2grid((3,5), (2,4), colspan = 1)
    plt.xlabel('Crowd F814W',fontdict = font)
    plt.ylabel('Count',fontdict = font)
    crd8.hist(crd814[cut1],bins=50,color='c')
    ###################################################
    if (dectext == 'y'): 
        textfile(folder, name, cut1, star, xsn, ysn,
             #unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd,
             srp435,srp555,srp625,srp814,
             rnd435,rnd555,rnd625,rnd814,
             crd435,crd555,crd625,crd814)
    if (decsave == 'y'):
        save(SNname)
    else:
        print "Not saving"
    ###################################################
        
main()