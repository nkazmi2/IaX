# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 13:23:45 2014

@author: Nova
"""


import numpy as np
import pyregion

#start = pyregion.open('../SN2008GE/aftercut.reg')
#for i in xrange(len(start)):
    #print start[i].comment
    
np.savetxt('test.reg', 'circle(3000.5,2,3000.5,2)',
           fmt = "%s",
           header ='# Region file format: DS9 version 4.1 #', 
           comments = 'global color=red dashlist=8 3 width=1'
           ' font="helvetica 10 normal" text = {This message has both a in it} select=1' \
           ' highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1' \
           '\nimage;' )