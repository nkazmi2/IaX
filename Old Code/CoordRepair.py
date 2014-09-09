# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 19:27:47 2014

@author: Nova
"""
import numpy as np
import pyregion

identify = pyregion.open('SN2008HA/sn2008ha_prog.reg')
keep     = pyregion.open('SN2008HA/sn2008ha_coord.reg')

#print pyregion.ShapeList(identify[0].attr[1].get("color")) == ['c', 'y', 'a', 'n']
#print pyregion.ShapeList(identify[1].attr[1].get("color")) == ['y', 'e', 'l', 'l', 'o', 'w']
#print pyregion.ShapeList(keep[1].attr[1].get("color"))
save = []
for i in range(len(identify)):
    if (pyregion.ShapeList(identify[i].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
        save.append(i)
        
for i in range(len(save)):
    keep[save[i]].attr[1]["color"] = 'yellow'
    
np.save("sn2008ha_coord_exp.reg",keep)