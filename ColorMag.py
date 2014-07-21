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
"""
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
"""
################################################### 
######### Things that change for each sn ##########
##################### 2008ge ######################
#"""
folder   = "SN2008GE"
name     = 'sn2008ge_new.phot' 

# Magnitude of the Milkyway Galaxy 
ACS435   = 0.046 #F435W
ACS555   = 0.036 #F555W	
ACS625   = 0.028 #F625W	
ACS814   = 0.020 #F814W	
MW       = 0.011
Host     = 0.0

# Median (redshift independent) distance modulus of host galaxy
dmod     = 31.27 

# Actual X & Y pixel coordinates of sn
xsn      = 3247.539
ysn      = 3419.971
#radius   = 50.0 #pixels
#radius   = [36.1008,46.0927]
#radius   = 36.1008 # theta = .0005014 deg, phys radius =  1566.443 au, distance = 17.95e7 pc
radius   = [100]
special  = 'sn08ge'

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
# Median (redshift independent) distance modulus of host galaxy
dmod     = 31.64 #31.50 # value I got from NED

# Actual X & Y pixel coordinates of sn
xsn      = 1726.352
ysn      = 3172.530

#radius  = 32.4   theta = .00045 deg, phys radius = 1570.796 au, distance = 20e7 pc
#radius  = 41.25  theta = .0057  deg, phys radius = 2000 au    , distance = 20e7 pc
#radius   = [32.4, 41.2531]
radius   = [100]
special  = 'sn08ha'
xclust   = 1716.352
yclust   = 3163.780

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

# Median (redshift independent) distance modulus of host galaxy
dmod     = 30.58 

# Actual X & Y pixel coordinates of sn
xsn      = 1796.640
ysn      = 1931.995
#radius  = 30.0 #pixels
#radius   = [49.4712,62.9816] # theta = .0006871 deg, phys radius = 1570.972 au, distance = 13.1e7 pc
radius   = [100]
special  = 'sn10ae'
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

# Median (redshift independent) distance modulus of host galaxy
dmod     = 29.99 

# Actual X & Y pixel coordinates of sn
xsn      = 2418.859
ysn      = 1570.826
#radius  = 50.0 #pixels
#radius   = [65.0016,82.7545] # theta = .0009028 deg, phys radius = 1570.95 au distance = 9.97e7 pc
radius   = [100]
special  = 'sn10el'
"""
###################################################    
######### Open and read in the data file ##########

print "Opening file: ",name

print "Extracting ", name, " information..."
data = np.loadtxt(folder + '/' + name)

title = name[:-8]
################################################### 
######## append data from file to an array ########

"""
for line in photfile:
    columns = line.split()
    data.append(columns) # slowest step thus far
"""
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
"""
print "Calculating Absolute Magnitude..."
 
f435Abs = f435mag - dmod - ACS435 - MW - Host
f555Abs = f555mag - dmod - ACS555 - MW - Host
f625Abs = f625mag - dmod - ACS625 - MW - Host
f814Abs = f814mag - dmod - ACS814 - MW - Host
"""
################################################### 
########### Deal with bad points ##########
"""
bad  = []
badX = []
badY = []
#bad  = np.array(np.loadtxt(folder +'/'+ name[:-8]+'questionable.txt'))
#bad  = np.array(np.loadtxt(name[:-8]+'questionable.reg')) -.5
bad  = np.array(np.loadtxt(folder +'/'+ name[:-8]+'questionable.reg')) -.5

badX = bad[:][0]
badY = bad[:][1]
"""
################################################### 
##### Find correct color magnitudes make cuts #####
# So many for loops @.@ 
# somehow need to get around this :/

print "Applying contrains to SN Data..."
"""
for m in range(3,6):
    print m
    for i in range(len(radius)):
        print i
        #for w in range(len(badX)):
        if (special == 'sn08ha'):
            cut435555.append(np.where((star <= 2) &# ((snr435 >= m) | (snr555 >= m)) & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])     &
                    (snr435 >= 3) & (snr555 >= 3)))# & 
                    #list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
            cut625814.append(np.where((star <= 2) & #((snr625 >= m) | (snr814 >= m)) & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])     &
                    (snr625 >= 3) & (snr814 >= 3)))# & 
                    #list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
        elif (special == 'sn08ge'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])      & 
                    (snr435 >= 3) & (snr555 >= 3) & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])      & 
                    (snr625 >= 3) & (snr814 >= 3)  & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
        elif (special == 'sn10ae'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])      & 
                    (snr435 >= 3) & (snr555 >= 3)& 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])      & 
                    (snr625 >= 3) & (snr814 >= 3) & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
        elif (special == 'sn10el'):
            cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])      & 
                    (snr435 >= 3) & (snr555 >= 3) & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
            cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m))  & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])      & 
                    (snr625 >= 3) & (snr814 >= 3) & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))

"""
cut = []
cut.append(np.where((star <= 2) & (((snr435 >= 3) | (snr555 >= 3)) 
                | ((snr625 >= 3) | (snr814 >= 3)))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[0])))
                
first = np.c_[xcoord[cut[0]]+.5 ,ycoord[cut[0]]+.5]
np.savetxt(folder +'/'+ title + 'all.txt', first,fmt = "%1.2f")
############ Save coordinates to a file ###########
"""
first = np.c_[xcoord[cut435555[0]]+.5 ,ycoord[cut435555[0]]+.5] #combine to one array
second= np.c_[xcoord[cut625814[0]]+.5 ,ycoord[cut625814[0]]+.5]
# More flaws in this, removes too many of the good points :/
final = np.r_[first,second].tolist()

toRemove = []
for i, val in enumerate(final):
    if val in final[i+1:]:#if value is in the rest of the array after this point.
        toRemove.append(final[i+1:].index(val)) #add it to the index to remove
     
toRemove.sort(reverse = True)#sort in reverse order to that we don't fuck up indices
for idx in toRemove:
    final.pop(idx)#pop it out
# it removes the last value in first, and adds the second to last 
# value from first, to final. It's doubled, something wrong with 
# removing values.
    
final = np.vstack((final,first[-1]))#fucked up indices, need to add the last item in the "first" list
final = np.array(final)

np.savetxt(folder +'/'+ title + 'all.txt', final,fmt = "%1.2f")
np.savetxt(folder +'/'+ title + '435555.txt', first,fmt = "%1.2f")
np.savetxt(folder +'/'+ title + '625814.txt', second,fmt = "%1.2f")
"""

################################################### 
############ Save good arrays to a file ###########
"""
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
        pickle.dump( snr435_555[n], open(folder +'/'+ title+'f435f555_r1_' + str(abs(n-(o))) + '.p', "wb" ) )
    elif (n % 2 != 0):
        o += 1
        pickle.dump( snr435_555[n], open(folder+'/'+ title+'f435f555_r2_' + str(abs((n)-(o)+1)) + '.p', "wb" ) )
        #pickle.dump( snr435_555[n], open( title+'f435f555_'+ str(radius[1]) +'_' + str(abs((n)-(o)+1)) + '.p', "wb" ) )

for p in range(len(cut625814)):  
    q += 1
    snr625_814.append(( f625Abs[cut625814[p]],f814Abs[cut625814[p]], 
                       unc625[cut625814[p]],
                        (unc625[cut625814[p]]**2 + unc814[cut625814[p]]**2)**.5 ))
    if (p % 2 == 0) :  
        #print title+'f625f814_r1_' + str(abs(p-(q))) + '.p'
        pickle.dump( snr625_814[p], open(folder +'/'+ title+'f625f814_r1_' + str(abs(p-(q))) + '.p', "wb" ) )
        #pickle.dump( snr625_814[p], open( title+'f625f814_' + str(radius[0]) +'_' + str(abs(p-(q))) + '.p', "wb" ) )
    elif (p % 2 != 0):
        q += 1
        #print title+'f625f814_r2_' + str(abs((p)-(q)+1)) + '.p'
        pickle.dump( snr625_814[p], open(folder +'/'+ title+'f625f814_r2_' + str(abs((p)-(q)+1)) + '.p', "wb" ) )    
        #pickle.dump( snr625_814[p], open( title+'f625f814_' + str(radius[1]) +'_' + str(abs((p)-(q)+1)) + '.p', "wb" ) )
    
print "Pickled."
"""
"""
cat = []
cat.append(('Object', 'X pix', 'Y pix', 
            'S/N 435', 'S/N 555', 'S/N 625', 'S/N 814',
            'Mag 435', 'Mag 555', 'Mag 625', 'Mag 814',
            'AbsMag 435', 'AbsMag 555', 'AbsMag 625', 'AbsMag 814',
              star[cut435555[0]]   ,xcoord[cut435555[0]] ,ycoord[cut435555[0]],
              snr435[cut435555[0]] ,snr555[cut435555[0]] ,
              snr625[cut435555[0]] ,snr814[cut435555[0]] ,
              f435mag[cut435555[0]],f555mag[cut435555[0]],
              f625mag[cut435555[0]],f814mag[cut435555[0]],
              f435Abs[cut435555[0]],f555Abs[cut435555[0]],
              f625Abs[cut435555[0]],f814Abs[cut435555[0]],
              #unc435[cut435555[0]] ,unc555[cut435555[0]] ,
              #unc625[cut435555[0]] ,unc814[cut435555[0]] ,
            'Object', 'X pix', 'Y pix', 
            'S/N 435', 'S/N 555', 'S/N 625', 'S/N 814',
            'Mag 435', 'Mag 555', 'Mag 625', 'Mag 814',
            'AbsMag 435', 'AbsMag 555', 'AbsMag 625', 'AbsMag 814',
              star[cut625814[0]]   ,xcoord[cut625814[0]] ,ycoord[cut625814[0]],
              snr435[cut625814[0]] ,snr555[cut625814[0]] ,
              snr625[cut625814[0]] ,snr814[cut625814[0]] ,
              f435mag[cut625814[0]],f555mag[cut625814[0]],
              f625mag[cut625814[0]],f814mag[cut625814[0]],
              f435Abs[cut625814[0]],f555Abs[cut625814[0]],
              f625Abs[cut625814[0]],f814Abs[cut625814[0]],
              #unc435[cut625814[0]] ,unc555[cut625814[0]] ,
              #unc625[cut625814[0]] ,unc814[cut625814[0]]
              ))
pickle.dump(cat, open(title + 'List.p', 'wb'))
"""
