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
srp814  = [] # Column 60 Sharp for F814W'

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

################################################### 
######### Things that change for each sn ##########
##################### 2008ge ######################
#"""
folder   = "SN2008GE"
name     = 'sn2008ge.phot' 
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
dmod     = 31.08 #31.27 

# Actual X & Y pixel coordinates of sn
xsn      = 3247.539
ysn      = 3419.971
radius   = [10.342,17.24,23.00,34.47,50.556] # 450,750,1000,1500,2200
#radius   = [10,50,100,150,200]
#"""
##################### 2008ha ######################
"""
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

radius   = [9.282,15.469,20.63,30.94,45] # 450,750,1000,1500,2200
"""
##################### 2010ae ######################
"""
folder   = "SN2010AE"
name     = 'sn2010ae_new.phot'

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
dmod     = 30.51 #30.58 

# Actual X & Y pixel coordinates of sn
xsn      = 1795.3831# 1796.640
ysn      = 1931.8080# 1931.995

radius   = [14.171,23.62,31.50,47.236,67.295] # 450,750,1000,1500,2200
"""
##################### 2010el ######################
"""    
folder   = "SN2010EL"
name     = 'sn2010el_new.phot'
    
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
dmod     = 30.29 #29.99 

# Actual X & Y pixel coordinates of sn
xsn      = 2418.859
ysn      = 1570.826

radius   = [18.62,31.03,41.38,62.065,91.0287] # 450,750,1000,1500,2200
"""
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
srp814  = data[:,59] # Column 60 Sharp for F814W'

rnd435  = data[:,21] # Column 22 Round for F435W
rnd555  = data[:,34] # Column 35 Round for F555W
rnd625  = data[:,47] # Column 48 Round for F625W
rnd814  = data[:,60] # Column 61 Round for F814W

crd435  = data[:,22] # Column 23 Crowd for F435W
crd555  = data[:,35] # Column 36 Crowd for F555W
crd625  = data[:,48] # Column 49 Crowd for F625W
crd814  = data[:,61] # Column 62 Crowd for F814W


#chi435  = data[:,18] # Chi for fit
#chi555  = data[:,31] 
#chi625  = data[:,44] 
#chi814  = data[:,57]

xcoord  = data[:, 2]
ycoord  = data[:, 3]

#data.close()
################################################### 
########### Calculate Absolute Magnitude ##########

print "Calculating Absolute Magnitude..."
#dmod = 5*log(D(pc)) - 5

f435Abs = f435mag - dmod - ACS435 #- H435
f555Abs = f555mag - dmod - ACS555 #- H555
f625Abs = f625mag - dmod - ACS625 #- H625
f814Abs = f814mag - dmod - ACS814 #- H814
"""

f435Abs = f435mag - dmod - ACS435 - H435
f555Abs = f555mag - dmod - ACS555 - H555
f625Abs = f625mag - dmod - ACS625 - H625
f814Abs = f814mag - dmod - ACS814 - H814
"""
################################################### 
########### Deal with bad points ##########
if (folder == "SN2008GE"):   
    identify = pyregion.open(folder + '/sn2008ge_threeprog2.reg') #sn08ge
    r = pyregion.open(folder + '/sn2008ge_three.reg')
    #identify = pyregion.open(folder + '/sn2008ge_3good.reg') #sn08ge
    #r = pyregion.open(folder + '/sn2008ge_coord3.reg')
else:
    identify = pyregion.open(folder + '/'+ title +'final.reg') #sn08ha
    r = pyregion.open(folder + '/'+ title +'coord.reg')
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
    
#identify.close()
#r.close()
################################################### 
##### Find correct color magnitudes make cuts #####
# hard contrains because the mean of the list 
# isn't an accurate way to limit the good values
# using the contraints from 08ha, I've set
# the limits for sharp and round
sharpmax = 0.163
sharpmin = -.786
roundmax = 1.46
crowdmax = 1.2
#rad = []
#snr = []
if (folder == "SN2008GE"):
    #for m in range(3,6):
    #for i in range(len(radius)):
    cut435555.append(np.where((star <= 2)   & (crowd <= crowdmax ) 
                & (sharp <= sharpmax) & (sharp >= sharpmin) 
                & (roond <= roundmax)
                #((snr435 >= m) | (snr555 >= m)) & 
                #(snr435 >= 3) & (snr555 >= 3)  & 
                & ((snr435 > 0 ) & (snr555 > 0 )) 
                & ((snr435 >= 3) | (snr555 >= 3)) 
                & ((snr435 <= 55) & (snr555 <= 55) & (snr625 <= 55) & (snr814 <= 55))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[4])   #))#   
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord)) ))
    cut625814.append(np.where((star <= 2)   & (crowd <= crowdmax )  
                & (sharp <= sharpmax) & (sharp >= sharpmin) 
                & (roond <= roundmax) 
                #((snr625 >= m) | (snr814 >= m)) & 
                #(snr625 >= 3) & (snr814 >= 3)   &                 
                #(snr625 >= 0) & (snr814 >= 0)   & 
                & ((snr625 > 0 ) & (snr814 > 0 )) 
                & ((snr625 >= 3) | (snr814 >= 3)) 
                & ((snr435 <= 55) & (snr555 <= 55) & (snr625 <= 55) & (snr814 <= 55))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[4])   #))#     
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
            #rad.append(i)
            #snr.append(m)
"""else:    
    for m in range(3,6):
        for i in range(len(radius)):
            cut435555.append(np.where((star <= 2)   & (crowd <= crowdmax ) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & 
                ((snr435 >= m) | (snr555 >= m)) & 
                (snr435 >= 3) & (snr555 >= 3)  & 
                ((snr435 <= 30) & (snr555 <= 30) & (snr625 <= 30) & (snr814 <= 30)) & 
                ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[i])   #))#   
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord)) ))
            cut625814.append(np.where((star <= 2)   & (crowd <= crowdmax ) & 
                (sharp <= sharpmax) & (sharp >= sharpmin) & 
                (roond <= roundmax) & 
                ((snr625 >= m) | (snr814 >= m)) & 
                (snr625 >= 3) & (snr814 >= 3)   &                 
                ((snr435 <= 30) & (snr555 <= 30) & (snr625 <= 30) & (snr814 <= 30)) & 
                ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius[i])   #))#     
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
            rad.append(i)
            snr.append(m)
"""

sn3 = []
sn3 = np.where((star <= 2) & (snr555 == 3.0) &
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 50))    
print "Mean f555w Abs Mag at S/N = 3 : ", np.mean(f555Abs[sn3])
sn8143 = []
sn8143 = np.where((star <= 2) & (snr814 == 3.0) &
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 50))  
print "Mean f814w Abs Mag at S/N = 3 : ", np.mean(f814Abs[sn8143])
print "Applying contrains to SN Data..."

#print "Mean Sharp Value " + title[:-1] + " : " + str(np.mean(sharp))
#print "Mean Round Value " + title[:-1] + " : " + str(np.mean(roond))

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
                    (((xsn - xcoord[cut435555[0]])**2 + (ysn - ycoord[cut435555[0]])**2)**.5),
                    ))
pickle.dump( snr435_555[0], open(folder + '/' + title + '8ge_f435f555.p', "wb" ) )
pickle.dump( snr625_814[0], open(folder + '/' + title + '8ge_f625f814.p', "wb" ) )
 
"""
for n in range(len(cut435555)):
    print n
    snr435_555.append(( f435Abs[cut435555[n]],f555Abs[cut435555[n]], 
                       unc555[cut435555[n]],
                        ((unc435[cut435555[n]]**2 + unc555[cut435555[n]]**2)**.5 ),
                        snr435[cut435555[n]], snr555[cut435555[n]],
                        xcoord[cut435555[n]], ycoord[cut435555[n]],
                        f435mag[cut435555[n]],f555mag[cut435555[n]] ))
    snr625_814.append(( f625Abs[cut625814[n]],f814Abs[cut625814[n]],
                       unc814[cut625814[n]],
                        ((unc625[cut625814[n]]**2 + unc814[cut625814[n]]**2)**.5 ),
                        snr625[cut625814[n]], snr814[cut625814[n]],
                        xcoord[cut625814[n]], ycoord[cut625814[n]], 
                        f625mag[cut625814[n]],f814mag[cut625814[n]] ))
    pickle.dump( snr435_555[n], open(folder + '/' + title + '8ge_f435f555_sn' + str(snr[n]) + '_rad' + str(rad[n]) + '.p', "wb" ) )
    pickle.dump( snr625_814[n], open(folder + '/' + title + '8ge_f625f814_sn' + str(snr[n]) + '_rad' + str(rad[n]) + '.p', "wb" ) )
    #pickle.dump( snr435_555[n], open(folder + '/' + title + '8ge_f435f555_sn' + str(3) + '_rad' + str(0) + '.p', "wb" ) )
    #pickle.dump( snr625_814[n], open(folder + '/' + title + '8ge_f625f814_sn' + str(3) + '_rad' + str(0) + '.p', "wb" ) )
"""
print "Pickled."
################################################### 
############ Save coordinates to a file ###########
################################################### 

print "Save into text file"
yax1 = []
yax2 = []
dataOut_1 = np.array(np.c_[star[cut435555[0]]  ,
    xcoord[cut435555[0]]+.5 ,ycoord[cut435555[0]]+.5 ,
    (((xsn - xcoord[cut435555[0]])**2 + (ysn - ycoord[cut435555[0]])**2)**.5),
    (f435Abs[cut435555[0]] - f555Abs[cut435555[0]]),
    snr435[cut435555[0]] ,snr555[cut435555[0]] ,
    snr625[cut435555[0]] ,snr814[cut435555[0]] ,
    f435Abs[cut435555[0]],f555Abs[cut435555[0]],
    f625Abs[cut435555[0]],f814Abs[cut435555[0]],
    sharp[cut435555[0]],#data[:,22][cut435555[0]],data[:,33][cut435555[0]],
    roond[cut435555[0]],#data[:,20][cut435555[0]],data[:,34][cut435555[0]],
    crowd[cut435555[0]]])#,data[:,21][cut435555[0]],data[:,35][cut435555[0]] 
np.savetxt(folder +'/'+ title + 'cut435555.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
    header ='Object Xpix        Ypix        DisfromSN   Sub    S/N 435   S/N 555   S/N 625   S/N 814 ' \
    #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
    '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
    'Sharp Round Crowd')
    
dataOut_2 = np.array(np.c_[star[cut625814[0]] ,
    xcoord[cut625814[0]]+.5 ,ycoord[cut625814[0]]+.5,
    (((xsn - xcoord[cut625814[0]])**2 + (ysn - ycoord[cut625814[0]])**2)**.5),
    (f625Abs[cut625814[0]] - f814Abs[cut625814[0]]),
    snr435[cut625814[0]] ,snr555[cut625814[0]] ,
    snr625[cut625814[0]] ,snr814[cut625814[0]] ,
    f435Abs[cut625814[0]],f555Abs[cut625814[0]],
    f625Abs[cut625814[0]],f814Abs[cut625814[0]],
    sharp[cut625814[0]],#data[:,46][cut625814[0]],data[:,59][cut625814[0]],
    roond[cut625814[0]],#data[:,47][cut625814[0]],data[:,60][cut625814[0]],
    crowd[cut625814[0]]])#,data[:,48][cut625814[4]],data[:,61][cut625814[4]]    
np.savetxt(folder +'/'+ title + 'cut625814.txt', dataOut_2 ,delimiter='   ', fmt = "%1.4f",
    header ='Object Xpix        Ypix        DisFromSN   Sub    S/N 435  S/N 555  S/N 625  S/N 814 ' \
    #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
    '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '\
    'Sharp Round Crowd')

"""
print "Save into text file"
yax1 = []
yax2 = []
#print "top"
#print f435Abs[cut435555[4]] - f555Abs[cut435555[4]]
#print "bottom"
#print f625Abs[cut625814[4]] - f814Abs[cut625814[4]]
dataOut_1 = np.array(np.c_[star[cut435555[4]]  ,
    xcoord[cut435555[4]] ,ycoord[cut435555[4]] ,
    (((xsn - xcoord[cut435555[4]])**2 + (ysn - ycoord[cut435555[4]])**2)**.5),
    (f435Abs[cut435555[4]] - f555Abs[cut435555[4]]),
    snr435[cut435555[4]] ,snr555[cut435555[4]] ,
    snr625[cut435555[4]] ,snr814[cut435555[4]] ,
    #f435mag[cut435555[4]],f555mag[cut435555[4]],
    #f625mag[cut435555[4]],f814mag[cut435555[4]],
    f435Abs[cut435555[4]],f555Abs[cut435555[4]],
    f625Abs[cut435555[4]],f814Abs[cut435555[4]],
    sharp[cut435555[4]],#data[:,22][cut435555[4]],data[:,33][cut435555[4]],
    roond[cut435555[4]],#data[:,20][cut435555[4]],data[:,34][cut435555[4]],
    crowd[cut435555[4]]])#,data[:,21][cut435555[4]],data[:,35][cut435555[4]] 
np.savetxt(folder +'/'+ title + 'cut435555.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
    header ='Object Xpix        Ypix        DisfromSN   Sub    S/N 435   S/N 555   S/N 625   S/N 814 ' \
    #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
    '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '    \
    'Sharp Round Crowd')
    
dataOut_2 = np.array(np.c_[star[cut625814[4]] ,
    xcoord[cut625814[4]] ,ycoord[cut625814[4]],
    (((xsn - xcoord[cut625814[4]])**2 + (ysn - ycoord[cut625814[4]])**2)**.5),
    (f625Abs[cut625814[4]] - f814Abs[cut625814[4]]),
    snr435[cut625814[4]] ,snr555[cut625814[4]] ,
    snr625[cut625814[4]] ,snr814[cut625814[4]] ,
    #f435mag[cut625814[4]],f555mag[cut625814[4]],
    #f625mag[cut625814[4]],f814mag[cut625814[4]],
    f435Abs[cut625814[4]],f555Abs[cut625814[4]],
    f625Abs[cut625814[4]],f814Abs[cut625814[4]],
    sharp[cut625814[4]],#data[:,46][cut625814[4]],data[:,59][cut625814[4]],
    roond[cut625814[4]],#data[:,47][cut625814[4]],data[:,60][cut625814[4]],
    crowd[cut625814[4]]])#,data[:,48][cut625814[4]],data[:,61][cut625814[4]]    
np.savetxt(folder +'/'+ title + 'cut625814.txt', dataOut_2 ,delimiter='   ', fmt = "%1.4f",
    header ='Object Xpix        Ypix        DisFromSN   Sub    S/N 435  S/N 555  S/N 625  S/N 814 ' \
    #'Mag 435 Mag 555 Mag 625 Mag 814 ' \
    '  AbsMag 435 AbsMag 555 AbsMag 625 AbsMag 814 '      \
    'Sharp Round Crowd')
"""
