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

x1 = 1000
y1 = 1000
x2 = 1000
y2 = 1000  
 
#cent1 = 3399.500 #3399.971 #3400.000 #
#cent2 = 3371.500 #3371.539 #3371.000 #
#################################################################
######################## Functions ##############################
#################################################################
######################## Save Fits ##############################
#################################################################
def savefig(f,box,combo,header):
    ##for k in range(len(quadrant)):
    ##fits.writeto(f[:-13] + "quad_" + str(k+1) + ".fits", quadrant[k] , clobber=True)
    #print "Creating file " + f[:-13] + "residual.fits"
    #fits.writeto(f[:-13]   + "residual.fits", box , header, clobber=True)   
    print "Creating file " + f[:-13] + "fullfig.fits"
    
    fits.writeto(f[:-13]   + "subtest_2.fits", combo, header, clobber=True)
    """    
    print "Looking at standard dev"
    
    cent1 = 3399.00 
    cent2 = 3371.00
    one = []
    two = []
    the = []
    fou = []
    for a in range(100):
        for b in range(100):
            one = np.mean(combo[cent1+a][cent2+b])
            two = np.mean(combo[cent1-a][cent2+b])
            the = np.mean(combo[cent1-a][cent2-b])
            fou = np.mean(combo[cent1+a][cent2-b])
    print one, two, the, fou
    dip = []
    ole = []
    bo  = []
    ox  = []
    reg = []
    ion = []
    for a in range(100):
        for b in range(100): 
            dip.append(np.sqrt((1/100)*(combo[cent1-a][cent2+b]-two)**2))
            ole.append(np.sqrt((1/100)*(combo[cent1+a][cent2-b]-fou)**2))
            reg.append(np.sqrt((1/100)*(combo[cent1+a][cent2+b]-one)**2))
            ion.append(np.sqrt((1/100)*(combo[cent1-a][cent2-b]-the)**2))
    np.savetxt("Lookat.txt", np.c_[dip,ole,reg,ion])
    """
#################################################################
######################## Coordinates ############################
#################################################################         
def newCoord():
    print "Opening coordinate files..."
    name = 'sn2008ge_all.txt'

    newxcoord = []
    newycoord = []
    data      = []
    circ      = []
    clos      = []
    comm      = []
    #x1 = 300
    #y1 = 350        
    cent1 = 3399.00 
    cent2 = 3371.00
    adj1  = cent2-y1
    adj2  = cent1-x1
    print "Adjusting coordinates..."
    data = np.loadtxt(name)
    
    #data = np.recfromcsv(filename, names=['a','a','a'])   
    for i in range(len(data)):
        newxcoord.append(data[i][0] - adj1)
        newycoord.append(data[i][1] - adj2)
        circ.append('circle(')
        comm.append(',')
        clos.append(',2)')

    np.savetxt('sn2008ge_newcoord_temp.reg', np.c_[circ,newxcoord,comm,newycoord,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=cyan dashlist=8 3 width=1'
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1' \
               '\nimage;' )
    print "Done with this bizz-nich"    # truely, I hope no ones reads my code
    
def main():
    #######################################################
    ################## File Names #########################
    #######################################################

    title    = ['sn2008ge_f814w_lacosmic.fits']
    #['sn2008ge_f435w_lacosmic.fits','sn2008ge_f555w_lacosmic.fits',
               # 'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']

    #######################################################
    ################### Main Code #########################
    #######################################################
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
        head  = image[0].header #info() 

        scidata = image[0].data 
        
        combo = np.array(scidata)
        
        if (title[m] == 'sn2008ge_f814w_lacosmic.fits'):
            cent1 = 3400.0
            cent2 = 3371.0
        else:
            cent1 = 3399.00 #3399.971 #3400.000 #
            cent2 = 3371.00 #3371.539 #3371.000 #

        """
        # Looking at only the center of the galaxy
        litt1 = 3400.00 - 300 
        litt2 = 3371.00 - 300
        bottotop = []
        toptobot = []
        for n in range(600):
            for p in range(600):   
                bottotop.append(scidata[litt1+n][litt2+p])
                toptobot.append(scidata[litt1+600-n][litt2+600-p])
                
        lay     = np.reshape( bottotop , (600,600) )
        ers     = np.reshape( toptobot , (600,600) )
        
        quad = np.flipud(np.fliplr(np.matrix( ers - lay )))
        lay = np.matrix(lay)
        ers = np.matrix(ers)
        
        fits.writeto("center.fits", quad, head, clobber=True)
        fits.writeto("quad2.fits" , lay , head, clobber=True)
        fits.writeto("quad4.fits" , ers , head, clobber=True)
        """
        #scidata = np.asmatrix(scidata)
        #print "Shape   ", np.shape(scidata)
        
        #print scidata[cent1][cent2] 
        scidata[cent1][cent2] = 0
        #print scidata[cent1][cent2] 
        #print "Center  ", scidata[cent1][cent2]
        #print "OrgCen  ", scidata[3400][3371.0]
        #print "OrgCen  ", scidata[3400][3372.0]
        #print np.max(scidata)
        
        #print scidata[np.where(scidata.argmax() == 10689040)]
        #from numpy import unravel_index
        #print unravel_index(scidata.argmax(), scidata.shape)
        ###################################################
        ############### Crop and subtract #################
        ###################################################

        print "Begin subtraction process..."
        print "Center Point: (", cent1, ', ' , cent2 ,")"
        for n in range(x1):
            for p in range(y1):   
                bx.append(scidata[cent1-n][cent2+p])
                dx.append(scidata[cent1+n][cent2-p])
                #bx.append(scidata[3400.000-n][3371.000+p])
                #dx.append(scidata[3400.000+n][3371.000-p])
                #bx.append(scidata[3399.971-n][3371.539+p])
                #dx.append(scidata[3399.971+n][3371.539-p])
        for i in range(x2):
            for j in range(y2):
                ax.append(scidata[cent1+i][cent2+j])
                cx.append(scidata[cent1-i][cent2-j])
                #ax.append(scidata[3399.971+i][3371.539+j])
                #cx.append(scidata[3399.971-i][3371.539-j])  
        
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
        ###################################################
        ############### Combine the images ################
        ###################################################
        print "Combining pieces..."
        top   = np.hstack([quad2, quad1])    
        bot   = np.hstack([quad3, quad4])
        box   = np.vstack((bot,top))
    
        for t in range(x1*2):
            for u in range(y1*2):  
                combo[cent1-x1+t][cent2-y1+u] = box[t,u] 
        ###################################################
        ################ Save the images ##################
        ###################################################
        print "Begin saving figure..."
        savefig(title[m],box,combo,head)

#newCoord()  
main()       