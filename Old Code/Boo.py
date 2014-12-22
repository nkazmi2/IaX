# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 13:51:48 2014

@author: Nova
"""

import numpy               as np
import matplotlib.pyplot   as plt

c1plt = plt.subplot2grid((1,1), (0,0), rowspan = 2)
plt.gca().invert_yaxis()
name = "Z01576Y26.dat"
d = []
d.append(np.loadtxt('../Metallicity/'+name))
d = np.array(d)

#print d
#print np.shape(d) #(1L, 16776L, 21L)

logAGE = []
F435W  = []
F555W  = []
F625W  = []
F814W  = []

logAGE = d[:,:,0]
F435W  = d[:,:,7]
F555W  = d[:,:,10]
F625W  = d[:,:,12]
F814W  = d[:,:,16]

age70   = np.where((logAGE == 7.0))
age71   = np.where((logAGE == 7.1))
age711  = np.where((logAGE == 7.11))
age712  = np.where((logAGE == 7.12))
age713  = np.where((logAGE == 7.13))
age714  = np.where((logAGE == 7.14))
age715  = np.where((logAGE == 7.15))
age716  = np.where((logAGE == 7.16))
age717  = np.where((logAGE == 7.17))
age718  = np.where((logAGE == 7.18))
age719  = np.where((logAGE == 7.19))
age72   = np.where((logAGE == 7.2))
age721  = np.where((logAGE == 7.21))
age722  = np.where((logAGE == 7.22))
age723  = np.where((logAGE == 7.23))
age724  = np.where((logAGE == 7.24))
age725  = np.where((logAGE == 7.25))
age726  = np.where((logAGE == 7.26))
age727  = np.where((logAGE == 7.27))
age728  = np.where((logAGE == 7.28))
age729  = np.where((logAGE == 7.98))
age73   = np.where((logAGE == 7.3))
age731  = np.where((logAGE == 7.31))
age732  = np.where((logAGE == 7.32))
age733  = np.where((logAGE == 7.33))
age734  = np.where((logAGE == 7.34))
age735  = np.where((logAGE == 7.35))
age736  = np.where((logAGE == 7.36))
age737  = np.where((logAGE == 7.37))
age738  = np.where((logAGE == 7.38))
age739   = np.where((logAGE == 7.39))
age74   = np.where((logAGE == 7.4))
age741  = np.where((logAGE == 7.41))
age742  = np.where((logAGE == 7.42))
age743  = np.where((logAGE == 7.43))
age744  = np.where((logAGE == 7.44))
age745  = np.where((logAGE == 7.45))
age746  = np.where((logAGE == 7.46))
age747  = np.where((logAGE == 7.47))
age748  = np.where((logAGE == 7.48))
age749  = np.where((logAGE == 7.49))
age75   = np.where((logAGE == 7.5))
age751  = np.where((logAGE == 7.51))
age752  = np.where((logAGE == 7.52))
age753  = np.where((logAGE == 7.53))
age754  = np.where((logAGE == 7.54))
age755  = np.where((logAGE == 7.55))
age756  = np.where((logAGE == 7.56))
age757  = np.where((logAGE == 7.57))
age758  = np.where((logAGE == 7.58))
age759  = np.where((logAGE == 7.59))
age76   = np.where((logAGE == 7.6))
age765  = np.where((logAGE == 7.65))
age77   = np.where((logAGE == 7.7))
age771  = np.where((logAGE == 7.71))
age772  = np.where((logAGE == 7.72))
age773  = np.where((logAGE == 7.73))
age774  = np.where((logAGE == 7.74))
age775  = np.where((logAGE == 7.75))
age776  = np.where((logAGE == 7.76))
age777  = np.where((logAGE == 7.77))
age778  = np.where((logAGE == 7.78))
age78  = np.where((logAGE == 7.8))
age781  = np.where((logAGE == 7.81))
age782  = np.where((logAGE == 7.82))
age783  = np.where((logAGE == 7.83))
age784  = np.where((logAGE == 7.84))
age785  = np.where((logAGE == 7.85))
age786  = np.where((logAGE == 7.86))
age787  = np.where((logAGE == 7.87))
age788  = np.where((logAGE == 7.88))
age789  = np.where((logAGE == 7.89))
age79   = np.where((logAGE == 7.9))   
age80   = np.where((logAGE == 8.0))      


plt.annotate('', xy=(.9, -5.217), xycoords = 'data',
                 xytext = (1.638, -2.7), textcoords = 'data',
                    arrowprops = {'arrowstyle':'->'})
plt.annotate('A${_v}}$ = 3.4105', xy=(0.2,-5.2), xycoords = 'data',
                 xytext = (2, 3), textcoords = 'offset points')
c1plt.plot(np.subtract(F435W[age783], F555W[age783]), F555W[age783],  
        'g--', label = 'Age = 10$^{7.83}$ yrs')
c1plt.plot(np.subtract(F435W[age784], F555W[age784]), F555W[age784],  
        'b--' , label = 'Age = 10$^{7.84}$ yrs')
c1plt.plot(np.subtract(F435W[age785], F555W[age785]), F555W[age785],  
        'm--' , label = 'Age = 10$^{7.85}$ yrs')
c1plt.plot(np.subtract(F435W[age786], F555W[age786]), F555W[age786],  
        'r--' , label = 'Age = 10$^{7.86}$ yrs')
c1plt.plot(np.subtract(F435W[age787], F555W[age787]), F555W[age787],  
           'k--' , label = 'Age = 10$^{7.87}$ yrs')
c1plt.plot(np.subtract(F435W[age788], F555W[age788]), F555W[age788],  
         'g--', label = 'Age = 10$^{7.88}$ yrs')
c1plt.plot(np.subtract(F435W[age789], F555W[age789]), F555W[age789],  
         'b--' , label = 'Age = 10$^{7.89}$ yrs')
c1plt.plot(np.subtract(F435W[age79], F555W[age79]), F555W[age79],  
         'm--' , label = 'Age = 10$^{7.9}$ yrs')
c1plt.plot(np.subtract(F435W[age70],  F555W[age70]),  F555W[age70],  
        'r--', label = 'Age = 10$^{7.0}$ yrs')
c1plt.plot(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  
       'y-', label = 'Age = 10$^{7.1}$ yrs')
c1plt.plot(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  
       'g:', label = 'Age = 10$^{7.2}$ yrs')
c1plt.plot(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  
       'c-', label = 'Age = 10$^{7.3}$ yrs')
c1plt.plot(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  
       'b:' , label = 'Age = 10$^{7.4}$ yrs')
c1plt.plot(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  
       'c-.', label = 'Age = 10$^{7.5}$ yrs')
c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
       'r--', label = 'Age = 10$^{7.6}$ yrs') 
c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
      'y-' , label = 'Age = 10$^{7.7}$ yrs')
c1plt.plot(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  
      'g:' , label = 'Age = 10$^{7.8}$ yrs')
c1plt.plot(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  
       'r--', label = 'Age = 10$^{7.6}$ yrs') 
c1plt.plot(np.subtract(F435W[age785], F555W[age785]), F555W[age785],  
        'g--' , label = 'Age = 10$^{7.85}$ yrs')
c1plt.plot(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  
           'y-' , label = 'Age = 10$^{7.7}$ yrs')
c1plt.plot(np.subtract(F435W[age785], F555W[age785]), F555W[age785],  
          'r--' , label = 'Age = 10$^{7.85}$ yrs')
c1plt.plot(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  
           'c-.', label = 'Age = 10$^{7.9}$ yrs') 
c1plt.plot(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  
           'b:' , label = 'Age = 10$^{8.0}$ yrs')   
