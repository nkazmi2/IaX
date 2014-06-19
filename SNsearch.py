# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""

from astropy.io import fits
import numpy as np
import os

######################## Functions ##############################

def savefig(f,quadrant):
    for k in range(len(quadrant)):
        if (os.path.isfile(f[:-13] + str(k+1) + ".fits") == True ):
            os.remove(f[:-13] + str(k+1) + ".fits")
        elif (os.path.isfile(f[:-13] + str(k+1) + ".fits") == False ): 
            fits.writeto(f[:-13] + str(k+1) + ".fits", quadrant[k])

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
    
    image = fits.open(title[m],mode='copyonwrite', memmap=True)
    
    name = image[0].header['targname']
    header = image.info() 
    scidata = image[0].data 

    ############### Crop and subtract ###############
    for n in range(150):
        for p in range(200):   
             bx.append(scidata[3370-n][3400+p])
             dx.append(scidata[3370+n][3400-p])
    for i in range(110):
        for j in range(175):
            ax.append(scidata[3370+i][3400+j])
            cx.append(scidata[3370-i][3400-j])  

    b = np.reshape( bx , (150,200) )
    d = np.reshape( dx , (150,200) )          
    a = np.reshape( ax , (110,175) )
    c = np.reshape( cx , (110,175) )

    quad2 = b - d
    quad4 = d - b
    
    quad1 = a - c
    quad3 = c - a
    
    ############### Save the images ################
    quadrant = [quad1,quad2,quad3,quad4]
    savefig(title[m],quadrant)
    

"""
print image.info()
header = image.info() # I think this is the header
scidata = image[0].data # scidata is the image, pixel is a location
print np.shape(scidata)
cent = scidata[3356][3381] # what I chose to be center

for i in range(150):
    for j in range(200):
            bx.append(scidata[3370-i][3400+j])
            dx.append(scidata[3370+i][3400-j])
for i in range(110):
    for j in range(175):
            ax.append(scidata[3370+i][3400+j])
            cx.append(scidata[3370-i][3400-j])           
            
b = np.reshape(bx, (150,200))
d = np.reshape(dx, (150,200))
a = np.reshape(ax, (110,175))
c = np.reshape(cx, (110,175))

quad2 = b - d
quad4 = d - b
quad1 = a - c
quad3 = c - a

quadrant = [quad1,quad2,quad3,quad4]
savefig(f,quadrant)

if (os.path.isfile(f[:-13] + "1.fits") == True ):
    os.remove(f[:-13] + "1.fits")
elif (os.path.isfile(f[:-13] + "1.fits") == False ): 
    fits.writeto(f[:-13] + "1.fits", quad1)
    
if (os.path.isfile(f[:-13] + "2.fits") == True ):
    os.remove(f[:-13] + "2.fits")
elif (os.path.isfile(f[:-13] + "1.fits") == False ): 
    fits.writeto(f[:-13] + "2.fits", quad2)
    
if (os.path.isfile(f[:-13] + "3.fits") == True ):
    os.remove(f[:-13] + "3.fits")
elif (os.path.isfile(f[:-13] + "1.fits") == False ):    
    fits.writeto(f[:-13] + "3.fits", quad3)
    
if (os.path.isfile(f[:-13] + "4.fits") == True ):
    os.remove(f[:-13] + "4.fits")
elif (os.path.isfile(f[:-13] + "1.fits") == False ): 
    fits.writeto(f[:-13] + "4.fits", quad4)
"""