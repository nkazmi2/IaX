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
dmod    = 31.64 #31.50 

# Actual X & Y pixel coordinates of sn
xsn     = 1726.352
ysn     = 3172.530
radius  = 50.0 #pixels
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
radius  = 30.0 #pixels
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
#good = np.where((star <= 2) & (SNR >= 6) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius))
# cut 1 chooses the object, SNR, and SNR for f435w and f555w
#cut1 = np.where((star <= 2) & (snr435 >= 3) & (snr555 >= 3))
#cut2 = np.where((star <= 2) & (snr625 >= 3) & (snr814 >= 3))

# cuts even : object, SNR, f435w and f555w, and position 
cut1  = np.where((star <= 2) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius) &  ((snr625 >= 3)))
cut2  = np.where((star <= 2) & ((snr435 >= 3) | (snr555 >= 3)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut4  = np.where((star <= 2) & ((snr435 >= 4) | (snr555 >= 4)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut6  = np.where((star <= 2) & ((snr435 >= 5) | (snr555 >= 5)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut8  = np.where((star <= 2) & ((snr435 >= 6) | (snr555 >= 6)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut10 = np.where((star <= 2) & ((snr435 >= 7) | (snr555 >= 7)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut12 = np.where((star <= 2) & ((snr435 >= 8) | (snr555 >= 8)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 

# cuts odd : object, SNR, f625w and f814w, and position 
cut3  = np.where((star <= 2) & ((snr625 >= 3) | (snr814 >= 3)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut5  = np.where((star <= 2) & ((snr625 >= 4) | (snr814 >= 4)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut7  = np.where((star <= 2) & ((snr625 >= 5) | (snr814 >= 5)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut9  = np.where((star <= 2) & ((snr625 >= 6) | (snr814 >= 6)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut11 = np.where((star <= 2) & ((snr625 >= 7) | (snr814 >= 7)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
cut13 = np.where((star <= 2) & ((snr625 >= 8) | (snr814 >= 8)) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius)) 
#blue = np.subtract(f625Abs[cut5], f814Abs[cut5])
#print blue < -0.4
#cut15 = np.where
#cut14 = np.where((star <= 2) & (snr625 >= 4) & (snr814 >= 4) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < radius) & (blue <= -0.4))

#print len(chi435[cut9])
#print len(chi625[cut11])
#print chi814[cut13]
#print xcoord[cut5] < -0.4
#print ycoord[cut5]
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

print "Pickling!"

snr435_555 = ( f435Abs[cut1],f555Abs[cut1],(unc435[cut1]**2 + unc555[cut1]**2)**.5 )
pickle.dump( snr435_555, open( title+'f435f555.p', "wb" ) )
snr625_814 = ( f625Abs[cut1],f814Abs[cut1],(unc625[cut1]**2 + unc814[cut1]**2)**.5 )
pickle.dump( snr625_814, open( title+'f625f814.p', "wb" ) )

snr435_555_3 = ( f435Abs[cut2],f555Abs[cut2],(unc435[cut2]**2 + unc555[cut2]**2)**.5 )
pickle.dump( snr435_555_3, open( title+'f435f555_3.p', "wb" ) )
snr625_814_3 = ( f625Abs[cut3],f814Abs[cut3],(unc625[cut3]**2 + unc814[cut3]**2)**.5 )
pickle.dump( snr625_814_3, open( title+'f625f814_3.p', "wb" ) )

snr435_555_4 = ( f435Abs[cut4],f555Abs[cut4],(unc435[cut4]**2 + unc555[cut4]**2)**.5 )
pickle.dump( snr435_555_4, open( title+'f435f555_4.p', "wb" ) )
snr625_814_4 = ( f625Abs[cut5],f814Abs[cut5],(unc625[cut5]**2 + unc814[cut5]**2)**.5 )
pickle.dump( snr625_814_4, open( title+'f625f814_4.p', "wb" ) )

snr435_555_5 = ( f435Abs[cut6],f555Abs[cut6],(unc435[cut6]**2 + unc555[cut6]**2)**.5 )
pickle.dump( snr435_555_5, open( title+'f435f555_5.p', "wb" ) )
snr625_814_5 = ( f625Abs[cut7],f814Abs[cut7],(unc625[cut7]**2 + unc814[cut7]**2)**.5 )
pickle.dump( snr625_814_5, open( title+'f625f814_5.p', "wb" ) )

snr435_555_6 = ( f435Abs[cut8],f555Abs[cut8],(unc435[cut8]**2 + unc555[cut8]**2)**.5 )
pickle.dump( snr435_555_6, open( title+'f435f555_6.p', "wb" ) )
snr625_814_6 = ( f625Abs[cut9],f814Abs[cut9],(unc625[cut9]**2 + unc814[cut9]**2)**.5 )
pickle.dump( snr625_814_6, open( title+'f625f814_6.p', "wb" ) )

snr435_555_7 = ( f435Abs[cut10],f555Abs[cut10],(unc435[cut10]**2 + unc555[cut10]**2)**.5 )
pickle.dump( snr435_555_7, open( title+'f435f555_7.p', "wb" ) )
snr625_814_7 = ( f625Abs[cut11],f814Abs[cut11],(unc625[cut11]**2 + unc814[cut11]**2)**.5 )
pickle.dump( snr625_814_7, open( title+'f625f814_7.p', "wb" ) )

snr435_555_8 = ( f435Abs[cut12],f555Abs[cut12],(unc435[cut12]**2 + unc555[cut12]**2)**.5 )
pickle.dump( snr435_555_8, open( title+'f435f555_8.p', "wb" ) )
snr625_814_8 = ( f625Abs[cut13],f814Abs[cut13],(unc625[cut13]**2 + unc814[cut13]**2)**.5 )
pickle.dump( snr625_814_8, open( title+'f625f814_8.p', "wb" ) )

#blue = np.subtract(f625Abs[cut5], f814Abs[cut5])
#blue = np.where(((f625Abs[cut5] - f814Abs[cut5])) <= 0.4)
#print blue
#with open(title+'F625W_F814W_snr4_blue.csv', 'wb') as g:
    #writer = csv.writer(g)  
    #writer.writerows(izip(xcoord[cut5]+.5,ycoord[cut5]+.5,blue))
print "Pickled."


print "Open file to save contrained data..."

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

#with open(title+'coord.csv', 'wb') as f:
#    writer = csv.writer(f)
#    writer.writerows(izip(xcoord[cut3],ycoord[cut3]))    
#    writer.writerows(izip(xcoord[cut4],ycoord[cut4]))
#    #writer.writerows(izip(xcoord[cut3],ycoord[cut3],chi435[cut3],SNR[cut3],CHI[cut3],SNR[cut4],f435Abs[cut3],f555Abs[cut3],f435mag[cut3],f555mag[cut3],chi435[cut3],chi555[cut3],snr435[cut3],snr555[cut3],xcoord[cut4],ycoord[cut4],chi625[cut4],SNR[cut4],CHI[cut4],SNR[cut4],f625Abs[cut4],f814Abs[cut4],f625mag[cut4],f814mag[cut4],chi625[cut4],chi814[cut4],snr625[cut4],snr814[cut4]))
#print "Saveing file "+title+"coord.csv"

print "Saving file " + title + "F435W_F555W.csv & " + title + "F625W_F814W.csv and all others"

################################################### 
############ Make scatter plots for CMD ###########
"""
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
#c1plt.scatter(np.subtract(f435Abs[cut2], f555Abs[cut2]),f555Abs[cut2], c="g",marker='8')
c1plt.scatter(np.subtract(f435Abs[cut4], f555Abs[cut4]),f555Abs[cut4], c="b",marker='p')
c1plt.scatter(np.subtract(f435Abs[cut6], f555Abs[cut6]),f555Abs[cut6], c="r",marker='v')
#c1plt.scatter(np.subtract(f435Abs[cut4], f555Abs[cut4]),f555Abs[cut4], c="r",marker='o')
#c1plt.scatter(np.subtract(f435Abs[check], f555Abs[check]),f435Abs[check],c="g",marker='o')
#c1plt.scatter(np.subtract(f435mag[cut3], f555mag[cut3]),f435mag[cut3], c="r",marker='o')

# plotting the title, and for magical reasons, it works when it's here
plt.title("Color Magnitude Diagram for " + title[:-1], fontdict = font)

# c2 refers to the cut2 
c2plt = plt.subplot2grid((2,2), (1,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F625W - F814W",fontdict = font)
plt.ylabel("F625W",fontdict = font)
#c2plt.scatter(np.subtract(f625Abs[cut3], f814Abs[cut3]),f625Abs[cut3], c="g",marker='8')
c2plt.scatter(np.subtract(f625Abs[cut5], f814Abs[cut5]),f625Abs[cut5], c="b",marker='p')
c2plt.scatter(np.subtract(f625Abs[cut7], f814Abs[cut7]),f625Abs[cut7], c="r",marker='v')
#c2plt.scatter(np.subtract(f625mag[cut4], f814mag[cut4]),f625mag[cut4], c="r",marker='o')

#plt.legend((c1plt,c2plt),('R = 30 pixels','R = 30 pixels'))
print "Save and show CMDs..."
plt.savefig(title+"_limits.png")
#plt.show()
"""