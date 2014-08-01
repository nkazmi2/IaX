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
cut435555r1= []
cut625814r1= []
cut435555r2= []
cut625814r2= []

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
folder   = "SN2008GE"
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

# Actual X & Y pixel coordinates of sn
xsn      = 3247.539
ysn      = 3419.971
radius   = [10.342,17.24,23.00,34.47] # 450,750,1000,1500

"""
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
dmod     = 31.64 #31.50 # value I got from NED

# Actual X & Y pixel coordinates of sn
xsn      = 1726.352
ysn      = 3172.530

radius   = [9.282,15.469,20.63,30.94] # 450,750,1000,1500
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

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod     = 30.58 

# Actual X & Y pixel coordinates of sn
xsn      = 1796.640
ysn      = 1931.995

radius   = [14.171,23.62,31.50,47.236] # 450,750,1000,1500
"""
##################### 2010el ######################
#"""    
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
dmod     = 29.99 

# Actual X & Y pixel coordinates of sn
xsn      = 2418.859
ysn      = 1570.826

radius   = [18.62,31.03,41.38,62.065] # 450,750,1000,1500
#"""
###################################################    
######### Open and read in the data file ##########

print "Opening file: ",name

print "Extracting ", name, " information..."
data = np.loadtxt(folder + '/' + name)

title = name[:-8]
################################################### 
######## append data from file to an array ########

print "Organizing ", name, " information..."

data    = np.array(data)
data    = data.astype(float)

star    = data[:,10] # type
#SNR     = data[:, 5] # general signal to noise
#CHI     = data[:, 4] # general chi for fit 

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

#chi435  = data[:,18] # Chi for fit
#chi555  = data[:,31] 
#chi625  = data[:,44] 
#chi814  = data[:,57]

xcoord  = data[:, 2]
ycoord  = data[:, 3]
################################################### 
########### Calculate Absolute Magnitude ##########

print "Calculating Absolute Magnitude..."
 
f435Abs = f435mag - dmod - ACS435 #- H435
f555Abs = f555mag - dmod - ACS555 #- H555
f625Abs = f625mag - dmod - ACS625 #- H625
f814Abs = f814mag - dmod - ACS814 #- H814

################################################### 
########### Deal with bad points ##########

identify = pyregion.open(folder + '/'+ title +'prog.reg')
r = pyregion.open(folder + '/'+ title +'coord.reg')
save = []
badX = []
badY = []
fix  = []

for i in range(len(identify)):
    if (pyregion.ShapeList(identify[i].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
        fix.append(i)
        
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
##### Find correct color magnitudes make cuts #####
# So many for loops @.@ 
# somehow need to get around this :/

print "Applying contrains to SN Data..."
snr = []
rad = []
for m in range(3,6):
    for i in range(len(radius)):
        cut435555.append(np.where((star <= 2) & ((snr435 >= m) | (snr555 >= m)) & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])     &
                    (snr435 >= 3) & (snr555 >= 3) & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
        cut625814.append(np.where((star <= 2) & ((snr625 >= m) | (snr814 >= m)) & 
                    ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[i])     & 
                    (snr625 >= 3) & (snr814 >= 3)  & 
                    list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))))
        rad.append(i)
        snr.append(m)
        
################################################### 
############ Save good arrays to a file ###########

print "Pickling!"

for n in range(len(cut435555)):
    snr435_555.append(( f435Abs[cut435555[n]],f555Abs[cut435555[n]], 
                       unc555[cut435555[n]],
                        (unc435[cut435555[n]]**2 + unc555[cut435555[n]]**2)**.5 ))
    snr625_814.append(( f625Abs[cut625814[n]],f814Abs[cut625814[n]], 
                       unc625[cut625814[n]],
                        (unc625[cut625814[n]]**2 + unc814[cut625814[n]]**2)**.5 ))
    pickle.dump( snr435_555[n], open(folder + '/' + title + 'f435f555_sn' + str(snr[n]) + '_rad' + str(rad[n]) + '.p', "wb" ) )
    pickle.dump( snr625_814[n], open(folder + '/' + title + 'f625f814_sn' + str(snr[n]) + '_rad' + str(rad[n]) + '.p', "wb" ) )

print "Pickled."

############ Save coordinates to a file ###########
"""
circ = []
comm = []
clos = []
#cut  = []
#cut.append(np.where((star <= 2) & (((snr435 >= 3) | (snr555 >= 3)) 
#                | ((snr625 >= 3) | (snr814 >= 3)))
#                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius[0])))
             
#first = np.c_[xcoord[cut[0]]+.5 ,ycoord[cut[0]]+.5]
cut435555.append(np.where((star <= 2) & (((snr435 >= 3) | (snr555 >= 3)) 
                | ((snr625 >= 3) | (snr814 >= 3)))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)))
for i in range(len(xcoord[cut435555[0]])):
    circ.append('circle(')
    comm.append(',')
    clos.append(',2)')
        
np.savetxt(folder +'/'+ title + 'temp.reg', np.c_[circ,xcoord[cut435555[0]]+.5,comm,ycoord[cut435555[0]]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=cyan dashlist=8 3 width=1'
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1' \
               '\nimage;' )
np.savetxt(folder +'/'+ title + 'all.txt',np.c_[xcoord[cut435555[0]]+.5,ycoord[cut435555[0]]+.5],fmt = "%1.2f")
print 'Files Saved'
"""
"""
h = [2, 5] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

supe  = plt.subplot2grid((2,2), (0,0), colspan = 1)
#supe.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("Signal/Noise F435W",fontdict = font)
plt.ylabel("Magnitude",fontdict = font)
supe.scatter(snr435[cut435555[2]],f435Abs[cut435555[2]])

sope  = plt.subplot2grid((2,2), (0,1), colspan = 1)
#sope.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("Signal/Noise F555W",fontdict = font)
plt.ylabel("Magnitude",fontdict = font)
sope.scatter(snr555[cut435555[2]],f555Abs[cut435555[2]])

soap  = plt.subplot2grid((2,2), (1,0), colspan = 1)
#soap.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("Signal/Noise F625W",fontdict = font)
plt.ylabel("Magnitude",fontdict = font)
soap.scatter(snr625[cut625814[2]],f625Abs[cut625814[2]])

squid = plt.subplot2grid((2,2), (1,1), colspan = 1)
#squid.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("Signal/Noise F814W",fontdict = font)
plt.ylabel("Magnitude",fontdict = font)
squid.scatter(snr814[cut625814[2]],f814Abs[cut625814[2]])
plt.savefig("AbsMagSN_.png")    
"""
######################
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
