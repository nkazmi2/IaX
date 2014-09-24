# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 16:06:33 2014

@author: Nova
"""
import pyfits
#from astropy.io import fits

def tofits(filename, data, hdr=None,clobber=False):

        """simple pyfits wrapper to make saving fits files easier."""
        from pyfits import PrimaryHDU,HDUList

        hdu = PrimaryHDU(data.astype('i'))

        if not hdr is None: hdu.header = hdr

        hdulist = HDUList([hdu])

        hdulist.writeto(filename, clobber=clobber,output_verify='ignore')

title    =  ['sn2008ge_f435w_lacosmic.fits','sn2008ge_f555w_lacosmic.fits',
             'sn2008ge_f625w_lacosmic.fits', 'sn2008ge_f814w_lacosmic.fits']

for m in range(4):
    hdu = pyfits.open(title[m])

    mask = hdu[0].data == 0
    name = title[m][:-14] + '.bpm.fits'

    tofits(name, mask)
