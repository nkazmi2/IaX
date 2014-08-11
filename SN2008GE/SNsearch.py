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

x1 = 1000
y1 = 1000
cent1 = 3399.0 # 3400.0 #3399.971 
cent2 = 3371.0 #3371.539 #
 
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
    
    #fits.writeto(f[:-13]   + "test8.fits", combo, header, clobber=True)
    
    #test1 is code as is
    #test2 is:        quadI   = np.reshape(scidata[cent1-1:cent1+x1-1,cent2-1:cent2+y1-1], (x1,y1) )
       # quadII  = np.flipud( np.reshape(scidata[cent1-x1-1:cent1-1,cent2-1:cent2+y1-1], (x1,y1) ) )
       # quadIII = np.flipud( np.fliplr( np.reshape(scidata[cent1-x1-1:cent1-1,cent2-y1-1:cent2-1], (x1,y1) ) ) )
       # quadIV  = np.fliplr( np.reshape(scidata[cent1-1:cent1+x1-1,cent2-y1-1:cent2-1], (x1,y1) ) ) 

    #############################################################
 
    mean = np.mean(combo[cent1-150:cent1+150,cent2-150:cent2+150])
    standme = [] 
    Xaxis = combo[cent1,cent2-150:cent2+150]
    Yaxis = combo[cent1-150:cent1+150,cent2]
    print len(Xaxis)
    print len(Yaxis)
    #for a in range(301):
    #    for b in range(301): 
    #      standme.append(np.sqrt(float((1/100.0)*(combo[cent1-150+a][cent2-150+b] - mean)**2)))
    bar = (float((1/100.0)*(combo[cent1,cent2-150:cent2+150] - mean)**2))
    print len(bar)       
    #column = np.sqrt(float((1/100.0)*(combo[cent1,cent2-150:cent2+150] - mean)**2))
    #standme = np.matrix(np.reshape(standme, (301,301)))
    #plt.scatter(Xaxis,standme)
    #plt.show()
    """
    print "Looking at standard dev"
    
    cent1 = 3400.00 
    cent2 = 3371.00
    
    #intens = np.reshape(combo[cent1-150:cent1+150,cent2-150:cent2+150], (300,300) )
    #meanss = np.mean(intens)
    #print meanss
    mean = np.mean(combo[cent1-150:cent1+150,cent2-150:cent2+150])
    
    #one = []
    #two = []
    #the = []
    #fou = []
    #tots = []
    for a in range(301):
        for b in range(301):
            tots = np.mean(combo[cent1-150+a][cent2-150+b])
            #one = np.mean(combo[cent1+a][cent2+b])
            #two = np.mean(combo[cent1-a][cent2+b])
            #the = np.mean(combo[cent1-a][cent2-b])
            #fou = np.mean(combo[cent1+a][cent2-b])
    #print one, two, the, fou
    #print tots

    #dip = []
    #ole = []
    #bo  = []
    #ox  = []
    #reg = []
    #ion = []
    standev = []
    standme = []
    for a in range(301):
        for b in range(301): 
            standev.append(np.sqrt(float((1/100.0)*(combo[cent1-150+a][cent2-150+b] - tots)**2)))
            standme.append(np.sqrt(float((1/100.0)*(combo[cent1-150+a][cent2-150+b] - mean)**2)))
            #box.append(HMM)            
            #dip.append(np.sqrt((1/100)*(combo[cent1-a][cent2+b]-two)**2))
            #ole.append(np.sqrt((1/100)*(combo[cent1+a][cent2-b]-fou)**2))
            #reg.append(np.sqrt((1/100)*(combo[cent1+a][cent2+b]-one)**2))
            #ion.append(np.sqrt((1/100)*(combo[cent1-a][cent2-b]-the)**2))
    #print standev
    #np.savetxt("StDev.txt", np.c_[dip,ole,reg,ion],fmt = "%1.4f")
    standev = np.matrix(np.reshape(standev, (301,301)))
    standme = np.matrix(np.reshape(standme, (301,301)))
    np.savetxt("StDevMean1.txt", standev,fmt = "%1.4f")
    np.savetxt("StDevMean2.txt", standme,fmt = "%1.4f")
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

    title    =  ['sn2008ge_f814w_lacosmic.fits']
    #['sn2008ge_f435w_lacosmic.fits','sn2008ge_f555w_lacosmic.fits',
    #             'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']

   #
  
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
        #if (title[m] == 'sn2008ge_f814w_lacosmic.fits'):
        #    cent1 = 3399.0
        #    cent2 = 3371.0
        #else:
        #    cent1 = 3399.0 #3399.971 #3400.000 #
        #    cent2 = 3371.0 #3371.539 #3371.000 #
        
        print "Center Point: (", cent1, ', ' , cent2 ,")"
        #quad1 = []
        #quad2 = []
        #quad3 = []
        #quad4 = []
        quadI   = np.reshape(scidata[cent1+1:cent1+x1+1,cent2+1:cent2+y1+1], (x1,y1) )
        quadII  = np.flipud( np.reshape(scidata[cent1-x1-1:cent1-1,cent2+1:cent2+y1+1], (x1,y1) ) )
        quadIII = np.flipud( np.fliplr( np.reshape(scidata[cent1-x1-1:cent1-1,cent2-y1-1:cent2-1], (x1,y1) ) ) )
        quadIV  = np.fliplr( np.reshape(scidata[cent1+1:cent1+x1+1,cent2-y1-1:cent2-1], (x1,y1) ) ) 

        #np.savetxt("HIII0.txt", scidata[3385:3415, 3355:3385],fmt = "%1.4f")
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
        """
        #scidata = np.asmatrix(scidata)
        #print "Shape   ", np.shape(scidata)
        
        #print scidata[cent1][cent2] 
        #scidata[cent1][cent2] = 0
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
        bx = []
        dx = []
        ax = []
        cx = []
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
        """
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
        #top   = np.hstack([quadII, quadI])    
        #bot   = np.hstack([quadIII, quadIV])
        top   = np.hstack([quad2, quad1])    
        bot   = np.hstack([quad3, quad4])
        box   = np.vstack((bot,top))
    
        for t in range(x1*2):
            for u in range(y1*2):  
                combo[cent1-x1+t,cent2-y1+u]= box[t,u] 
        ###################################################
        ################ Save the images ##################
        ###################################################
        print "Begin saving figure..."
        savefig(title[m],box,combo,head)

#newCoord()  
main()       