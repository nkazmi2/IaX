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

special = 'sn08ge'

"""
##################### 2008ha ######################
"""
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
special = 'sn08ha'
xclust  = 1716.352
yclust  = 3163.780

#bad  = []
#badX = []
#badY = []
#bad  = np.array(np.loadtxt(name[:-8]+'questionable.txt'))
##bad = np.recfromcsv(filename, names=['a','a','a'])
#badX = (bad[:,0] - .5)
#badY = (bad[:,1] - .5)
"""
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

special = 'sn10ae'
"""
##################### 2010el ######################
#"""    
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

special = 'sn10el'
#"""
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

chi435  = data[:,18] # Chi for fit
chi555  = data[:,31] 
chi625  = data[:,44] 
chi814  = data[:,57]

xcoord  = data[:, 2]
ycoord  = data[:, 3]

################################################### 
########### Calculate Absolute Magnitude ##########

print "Calculating Absolute Magnitude..."
 
f435Abs = f435mag - dmod - ACS435
f555Abs = f555mag - dmod - ACS555
f625Abs = f625mag - dmod - ACS625
f814Abs = f814mag - dmod - ACS814 

################################################### 
########### Deal with bad points ##########

bad  = []
badX = []
badY = []
bad  = np.array(np.loadtxt(name[:-8]+'questionable.txt'))
#bad = np.recfromcsv(filename, names=['a','a','a'])
badX = (bad[:,0] - .5)
badY = (bad[:,1] - .5)

################################################### 
##### Find correct color magnitudes make cuts #####
# So many for loops @.@ 
# somehow need to get around this :/

print "Applying contrains to SN Data..."
for m in range(4,9):
    for i in range(len(radius)):
        #for w in range(len(badX)):
        if (special == 'sn08ha'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)         &
                    (snr435 >= 3) & (snr555 >= 3) 
                    & ((xcoord != badX[0]) & (ycoord != badY[0]))
                    & ((xcoord != badX[1]) & (ycoord != badY[1]))
                    & ((xcoord != badX[2]) & (ycoord != badY[2]))
                    & ((xcoord != badX[3]) & (ycoord != badY[3]))
                    & ((xcoord != badX[4]) & (ycoord != badY[4]))
                    & ((xcoord != badX[5]) & (ycoord != badY[5]))
                    & ((xcoord != badX[6]) & (ycoord != badY[6]))
                    ))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    ((((xcoord - xclust)**2 + (ycoord - yclust)**2)**.5) >= 4.8)         &
                    (snr625 >= 3) & (snr814 >= 3)    
                    & ((xcoord != badX[0]) & (ycoord != badY[0]))
                    & ((xcoord != badX[1]) & (ycoord != badY[1]))
                    & ((xcoord != badX[2]) & (ycoord != badY[2]))
                    & ((xcoord != badX[3]) & (ycoord != badY[3]))
                    & ((xcoord != badX[4]) & (ycoord != badY[4]))
                    & ((xcoord != badX[5]) & (ycoord != badY[5]))
                    & ((xcoord != badX[6]) & (ycoord != badY[6]))
                    ))
        elif (special == 'sn08ge'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    (snr435 >= 3) & (snr555 >= 3) 
                    ))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    (snr625 >= 3) & (snr814 >= 3)  
                    ))
        elif (special == 'sn10ae'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    (snr435 >= 3) & (snr555 >= 3) 
                    & ((xcoord != badX[0]) & (ycoord != badY[0]))
                    & ((xcoord != badX[1]) & (ycoord != badY[1]))
                    & ((xcoord != badX[2]) & (ycoord != badY[2]))
                    & ((xcoord != badX[3]) & (ycoord != badY[3]))
                    & ((xcoord != badX[4]) & (ycoord != badY[4]))
                    & ((xcoord != badX[5]) & (ycoord != badY[5]))
                    & ((xcoord != badX[6]) & (ycoord != badY[6]))
                    & ((xcoord != badX[7]) & (ycoord != badY[7]))
                    & ((xcoord != badX[8]) & (ycoord != badY[8]))
                    & ((xcoord != badX[9]) & (ycoord != badY[9]))
                    & ((xcoord != badX[10]) & (ycoord != badY[10]))
                    & ((xcoord != badX[11]) & (ycoord != badY[11]))
                    & ((xcoord != badX[12]) & (ycoord != badY[12]))
                    & ((xcoord != badX[14]) & (ycoord != badY[13]))                    
                    & ((xcoord != badX[15]) & (ycoord != badY[14]))
                    & ((xcoord != badX[16]) & (ycoord != badY[15]))
                    & ((xcoord != badX[17]) & (ycoord != badY[16]))
                    & ((xcoord != badX[18]) & (ycoord != badY[18]))
                    & ((xcoord != badX[19]) & (ycoord != badY[19]))
                    & ((xcoord != badX[20]) & (ycoord != badY[20]))
                    & ((xcoord != badX[21]) & (ycoord != badY[21]))
                    ))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    (snr625 >= 3) & (snr814 >= 3)  
                    & ((xcoord != badX[0]) & (ycoord != badY[0]))
                    & ((xcoord != badX[1]) & (ycoord != badY[1]))
                    & ((xcoord != badX[2]) & (ycoord != badY[2]))
                    & ((xcoord != badX[3]) & (ycoord != badY[3]))
                    & ((xcoord != badX[4]) & (ycoord != badY[4]))
                    & ((xcoord != badX[5]) & (ycoord != badY[5]))
                    & ((xcoord != badX[6]) & (ycoord != badY[6]))
                    & ((xcoord != badX[7]) & (ycoord != badY[7]))
                    & ((xcoord != badX[8]) & (ycoord != badY[8]))
                    & ((xcoord != badX[9]) & (ycoord != badY[9]))
                    & ((xcoord != badX[10]) & (ycoord != badY[10]))
                    & ((xcoord != badX[11]) & (ycoord != badY[11]))
                    & ((xcoord != badX[12]) & (ycoord != badY[12]))
                    & ((xcoord != badX[14]) & (ycoord != badY[13]))                    
                    & ((xcoord != badX[15]) & (ycoord != badY[14]))
                    & ((xcoord != badX[16]) & (ycoord != badY[15]))
                    & ((xcoord != badX[17]) & (ycoord != badY[16]))
                    & ((xcoord != badX[18]) & (ycoord != badY[18]))
                    & ((xcoord != badX[19]) & (ycoord != badY[19]))
                    & ((xcoord != badX[20]) & (ycoord != badY[20]))
                    & ((xcoord != badX[21]) & (ycoord != badY[21]))
                    ))
        elif (special == 'sn10el'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    (snr435 >= 3) & (snr555 >= 3) 
                    & ((xcoord != badX[0]) & (ycoord != badY[0]))
                    & ((xcoord != badX[1]) & (ycoord != badY[1]))
                    & ((xcoord != badX[2]) & (ycoord != badY[2]))
                    & ((xcoord != badX[3]) & (ycoord != badY[3]))
                    & ((xcoord != badX[4]) & (ycoord != badY[4]))
                    & ((xcoord != badX[5]) & (ycoord != badY[5]))
                    & ((xcoord != badX[6]) & (ycoord != badY[6]))
                    & ((xcoord != badX[7]) & (ycoord != badY[7]))
                    & ((xcoord != badX[8]) & (ycoord != badY[8]))
                    & ((xcoord != badX[9]) & (ycoord != badY[9]))
                    & ((xcoord != badX[10]) & (ycoord != badY[10]))
                    & ((xcoord != badX[11]) & (ycoord != badY[11]))
                    & ((xcoord != badX[12]) & (ycoord != badY[12]))
                    & ((xcoord != badX[13]) & (ycoord != badY[13]))                    
                    & ((xcoord != badX[14]) & (ycoord != badY[14]))
                    & ((xcoord != badX[15]) & (ycoord != badY[15]))
                    & ((xcoord != badX[16]) & (ycoord != badY[16]))
                    & ((xcoord != badX[17]) & (ycoord != badY[17]))
                    & ((xcoord != badX[18]) & (ycoord != badY[18]))
                    & ((xcoord != badX[19]) & (ycoord != badY[19]))
                    & ((xcoord != badX[20]) & (ycoord != badY[20]))
                    & ((xcoord != badX[21]) & (ycoord != badY[21]))
                    & ((xcoord != badX[22]) & (ycoord != badY[22]))                    
                    & ((xcoord != badX[23]) & (ycoord != badY[23]))
                    & ((xcoord != badX[24]) & (ycoord != badY[24]))
                    & ((xcoord != badX[25]) & (ycoord != badY[25]))
                    & ((xcoord != badX[26]) & (ycoord != badY[26]))
                    & ((xcoord != badX[27]) & (ycoord != badY[27]))
                    & ((xcoord != badX[28]) & (ycoord != badY[28]))
                    & ((xcoord != badX[29]) & (ycoord != badY[29]))
                    & ((xcoord != badX[30]) & (ycoord != badY[30]))
                    & ((xcoord != badX[31]) & (ycoord != badY[31]))                    
                    & ((xcoord != badX[32]) & (ycoord != badY[32]))
                    & ((xcoord != badX[33]) & (ycoord != badY[33]))
                    & ((xcoord != badX[34]) & (ycoord != badY[34]))
                    & ((xcoord != badX[35]) & (ycoord != badY[35]))                    
                    & ((xcoord != badX[36]) & (ycoord != badY[36]))
                    ))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])          & 
                    (snr625 >= 3) & (snr814 >= 3) 
                    & ((xcoord != badX[0]) & (ycoord != badY[0]))
                    & ((xcoord != badX[1]) & (ycoord != badY[1]))
                    & ((xcoord != badX[2]) & (ycoord != badY[2]))
                    & ((xcoord != badX[3]) & (ycoord != badY[3]))
                    & ((xcoord != badX[4]) & (ycoord != badY[4]))
                    & ((xcoord != badX[5]) & (ycoord != badY[5]))
                    & ((xcoord != badX[6]) & (ycoord != badY[6]))
                    & ((xcoord != badX[7]) & (ycoord != badY[7]))
                    & ((xcoord != badX[8]) & (ycoord != badY[8]))
                    & ((xcoord != badX[9]) & (ycoord != badY[9]))
                    & ((xcoord != badX[10]) & (ycoord != badY[10]))
                    & ((xcoord != badX[11]) & (ycoord != badY[11]))
                    & ((xcoord != badX[12]) & (ycoord != badY[12]))
                    & ((xcoord != badX[13]) & (ycoord != badY[13]))                    
                    & ((xcoord != badX[14]) & (ycoord != badY[14]))
                    & ((xcoord != badX[15]) & (ycoord != badY[15]))
                    & ((xcoord != badX[16]) & (ycoord != badY[16]))
                    & ((xcoord != badX[17]) & (ycoord != badY[17]))
                    & ((xcoord != badX[18]) & (ycoord != badY[18]))
                    & ((xcoord != badX[19]) & (ycoord != badY[19]))
                    & ((xcoord != badX[20]) & (ycoord != badY[20]))
                    & ((xcoord != badX[21]) & (ycoord != badY[21]))
                    & ((xcoord != badX[22]) & (ycoord != badY[22]))                    
                    & ((xcoord != badX[23]) & (ycoord != badY[23]))
                    & ((xcoord != badX[24]) & (ycoord != badY[24]))
                    & ((xcoord != badX[25]) & (ycoord != badY[25]))
                    & ((xcoord != badX[26]) & (ycoord != badY[26]))
                    & ((xcoord != badX[27]) & (ycoord != badY[27]))
                    & ((xcoord != badX[28]) & (ycoord != badY[28]))
                    & ((xcoord != badX[29]) & (ycoord != badY[29]))
                    & ((xcoord != badX[30]) & (ycoord != badY[30]))
                    & ((xcoord != badX[31]) & (ycoord != badY[31]))                    
                    & ((xcoord != badX[32]) & (ycoord != badY[32]))
                    & ((xcoord != badX[33]) & (ycoord != badY[33]))
                    & ((xcoord != badX[34]) & (ycoord != badY[34]))
                    & ((xcoord != badX[35]) & (ycoord != badY[35]))                    
                    & ((xcoord != badX[36]) & (ycoord != badY[36]))
                    ))
################################################### 
############ Save good arrays to a file ###########
print "Pickling!"

o = 3
q = 3   

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
        #print title+'f625f814_r1_' + str(abs(p-(q))) + '.p'
        pickle.dump( snr625_814[p], open( title+'f625f814_r1_' + str(abs(p-(q))) + '.p', "wb" ) )
        #pickle.dump( snr625_814[p], open( title+'f625f814_' + str(radius[0]) +'_' + str(abs(p-(q))) + '.p', "wb" ) )
    elif (p % 2 != 0):
        q += 1
        #print title+'f625f814_r2_' + str(abs((p)-(q)+1)) + '.p'
        pickle.dump( snr625_814[p], open( title+'f625f814_r2_' + str(abs((p)-(q)+1)) + '.p', "wb" ) )    
        #pickle.dump( snr625_814[p], open( title+'f625f814_' + str(radius[1]) +'_' + str(abs((p)-(q)+1)) + '.p', "wb" ) )
    
print "Pickled."


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