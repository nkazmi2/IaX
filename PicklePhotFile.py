# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 10:56:47 2014

@author: nova
"""
import pandas
import pickle

folder   = "SN2010AE"
name     = 'sn2010ae.phot.out' 
title    = name[:-9]

print "Extracting ", name, " information..."

data = pandas.read_csv(folder + '/' + name,delim_whitespace=True, header=None)

alldata = []
print "Pickling!"
alldata.append((data))
                    
pickle.dump( alldata[0], open(folder + '/' + title + '_photfile.p', "wb" ) )
print "Pickl-e-fried"