# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 17:24:17 2015

@author: nova
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 27 10:30:07 2014

@author: Nova
"""

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

#############################################################
################## Changing font parameters #################

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
radius = [5000]
################################################### 
######### Things that change for each sn ##########
##################### 2008ge ######################
#title = 'SN08ge'
#title = 'SN08ha'
title = 'SN10ae'
#title = 'SN10el'

if (title == 'SN08ge'):
    folder   = "SN2008GE"
    name     = 'sn2008ge.phot.out' 
    #name     = 'sn2008ge_20141015_final.out' #'sn2008ge_new.out'renamed for constistancy 

    # Magnitude of the Milkyway Galaxy 
    ACS435   = 0.046 #F435W
    ACS555   = 0.036 #F555W	
    ACS625   = 0.028 #F625W	
    ACS814   = 0.020 #F814W	
    MW       = 0.011
    Host     = 0.0
    
    H435     = 0 #F435W
    H555     = 0 #F555W	
    H625     = 0 #F625W	
    H814     = 0 #F814W	

    # Median (redshift independent) distance modulus of host galaxy
    dmod     = 31.33 

    # Actual X & Y pixel coordinates of sn
    xsn      = 3247.539
    ysn      = 3419.971
    #radius   = [200]
elif (title == 'SN08ha'):
    folder   = "SN2008HA"
    name     = 'sn2008ha_new.phot'
    # Magnitude of the Milkyway Galaxy 
    ACS435   = 0.284 #F435W
    ACS555   = 0.219 #F555W	
    ACS625   = 0.174 #F625W	
    ACS814   = 0.120 #F814W	
    MW       = 0.07
    Host     = 0.0

    H435     = 0 #F435W
    H555     = 0 #F555W	
    H625     = 0 #F625W	
    H814     = 0 #F814W	

    # Median (redshift independent) distance modulus of host galaxy
    dmod     = 31.64 #31.50 is the value I got from NED

    # Actual X & Y pixel coordinates of sn
    xsn      = 1736.199
    ysn      = 3171.792

    #radius   = [50] # 450,750,1000,1500,2200
elif (title == 'SN10ae'):
    folder   = "SN2010AE"
    name     = 'sn2010ae.phot.out'

    # Magnitude of the Milkyway Galaxy m is low(?) .1sol
    ACS435   = 0.509 #F435W
    ACS555   = 0.394 #F555W	
    ACS625   = 0.313 #F625W	
    ACS814   = 0.215 #F814W	
    MW       = 0.124
    Host     = 0.5
    
    H435     = 2.052 #F435W
    H555     = 1.588 #F555W	
    H625     = 1.262 #F625W	
    H814     = 0.867 #F814W	
    
    # Median (redshift independent) distance modulus of host galaxy
    dmod     = 30.9

    # Actual X & Y pixel coordinates of sn
    xsn      = 1795.3831# 1796.640
    ysn      = 1931.8080# 1931.995

    #radius   = [100] # 450,750,1000,1500,2200
elif (title == 'SN10el'):
    folder   = "SN2010EL"
    name     = 'sn2010el.phot.out'
    
    # Magnitude of the Milkyway Galaxy 
    ACS435   = 0.033 #F435W
    ACS555   = 0.025 #F555W	
    ACS625   = 0.020 #F625W	
    ACS814   = 0.014 #F814W	
    MW       = 0.008
    Host     = 0.8

    H435     = 3.255 #F435W
    H555     = 2.517 #F555W	
    H625     = 2.001 #F625W	
    H814     = 1.376 #F814W	
    
    # Median (redshift independent) distance modulus of host galaxy
    dmod     = 30.09 
    
    # Actual X & Y pixel coordinates of sn
    xsn      = 2418.859
    ysn      = 1570.826

    #radius   = [100] # 450,750,1000,1500,2200

###################################################    
######### Open and read in the data file ##########

print "Opening file: ",name

print "Extracting ", name, " information..."
#data = np.loadtxt(folder + '/' + name)
data = pandas.read_csv(folder + '/' + name,delim_whitespace=True, header=None)


title = name[:-8]
#title = name[:-18]
################################################### 
######## append data from file to an array ########

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

#data.close()
################################################### 
########### Calculate Absolute Magnitude ##########

print "Calculating Absolute Magnitude..."


f435Abs = f435mag - dmod - ACS435 #- H435
f555Abs = f555mag - dmod - ACS555 #- H555
f625Abs = f625mag - dmod - ACS625 #- H625
f814Abs = f814mag - dmod - ACS814 #- H814

################################################### 
print "Filter bad sources...."
print "Looking in " + folder

identify = pyregion.open(folder + '/NewCat.reg') 
r = pyregion.open(folder + '/NewCatCoord.reg')  

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
    
################################################### 
print "Make final cuts..." 
sharpmax = 0.46
sharpmin = -.6
roundmax = 1.0
crowdmax = 0.7
cut435555.append(np.where((star <= 2) 
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)    
                #& (( snr435 >= 15) & (snr555 >= 15))
                #& (( snr435 >= 10) & (snr555 >= 10))
                & (( snr435 >= 5) & (snr555 >= 5))
                #& (( snr435 >= 3) & (snr555 >= 3))
                & ((f435mag <= 80) & (f555mag <= 80)) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))
                )) 
cut625814.append(np.where((star <= 2) 
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & (roond <= roundmax)                    #& (( snr435 >= 15) & (snr555 >= 15))
                #& (( snr435 >= 10) & (snr555 >= 10))
                & ((snr625 >= 5) & (snr814 >= 5)) 
                #& ((snr625 >= 3) & (snr814 >= 3)) 
                & ((f625mag <= 80) & (f814mag <= 80))
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
   
print "Applying contrains to SN Data..."


################################################### 
############ Save good arrays to a file ###########
################################################### 

print "Pickling!"
snr435_555.append(( f435Abs[cut435555[0]],f555Abs[cut435555[0]], 
                    f435mag[cut435555[0]],f555mag[cut435555[0]],
                    ((unc435[cut435555[0]]**2 + unc555[cut435555[0]]**2)**.5 ),
                    unc555[cut435555[0]],
                    snr435[cut435555[0]], snr555[cut435555[0]],
                    (((xsn - xcoord[cut435555[0]])**2 + (ysn - ycoord[cut435555[0]])**2)**.5),
                    ))
snr625_814.append(( f625Abs[cut625814[0]],f814Abs[cut625814[0]],
                    f625mag[cut625814[0]],f814mag[cut625814[0]], 
                    ((unc625[cut625814[0]]**2 + unc814[cut625814[0]]**2)**.5 ),
                    unc814[cut625814[0]],
                    snr625[cut625814[0]], snr814[cut625814[0]],
                    (((xsn - xcoord[cut625814[0]])**2 + (ysn - ycoord[cut625814[0]])**2)**.5),
                    ))
                    
pickle.dump( snr435_555[0], open(folder + '/' + title + 'f435f555.p', "wb" ) )
pickle.dump( snr625_814[0], open(folder + '/' + title + 'f625f814.p', "wb" ) )

print "Pickled."
