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

#Xaxis.append((1.0/(814*10**-3), #0
              #1.0/(806*10**-3),
              #1.0/(658*10**-3),
              #1.0/(625*10**-3), #3
              #1.0/(555*10**-3), #4
              #1.0/(551*10**-3),
              #1.0/(445*10**-3),
              #1.0/(435*10**-3))) #7
#Xaxis = np.reshape(Xaxis,(8,1))
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
MWge       = 0.011 #E(B-V)
Hostge     = 0.0
A_Vge      = 0.033

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	


#bestfit = np.polyfit([(1.0/(814*10**-3)),(1.0/(625*10**-3)),(1.0/(555*10**-3)),(1.0/(435*10**-3))], 
#                     [ACS814ge/MWge,ACS625ge/MWge,ACS555ge/MWge,ACS435ge/MWge], 4)
#polynomial = np.poly1d(bestfit)
#Curve = polynomial(Xaxis)
"""
folder   = "SN2008GE"
name     = 'sn2008ge_new.phot'
dmod     = 31.64
data     = np.loadtxt(folder + '/' + name)
data     = np.array(data)
data     = data.astype(float)
f435mag  = data[:,15] 
f555mag  = data[:,28]
f625mag  = data[:,41]
f814mag  = data[:,55]
"""
squid = plt.subplot2grid((2,2), (0,0), colspan = 1)
#squid.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2008ge 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#squid.scatter(Xaxis,[ACS814ge,ACS625ge,ACS555ge,ACS435ge])
#squid.plot(Xaxis,[(ACS814ge)/MWge,(ACS625ge)/MWge,(ACS555ge)/MWge,(ACS435ge)/MWge],'-o')
#squid.plot(Xaxis,[(ACS814ge - ACS555ge)/MWge,(ACS625ge - ACS555ge)/MWge,(ACS555ge - ACS555ge)/MWge,(ACS435ge - ACS555ge)/MWge,(ACS814ge - ACS555ge)/MWge,(ACS625ge - ACS555ge)/MWge,(ACS555ge - ACS555ge)/MWge,(ACS435ge - ACS555ge)/MWge],'-o')
#squid.plot(Xaxis,[(ACS814ge - A_Vge)/MWge,(ACS625ge - A_Vge)/MWge,(ACS555ge - A_Vge)/MWge,(ACS435ge - A_Vge)/MWge],'-o')
squid.plot([(1.0/(435*10**-3)),(1.0/(475*10**-3)),(1.0/(550*10**-3)),
            (1.0/(555*10**-3)),(1.0/(606*10**-3)),(1.0/(625*10**-3)),
            (1.0/(775*10**-3)),(1.0/(814*10**-3)),(1.0/(850*10**-3))],
            [(0.046-A_Vge)/MWge,(0.042-A_Vge)/MWge,(0.033-A_Vge)/MWge,
             (0.036-A_Vge)/MWge,(0.032-A_Vge)/MWge,(0.028-A_Vge)/MWge,
             (0.021-A_Vge)/MWge,(0.019-A_Vge)/MWge,(0.016-A_Vge)/MWge],'-v')
                    
             
#squid.plot(Xaxis,[(f814mag - dmod - ACS814ge - ACS555ge)/MWge,(f625mag - dmod - ACS625ge - ACS555ge)/MWge,(f555mag - dmod - ACS555ge - ACS555ge)/MWge,(f435mag - dmod - ACS435ge - ACS555ge)/MWge],'-o')
#squid.plot(polynomial,bestfit)
#print "SN08ge : " + str((ACS814ge - ACS555ge)/MWge) + ", " + str((ACS625ge - ACS555ge)/MWge) + ", " + str((ACS555ge - ACS555ge)/MWge) + ", " + str((ACS435ge - ACS555ge)/MWge)
#squid.plot([(1.0/(360*10**-3)),(1.0/(450*10**-3)),(1.0/(550*10**-3)),
            #(1.0/(660*10**-3)),(1.0/(800*10**-3)),(1.0/(1250*10**-3)),
            #(1.0/(1650*10**-3)),(1.0/(2200*10**-3)),(1.0/(3500*10**-3)),
            #(1.0/(4800*10**-3))],
            #[1.531,1.324,1,0.748,0.482,0.282,0.175,0.112,0.058,0.023],'-v')

##################### 2008ha ######################

SNname2  = "SN 2008HA"

# Magnitude of the Milkyway Galaxy 
ACS435ha   = 0.284 #F435W
ACS555ha   = 0.219 #F555W	
ACS625ha   = 0.174 #F625W	
ACS814ha   = 0.120 #F814W	
MWha       = 0.07  #E(B-V)
Hostha     = 0.0
A_Vha      = 0.206

H435     = 0 #F435W
H555     = 0 #F555W	
H625     = 0 #F625W	
H814     = 0 #F814W	
"""
folder   = "SN2008HA"
name     = 'sn2008ha_new.phot'
data     = np.loadtxt(folder + '/' + name)
data     = np.array(data)
data     = data.astype(float)
f435mag  = data[:,15] 
f555mag  = data[:,28]
f625mag  = data[:,41]
f814mag  = data[:,55]
"""
soap  = plt.subplot2grid((2,2), (0,1), colspan = 1)
#soap.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2008ha 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#soap.scatter(Xaxis,[ACS814ha,ACS625ha,ACS555ha,ACS435ha])
#soap.plot(Xaxis,[(ACS814ha - ACS555ha)/MWha,(ACS625ha - ACS555ha)/MWha,(ACS555ha - ACS555ha)/MWha,(ACS435ha - ACS555ha)/MWha,(ACS814ha - ACS555ha)/MWha,(ACS625ha - ACS555ha)/MWha,(ACS555ha - ACS555ha)/MWha,(ACS435ha - ACS555ha)/MWha],'-o')
#soap.plot(Xaxis,[(ACS814ha - A_Vha)/MWha,(ACS625ha - A_Vha)/MWha,(ACS555ha - A_Vha)/MWha,(ACS435ha - A_Vha)/MWha],'-o')
soap.plot([(1.0/(435*10**-3)),(1.0/(475*10**-3)),(1.0/(550*10**-3)),
            (1.0/(555*10**-3)),(1.0/(606*10**-3)),(1.0/(625*10**-3)),
            (1.0/(775*10**-3)),(1.0/(814*10**-3)),(1.0/(850*10**-3))],
            [(0.284-A_Vha)/MWha,(0.257-A_Vha)/MWha,(0.206-A_Vha)/MWha,
             (0.219-A_Vha)/MWha,(0.194-A_Vha)/MWha,(0.174-A_Vha)/MWha,
             (0.128-A_Vha)/MWha,(0.120-A_Vha)/MWha,(0.098-A_Vha)/MWha],'-v')
             
#soap.plot(Xaxis,[(ACS814ha)/MWha,(ACS625ha)/MWha,(ACS555ha)/MWha,(ACS435ha)/MWha],'-o')
#print "SN08ha : " +  str((ACS814ha - ACS555ha)/MWha) + ", " + str((ACS625ha - ACS555ha)/MWha) + ", " + str((ACS555ha - ACS555ha)/MWha) + ", " + str((ACS435ha - ACS555ha)/MWha)
#soap.plot([(1.0/(360*10**-3)),(1.0/(450*10**-3)),(1.0/(550*10**-3)),
            #(1.0/(660*10**-3)),(1.0/(800*10**-3)),(1.0/(1250*10**-3)),
            #(1.0/(1650*10**-3)),(1.0/(2200*10**-3)),(1.0/(3500*10**-3)),
            #(1.0/(4800*10**-3))],
            #[1.531,1.324,1,0.748,0.482,0.282,0.175,0.112,0.058,0.023],'-v')
##################### 2010ae ######################

SNname3  = "SN 2010AE"

# Magnitude of the Milkyway Galaxy m is low(?) .1sol
ACS435ae   = 0.509 #F435W
ACS555ae   = 0.394 #F555W	
ACS625ae   = 0.313 #F625W	
ACS814ae   = 0.215 #F814W	
MWae       = 0.124 #E(B-V)
Hostae     = 0.5
A_Vae      = 0.369

H435     = 2.052 #F435W
H555     = 1.588 #F555W	
H625     = 1.262 #F625W	
H814     = 0.867 #F814W	

"""
folder   = "SN2010AE"
name     = 'sn2010ae_new.phot'
data     = np.loadtxt(folder + '/' + name)
data     = np.array(data)
data     = data.astype(float)
f435mag  = data[:,15] 
f555mag  = data[:,28]
f625mag  = data[:,41]
f814mag  = data[:,55]
"""
sope  = plt.subplot2grid((2,2), (1,0), colspan = 1)
#sope.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2010ae 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#sope.scatter(Xaxis,[ACS814ae,ACS625ae,ACS555ae,ACS435ae])

#sope.plot(Xaxis,[(ACS814ae - ACS555ae)/MWae,(ACS625ae - ACS555ae)/MWae,(ACS555ae - ACS555ae)/MWae,(ACS435ae - ACS555ae)/MWae,(ACS814ae - ACS555ae)/MWae,(ACS625ae - ACS555ae)/MWae,(ACS555ae - ACS555ae)/MWae,(ACS435ae - ACS555ae)/MWae],'-o')
#sope.plot(Xaxis,[(ACS814ae - A_Vae)/MWae,(ACS625ae - A_Vae)/MWae,(ACS555ae - A_Vae)/MWae,(ACS435ae - A_Vae)/MWae],'-o')
sope.plot([(1.0/(435*10**-3)),(1.0/(475*10**-3)),(1.0/(550*10**-3)),
            (1.0/(555*10**-3)),(1.0/(606*10**-3)),(1.0/(625*10**-3)),
            (1.0/(775*10**-3)),(1.0/(814*10**-3)),(1.0/(850*10**-3))],
            [(0.509-A_Vae)/MWae,(0.461-A_Vae)/MWae,(0.369-A_Vae)/MWae,
             (0.394-A_Vae)/MWae,(0.348-A_Vae)/MWae,(0.313-A_Vae)/MWae,
             (0.230-A_Vae)/MWae,(0.215-A_Vae)/MWae,(0.175-A_Vae)/MWae],'-v')
#sope.plot(Xaxis,[(ACS814ae)/MWae,(ACS625ae)/MWae,(ACS555ae)/MWae,(ACS435ae)/MWae],'-o')
#print "SN10ae : " +  str((ACS814ae - ACS555ae)/MWae) + ", " + str((ACS625ae - ACS555ae)/MWae) + ", " + str((ACS555ae - ACS555ae)/MWae) + ", " + str((ACS435ae - ACS555ae)/MWae)
#sope.plot([(1.0/(360*10**-3)),(1.0/(450*10**-3)),(1.0/(550*10**-3)),
            #(1.0/(660*10**-3)),(1.0/(800*10**-3)),(1.0/(1250*10**-3)),
            #(1.0/(1650*10**-3)),(1.0/(2200*10**-3)),(1.0/(3500*10**-3)),
            #(1.0/(4800*10**-3))],
            #[1.531,1.324,1,0.748,0.482,0.282,0.175,0.112,0.058,0.023],'-v')
##################### 2010el ######################
    
SNname4   = "SN 2010EL"
    
# Magnitude of the Milkyway Galaxy 
ACS435el   = 0.033 #F435W
ACS555el   = 0.025 #F555W	
ACS625el   = 0.020 #F625W	
ACS814el   = 0.014 #F814W	
MWel       = 0.008 #E(B-V)
Hostel     = 0.8
A_Vel      = 0.024

H435el     = 3.255
H555el     = 2.517
H625el     = 2.001 
H814el     = 1.376 	

""""
folder   = "SN2010el"
name     = 'sn2010el_new.phot'
data     = np.loadtxt(folder + '/' + name)
data     = np.array(data)
data     = data.astype(float)
f435mag  = data[:,15] 
f555mag  = data[:,28]
f625mag  = data[:,41]
f814mag  = data[:,55]
"""

supe  = plt.subplot2grid((2,2), (1,1), colspan = 1)
#supe.update(left=0.05, right=0.48, wspace=0.05)
plt.xlabel("SN 2010el 1/$\lambda \, (\mu m^{-1})$",fontdict = font)
plt.ylabel("$E (\lambda - V) \, / \, E(B-V)$",fontdict = font)
#supe.scatter(Xaxis,[ACS814el,ACS625el,ACS555el,ACS435el])
#supe.plot(Xaxis,[(ACS814el - ACS555el)/MWel,(ACS625el - ACS555el)/MWel,(ACS555el - ACS555el)/MWel,(ACS435el - ACS555el)/MWel,(ACS814el - ACS555el)/MWel,(ACS625el - ACS555el)/MWel,(ACS555el - ACS555el)/MWel,(ACS435el - ACS555el)/MWel],'-o')
#supe.plot(Xaxis,[(ACS814el - A_Vel)/MWel,(ACS625el - A_Vel)/MWel,(ACS555el - A_Vel)/MWel,(ACS435el - A_Vel)/MWel],'-o')
supe.plot([(1.0/(435*10**-3)),(1.0/(475*10**-3)),(1.0/(550*10**-3)),
            (1.0/(555*10**-3)),(1.0/(606*10**-3)),(1.0/(625*10**-3)),
            (1.0/(775*10**-3)),(1.0/(814*10**-3)),(1.0/(850*10**-3))],
            [(0.033-A_Vel)/MWel,(0.030-A_Vel)/MWel,(0.024-A_Vel)/MWel,
             (0.025-A_Vel)/MWel,(0.022-A_Vel)/MWel,(0.020-A_Vel)/MWel,
             (0.015-A_Vel)/MWel,(0.014-A_Vel)/MWel,(0.011-A_Vel)/MWel],'-v')

#supe.plot(Xaxis,[(ACS814el)/MWel,(ACS625el)/MWel,(ACS555el)/MWel,(ACS435el)/MWel],'-o')
#supe.plot(Xaxis,[(H814el)/MWel,(H625el)/MWel,(H555el)/MWel,(H435el)/MWel],'-o')
#print "SN10el : " +  str((ACS814el - ACS555el)/MWel) + ", " + str((ACS625el - ACS555el)/MWel) + ", " + str((ACS555el - ACS555el)/MWel) + ", " + str((ACS435el - ACS555el)/MWel)
#supe.plot([(1.0/(360*10**-3)),(1.0/(450*10**-3)),(1.0/(550*10**-3)),
            #(1.0/(660*10**-3)),(1.0/(800*10**-3)),(1.0/(1250*10**-3)),
            #(1.0/(1650*10**-3)),(1.0/(2200*10**-3)),(1.0/(3500*10**-3)),
            #(1.0/(4800*10**-3))],
            #[1.531,1.324,1,0.748,0.482,0.282,0.175,0.112,0.058,0.023],'-v')
###################################################
#print Xaxis
plt.tight_layout()
plt.savefig("Figures/Extinction_2.png")    
plt.show()