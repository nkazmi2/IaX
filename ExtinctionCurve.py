# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 10:39:29 2014

@author: Nova
"""
###################################################  
############# Extinction curve ####################
################################################### 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

################################################### 

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
        
Xaxis = []
#Xaxis.append([1.0/814,1.0/625,1.0/555,1.0/435])

Xaxis.append((1.0/(814*10**-3),
              1.0/(625*10**-3),
              1.0/(555*10**-3),
              1.0/(435*10**-3)))
Xaxis = np.reshape(Xaxis,(4,1))

h = [2, 5] # height of the plotted figure
fig = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
#fig.subplots_adjust(wspace=.5)
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

#fig.suptitle('Extinction curves for Supernovae',
#          fontdict = font, size=12)
################################################### 
######### Things that change for each sn ##########
##################### 2008ge ######################

SNname1  = "SN 2008GE"

# Magnitude of the Milkyway Galaxy 
ACS435ge   = 0.046 #F435W
ACS555ge   = 0.036 #F555W	
ACS625ge   = 0.028 #F625W	
ACS814ge   = 0.020 #F814W	
MWge       = 0.011
Host       = 0.0

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	


#bestfit = np.polyfit([(1.0/(814*10**-3)),(1.0/(625*10**-3)),(1.0/(555*10**-3)),(1.0/(435*10**-3))], 
#                     [ACS814ge/MWge,ACS625ge/MWge,ACS555ge/MWge,ACS435ge/MWge], 4)
#polynomial = np.poly1d(bestfit)
#Curve = polynomial(Xaxis)

squid = plt.subplot2grid((2,2), (1,1), colspan = 1)
#squid.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2008ge 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#squid.scatter(Xaxis,[ACS814ge,ACS625ge,ACS555ge,ACS435ge])
squid.scatter(Xaxis,[ACS814ge/MWge,ACS625ge/MWge,ACS555ge/MWge,ACS435ge/MWge],marker='.')
#squid.plot(polynomial,bestfit)

##################### 2008ha ######################

SNname2  = "SN 2008HA"

# Magnitude of the Milkyway Galaxy 
ACS435ha   = 0.284 #F435W
ACS555ha   = 0.219 #F555W	
ACS625ha   = 0.174 #F625W	
ACS814ha   = 0.120 #F814W	
MWha       = 0.07
Host     = 0.0

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	

soap  = plt.subplot2grid((2,2), (1,0), colspan = 1)
#soap.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2008ha 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#soap.scatter(Xaxis,[ACS814ha,ACS625ha,ACS555ha,ACS435ha])
soap.scatter(Xaxis,[ACS814ha/MWha,ACS625ha/MWha,ACS555ha/MWha,ACS435ha/MWha],marker='.')
##################### 2010ae ######################

SNname3  = "SN 2010AE"

# Magnitude of the Milkyway Galaxy m is low(?) .1sol
ACS435ae   = 0.509 #F435W
ACS555ae   = 0.394 #F555W	
ACS625ae   = 0.313 #F625W	
ACS814ae   = 0.215 #F814W	
MWae       = 0.124
Hostae     = 0.5

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	

sope  = plt.subplot2grid((2,2), (0,1), colspan = 1)
#sope.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2010ae 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#sope.scatter(Xaxis,[ACS814ae,ACS625ae,ACS555ae,ACS435ae])
sope.scatter(Xaxis,[ACS814ae/MWae,ACS625ae/MWae,ACS555ae/MWae,ACS435ae/MWae],marker='.')
##################### 2010el ######################
    
SNname4   = "SN 2010EL"
    
# Magnitude of the Milkyway Galaxy 
ACS435el   = 0.033 #F435W
ACS555el   = 0.025 #F555W	
ACS625el   = 0.020 #F625W	
ACS814el   = 0.014 #F814W	
MWel       = 0.008
Hostel     = 0.8

H435el     = 3.255 #F435W
H555el     = 2.517 #F555W	
H625el     = 2.001 #F625W	
H814el     = 1.376 #F814W	

supe  = plt.subplot2grid((2,2), (0,0), colspan = 1)
#supe.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2010el 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#supe.scatter(Xaxis,[ACS814el,ACS625el,ACS555el,ACS435el])
supe.scatter(Xaxis,[ACS814el/MWel,ACS625el/MWel,ACS555el/MWel,ACS435el/MWel],marker='.')
###################################################

plt.tight_layout()
plt.savefig("Extinction.png")    
