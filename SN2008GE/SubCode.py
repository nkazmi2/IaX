# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 22:45:44 2014

@author: Nova
"""


from astropy.io import fits
import numpy as np
#from numpy.linalg import inv
#import Image as pil
#import os
#import matplotlib.pyplot as plt

def main():
    #######################################################
    ################## File Names #########################
    #######################################################

    title    =  ['sn2008ge_f814w_lacosmic.fits']
    #['sn2008ge_f435w_lacosmic.fits','sn2008ge_f555w_lacosmic.fits',
    #             'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']
    x1 = 1000
    y1 = 1000
    ceny = 3371
    cenx = 3399

    halfx = 0
    halfy = 1

    n_pix = 1000
    
    subx1 = cenx - n_pix
    subx2 = cenx - 1
    
    suby1 = ceny - n_pix
    suby2 = ceny - 1
    
    subx3 = cenx + halfx
    subx4 = cenx + halfx + n_pix - 1
    
    suby3 = ceny + halfy

    suby4 = ceny + halfy + n_pix - 1
    
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
        print "Center Point: (", cenx, ', ' , ceny ,")"
        
        #box11 = np.reshape(scidata[subx1:subx2,suby1:suby2], (x1,y1) )
        #box12 = np.reshape(scidata[subx1:subx2,suby3:suby4], (x1,y1) )
        #box21 = np.reshape(scidata[subx3:subx4,suby1:suby2], (x1,y1) )
        #box22 = np.reshape(scidata[subx3:subx4,suby3:suby4], (x1,y1) )
      
        #quadII   = np.reshape(scidata[subx1:subx2,suby1:suby2], (x1-1,y1-1) )
        #quadI    = np.flipud( np.reshape(scidata[subx1:subx2,suby3:suby4], (x1-1,y1-1) ) )
        #quadIV   = np.flipud( np.fliplr( np.reshape(scidata[subx3:subx4,suby1:suby2], (x1-1,y1-1) ) ) )
        #quadIII  = np.fliplr( np.reshape(scidata[subx3:subx4,suby3:suby4], (x1-1,y1-1) ) )        

        quadI    = np.reshape(scidata[subx3:subx4,suby3:suby4], (x1-1,y1-1) ) 
        quadII   = np.flipud( np.reshape(scidata[subx1:subx2,suby3:suby4], (x1-1,y1-1) ) )
        quadIII  = np.flipud( np.fliplr( np.reshape(scidata[subx1:subx2,suby1:suby2], (x1-1,y1-1) ) ) )
        quadIV   = np.fliplr( np.reshape(scidata[subx3:subx4,suby1:suby2], (x1-1,y1-1) ) )

        print "Begin subtraction process..."   
        quad1 = []
        quad2 = []
        quad3 = []
        quad4 = []         
        """
        for t in range(x1-1):
            for u in range(y1-1):
                quad1 = np.matrix( quadI   - quadIII ) 
                quad2 = np.matrix( quadIV  - quadII  )
                quad3 = np.matrix( quadIII - quadI   ) 
                quad4 = np.matrix( quadII  - quadIV  ) 
        """       
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
                
        if (halfx == 1):
            combo[cenx,suby1:suby4] = 0
        if (halfy == 1):
            combo[subx1:subx4,ceny] = 0
        ###################################################
        ################ Save the images ##################
        ###################################################
        print "Begin saving figure..."    
        plotname = title[m][:-13]   + "subtest_02.fits"
        fits.writeto(plotname, combo, head, clobber=True)
        print "Plotting " + plotname

    
main()       