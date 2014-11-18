# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 13:23:45 2014

@author: Nova
"""

import math

radius1   = [50,100,150,175,200]#[50,75,100,125,150]#[10,25,50,75,100]#[10,17,23,34,50]#
radius2   = [50,100,150,175,200]#[50,75,100,125,150]#[10,25,50,75,100]#[10,17,23,34,50]#
dist      = 17.95e7
conver    = (2.5*math.pi)/(50.0*3600*180)
print round(dist*(math.tan(radius1[4]*conver)),-2)