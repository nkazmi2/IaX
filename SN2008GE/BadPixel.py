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


hdu = pyfits.open('sn2008ge_f435w_lacosmic.fits')

mask = hdu[0].data == 0
tofits('sn2008ge_f435w.bpm.fits', mask)
