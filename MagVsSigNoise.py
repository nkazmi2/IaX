# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 13:37:31 2014

@author: Nova
"""
###################################################  
############# Mag vs Sig/Noise ####################
################################################### 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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
##################### 2008ge ######################
"""

folder   = "SN2008GE"
SNname = "SN 2008GE"
name     = 'sn2008ge_new.phot'

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
dmod     = 31.27 

xsn      = 3247.539
ysn      = 3419.971
"""
##################### 2008ha ######################
#"""
folder   = "SN2008HA"
SNname  = "SN 2008HA"
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

dmod     = 31.64

xsn      = 1726.352
ysn      = 3172.530
#"""
##################### 2010ae ######################
"""
folder   = "SN2010AE"
SNname  = "SN 2010AE"
name     = 'sn2010ae_new.phot'

# Magnitude of the Milkyway Galaxy m is low(?) .1sol
ACS435   = 0.509 #F435W
ACS555   = 0.394 #F555W	
ACS625   = 0.313 #F625W	
ACS814   = 0.215 #F814W	
MW       = 0.124
Host     = 0.5

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	

dmod     = 30.58 

xsn      = 1796.640
ysn      = 1931.995
"""
##################### 2010el ######################
"""
folder   = "SN2010EL"
SNname   = "SN 2010EL"
name     = 'sn2010el_new.phot'
    
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

dmod     = 29.99 

xsn      = 2418.859
ysn      = 1570.826
#"""
###################################################

print "Opening file: ",name

print "Extracting ", name, " information..."
data = np.loadtxt(folder + '/' + name)

title = name[:-8]

data    = np.array(data)
data    = data.astype(float)

star    = data[:,10] # type

sharp   = data[:, 6]
roond   = data[:, 7] # round is already a special word
crowd   = data[:, 9]

f435mag = data[:,15] # instramental VEGAMAG magnitude
f555mag = data[:,28]
f625mag = data[:,41]
f814mag = data[:,55]

snr435  = data[:,19] # signal to noise
snr555  = data[:,32]
snr625  = data[:,45]
snr814  = data[:,58]

xcoord  = data[:, 2]
ycoord  = data[:, 3]

###################################################


sharpmax =  .3 #.54 #np.mean(sharp) + .5
sharpmin = -.45#-.467#np.mean(sharp) - .5
roundmax = 2.0 #np.mean(roond) + .8

f435Abs = []
f555Abs = []
f625Abs = []
f814Abs = []
f435Abs = f435mag - dmod - ACS435 #- H435
f555Abs = f555mag - dmod - ACS555 #- H555
f625Abs = f625mag - dmod - ACS625 #- H625
f814Abs = f814mag - dmod - ACS814 #- H814

cut1  = []
cut2  = []
cut3  = []
cut4  = []
cut1  = (np.where((star <= 2) & (snr435 >= 3) & (crowd <= .43 ) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & (snr435 <= 30) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 200)))
cut2  = (np.where((star <= 2) & (snr555 >= 3) & (crowd <= .43 ) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & (snr555 <= 30) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 200)))
cut3  = (np.where((star <= 2) & (snr625 >= 3) & (crowd <= .43 ) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & (snr625 <= 30) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 200)))
cut4  = (np.where((star <= 2) & (snr814 >= 3) & (crowd <= .43 ) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & (snr814 <= 30) 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 200)))
###################################################
print "Begin Plotting..."
h = [2, 5] # height of the plotted figure
fig = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(1, 1, height_ratios = h, hspace = 0.005)

squid = plt.subplot2grid((2,2), (0,0), colspan = 1)
plt.xlabel("Sig/Noise",fontdict = font)
plt.ylabel("Absolute Mag f435w (mag)",fontdict = font)
squid.scatter(snr435[cut1],f435Abs[cut1],marker='.')

soap  = plt.subplot2grid((2,2), (0,1), colspan = 1)
plt.xlabel("Sig/Noise",fontdict = font)
plt.ylabel("Absolute Mag f555w (mag)",fontdict = font)
soap.scatter(snr555[cut2],f555Abs[cut2],marker='.')

sope  = plt.subplot2grid((2,2), (1,0), colspan = 1)
plt.xlabel("Sig/Noise",fontdict = font)
plt.ylabel("Absolute Mag f625w (mag)",fontdict = font)
sope.scatter(snr625[cut3],f625Abs[cut3],marker='.')

supe  = plt.subplot2grid((2,2), (1,1), colspan = 1)
plt.xlabel("Sig/Noise",fontdict = font)
plt.ylabel("Absolute Mag f814w (mag)",fontdict = font)
supe.scatter(snr814[cut4],f814Abs[cut4],marker='.')

plt.tight_layout()
plt.savefig('Figures/' + SNname + "_MagSigNoise.png")    
plt.show()