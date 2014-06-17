# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:34:33 2014

@author: Nova
"""
from scipy import stats
from astropy.io import fits
import numpy as np
import Image
#import fitsread
import ds9

x = np.arange(-3, 3, 0.1)
xx, yy = np.meshgrid(x, x)
gauss2d = stats.norm.pdf(xx) * stats.norm.pdf(yy)

d = ds9.ds9()

d.set_np2arr(gauss2d)

d.set('zoom to fit')

d.set('cmap bb')
d.set('scale log')

print d.get('scale')
#'sn2008ge_f555w_lacosmic.fits'
#'sn2008ge_f625w_lacosmic.fits'
#'sn2008ge_f814w_lacosmic.fits'
"""
image = fits.open('sn2008ge_f435w_lacosmic.fits',mode='copyonwrite', memmap=True)

print image.info()

#print image[0].header['targname'] # SN-2008GE

scidata = image[1].data
"""
"""
#data = []
#data = np.array(data)
filename = 'sn2008ge_f435w_lacosmic.fits'
data = fitsread(filename)
print data
"""
"""
scidata = image[1].data  # assume the first extension is an image
print scidata[1,4] 
print scidata.shape
"""