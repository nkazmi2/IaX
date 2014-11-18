# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 10:56:47 2014

@author: nova
"""
#Pickle dis ish
# Check Radii
# Redo Bad List
# ping curtis

import pandas
import pickle

folder   = "SN2008GE"
name     = 'sn2008ge_new.phot' 
title    = name[:-9]

print "Extracting ", name, " information..."

data = pandas.read_csv(folder + '/' + name,delim_whitespace=True, header=None)

alldata = []
print "Pickling!"
alldata.append((data))
                    
pickle.dump( alldata[0], open(folder + '/' + title + 'photfile.p', "wb" ) )
print "Pickl-e-fried"