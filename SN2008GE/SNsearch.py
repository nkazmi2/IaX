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
from numpy.linalg import inv
import Image as pil
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

cenx = 3399
ceny = 3371
        
#cenx = 3399.500 #3399.971 #3400.000 #
#ceny = 3371.500 #3371.539 #3371.000 #
#################################################################
######################## Functions ##############################
#################################################################
######################## Save Fits ##############################
#################################################################
def StandDev(f,combo,header):  
    print "Figuring out how to do calculations with a .fits file"
    #combo (5200L, 5200L)
    #mean = np.mean(combo[cenx-150:cenx+150,ceny-150:ceny+150]) #(300L, 300L)
    #print mean
    
    box = []
    box = np.matrix(combo[cenx-150:cenx+150,ceny-150:ceny+150])
    #print np.shape(box)
    #print 
    #print np.std(box, axis=1)
    Xaxis = []
    Yaxis = []
    Xaxis = np.std(box, axis=0)
    print Xaxis
    Yaxis = np.std(box, axis=1)
    print Yaxis
    #plt.scatter()
    #plt.show()
    
    """
    fig = plt.figure(figsize=(10,10))
    ax = Axes3D(fig)

    z = np.linspace(0, 1, 300)
    x = np.std(box, axis=0)
    y = np.std(box, axis=1)
    
    #c = x + y
    
    ax.scatter(x, y, z)#, c=c)
    """
#################################################################
######################## Coordinates ############################
#################################################################         
    
def main():
    #######################################################
    ################## File Names #########################
    #######################################################

    title    =      [ 'sn2008ge_f435w_lacosmic.fits','sn2008ge_f555w_lacosmic.fits',
                  'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']
    # ['sn2008ge_f814w_lacosmic.fits']

    #######################################################
    ################### Main Code #########################
    #######################################################
    for m in range(len(title)):
        scidata  = []
        combo    = []
        print "Opening " + title[m]

        image = fits.open(title[m], mode='copyonwrite', memmap=True)

        #name    = image[0].header['targname']
        head  = image[0].header #info() 

        scidata = image[0].data # takes fits file data and puts it into an array
        
        combo = np.array(scidata) # do I even use this? YES! -.-       

        print "Establishing quadrants..."
        
        halfx = 1
        halfy = 1
        x1    = 1000
        y1    = 1000
        n_pix = 1000
    
        subx1 = cenx - n_pix
        subx2 = cenx - 1
    
        suby1 = ceny - n_pix
        suby2 = ceny - 1
    
        subx3 = cenx + halfx
        subx4 = cenx + halfx + n_pix - 1
    
        suby3 = ceny + halfy

        suby4 = ceny + halfy + n_pix - 1
        print "Center Point: (", cenx, ', ' , ceny ,")"
        
        quadI    = np.reshape(scidata[subx3:subx4,suby3:suby4], (x1-1,y1-1) ) 
        quadII   = np.flipud( np.reshape(scidata[subx1:subx2,suby3:suby4], (x1-1,y1-1) ) )
        quadIII  = np.flipud( np.fliplr( np.reshape(scidata[subx1:subx2,suby1:suby2], (x1-1,y1-1) ) ) )
        quadIV   = np.fliplr( np.reshape(scidata[subx3:subx4,suby1:suby2], (x1-1,y1-1) ) )

        ####SAVE quadI   = np.reshape(scidata[cent1+1:cent1+n_pix+1,cent2+1:cent2+n_pix+1], (n_pix,n_pix) )
        ####SAVE quadII  = np.flipud( np.reshape(scidata[cent1-n_pix-1:cent1-1,cent2+1:cent2+n_pix+1], (n_pix,n_pix) ) )
        ####SAVE quadIII = np.flipud( np.fliplr( np.reshape(scidata[cent1-n_pix-1:cent1-1,cent2-n_pix-1:cent2-1], (n_pix,n_pix) ) ) )
        ####SAVE quadIV  = np.fliplr( np.reshape(scidata[cent1+1:cent1+n_pix+1,cent2-n_pix-1:cent2-1], (n_pix,n_pix) ) ) 

        ###################################################
        ############### Crop and subtract #################
        ###################################################

        print "Begin subtraction process..."
        quad1 = np.matrix( quadI   - quadIII )

        quad2 = np.matrix( quadIV  - quadII  )
        quad2 = np.fliplr(quad2)
    
        quad3 = np.matrix( quadIII - quadI   ) 
        quad3 = np.fliplr(np.flipud(quad3))
                        
        quad4 = np.matrix( quadII  - quadIV  )
        quad4 = np.flipud(quad4)
        
        print "Calculation complete..."
        ###################################################
        ############### Combine the images ################
        ###################################################
        print "Combining pieces..."
        top   = np.hstack([quad2, quad1])    
        bot   = np.hstack([quad3, quad4])
        box   = np.vstack((bot,top))
    
        for t in range((x1*2)-2):
            for u in range((y1*2)-2): 
                combo[cenx-x1+t,ceny-y1+u]= box[t,u] 

        subx1 = cenx - 1000
        suby1 = ceny - 1000
        
        subx4 = cenx + 1000 #- 1
        suby4 = ceny + 1000 #- 1

        #if (halfx != 0):
        #    combo[cenx,suby1:suby4] = 0
        #if (halfy != 0):
        #    combo[subx1:subx4,ceny] = 0
        ###################################################
        ################ Save the images ##################
        ###################################################
        print "Begin saving figure..."
        
        plotname = title[m][:-13]   + "nocolumnrow.fits"
        fits.writeto(plotname, combo, head, clobber=True)
        print "Plotting " + plotname
        
        #StandDev(title[m],combo,head)
main()       