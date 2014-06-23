# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""

from astropy.io import fits
import numpy as np
#from numpy.linalg import inv
#import Image as pil
#import os
######################## Functions ##############################

def savefig(f,box,combo):
    #for k in range(len(quadrant)):
    #fits.writeto(f[:-13] + "quad_" + str(k+1) + ".fits", quadrant[k] , clobber=True)
    print "Creating file " + f[:-13] + "residual.fits"
    fits.writeto(f[:-13] + "residual.fits", box , clobber=True)   
    print "Creating file " + f[:-13] + "fullfig.fits"
    fits.writeto(f[:-13] + "fullfig.fits", combo , clobber=True)
    
        
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
    scidata  = []
    combo    = []
    
    image = fits.open(title[m], mode='copyonwrite', memmap=True)
    
    name    = image[0].header['targname']
    header  = image.info() 
    scidata = image[0].data 

    combo = np.array(scidata)
    #scidata = np.asmatrix(scidata)

    ############### Crop and subtract ###############
    x1 = 150
    y1 = 200
    x2 = 150
    y2 = 200
    for n in range(x1):
        for p in range(y1):   
            bx.append(scidata[3399.971-n][3371.539+p])
            dx.append(scidata[3399.971+n][3371.539-p])
    for i in range(x2):
        for j in range(y2):
            ax.append(scidata[3399.971+i][3371.539+j])
            cx.append(scidata[3399.971-i][3371.539-j])  

    b     = np.reshape( bx , (x1,y1) )
    d     = np.reshape( dx , (x1,y1) )
      
    a     = np.reshape( ax , (x2,y2) )
    c     = np.reshape( cx , (x2,y2) )
        
    quad1 = np.matrix( a - c )
    
    quad2 = np.matrix( d - b )
    quad2 = np.fliplr(quad2)
    
    quad3 = np.matrix( c - a ) 
    quad3 = np.fliplr(np.flipud(quad3))
    
    quad4 = np.matrix( b - d )
    quad4 = np.flipud(quad4)
    
    ############## Combine the images ##############   
    
    top   = np.hstack([quad2, quad1])    
    bot   = np.hstack([quad3, quad4])
    box   = np.vstack((bot,top))
    
    for t in range(x1*2):
        for u in range(y1*2):  
            combo[3249.971+t][3171.539+u] = box[t,u]

    ############### Save the images ################


    savefig(title[m],box,combo)
    
        #quadrant = [quad1,quad2,quad3,quad4] 
    #quadrant = np.arange((quad2+quad1),(400,300))
    #savefig(title[m],quadrant)
    
    #box   = np.array(box)
    #where = np.where((scidata[3299:3599][3171:3571]) )
    #print box[1,5]
    #print image[3299][3171] 
    #print box[0][0]
    #image[3299][3171] = box[0][0]
    #print image[3299][3171] 
            #image[3171+t][3299+u] = box[t,u]
            #,casting='equiv',where = where)
            #[3299+t][3171+u]  :3599  :3571
    #allcombo = np.matrix( image )
    #fits.writeto("all2.fits", combo , clobber=True)
    
    ###################### Coordinates ############################  
"""
    for t in range(x1*2):
        for u in range(y1*2):  
            #image[3171+t][3299+u] = box[t,u]
            image[3399.971-t][3371.539+u] = quad2[t,u]
take the original coordinates and convert them to the new fits file coord
rotate the fits files
"""