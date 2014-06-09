# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:14:02 2014

@author: Nova

Read in the data, check which columns are which
"""

f = open('sn2010el_new.phot.columns','r')
info = f.read()
f.close()
print info
