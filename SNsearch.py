# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""

from astropy.io import fits
import numpy as np
#from numpy.linalg import inv
import Image as pil
import os

######################## Functions ##############################

def savefig(f,quadrant):
    for k in range(len(quadrant)):
        fits.writeto(f[:-13] + "quad_" + str(k+1) + ".fits", quadrant[k] , clobber=True)

###################### Variable ################################

title = ['sn2008ge_f435w_lacosmic.fits', 'sn2008ge_f555w_lacosmic.fits', 
         'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']

###################### Main Code ###############################  

for m in range(len(title)):
    bx = []
    dx = []
    ax = []
    cx = []
    quadrant = []
    
    image = fits.open(title[m], mode='copyonwrite', memmap=True)
    
    name    = image[0].header['targname']
    header  = image.info() 
    scidata = image[0].data 
    #scidata = np.asmatrix(scidata)

    ############### Crop and subtract ###############
    x1 = 150
    y1 = 200
    x2 = 110
    y2 = 175
    for n in range(x1):
        for p in range(y1):   
             bx.append(scidata[3370-n][3400+p])
             dx.append(scidata[3370+n][3400-p])
    for i in range(x2):
        for j in range(y2):
            ax.append(scidata[3370+i][3400+j])
            cx.append(scidata[3370-i][3400-j])  

    b = np.reshape( bx , (x1,y1) )
    d = np.reshape( dx , (x1,y1) )          
    a = np.reshape( ax , (x2,y2) )
    c = np.reshape( cx , (x2,y2) )

    quad2 = np.matrix( b - d )
    #quad2 = np.swapaxes(quad2,0,1)
    quad2 = np.fliplr(quad2)
    
    quad4 = np.matrix( d - b )
    quad4 = np.fliplr(quad4)
    #quad4 = np.flipud(quad4)
    
    quad1 = np.matrix( a - c )
    
    quad3 = np.matrix( c - a ) 
    #quad3 = np.swapaxes(quad3,0,1)
    quad3 = np.fliplr(np.flipud(quad3))
 
    ############### Save the images ################
    quadrant = [quad1,quad2,quad3,quad4]
    savefig(title[m],quadrant)
    

###################### Coordinates ############################  
"""
take the original coordinates and convert them to the new fits file coord
rotate the fits files
"""