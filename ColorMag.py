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

################################################### 
############### declared variables ################

data    = []

star    = [] # Column 11 the object type
SNR     = [] # Column 06 the signal to noise
CHI     = [] # Column 05 the Chi Fit 
xcoord  = [] # Column 03 the x pix coordinate
ycoord  = [] # Column 04 the y pix coordinate

chi435  = [] # Column 19 Chi for F435W
chi555  = [] # Column 32 Chi for F555W
chi625  = [] # Column 45 Chi for F625W
chi814  = [] # Column 58 Chi for F814W

snr435  = [] # Column 20 SNR for F435W
snr555  = [] # Column 33 SNR for F555W
snr625  = [] # Column 46 SNR for F625W
snr814  = [] # Column 59 SNR for F814W

good    = []

# arrays after the respective cuts

f435mag = [] # Column 16 F435W Apparent Magnitude
f555mag = [] # Column 29 F555W Apparent Magnitude
f625mag = [] # Column 42 F625W Apparent Magnitude
f814mag = [] # Column 55 F814W Apparent Magnitude

f435Abs = [] # Absolute F435W Magnitudes
f555Abs = [] # Absolute F555W Magnitudes
f625Abs = [] # Absolute F625W Magnitudes
f814Abs = [] # Absolute F814W Magnitudes

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
radius  = 50.0 #pixels

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
dmod    = 31.50 

# Actual X & Y pixel coordinates of sn
xsn     = 1726.352
ysn     = 3172.530
radius  = 100.0 #pixels
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
radius  = 50.0 #pixels
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
radius  = 50.0 #pixels
"""
###################################################    
######### Open and read in the data file ##########

print "Opening file: ", name

photfile = open(name,'r')

if name.endswith('new.phot'):
    title = name[:-8]

################################################### 
######## append data from file to an array ########

print "Extracting ", name, " information..."

for line in photfile:
    columns = line.split()
    data.append(columns) # slowest step thus far

data    = np.array(data)
data    = data.astype(float)

star    = data[:,10]
SNR     = data[:, 5]
CHI     = data[:, 4] 

f435mag = data[:,15]
f555mag = data[:,28]
f625mag = data[:,41]
f814mag = data[:,55]

snr435  = data[:,19]
snr555  = data[:,32]
snr625  = data[:,45]
snr814  = data[:,58]

chi435  = data[:,18] 
chi555  = data[:,31] 
chi625  = data[:,44] 
chi814  = data[:,57]

xcoord  = data[:, 2]
ycoord  = data[:, 3]

#checking lengths of data
#print len(data)      #156557 number of lines 
#print len(data[10])  #271, the is the columns 

################################################### 
########### Calculate Absolute Magnitude ##########

print "Calculating Absolute Magnitude..."
 
f435Abs = f435mag - dmod - ACS435
f555Abs = f555mag - dmod - ACS555
f625Abs = f625mag - dmod - ACS625
f814Abs = f814mag - dmod - ACS814 

################################################### 
##### Find correct color magnitudes make cuts #####

print "Applying contrains to SN Data..."

# good is a cut of the object type and the "overall" SNR
good = np.where((star <= 2) & (SNR >= 6) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius))
# cut 1 chooses the object, SNR, and SNR for f435w and f555w
cut1 = np.where((star <= 2) & (snr435 >= 3) & (snr555 >= 3))
# cut 2 chooses the object, SNR, and SNR for f625w and f814w
cut2 = np.where((star <= 2) & (snr625 >= 3) & (snr814 >= 3))
# cut 3 object, SNR, f435w and f555w, and position 
cut3 = np.where((star <= 2) & (snr435 >= 3) & (snr555 >= 3) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
# cut 3 object, SNR, f435w and f555w, and position 
cut4 = np.where((star <= 2) & (snr625 >= 3) & (snr814 >= 3) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
# cut 3 object, SNR, f435w and f555w, and position 
cut5 = np.where((star == 1) & (snr435 >= 4) & (snr555 >= 4) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
# cut 3 object, SNR, f435w and f555w, and position 
cut6 = np.where((star == 1) & (snr625 >= 4) & (snr814 >= 4) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 

################################################### 
############ Save good arrays to a file ###########
#print "Testing repeated values..." 
# stupid tests
#t = []
#u = []
#y = []
#v = []
#t = xcoord[cut4]
#u = ycoord[cut4]
#y = xcoord[cut3]
#v = ycoord[cut3]
#print t,y
#for k in range(len(xcoord[cut4])):
#how = np.where(xcoord[cut4] == xcoord[cut3])
#print t[how != True], u[how != True], y[how != True], v[how != True]
#print len(xcoord[cut4]), len(xcoord[how])
#writer.writerows(izip(xcoord[how != True],ycoord[how != True]))
#writer.writerows(izip(y[how != True],v[how != True]))

print "Open file to save contrained data..."

with open(title+'F435W_F555W_g6.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(xcoord[good]+.5,ycoord[good]+.5))
    
with open(title+'F435W_F555W_3.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(xcoord[cut3]+.5,ycoord[cut3]+.5))

with open(title+'F625W_F814W_3.csv', 'wb') as g:
    writer = csv.writer(g)  
    writer.writerows(izip(xcoord[cut4]+.5,ycoord[cut4]+.5))
    
with open(title+'F435W_F555W_4.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(xcoord[cut5]+.5,ycoord[cut5]+.5))

with open(title+'F625W_F814W_4.csv', 'wb') as g:
    writer = csv.writer(g)  
    writer.writerows(izip(xcoord[cut6]+.5,ycoord[cut6]+.5))
    
#with open(title+'coord.csv', 'wb') as f:
#    writer = csv.writer(f)
#    writer.writerows(izip(xcoord[cut3],ycoord[cut3]))    
#    writer.writerows(izip(xcoord[cut4],ycoord[cut4]))
#    #writer.writerows(izip(xcoord[cut3],ycoord[cut3],chi435[cut3],SNR[cut3],CHI[cut3],SNR[cut4],f435Abs[cut3],f555Abs[cut3],f435mag[cut3],f555mag[cut3],chi435[cut3],chi555[cut3],snr435[cut3],snr555[cut3],xcoord[cut4],ycoord[cut4],chi625[cut4],SNR[cut4],CHI[cut4],SNR[cut4],f625Abs[cut4],f814Abs[cut4],f625mag[cut4],f814mag[cut4],chi625[cut4],chi814[cut4],snr625[cut4],snr814[cut4]))
#print "Saveing file "+title+"coord.csv"
    
print "Saving file " + title + "F435W_F555W.csv & " + title + "F625W_F814W.csv and all others"

################################################### 
############ Make scatter plots for CMD ###########

print "Begin plotting CMD..."
h = [6, 6] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [6, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.001)
#plots = plt.subplot(gs[0])

# c1 refers to the cut1
c1plt = plt.subplot2grid((2,2), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W",fontdict = font)
plt.ylabel("F555W",fontdict = font)
c1plt.scatter(np.subtract(f435Abs[cut3], f555Abs[cut3]),f555Abs[cut3], c="b",marker='o')
#c1plt.scatter(np.subtract(f625Abs[cut4], f814Abs[cut4]),f625Abs[cut4], c="r",marker='o')
#c1plt.scatter(np.subtract(f435Abs[check], f555Abs[check]),f435Abs[check],c="g",marker='o')
#c1plt.scatter(np.subtract(f435mag[cut3], f555mag[cut3]),f435mag[cut3], c="r",marker='o')

# plotting the title, and for magical reasons, it works when it's here
plt.title("Color Magnitude Diagram for " + title[:-1], fontdict = font)

# c2 refers to the cut2 
c2plt = plt.subplot2grid((2,2), (1,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F625W - F814W",fontdict = font)
plt.ylabel("F625W",fontdict = font)
c2plt.scatter(np.subtract(f625Abs[cut4], f814Abs[cut4]),f625Abs[cut4], c="r",marker='o')
#c2plt.scatter(np.subtract(f625mag[cut4], f814mag[cut4]),f625mag[cut4], c="r",marker='o')

#plt.legend((c1plt,c2plt),('R = 30 pixels','R = 30 pixels'))
print "Save and show CMDs..."
plt.savefig(title+"_limits.png")
#plt.show()
