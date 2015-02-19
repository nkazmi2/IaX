import numpy as np
#import csv
import pandas
import pickle
import pyregion
################################################### 

def cutdata(SNname, sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn, ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord,
            badX, badY,
            badXL, badYL,
            srp435,srp555,srp625,srp814,crd814):
    print "Make final cuts for", SNname 
    cutL = []
    cutR = []
    if (SNname == 'sn08ha'):
        cutL.append(np.where((star <= 2) 
                & (crowd <= crowdmax ) 
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((f435mag <= 90) & (f555mag <= 90))                 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)       
                & ((((1716.4613  - xcoord)**2 + (3163.7546 - ycoord)**2)**.5) >= 7)    
                & list(np.any(x not in badXL for x in xcoord) and np.any(y not in badYL for y in ycoord)) ))
        cutR.append(np.where((star <= 2) 
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax) 
                & ((snr625 >= 3) & (snr814 >= 3))
                & ((f625mag <= 90) & (f814mag <= 90))                
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)      
                & ((((1716.4613  - xcoord)**2 + (3163.7546 - ycoord)**2)**.5) >= 7) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
    elif (SNname == 'sn08ge'):    
        cutL.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)                 
                & (crd814 <= 2)
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((snr435 > 0 ) & (snr555 > 0 )) 
                & ((f435mag <= 90) & (f555mag <= 90)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)      
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25)  
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cutR.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)                 
                & (crd814 <= 2)
                & ((snr625 >= 3) & (snr814 >= 3)) 
                & ((snr625 > 0 ) & (snr814 > 0 )) 
                & ((f625mag <= 90) & (f814mag <= 90))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)      
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25)  
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    elif (SNname == 'sn10ae'): 
        cutL.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)                  
                & (srp814 >= -3)   
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((f435mag <= 90) & (f555mag <= 90)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cutR.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)    
                & ((snr625 >= 3) & (snr814 >= 3))  
                & ((f625mag <= 90) & (f814mag <= 90))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    else:
        cutL.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)   
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((f435mag <= 90) & (f555mag <= 90)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cutR.append(np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (roond <= roundmax)    
                & ((snr625 >= 3) & (snr814 >= 3))  
                & ((f625mag <= 90) & (f814mag <= 90))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    return cutL, cutR
               
################################################### 

def pcklfile(folder, title, star, bluecuts, redcuts,xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord):
    snr435_555 = []
    snr625_814 = []
    snr435_555.append(( f435Abs[bluecuts],f555Abs[bluecuts], 
                    f435mag[bluecuts],f555mag[bluecuts],
                    ((unc435[bluecuts]**2 + unc555[bluecuts]**2)**.5 ),
                    unc555[bluecuts],
                    snr435[bluecuts], snr555[bluecuts],
                    (((xsn - xcoord[bluecuts])**2 + (ysn - ycoord[bluecuts])**2)**.5),
                    ))
    snr625_814.append(( f625Abs[redcuts],f814Abs[redcuts],
                    f625mag[redcuts],f814mag[redcuts], 
                    ((unc625[redcuts]**2 + unc814[redcuts]**2)**.5 ),
                    unc814[redcuts],
                    snr625[redcuts], snr814[redcuts],
                    (((xsn - xcoord[redcuts])**2 + (ysn - ycoord[redcuts])**2)**.5),
                    ))
                    
    pickle.dump( snr435_555[0], open(folder + '/' + title + 'f435f555.p', "wb" ) )
    pickle.dump( snr625_814[0], open(folder + '/' + title + 'f625f814.p', "wb" ) )

    print "Pickles!"
    
################################################### 
def SNinfo(SNname):
        ##### Things that change for each sn ######
        #[folder, file,
        #ACS435,ACS555,ACS625,ACS814,
        #MW,Host,
        #H435,H555,H625,H814,
        #dmod,xsn,ysn,radius,
        #coordlist, good/bad source list,
        #sharpmax, sharpmin, round, crowd]
    Info = []
    if (SNname == "sn08ge"):
        Info = ['SN2008GE', 'sn2008ge.phot.out', 
                0.046,0.036,0.028,0.020,
                0.011,0.0,
                0.0,0.0,0.0,0.0,
                31.33,3249.22,3421.6611,231,
                'NewCat.reg','NewCatCoord.reg',
                0.06,-0.35,1.5,0.2]
    elif (SNname == "sn08ha"):
        Info = ['SN2008HA', 'sn2008ha_new.phot',
                0.284,0.219,0.174,0.120,
                0.07,0.0,
                0.0,0.0,0.0,0.0,
                31.64,1736.199,3171.792,50,
                'sn2008ha_coord.reg', 'sn08ha_right.reg',
                0.55,-0.44,2.7,1.7]
    elif (SNname == "sn10ae"):
        Info = ['SN2010AE', 'sn2010ae.phot.out',
                0.509,0.394,0.313,0.215,
                0.124,0.5,
                2.052,1.588,1.262,0.867,
                30.9,1783.3953,1923.19955,9,
                'NewCat.reg','NewCatCoord.reg', 
                3.0,-0.9,1.5,0.8]#.46,-.6,1.0,0.7]
    elif (SNname == "sn10el"):
        Info = ['SN2010EL', 'sn2010el.phot.out',
                0.033,0.025,0.020,0.014,
                0.008,0.8,
                3.255,2.517,2.001,1.376,
                30.09,2419.791,1563.517,22,
                'NewCat.reg','NewCatCoord.reg',
                0.66,-0.40,0.62,0.45]
    return Info
################################################### 
def regfile(folder, bluecuts, redcuts,xsn,ysn,xcoord,ycoord): 
     
    print "Save into region file"

    circ      = []
    comm      = []
    clos      = []
    circR     = []
    commR     = []
    closR     = []
    for i in range(len(xcoord[redcuts])):
            circ.append('circle(')
            comm.append(',')
            clos.append(',2)')
    np.savetxt(folder +'/delL.reg', np.c_[circ,xcoord[redcuts]+.5,comm,ycoord[redcuts]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=green dashlist=8 3 width=1' \
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1' \
               '\nimage;' )
    for i in range(len(xcoord[bluecuts])):
            circR.append('circle(')
            commR.append(',')
            closR.append(',2)')
    np.savetxt(folder +'/delR.reg', np.c_[circR,xcoord[bluecuts]+.5,commR,ycoord[bluecuts]+.5,closR],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=green dashlist=8 3 width=1' \
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1' \
               '\nimage;' )     
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
def textfile(folder, name, star, bluecuts, redcuts,xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd): 
     
    print "Save into text file"
    dataOut_1 = []
    dataOut_2 = []
    
    dataOut_1 = np.array(np.c_[star[bluecuts]  ,
        xcoord[bluecuts]+.5 ,ycoord[bluecuts]+.5 ,
        (((xsn - xcoord[bluecuts])**2 + (ysn - ycoord[bluecuts])**2)**.5),
        (f435mag[bluecuts] - f555mag[bluecuts]),
        snr435[bluecuts] ,snr555[bluecuts] ,
        snr625[bluecuts] ,snr814[bluecuts] ,
        f435Abs[bluecuts],f555Abs[bluecuts],
        f625Abs[bluecuts],f814Abs[bluecuts],
        sharp[bluecuts],
        roond[bluecuts],
        crowd[bluecuts]
        ])
        
    dataOut_2 = np.array(np.c_[star[redcuts] ,
        xcoord[redcuts]+.5 ,ycoord[redcuts]+.5,
        (((xsn - xcoord[redcuts])**2 + (ysn - ycoord[redcuts])**2)**.5),
        (f625mag[redcuts] - f814mag[redcuts]),
        snr435[redcuts] ,snr555[redcuts] ,
        snr625[redcuts] ,snr814[redcuts] ,
        f435Abs[redcuts],f555Abs[redcuts],
        f625Abs[redcuts],f814Abs[redcuts],
        sharp[redcuts],
        roond[redcuts],
        crowd[redcuts]
        ])

    np.savetxt(folder +'/'+ name + '.cut435555.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisfromSN   Sub    S/N 435   S/N 555   S/N 625   S/N 814 ' \
               #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
               '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
               'Sharp Round Crowd Sharp 435   555   625   814 Round 435   555  625   814 Crowd 435  555  625  814')

    
    np.savetxt(folder +'/'+ name + '.cut625814.txt', dataOut_2 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub    S/N 435  S/N 555  S/N 625  S/N 814 ' \
               '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
               'Sharp Round Crowd  Sharp 435   555   625   814 Round 435   555  625   814 Crowd 435  555  625  814')
      
    print "Text files " + name + ".cut435555.txt & "+ name + '.cut625814.txt made'
    
################################################### 
def viewsnr(star, xsn, ysn, xcoord, ycoord, 
            snr435, snr555, snr625, snr814,
            f435Abs, f555Abs, f625Abs, f814Abs):    
    sn1 = []
    sn2 = []
    sn3 = []
    sn4 = []
    sn1 = np.where((star <= 2) & (snr435 >= 3.0) & (snr435 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))  
    print "Mean f435w Abs Mag at S/N = 3 : ", np.mean(f435Abs[sn1])  
            #print f435Abs[sn1]

    sn2 = np.where((star <= 2) & (snr555 >= 3.0) & (snr555 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)) 
    print "Mean f555w Abs Mag at S/N = 3 : ", np.mean(f555Abs[sn2])
            #print f555Abs[sn2]

    sn3 = np.where((star <= 2) & (snr625 >= 3.0) & (snr625 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))  
    print "Mean f625w Abs Mag at S/N = 3 : ", np.mean(f625Abs[sn3])
            #print f625Abs[sn3]

    sn4 = np.where((star <= 2) & (snr814 >= 3.0) & (snr814 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)) 
    print "Mean f814w Abs Mag at S/N = 3 : ", np.mean(f814Abs[sn4])

######### Open and read in the data file ##########
def main():
    ################################################### 
    ############### declared variables ################
    data    = []
    star    = [] # Column 11 the object type
    xcoord  = [] # Column 03 the x pix coordinate
    ycoord  = [] # Column 04 the y pix coordinate

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
    
    decpick = raw_input('Do you want to pickle the file       (y/n):')
    dectxt  = raw_input('Do you want make a text file         (y/n):')
    decreg  = raw_input('Do you want make a region file       (y/n):')
    decsnr  = raw_input('Do you want to look at the wavebands (y/n):')
    
    SNstuff = SNinfo(SNname)
    
    folder  = SNstuff[0] 
    name    = SNstuff[1] 
    ACS435  = SNstuff[2]  
    ACS555  = SNstuff[3]  
    ACS625  = SNstuff[4]
    ACS814  = SNstuff[5]
    #MW      = SNstuff[6]
    #Host    = SNstuff[7]
    H435    = SNstuff[8]
    H555    = SNstuff[9]
    H625    = SNstuff[10]
    H814    = SNstuff[11]
    dmod    = SNstuff[12]
    xsn     = SNstuff[13]
    ysn     = SNstuff[14]
    radius  = SNstuff[15]
    
    good_list = SNstuff[16]
    coor_list = SNstuff[17]
    
    sharpmax = SNstuff[18]
    sharpmin = SNstuff[19]
    roundmax = SNstuff[20]
    crowdmax = SNstuff[21]

    print "Opening file: ",name
    print "Extracting ", name, " information..."
    data = pandas.read_csv(str(folder) + '/' + name,delim_whitespace=True, header=None)

    print "Organizing ", name, " information..."

    data    = np.array(data)
    data    = data.astype(float)

    star    = data[:,10] # object type

    sharp   = data[:, 6]
    roond   = data[:, 7] # round is already a special word
    crowd   = data[:, 9]
    
    f435mag = data[:,15] # instramental VEGAMAG magnitude
    f555mag = data[:,28]
    f625mag = data[:,41]
    f814mag = data[:,55]
    
    unc435  = data[:,17] # uncertainty 
    unc555  = data[:,30]
    unc625  = data[:,43]
    unc814  = data[:,56]
        
    snr435  = data[:,19] # signal to noise
    snr555  = data[:,32]
    snr625  = data[:,45]
    snr814  = data[:,58]

    srp435  = data[:,20] # Column 21 Sharp for F435W
    srp555  = data[:,33] # Column 34 Sharp for F555W
    srp625  = data[:,46] # Column 47 Sharp for F625W
    srp814  = data[:,59] # Column 60 Sharp for F814W
    
    crd814  = data[:,61] # Column 62 Crowd for F814W
    
    xcoord  = data[:, 2]
    ycoord  = data[:, 3]
    
################################################### 
########### Calculate Absolute Magnitude ##########
################################################### 
    
    print "Calculating Absolute Magnitude..."
    #dmod = 5*log(D(pc)) - 5
    f435Abs = f435mag - dmod - ACS435 - H435
    f555Abs = f555mag - dmod - ACS555 - H555
    f625Abs = f625mag - dmod - ACS625 - H625
    f814Abs = f814mag - dmod - ACS814 - H814
    
################################################### 
############### Deal with bad points ##############
################################################### 
    
    print "Looking in " + folder
     
    badX  = []
    badY  = []  
    badXL = []
    badYL = []  
    badX, badY, badXL, badYL = removBad(folder, good_list,coor_list)

################################################### 
############### Make final filters ################
################################################### 
       
    cut435555  = []
    cut625814  = []
    cut435555, cut625814 = cutdata(SNname,sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn,ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord,
            badX, badY,
            badXL, badYL,
            srp435,srp555,srp625,srp814,crd814)
            
################################################### 
############ Save good arrays to a file ###########
###################################################  

    if (decpick == 'y'):
        print "Where are the pickles??"
        pcklfile(folder,SNname,star,cut435555[0],cut625814[0],xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord)
    else:
        print "No pickles today."
        
################################################### 
        
    if (dectxt == 'y'):
        print "I miss the era of stone tablets"
        textfile(folder,SNname,star,cut435555[0],cut625814[0],xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd)
    else:
        print "Papyrus is going to come back in style."

###################################################  
       
    if (decreg == 'y'):
        regfile(folder,cut435555[0],cut625814[0],xsn,ysn,xcoord,ycoord)
    else:
        print "Moving along"
        
################################################### 
        
    if (decsnr == 'y'):
        print "Look at waveband limits"
        viewsnr(star, xsn, ysn, xcoord, ycoord, 
            snr435, snr555, snr625, snr814,
            f435Abs, f555Abs, f625Abs, f814Abs)
    else:
        print "No waves here"
main() 