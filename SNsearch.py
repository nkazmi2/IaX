# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""

from astropy.io import fits
import numpy as np

#'sn2008ge_f555w_lacosmic.fits'
#'sn2008ge_f625w_lacosmic.fits'
#'sn2008ge_f814w_lacosmic.fits'

image = fits.open('sn2008ge_f435w_lacosmic.fits',mode='copyonwrite', memmap=True)

#print image.info()
header = image.info() # I think this is the header
scidata = image[0].data # scidata is the image, pixel is a location
#print np.shape(scidata)
cent = scidata[3356][3381] # what I chose to be center

bx = []
dx = []
for i in range(200):
    for j in range(200):
            bx.append(scidata[3356-i][3381+j])
            dx.append(scidata[3356+i][3381-j])
b = np.reshape(bx, (200,200))

"""
for i in range(330):
    for j in range(330):
            dx.append(scidata[3382+i][3409-j])
"""
d = np.reshape(dx, (200,200))
block2 = b - d
block4 = d - b
####################################################
ax = []
cx = []
for i in range(175):
    for j in range(110):
            ax.append(scidata[3356+i][3381+j])
            cx.append(scidata[3356-i][3381-j])
a = np.reshape(ax, (175,110))

"""
for i in range(175):
    for j in range(110):
            cx.append(scidata[3382-i][3409-j])
"""
c = np.reshape(cx, (175,110))

block1 = a - c
block3 = c - a

fits.writeto("tos1.fits", block1, header)
fits.writeto("tos2.fits", block2, header)
fits.writeto("tos3.fits", block3, header)
fits.writeto("tos4.fits", block4, header)