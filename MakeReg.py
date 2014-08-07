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
SNR     = [] # Column 06 the signal to noise
xcoord  = [] # Column 03 the x pix coordinate
ycoord  = [] # Column 04 the y pix coordinate

snr435  = [] # Column 20 SNR for F435W
snr555  = [] # Column 33 SNR for F555W
snr625  = [] # Column 46 SNR for F625W
snr814  = [] # Column 59 SNR for F814W

# arrays after the respective cuts

cut  = []

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

# Actual X & Y pixel coordinates of sn
xsn      = 3247.539
ysn      = 3419.971
"""
##################### 2008ha ######################
#"""
folder   = "SN2008HA"
name     = 'sn2008ha_new.phot'

# Actual X & Y pixel coordinates of sn
xsn      = 1726.352
ysn      = 3172.530
#"""
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
data = np.loadtxt(folder + '/' + name)

title = name[:-8]
################################################### 
######## append data from file to an array ########

print "Organizing ", name, " information..."

data    = np.array(data)
data    = data.astype(float)

star    = data[:,10] # type

sharp   = data[:, 6]
roond   = data[:, 7] # round is already a special word
crowd   = data[:, 9]

snr435  = data[:,19] # signal to noise
snr555  = data[:,32]
snr625  = data[:,45]
snr814  = data[:,58]

xcoord  = data[:, 2]
ycoord  = data[:, 3]


################################################### 
############ Save coordinates to a file ###########
print "Choppin some SN-suey"
circ = []
comm = []
clos = []

cut.append(np.where((star <= 2) & (sharp >= 0) &#(crowd <= 1 ) &
                (((snr435 >= 3) | (snr555 >= 3)) |
                ((snr625 >= 3) | (snr814 >= 3)))
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)))
for i in range(len(xcoord[cut[0]])):
    circ.append('circle(')
    comm.append(',')
    clos.append(',2)')
        
np.savetxt(folder +'/'+ title + 'sharp.reg', np.c_[circ,xcoord[cut[0]]+.5,comm,ycoord[cut[0]]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=yellow dashlist=8 3 width=1'
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1' \
               '\nimage;' )
#np.savetxt(folder +'/'+ title + 'all.txt',np.c_[xcoord[cut435555[0]]+.5,ycoord[cut435555[0]]+.5],fmt = "%1.2f")
print 'Files Saved'
