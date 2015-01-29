# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 13:23:45 2014

@author: Nova
"""
import numpy as np
import pyregion
import pandas

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
"""
folder   = "SN2008GE"
name     = 'sn2008ge.phot.out' 
#name     = 'sn2008ge_new.phot' 
#name     = 'sn2008ge_20141015_final.out'

# Actual X & Y pixel coordinates of sn
xsn      = 3249.22
ysn      = 3421.6611
"""
##################### 2008ha ######################
"""
folder   = "SN2008HA"
name     = 'sn2008ha_new.phot'

# Actual X & Y pixel coordinates of sn
xsn      = 1736.199#1736.352
ysn      = 3171.792#3172.530
"""
##################### 2010ae ######################
"""
folder   = "SN2010AE"
name     = 'sn2010ae.phot.out'

# Actual X & Y pixel coordinates of sn
xsn      = 1783.3953#1795.3831# 1796.640
ysn      = 1923.19955#1931.8080# 1931.995
"""
##################### 2010el ######################
#"""    
folder   = "SN2010EL"
name     = 'sn2010el.phot.out'
    
# Actual X & Y pixel coordinates of sn
xsn      = 2419.791
ysn      = 1563.517
#"""
###################################################    
######### Open and read in the data file ##########
print "Making Region File"
print "Opening file: ",name

print "Extracting ", name, " information..."
#data = np.loadtxt(folder + '/' + name)

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
identify = pyregion.open(folder + '/NewCat.reg') #sn08ge
r = pyregion.open(folder + '/NewCatCoord.reg')  

save = []
badX = []
badY = []
fix  = []

for i in range(len(identify)):
    if (pyregion.ShapeList(identify[i].attr[1].get("color"))  == ['y','e','l','l','o','w']):
        fix.append(i)
    #yellow is good
    #cyan is bad

for i in range(len(fix)):
    r[fix[i]].attr[1]["color"] = 'yellow'
    
for i in range(len(r)):
    r1 = pyregion.ShapeList(r[i].attr[1].get("color"))
    if (r1[0] == 'c'): # to make a list with only the bad points change == to !=
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
"""
cut.append(np.where((star <= 2)
                #& (((snr625 >= 15) & (snr814 >= 15)) 
                #| (( snr435 >= 15) & (snr555 >= 15)))
                #& (((snr625 >= 10) & (snr814 >= 10)) 
                #| (( snr435 >= 10) & (snr555 >= 10)))
                #& (((snr625 >= 5) & (snr814 >= 5)) 
                #| (( snr435 >= 5) & (snr555 >= 5)))
                & (((snr625 >= 3) & (snr814 >= 3)) 
                | (( snr435 >= 3) & (snr555 >= 3)))
                ))
"""                

if (folder == "SN2010AE"): 
    sharpmax = 0.271 #0.46
    sharpmin = -0.569#-.6
    roundmax = 0.794 #1.0
    crowdmax = 0.506 #0.7
    cut.append(np.where((star <= 2)     
                & (((snr625 >= 3) & (snr814 >= 3)) 
                | (( snr435 >= 3) & (snr555 >= 3)))            
                & (crowd <= crowdmax) 
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin) 
                & (roond <= roundmax) 
                & (((f435mag <= 90) & (f555mag <= 90)) | ((f625mag <= 90) & (f814mag <= 90)))                               
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 20)      
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
elif (folder == "SN2010EL"): 
    """Sharp Max:  0.148
    Sharp Min:  -0.315
    SharpMean:  -0.0771
    Round Max:  0.341
    RoundMean:  0.1212
    Crowd Max:  0.291
    CrowdMean:  0.100633333333
    """
    sharpmax =  0.66 
    sharpmin = -0.56
    roundmax =  1.16 
    crowdmax =  0.72
    cut.append(np.where((star <= 2)     
                & (((snr625 >= 3) & (snr814 >= 3)) 
                | (( snr435 >= 3) & (snr555 >= 3)))          
                #& (crowd <= crowdmax)
                #& (sharp <= sharpmax) 
                #& (sharp >= sharpmin) 
                #& (roond <= roundmax) 
                & (((f435mag <= 90) & (f555mag <= 90)) | ((f625mag <= 90) & (f814mag <= 90)))               
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 21)      
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
elif (folder == "SN2008GE"):   
    sharpmax =  0.06
    sharpmin = -0.35
    roundmax =  1.5
    crowdmax =  0.2 # 1.15
    cut.append((np.where((star <= 2)   
                & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin) 
                & (roond <= roundmax) 
                & (((snr625 > 0 ) & (snr814 > 0 )) | ((snr435 > 0 ) & (snr555 > 0 )))
                & (((snr625 >= 3) & (snr814 >= 3)) | ((snr435 >= 3) & (snr555 >= 3)))            
                #& (((snr625 >= 3.5) & (snr814 >= 3.5)) | ((snr435 >= 3.5) & (snr555 >= 3.5)))            
                #& ((srp435 <= 3)  & (srp555 <= 3)  & (srp625 <= 3)  & (srp814 <= 3) 
                #& (srp435 >= -3)  & (srp555 >= -3) & (srp625 >= -3) & (srp814 >= -3))
                & (((f435mag <= 90) & (f555mag <= 90)) | ((f625mag <= 90) & (f814mag <= 90)))
                #& ((crd435 <= 9)  & (crd555 <= 9)  & (crd625 <= 9)  & (crd814 <= 9)) 
                & ((((xsn   - xcoord)**2 + (ysn  - ycoord)**2)**.5) <= 160)               
                & ((((3372  - xcoord)**2 + (3388 - ycoord)**2)**.5) >= 25) 
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))
                )))

for i in range(len(xcoord[cut[0]])):
    circ.append('circle(')
    comm.append(',')
    clos.append(',2)')

np.savetxt(folder +'/del2.reg', np.c_[circ,xcoord[cut[0]]+.5,comm,ycoord[cut[0]]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=green dashlist=8 3 width=1' \
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1' \
               '\nimage;' )
print 'Files Saved'


print "Sharp Max: ", np.max( sharp[cut[0]])
print "Sharp Min: ", np.min( sharp[cut[0]])
print "SharpMean: ", np.mean(sharp[cut[0]]) 
print "Round Max: ", np.max( roond[cut[0]])
print "RoundMean: ", np.mean(roond[cut[0]])
print "Crowd Max: ", np.max( crowd[cut[0]])
print "CrowdMean: ", np.mean(crowd[cut[0]])

print "435 values"
print "Sharp Max: ", np.max( srp435[cut[0]])
print "Sharp Min: ", np.min( srp435[cut[0]])
print "SharpMean: ", np.mean(srp435[cut[0]]) 
print "Round Max: ", np.max( rnd435[cut[0]])
print "RoundMean: ", np.mean(rnd435[cut[0]])
print "Crowd Max: ", np.max( crd435[cut[0]])
print "CrowdMean: ", np.mean(crd435[cut[0]])

print "555 values"
print "Sharp Max: ", np.max( srp555[cut[0]])
print "Sharp Min: ", np.min( srp555[cut[0]])
print "SharpMean: ", np.mean(srp555[cut[0]]) 
print "Round Max: ", np.max( rnd555[cut[0]])
print "RoundMean: ", np.mean(rnd555[cut[0]])
print "Crowd Max: ", np.max( crd555[cut[0]])
print "CrowdMean: ", np.mean(crd555[cut[0]])

print "625 values"
print "Sharp Max: ", np.max( srp625[cut[0]])
print "Sharp Min: ", np.min( srp625[cut[0]])
print "SharpMean: ", np.mean(srp625[cut[0]]) 
print "Round Max: ", np.max( rnd625[cut[0]])
print "RoundMean: ", np.mean(rnd625[cut[0]])
print "Crowd Max: ", np.max( crd625[cut[0]])
print "CrowdMean: ", np.mean(crd625[cut[0]])

print "814 values"
print "Sharp Max: ", np.max( srp814[cut[0]])
print "Sharp Min: ", np.min( srp814[cut[0]])
print "SharpMean: ", np.mean(srp814[cut[0]]) 
print "Round Max: ", np.max( rnd814[cut[0]])
print "RoundMean: ", np.mean(rnd814[cut[0]])
print "Crowd Max: ", np.max( crd814[cut[0]])
print "CrowdMean: ", np.mean(crd814[cut[0]])
"""
print "Make Text File"

yax1 = []
yax2 = []
dataOut_1 = np.array(np.c_[star[cut[0]]  ,
    xcoord[cut[0]]+.5 ,ycoord[cut[0]]+.5 ,
    (((xsn - xcoord[cut[0]])**2 + (ysn - ycoord[cut[0]])**2)**.5),
    #(f435mag[cut[0]] - f555mag[cut[0]]),
    snr435[cut[0]] ,snr555[cut[0]] ,
    snr625[cut[0]] ,snr814[cut[0]] ,
    #f435mag[cut[0]],f555mag[cut[0]],
    #f625mag[cut[0]],f814mag[cut[0]],
    sharp[cut[0]],#data[:,22][cut435555[0]],data[:,33][cut435555[0]],
    roond[cut[0]],#data[:,20][cut435555[0]],data[:,34][cut435555[0]],
    crowd[cut[0]],
    srp435[cut[0]],srp555[cut[0]],srp625[cut[0]],srp814[cut[0]],
    rnd435[cut[0]],rnd555[cut[0]],rnd625[cut[0]],rnd814[cut[0]],
    crd435[cut[0]],crd555[cut[0]],crd625[cut[0]],crd814[cut[0]],
    ])#,data[:,21][cut435555[0]],data[:,35][cut435555[0]] 
np.savetxt(folder +'/'+ title + 'del.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
    header ='Object Xpix        Ypix        DisfromSN   Sub    S/N 435   S/N 555   S/N 625   S/N 814 ' \
    #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
    '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
    'Sharp Round Crowd Sharp 435   555   625   814 Round 435   555  625   814 Crowd 435  555  625  814') 
    
print "Save into text file"
"""