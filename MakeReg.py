# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 13:23:45 2014

@author: Nova
"""
import numpy as np
import matplotlib.pyplot as plt
import pyregion

################################################### 
### Open the region file in ds9 and save
### to get it in the proper formatting
### Use ColorMag.py after. 
################################################### 
############### declared variables ################

data    = []

star    = [] # Column 11 the object type
xcoord  = [] # Column 03 the x pix coordinate
ycoord  = [] # Column 04 the y pix coordinate

f435mag = [] # Column 16 F435W Apparent Magnitude
f555mag = [] # Column 29 F555W Apparent Magnitude
f625mag = [] # Column 42 F625W Apparent Magnitude
f814mag = [] # Column 55 F814W Apparent Magnitude

snr435  = [] # Column 20 SNR for F435W
snr555  = [] # Column 33 SNR for F555W
snr625  = [] # Column 46 SNR for F625W
snr814  = [] # Column 59 SNR for F814W

sharp   = []
roond   = [] # round is already a special word
crowd   = []

srp435  = [] # Column 21 Sharp for F435W
srp555  = [] # Column 34 Sharp for F555W
srp625  = [] # Column 47 Sharp for F625W
srp814  = [] # Column 60 Sharp for F814W'

rnd435  = [] # Column 22 Round for F435W
rnd555  = [] # Column 35 Round for F555W
rnd625  = [] # Column 48 Round for F625W
rnd814  = [] # Column 61 Round for F814W

crd435  = [] # Column 23 Crowd for F435W
crd555  = [] # Column 36 Crowd for F555W
crd625  = [] # Column 49 Crowd for F625W
crd814  = [] # Column 62 Crowd for F814W

# arrays after the respective cuts

cut  = []

################################################### 
######### Things that change for each sn ##########
##################### 2008ge ######################
#"""
folder   = "SN2008GE"
name     = 'sn2008ge.phot' 
#name     = 'sn2008ge_20141015_final.out'

# Actual X & Y pixel coordinates of sn
xsn      = 3247.539
ysn      = 3419.971
#"""
##################### 2008ha ######################
"""
folder   = "SN2008HA"
name     = 'sn2008ha_new.phot'

# Actual X & Y pixel coordinates of sn
xsn      = 1726.352
ysn      = 3172.530
"""
##################### 2010ae ######################
"""

folder   = "SN2010AE"
name     = 'sn2010ae_new.phot'

# Actual X & Y pixel coordinates of sn
xsn      = 1796.640
ysn      = 1931.995
"""
##################### 2010el ######################
"""    
folder   = "SN2010EL"
name     = 'sn2010el_new.phot'
    
# Actual X & Y pixel coordinates of sn
xsn      = 2418.859
ysn      = 1570.826
"""
###################################################    
######### Open and read in the data file ##########

print "Opening file: ",name

print "Extracting ", name, " information..."
#data = np.loadtxt(folder + '/' + name)

import pandas
data = pandas.read_csv(folder + '/' + name,delim_whitespace=True, header=None)

title = name[:-9]
################################################### 
######## append data from file to an array ########

print "Organizing ", name, " information..."

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

srp435  = data[:,20] # Column 21 Sharp for F435W
srp555  = data[:,33] # Column 34 Sharp for F555W
srp625  = data[:,46] # Column 47 Sharp for F625W
srp814  = data[:,59] # Column 60 Sharp for F814W'

rnd435  = data[:,21] # Column 22 Round for F435W
rnd555  = data[:,34] # Column 35 Round for F555W
rnd625  = data[:,47] # Column 48 Round for F625W
rnd814  = data[:,60] # Column 61 Round for F814W

crd435  = data[:,22] # Column 23 Crowd for F435W
crd555  = data[:,35] # Column 36 Crowd for F555W
crd625  = data[:,48] # Column 49 Crowd for F625W
crd814  = data[:,61] # Column 62 Crowd for F814W

################################################### 
################################################### 

identify = pyregion.open(folder + '/sn2008ge_bad_search.reg') #sn08ge
#identify = pyregion.open(folder + '/'+ title +'final.reg') #sn08ha
r = pyregion.open(folder + '/sn2008ge.reg')
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
    badX.append(r[save[j]].coord_list[0] - .5)
    badY.append(r[save[j]].coord_list[1] - .5)

################################################### 
############ Save coordinates to a file ###########
print "Choppin some SN-suey"
circ = []
comm = []
clos = []

#sharpmax = np.mean(sharp) + .5
#sharpmin = np.mean(sharp) - .5
#roundmax = np.mean(roond) + .8

"""
sharpmax = 0.3 
sharpmin = -.45
roundmax = 2.0
crowdmax = 0.43

cut.append(np.where((star <= 2)     & (crowd <= crowdmax) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & 
                (((snr435 >= 3) | (snr555 >= 3)) |
                ((snr625 >= 3) | (snr814 >= 3))) &
                (((snr435 <= 30) & (snr555 <= 30)) |
                ((snr625 <= 30) & (snr814 <= 30)))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 150)))

""" 
#Sn2008ge testing stuff           
"""
sharpmax =  0.663
sharpmin = -0.792
roundmax =  2.048
crowdmax =  0.5
"""
sharpmax = 0.163
sharpmin = -.786
roundmax = 1.46
crowdmax = 1.2

cut.append(np.where((star <= 2)  & (crowd <= crowdmax ) 
                & (sharp <= sharpmax) & (sharp >= sharpmin) 
                & (roond <= roundmax)
                & ((snr625 > 0 ) & (snr814 > 0 )) 
                & ((snr625 >= 3) & (snr814 >= 3))              
                & ((srp435 <= 3)  & (srp555 <= 3)  & (srp625 <= 3)  & (srp814 <= 3) 
                & (srp435 >= -3)  & (srp555 >= -3) & (srp625 >= -3) & (srp814 >= -3))
                & ((snr435 <= 60) & (snr555 <= 60) & (snr625 <= 60) & (snr814 <= 60))
                & ((f625mag <= 80) & (f814mag <= 80))
                & ((crd435 <= 9)  & (crd555 <= 9)  & (crd625 <= 9)  & (crd814 <= 9))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= 50)                
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25)      
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord)) ))

print "Sharp Max: ", np.max(sharp[cut[0]])
print "Sharp Min: ", np.min(sharp[cut[0]])
print "SharpMean: ", np.mean(sharp[cut[0]]) 
print "Round Max: ", np.max(roond[cut[0]])
print "RoundMean: ", np.mean(roond[cut[0]])
print "Crowd Max: ", np.max(crowd[cut[0]])
print "CrowdMean: ", np.mean(crowd[cut[0]])

print "435 values"
print "Sharp Max: ", np.max(srp435[cut[0]])
print "Sharp Min: ", np.min(srp435[cut[0]])
print "SharpMean: ", np.mean(srp435[cut[0]]) 
print "Round Max: ", np.max(rnd435[cut[0]])
print "RoundMean: ", np.mean(rnd435[cut[0]])
print "Crowd Max: ", np.max(crd435[cut[0]])
print "CrowdMean: ", np.mean(crd435[cut[0]])

print "555 values"
print "Sharp Max: ", np.max(srp555[cut[0]])
print "Sharp Min: ", np.min(srp555[cut[0]])
print "SharpMean: ", np.mean(srp555[cut[0]]) 
print "Round Max: ", np.max(rnd555[cut[0]])
print "RoundMean: ", np.mean(rnd555[cut[0]])
print "Crowd Max: ", np.max(crd555[cut[0]])
print "CrowdMean: ", np.mean(crd555[cut[0]])

print "625 values"
print "Sharp Max: ", np.max(srp625[cut[0]])
print "Sharp Min: ", np.min(srp625[cut[0]])
print "SharpMean: ", np.mean(srp625[cut[0]]) 
print "Round Max: ", np.max(rnd625[cut[0]])
print "RoundMean: ", np.mean(rnd625[cut[0]])
print "Crowd Max: ", np.max(crd625[cut[0]])
print "CrowdMean: ", np.mean(crd625[cut[0]])

print "814 values"
print "Sharp Max: ", np.max(srp814[cut[0]])
print "Sharp Min: ", np.min(srp814[cut[0]])
print "SharpMean: ", np.mean(srp814[cut[0]]) 
print "Round Max: ", np.max(rnd814[cut[0]])
print "RoundMean: ", np.mean(rnd814[cut[0]])
print "Crowd Max: ", np.max(crd814[cut[0]])
print "CrowdMean: ", np.mean(crd814[cut[0]])


for i in range(len(xcoord[cut[0]])):
    circ.append('circle(')
    comm.append(',')
    clos.append(',2)')
    

np.savetxt(folder +'/toss.reg', np.c_[circ,xcoord[cut[0]]+.5,comm,ycoord[cut[0]]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=blue dashlist=8 3 width=1'
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1' \
               '\nimage;' )
print 'Files Saved'
"""
print "Make Text File"

dataOut_1 = np.array(np.c_[star[cut[0]]  ,
    xcoord[cut[0]] ,ycoord[cut[0]] ,
    (((xsn - xcoord[cut[0]])**2 + (ysn - ycoord[cut[0]])**2)**.5),
    (np.subtract(f435mag[cut[0]],f555mag[cut[0]])),
    snr435[cut[0]] ,snr555[cut[0]] ,
    snr625[cut[0]] ,snr814[cut[0]] ,
    f435mag[cut[0]],f555mag[cut[0]],
    f625mag[cut[0]],f814mag[cut[0]]  ,#])#   ,
    sharp[cut[0]],#data[:,22][cut[0]],data[:,33][cut[0]],
    roond[cut[0]],#data[:,20][cut[0]],data[:,34][cut[0]],
    crowd[cut[0]]])#,data[:,21][cut[0]],data[:,35][cut[0]] 
np.savetxt(folder +'/'+ title + 'sn5C.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
    header ='Object Xpix        Ypix        DisfromSN   Sub    S/N 435   S/N 555   S/N 625   S/N 814 ' \
    #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
    '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '   \
    'Sharp Round Crowd')
    
print "Save into text file"
"""