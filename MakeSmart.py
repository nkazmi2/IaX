import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import csv
#from itertools import izip
import pandas
import pickle
import pyregion
################################################### 
############### declared variables ################

special = []
data    = []

star    = [] # Column 11 the object type
SNR     = [] # Column 06 the signal to noise
CHI     = [] # Column 05 the Chi Fit 
xcoord  = [] # Column 03 the x pix coordinate
ycoord  = [] # Column 04 the y pix coordinate

unc435  = [] # Column 18 SNR for F435W
unc555  = [] # Column 31 SNR for F555W
unc625  = [] # Column 44 SNR for F625W
unc814  = [] # Column 57 SNR for F814W

chi435  = [] # Column 19 Chi for F435W
chi555  = [] # Column 32 Chi for F555W
chi625  = [] # Column 45 Chi for F625W
chi814  = [] # Column 58 Chi for F814W

snr435  = [] # Column 20 SNR for F435W
snr555  = [] # Column 33 SNR for F555W
snr625  = [] # Column 46 SNR for F625W
snr814  = [] # Column 59 SNR for F814W

sharp   = []
crowd   = []
roond   = [] 

srp435  = [] # Column 21 Sharp for F435W
srp555  = [] # Column 34 Sharp for F555W
srp625  = [] # Column 47 Sharp for F625W
srp814  = [] # Column 60 Sharp for F814W

rnd435  = [] # Column 22 Round for F435W
rnd555  = [] # Column 35 Round for F555W
rnd625  = [] # Column 48 Round for F625W
rnd814  = [] # Column 61 Round for F814W

crd435  = [] # Column 23 Crowd for F435W
crd555  = [] # Column 36 Crowd for F555W
crd625  = [] # Column 49 Crowd for F625W
crd814  = [] # Column 62 Crowd for F814W

good    = []
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

cut435555  = []
cut625814  = []

snr435_555 = []
snr625_814 = [] 

################################################### 
def pcklfile(Name, title, bluecuts, redcuts,xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord):
    print "Pickling!"
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
                    
    pickle.dump( snr435_555[0], open(Name + '/' + title + 'f435f555.p', "wb" ) )
    pickle.dump( snr625_814[0], open(Name + '/' + title + 'f625f814.p', "wb" ) )

    print "Pickled."
################################################### 
def SNinfo(Name):
    ################################################### 
    ######### Things that change for each sn ##########
    ##################### 2008ge ######################
        #[file,ACS435,ACS555,ACS625,ACS814,MW,Host,
        #H435,H555,H625,H814,
        #dmod,xsn,ysn,radius
        #coordlist, good/bad source list
        #sharpmax, sharpmin, round, crowd]
    Info = []
    if (Name == "SN2008GE"):
        Info = ['sn2008ge_new.phot',0.046,0.036,0.028,0.020,
                0.011,0.0,0,0,0,0,31.33,3247.539,3419.971,200,
                'sn2008ge.reg','sn2008ge_badList2.reg',
                0.165,-0.786,1.8,1.2]
    elif (Name == "SN2008HA"):
        Info = ['sn2008ha_new.phot',0.284,0.219,0.174,0.120,
                0.07,0.0,0,0,0,0,31.64,1736.199,3171.792,50,
                'sn2008ha_coord.reg', 'sn2008ha_1121.reg', 'sn2008ha_1121.reg',
                .55,-.44,2.7,1.7]
    elif (Name == "SN2010AE"):
        Info = ['sn2010ae.phot.out',0.509,0.394,0.313,0.215,
                0.124,0.5,2.052,1.588,1.262,0.867,30.9,1795.3831,1932.8080,100,
                'sn3coord.reg','sn3.reg', 
                .46,-.6,1.0,0.7]
    elif (Name == "SN2010EL"):
        Info = ['sn2010el.phot.out',0.033,0.025,0.020,0.014,
                0.008,0.8,3.255,2.517,2.001,1.376,30.09,2418.859,1570.826,100,
                'sn3coord.reg','sn3good.reg',
                .66,-.56,1.16,.72]
    return Info

################################################### 
def removBad(identify, r):
    save = []
    badX = []
    badY = []
    fix  = []
    for i in range(len(identify)):
        if (pyregion.ShapeList(identify[i].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
            fix.append(i)
            #yellow is good
            #cyan is bad

    for i in range(len(fix)):
        r[fix[i]].attr[1]["color"] = 'yellow'
        
    for i in range(len(r)):
        r1 = pyregion.ShapeList(r[i].attr[1].get("color"))
        if (r1[0] == 'c'):
            save.append(i) 
 
    for j in range(len(save)): 
        badX.append(r[save[j]].coord_list[0] - 0.5)
        badY.append(r[save[j]].coord_list[1] - 0.5)
    return badX, badY
################################################### 
def textfile(Name, title, bluecuts, redcuts,xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd): 
    print "Save into text file"
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
        crowd[bluecuts]#,
        #srp435[bluecuts],srp555[bluecuts],srp625[bluecuts],srp814[bluecuts],
        #rnd435[bluecuts],rnd555[bluecuts],rnd625[bluecuts],rnd814[bluecuts],
        #crd435[bluecuts],crd555[bluecuts],crd625[bluecuts],crd814[bluecuts],
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
        crowd[redcuts]#,
        #srp435[redcuts],srp555[redcuts],srp625[redcuts],srp814[redcuts],
        #rnd435[redcuts],rnd555[redcuts],rnd625[redcuts],rnd814[redcuts],
        #crd435[redcuts],crd555[redcuts],crd625[redcuts],crd814[redcuts],
        ])

    np.savetxt(Name +'/'+ title + 'cut435555.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisfromSN   Sub    S/N 435   S/N 555   S/N 625   S/N 814 ' \
               #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
               '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
               'Sharp Round Crowd Sharp 435   555   625   814 Round 435   555  625   814 Crowd 435  555  625  814')

    
    np.savetxt(Name +'/'+ title + 'cut625814.txt', dataOut_2 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub    S/N 435  S/N 555  S/N 625  S/N 814 ' \
               '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
               'Sharp Round Crowd  Sharp 435   555   625   814 Round 435   555  625   814 Crowd 435  555  625  814')



##################### 2012Z ######################
#dmod = 32.07 (TF)
###################################################    
######### Open and read in the data file ##########
def main():
    Name = "SN2010EL"
    print "Opening file: ",Name

    SNstuff = SNinfo(Name)
    name    = SNstuff[0] 
    ACS435  = SNstuff[1]  
    ACS555  = SNstuff[2]  
    ACS625  = SNstuff[3]
    ACS814  = SNstuff[4]
    #MW      = SNstuff[5]
    #Host    = SNstuff[6]
    #H435    = SNstuff[7]
    #H555    = SNstuff[8]
    #H625    = SNstuff[9]
    #H814    = SNstuff[10]
    dmod    = SNstuff[11]
    xsn     = SNstuff[12]
    ysn     = SNstuff[13]
    radius  = SNstuff[14]
    identify = pyregion.open(Name + '/' + SNstuff[14])
    r = pyregion.open(Name+ '/'+ SNstuff[15])    
    
    sharpmax = SNstuff[16]
    sharpmin = SNstuff[17]
    roundmax = SNstuff[18]
    crowdmax = SNstuff[19]
    
    print "Opening file: ",name
    print "Extracting ", name, " information..."
    data = pandas.read_csv(Name + '/' + name,delim_whitespace=True, header=None)
    title = name[:-8]

    print "Organizing ", name, " information..."

    data    = np.array(data)
    data    = data.astype(float)

    star    = data[:,10] # type
    #SNR     = data[:, 5] # general signal to noise
    #CHI     = data[:, 4] # general chi for fit 

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

    #rnd435  = data[:,21] # Column 22 Round for F435W
    #rnd555  = data[:,34] # Column 35 Round for F555W
    #rnd625  = data[:,47] # Column 48 Round for F625W
    #rnd814  = data[:,60] # Column 61 Round for F814W

    crd435  = data[:,22] # Column 23 Crowd for F435W
    crd555  = data[:,35] # Column 36 Crowd for F555W
    crd625  = data[:,48] # Column 49 Crowd for F625W
    crd814  = data[:,61] # Column 62 Crowd for F814W


    xcoord  = data[:, 2]
    ycoord  = data[:, 3]

################################################### 
########### Calculate Absolute Magnitude ##########

    print "Calculating Absolute Magnitude..."
    #dmod = 5*log(D(pc)) - 5

    f435Abs = f435mag - dmod - ACS435 #- H435
    f555Abs = f555mag - dmod - ACS555 #- H555
    f625Abs = f625mag - dmod - ACS625 #- H625
    f814Abs = f814mag - dmod - ACS814 #- H814
################################################### 
########### Deal with bad points ##########
    print "Filter bad sources...."
    print "Looking in " + Name
    badX, badY = removBad(identify, r)
    
    if (Name == "SN2008HA"):
        identifyL = pyregion.open(Name  + '/'+ title +'1121.reg') #sn08ha
        origcoord  = pyregion.open(Name  + '/'+ title +'coord.reg')
        badXL, badYL = removBad(identifyL, origcoord)

################################################### 
    print "Make final cuts..." 

    if (Name == "SN2008GE"):
        cut435555.append(np.where((star <= 2)   & (crowd <= crowdmax ) 
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin) 
                & (roond <= roundmax)
                & ((snr435 > 0 ) & (snr555 > 0 )) 
                & ((snr435 >= 3.5) & (snr555 >= 3.5))                 
                & ((srp435 <= 3)  & (srp555 <= 3)  & (srp625 <= 3)  & (srp814 <= 3) 
                & (srp435 >= -3)  & (srp555 >= -3) & (srp625 >= -3) & (srp814 >= -3))  
                & ((f435mag <= 80) & (f555mag <= 80)) 
                & ((crd435 <= 9)  & (crd555 <= 9)  & (crd625 <= 9)  & (crd814 <= 9))
                & ((((xsn   - xcoord)**2 + (ysn  - ycoord)**2)**.5) <= radius[0])               
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25)  
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord)) ))
        cut625814.append(np.where((star <= 2) & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin) 
                & (roond <= roundmax) 
                & ((snr625 > 0 ) & (snr814 > 0 )) 
                & ((snr625 >= 3.5) & (snr814 >= 3.5))              
                & ((srp435 <= 3)  & (srp555 <= 3)  & (srp625 <= 3)  & (srp814 <= 3) 
                & (srp435 >= -3)  & (srp555 >= -3) & (srp625 >= -3) & (srp814 >= -3))
                & ((f625mag <= 80) & (f814mag <= 80))
                & ((crd435 <= 9)  & (crd555 <= 9)  & (crd625 <= 9)  & (crd814 <= 9)) 
                & ((((xsn   - xcoord)**2 + (ysn  - ycoord)**2)**.5) <= radius[0])  
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25)
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))          
    elif (Name == "SN2008HA"):    
        cut435555.append(np.where((star <= 2) & (crowd <= crowdmax ) 
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((f435mag <= 90) & (f555mag <= 90))                 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[0])     
                & list(np.any(x not in badXL for x in xcoord) and np.any(y not in badYL for y in ycoord)) ))
        cut625814.append(np.where((star <= 2) & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax) 
                & ((snr625 >= 3) & (snr814 >= 3))
                & ((f625mag <= 90) & (f814mag <= 90))                
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[0]) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
    else:    
        cut435555.append(np.where((star <= 2)   & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)    
                & ((snr435 >= 3) & (snr555 >= 3))  
                & ((f435mag <= 90) & (f555mag <= 90)) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[0]) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cut625814.append(np.where((star <= 2)   & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)    
                & ((snr625 >= 3) & (snr814 >= 3))  
                & ((f625mag <= 90) & (f814mag <= 90))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[0]) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    sn1 = []
    sn2 = []
    sn3 = []
    sn4 = []
    sn1 = np.where((star <= 2) & (snr435 == 3.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))  
    print "Mean f435w Abs Mag at S/N = 3 : ", np.mean(f435Abs[sn1])  
    #print f435Abs[sn1]

    sn2 = np.where((star <= 2) & (snr555 == 3.0) &
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)) 
    print "Mean f555w Abs Mag at S/N = 3 : ", np.mean(f555Abs[sn2])
    #print f555Abs[sn2]

    sn3 = np.where((star <= 2) & (snr625 == 3.0) &
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))  
    print "Mean f625w Abs Mag at S/N = 3 : ", np.mean(f625Abs[sn3])
    #print f625Abs[sn3]

    sn4 = np.where((star <= 2) & (snr814 == 3.0) &
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)) 
    print "Mean f814w Abs Mag at S/N = 3 : ", np.mean(f814Abs[sn4])


    print "Applying contrains to SN Data..."

    #print "Mean Sharp Value " + title[:-1] + " : " + str(np.mean(sharp))
    #print "Mean Round Value " + title[:-1] + " : " + str(np.mean(roond))

################################################### 
############ Save good arrays to a file ###########
################################################### 
    pcklfile(Name,title,cut435555[0],cut625814[0],xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord)
    textfile(Name,title,cut435555[0],cut625814[0],xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd)


main() 