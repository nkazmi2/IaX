# -*- coding: utf-8 -*-
"""
Created on Tue May 27 10:30:07 2014

@author: Nova
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv
from itertools import izip
import pickle

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

snr435_555_3 = []
snr625_814_3 = []
snr435_555_4 = []
snr625_814_4 = []
snr435_555_5 = []
snr625_814_5 = []

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
o = 3
q = 3   

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
"""
name     = 'sn2008ge_new.phot' 

# Magnitude of the Milkyway Galaxy 
ACS435   = 0.046 #F435W
ACS555   = 0.036 #F555W	
ACS625   = 0.028 #F625W	
ACS814   = 0.020 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod    = 31.27 

# Actual X & Y pixel coordinates of sn
xsn     = 3247.539
ysn     = 3419.971
#radius  = 50.0 #pixels
radius  = [36.1008,46.0927]
#radius = 36.1008 # theta = .0005014 deg, phys radius =  1566.443 au, distance = 17.95e7 pc
#metalicity (?)
#isocrones on a website - metalicty and age(?) , pick filters (ACS)
"""
##################### 2008ha ######################
#"""
name     = 'sn2008ha_new.phot'

# Magnitude of the Milkyway Galaxy 
ACS435   = 0.284 #F435W
ACS555   = 0.219 #F555W	
ACS625   = 0.174 #F625W	
ACS814   = 0.120 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod    = 31.64 #31.50 

# Actual X & Y pixel coordinates of sn
xsn     = 1726.352
ysn     = 3172.530

#radius  = 32.4   theta = .00045 deg, phys radius = 1570.796 au, distance = 20e7 pc
#radius = 41.25  theta = .0057  deg, phys radius = 2000 au    , distance = 20e7 pc
radius = [32.4, 41.2531]
special = 'cluster'
xclust  = 1716.352
yclust  = 3163.780

bad  = []
badX = []
badY = []
bad  = np.array(np.loadtxt(name[:-8]+'questionable.txt'))
#bad = np.recfromcsv(filename, names=['a','a','a'])
badX = (bad[:,0] - .5)
badY = (bad[:,1] - .5)
#"""
##################### 2010ae ######################
"""
name     = 'sn2010ae_new.phot'

# Magnitude of the Milkyway Galaxy m is low(?) .1sol
ACS435   = 0.509 #F435W
ACS555   = 0.394 #F555W	
ACS625   = 0.313 #F625W	
ACS814   = 0.215 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod    = 30.58 

# Actual X & Y pixel coordinates of sn
xsn     = 1796.640
ysn     = 1931.995
#radius  = 30.0 #pixels
radius = [49.4712,62.9816] # theta = .0006871 deg, phys radius = 1570.972 au, distance = 13.1e7 pc
"""
##################### 2010el ######################
"""    
name     = 'sn2010el_new.phot'
    
# Magnitude of the Milkyway Galaxy 
ACS435   = 0.033 #F435W
ACS555   = 0.025 #F555W	
ACS625   = 0.020 #F625W	
ACS814   = 0.014 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod    = 29.99 

# Actual X & Y pixel coordinates of sn
xsn     = 2418.859
ysn     = 1570.826
#radius  = 50.0 #pixels
radius = [65.0016,82.7545] # theta = .0009028 deg, phys radius = 1570.95 au distance = 9.97e7 pc
"""
###################################################    
######### Open and read in the data file ##########

print "Opening file: ", name

photfile = open(name,'r')

title = name[:-8]

################################################### 
######## append data from file to an array ########

print "Extracting ", name, " information..."

for line in photfile:
    columns = line.split()
    data.append(columns) # slowest step thus far

print "Organizing ", name, " information..."

data    = np.array(data)
data    = data.astype(float)

star    = data[:,10] # type
SNR     = data[:, 5] # general signal to noise
CHI     = data[:, 4] # general chi for fit 
"""
f435mag = data[:,15] # instramental VEGAMAG magnitude
f555mag = data[:,28]
f625mag = data[:,41]
f814mag = data[:,55]

unc435  = data[:,17] # uncertainty 
unc555  = data[:,30]
unc625  = data[:,43]
unc814  = data[:,56]
"""
snr435  = data[:,19] # signal to noise
snr555  = data[:,32]
snr625  = data[:,45]
snr814  = data[:,58]
"""
chi435  = data[:,18] # Chi for fit
chi555  = data[:,31] 
chi625  = data[:,44] 
chi814  = data[:,57]
"""
xcoord  = data[:, 2]
ycoord  = data[:, 3]

################################################### 
########### Calculate Absolute Magnitude ##########
"""
print "Calculating Absolute Magnitude..."
 
f435Abs = f435mag - dmod - ACS435
f555Abs = f555mag - dmod - ACS555
f625Abs = f625mag - dmod - ACS625
f814Abs = f814mag - dmod - ACS814 
"""
################################################### 
##### Find correct color magnitudes make cuts #####

"""
16039   X
18300   X
21901   X
22885   X
23143   X
44710   X
50120   X
61659
105833
Testing bad Y values
222
16039   X
18300   X
21239
21901   X
22885   X
23143   X
27300
43644
44710   X
50120   X
60012
71374
142123
"""
badpos = []
cut    = []
cutorig= []
cutrem = []
for i in range(len(xcoord)):
    for j in range(len(badX)):
        if (xcoord[i] == badX[j]) & (ycoord[i] == badY[j]):
            badpos.append(i)     

#print xcoord[badpos]
for i in range(len(badpos)):
    cutorig  = np.where((star <= 2) & ((snr625 >= 4) | (snr814 >= 4))      & 
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[0])    & 
        ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)   &
        (snr625 >= 3) & (snr814 >= 3) )
for i in range(len(badpos)):
    cut  = np.where((star <= 2) & ((snr625 >= 4) | (snr814 >= 4))      & 
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[0])    & 
        ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)   &
        (snr625 >= 3) & (snr814 >= 3) & ((xcoord == badX[i]) & (ycoord == badY[i])))

for i in range(len(badpos)):
    cutrem  = np.where((star <= 2) & ((snr625 >= 4) | (snr814 >= 4))      & 
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[0])    & 
        ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)   &
        (snr625 >= 3) & (snr814 >= 3) & ((xcoord != badX[i]) & (ycoord != badY[i])))
#print xcoord[cut & badpos]

"""
def all(iterable):
    print "Testing all"
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    print "Testing any"
    for element in iterable:
        if element:
            return True
    return False
    
all(badpos)
any(badpos)
"""
#badpos = np.where((xcoord == badX) & (ycoord == badY))
#badpos = np.array(badpos,dtype=np.int64)
print xcoord[badpos]
print xcoord[cutorig]
print xcoord[cutrem]
print xcoord[cut]
"""
1732.34  1732.34  
1699.28  
1749.32  1749.32
1751.97  1751.97
1687.82  
1703.94  1703.94
1717.56  1717.56
1745.46
1753.85  1753.85
1724.89  1724.89  
1703.65  
1754.54  1754.54
1763.66  
1751.75  1751.75
1729.74  1729.74
1689.06 
        
        
1734.14  
1746.72  
1739.32  
1735.71  
1730.86  
1732.02  
1742.74
"""

#cut4  = np.where((star <= 2) & ((snr435 >= 4) | (snr555 >= 4))       & 
#              ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)     & 
#              ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8) &
#             (snr435 >= 3) & (snr555 >= 3))
#print np.shape(xcoord[cut])

#cut.append(badpos)

#print xcoord[cut]

"""
print "Applying contrains to SN Data..."
for m in range(4,9):
    for i in range(len(radius)):
        if (special == 'cluster'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)         &
                (snr435 >= 3) & (snr555 >= 3)                                    ))# &
                #((xcoord != badX) | (ycoord != badY))) 
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)         &
                (snr625 >= 3) & (snr814 >= 3)                                    ))# &
                #((xcoord != badX) | (ycoord != badY))) 
        else:
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])         & 
                (snr435 >= 3) & (snr555 >= 3)                                   ))# &
                #((xcoord != badX) | (ycoord != badY)))     
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])         & 
                (snr625 >= 3) & (snr814 >= 3)                                   ))# &
                #((xcoord != badX) | (ycoord != badY))) 
"""
################################################### 
############ Save good arrays to a file ###########
"""
print "Pickling!"

for n in range(len(cut435555)):
    o += 1
    snr435_555.append(( f435Abs[cut435555[n]],f555Abs[cut435555[n]], 
                       unc555[cut435555[n]],
                        (unc435[cut435555[n]]**2 + unc555[cut435555[n]]**2)**.5 ))
    if (n % 2 == 0) : 
        #pickle.dump( snr435_555[n], open( title+'f435f555_'+ str(radius[0]) +'_' + str(abs(n-(o))) + '.p', "wb" ) )
        pickle.dump( snr435_555[n], open( title+'f435f555_r1_' + str(abs(n-(o))) + '.p', "wb" ) )
    elif (n % 2 != 0):
        o += 1
        pickle.dump( snr435_555[n], open( title+'f435f555_r2_' + str(abs((n)-(o)+1)) + '.p', "wb" ) )
        #pickle.dump( snr435_555[n], open( title+'f435f555_'+ str(radius[1]) +'_' + str(abs((n)-(o)+1)) + '.p', "wb" ) )

for p in range(len(cut625814)):  
    q += 1
    snr625_814.append(( f625Abs[cut625814[p]],f814Abs[cut625814[p]], 
                       unc625[cut625814[p]],
                        (unc625[cut625814[p]]**2 + unc814[cut625814[p]]**2)**.5 ))
    if (p % 2 == 0) :  
        pickle.dump( snr625_814[p], open( title+'f625f814_r1_' + str(abs(p-(q))) + '.p', "wb" ) )
        #pickle.dump( snr625_814[p], open( title+'f625f814_' + str(radius[0]) +'_' + str(abs(p-(q))) + '.p', "wb" ) )
    elif (p % 2 != 0):
        q += 1
        pickle.dump( snr625_814[p], open( title+'f625f814_r2_' + str(abs((p)-(q)+1)) + '.p', "wb" ) )    
        #pickle.dump( snr625_814[p], open( title+'f625f814_' + str(radius[1]) +'_' + str(abs((p)-(q)+1)) + '.p', "wb" ) )
    
print "Pickled."
"""
"""
print "Open file to save coordinate data..."

with open(title+'F435W_F555W_snr3.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(xcoord[cut2]+.5,ycoord[cut2]+.5))

with open(title+'F625W_F814W_snr3.csv', 'wb') as g:
    writer = csv.writer(g)  
    writer.writerows(izip(xcoord[cut3]+.5,ycoord[cut3]+.5))

with open(title+'F435W_F555W_snr4.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(xcoord[cut4]+.5,ycoord[cut4]+.5))

with open(title+'F625W_F814W_snr4.csv', 'wb') as g:
    writer = csv.writer(g)  
    writer.writerows(izip(xcoord[cut5]+.5,ycoord[cut5]+.5))
    
with open(title+'F435W_F555W_snr5.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(xcoord[cut6]+.5,ycoord[cut6]+.5))

with open(title+'F625W_F814W_snr5.csv', 'wb') as g:
    writer = csv.writer(g)  
    writer.writerows(izip(xcoord[cut7]+.5,ycoord[cut7]+.5))


print "Saving file " + title + "F435W_F555W_*.csv & " + title + "F625W_F814W_*.csv"
"""