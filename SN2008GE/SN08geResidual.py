# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""

from astropy.io import fits
import numpy as np

#################################################################
######################## Coordinates ############################
#################################################################         
    
def main():
    #######################################################
    ################## File Names #########################
    #######################################################

    title    =  ['sn2008ge_f435w_lacosmic.fits','sn2008ge_f555w_lacosmic.fits',
                 'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']

    #######################################################
    ################### Main Code #########################
    #######################################################
    for m in range(len(title)):
        scidata  = []
        combo    = []
        
        print "Opening " + title[m]
        ###FIX COORDINATES!!!!

        image = fits.open("New_sn2008ge/" + title[m], mode='copyonwrite', memmap=True)

        head  = image[0].header #info() 

        scidata = image[0].data # takes fits file data and puts it into an array
        
        combo = np.array(scidata)   

        print "Establishing quadrants..."
        ## X and Y refer to the position of the values in the array [X,Y]
        ## not the actual pixel coordinates, xpix and ypix
        ## The larger dimension is run first, so what's actually the ypix
        ## is run first. 
        cen1 = 3388
        cen2 = 3372
        # next 20141015_lacosmic.fits files        
        #cen1 = 3387
        #cen2 = 3375
        # first set of lacosmic.fits files
        #cen1 = 3399
        #cen2 = 3371
        halfx = 0
        halfy = 1
        
        n_pix = 1000
    
        subx1 = cen1 - n_pix #- 1
        subx2 = cen1 #- 1
    
        suby1 = cen2 - n_pix #- 1
        suby2 = cen2 #- 1
    
        subx3 = cen1 + halfx #- 1
        subx4 = cen1 + halfx + n_pix #- 1
    
        suby3 = cen2 + halfy #- 1
        suby4 = cen2 + halfy + n_pix #- 1
        
        print "Center Point: (", cen2 , ', ' , cen1  ,")"
        print "Pixel Shift : (", halfx, ', ' , halfy ,")"
        
        quadI    = np.reshape(scidata[subx3:subx4,suby3:suby4], (subx4-subx3,suby4-suby3) ) 
        quadII   = np.flipud( np.reshape(scidata[subx1:subx2,suby3:suby4], (subx2-subx1,suby4-suby3) ) )
        quadIII  = np.flipud( np.fliplr( np.reshape(scidata[subx1:subx2,suby1:suby2], (subx2-subx1,suby2-suby1) ) ) )
        quadIV   = np.fliplr( np.reshape(scidata[subx3:subx4,suby1:suby2], (subx4-subx3,suby2-suby1) ) )
 
        ###################################################
        ################ Subtraction Time #################
        ###################################################

        print "Begin subtraction process..."
        quad1 = np.matrix( quadI   - quadIII )

        quad2 = np.matrix( quadIV  - quadII  )
        quad2 = np.fliplr(quad2)
    
        quad3 = np.matrix( quadIII - quadI   ) 
        quad3 = np.fliplr(np.flipud(quad3))
                        
        quad4 = np.matrix( quadII  - quadIV  )
        quad4 = np.flipud(quad4)
                
        print "Standard Deviation : ", np.std([quad1,quad2,quad3,quad4])

        print "Calculation complete..."
        ###################################################
        ############### Combine the images ################
        ###################################################
        print "Combining pieces..."
        combo[subx3:subx4,suby3:suby4] = quad1 
        combo[subx3:subx4,suby1:suby2] = quad2
        combo[subx1:subx2,suby1:suby2] = quad3
        combo[subx1:subx2,suby3:suby4] = quad4
          
        #combo[subx3-1:subx4-1,suby3-1:suby4-1] = quad1 
        #combo[subx3-1:subx4-1,suby1+1:suby2+1] = quad2
        #combo[subx1+1:subx2+1,suby1+1:suby2+1] = quad3
        #combo[subx1+1:subx2+1,suby3-1:suby4-1] = quad4
        

        if (halfx == 1):
            combo[cen1,suby1:suby4] = 0
        if (halfy == 1):
            combo[subx1:subx4,cen2] = 0
            
        ###################################################
        ################ Save the images ##################
        ###################################################
        print "Begin saving figure..."
        
        plotname  = title[m][:-14]   + "_residual.fits"
        plotname2 = title[m][:-14]   + "_box.fits"
        fits.writeto('sn2008ge/' + plotname , combo, head, clobber=True)
        #fits.writeto(plotname2,combo[cen1-500:cen1+500,cen2-500:cen2+500], head, clobber=True)
        print "Plotting " + plotname + " & " + plotname2
        
main()       