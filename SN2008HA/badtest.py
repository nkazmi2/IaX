# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 11:14:18 2014

@author: Nova
"""
import numpy as np
import pyregion

r = pyregion.open('sn2008ha_prog_play.reg')
save = []
badX = []
badY = []
for i in range(len(r)):
    r1 = pyregion.ShapeList(r[i].attr[1].get("color"))
    if (r1[0] == 'c'):
        save.append(i) 
for j in range(len(save)):
    badX.append(r[save[j]].coord_list[0] - .5)
    badY.append(r[save[j]].coord_list[1] - .5)

print badX
print badY
#r1 = pyregion.ShapeList([rr for rr in r if rr.comment.get("tag") == 'color=cyan font="helvetica 10 normal"'])
#print r1
"""
reg   = []
comm  = []
whoop = []
for i in range(len(r)):
    #comm.append(np.array(r[i].comment))
    #reg.append(np.array(r[i]))
    whoop.append(np.where(r[i].comment == 'color=cyan font="helvetica 10 normal"'))
    #whoop.append(np.where(r[i].comment == 'color=cyan font="helvetica 10 normal"'))
#reg = np.array(reg)
ach = pyregion.parse(region_string).as_imagecoord(r[0].header)   
print ach
#region = r[0]
#itch = pyregion.parse(r)
#print itch
"""
"""
r = np.array(r)
for i in range(630):
    print r[whoop[i]]
 
print r[whoop[0]]
"""   
#achoo.append(r[i].coord_list[0][whoop],r[i].coord_list[1][whoop])
"""
achoo = []
#list(np.any(x not in badX for x in xcoord))
print np.all(r).comment

whoop = np.where(np.all(r.comment[:-27]) == "color=cyan")
print type(whoop)

#print r[whoop].coord_list
"""
"""
for i in range(len(r)):
    print r[whoop].coord_list[0]
    print r[whoop].coord_list[1][whoop]
    achoo.append(r[i].coord_list[0][whoop],r[i].coord_list[1][whoop])
"""
# r is the entire file
# r[i].name the type of shape, first thing in the line
# r[i] is a specific line
# r[i].comment is the stuff behind the #, where the color info is
# r[i].attr[1] attributes, has all(?)
# r[3].coord_list gives the x (.coord_list[0]), y (.coord_list[1]) pix coord


#print r[1].comment[:-27] == "color=yellow"#