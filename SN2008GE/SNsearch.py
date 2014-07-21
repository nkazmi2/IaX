# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""
#################################################################
# The following code is used for sn2008ge specifically.
# This supernova is located near the bright center of a 
# galaxy. This code looks at the residual of the images 
# and ajusts the coordinates of the nearby sources.
#################################################################

from astropy.io import fits
import numpy as np
import csv
from itertools import izip
from numpy.linalg import inv
import Image as pil
import os
#################################################################
######################## Functions ##############################
#################################################################
######################## Save Fits ##############################
def savefig(f,box,combo,header):
    #for k in range(len(quadrant)):
    #fits.writeto(f[:-13] + "quad_" + str(k+1) + ".fits", quadrant[k] , clobber=True)
    print "Creating file " + f[:-13] + "residual.fits"
    fits.writeto(f[:-13]   + "residual.fits", box , header, clobber=True)   
    print "Creating file " + f[:-13] + "fullfig.fits"
    fits.writeto(f[:-13]   + "fullfig.fits", combo, header, clobber=True)
    
###################### Coordinates ############################         
def newCoord():
    print "Opening coordinate files..."
    name = 'sn2008ge_all.txt'

    newxcoord = []
    newycoord = []
    data      = []
    
    print "Adjusting coordinates..."
    data = np.loadtxt(name)

    #data = np.recfromcsv(filename, names=['a','a','a'])   
    for i in range(len(data)):
        newxcoord.append(data[i][0] - 3171.733)
        newycoord.append(data[i][1] - 3249.212)
    np.savetxt('sn2008ge_newcoord.txt', np.c_[newxcoord,newycoord],fmt = "%1.2f")
    print "Done with this bizz-nich"    # truely, I hope no ones reads my code
    
def main():
###################### File Names ##############################

    title    = ['sn2008ge_f435w_lacosmic.fits', 'sn2008ge_f555w_lacosmic.fits',
                'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']

###################### Main Code ###############################  

    for m in range(len(title)):
        bx = []
        dx = []
        ax = []
        cx = []
        scidata  = []
        combo    = []
        print "Opening " + title[m]
        image = fits.open(title[m], mode='copyonwrite', memmap=True)
        
        #name    = image[0].header['targname']
        header  = image.info() 
        scidata = image[0].data 
        
        combo = np.array(scidata)
        #scidata = np.asmatrix(scidata)
        
        ############### Crop and subtract ###############
        print "Begin subtraction process..."
        x1 = 150
        y1 = 250
        x2 = 150
        y2 = 250
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
        print "Calculation complete..."
        ############## Combine the images ##############   
        print "Combining pieces..."
        top   = np.hstack([quad2, quad1])    
        bot   = np.hstack([quad3, quad4])
        box   = np.vstack((bot,top))
    
        for t in range(x1*2):
            for u in range(y1*2):  
                combo[3249.971+t][3171.539+u] = box[t,u]

        ############### Save the images ################

        print "Saving figure..."
        savefig(title[m],box,combo,header)

newCoord()  
main()    
  
    


