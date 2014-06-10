# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 09:11:48 2014

@author: Nova
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#import glob
import pickle

params = {'legend.fontsize': 10, 
          'legend.linewidth': 2,
          'legend.font': 'serif',
          'mathtext.default': 'regular', 
          'xtick.labelsize': 10, 
          'ytick.labelsize': 10} # changes font size in the plot legend

plt.rcParams.update(params) # reset the plot parameters

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 10,
        } 
#####################################################################

d = []
d.append(np.loadtxt('Z017Y26.dat'))
d = np.array(d)

#print d
#print np.shape(d) #(1L, 16776L, 21L)
Length = 16776
logAGE = []
F435W = []
F555W = []

logAGE = d[:,:,0]
F435W  = d[:,:,7]
F555W  = d[:,:,10]
F625W  = d[:,:,12]
F814W  = d[:,:,16]

age70   = np.where((d[:,:,0] == 7.0))
age71   = np.where((d[:,:,0] == 7.1))
age72   = np.where((d[:,:,0] == 7.2))
age73   = np.where((d[:,:,0] == 7.3))
age74   = np.where((d[:,:,0] == 7.4))
age75   = np.where((d[:,:,0] == 7.5))
age76   = np.where((d[:,:,0] == 7.6))
age77   = np.where((d[:,:,0] == 7.7))
age78   = np.where((d[:,:,0] == 7.8))
age79   = np.where((d[:,:,0] == 7.9))
age80   = np.where((d[:,:,0] == 8.0))
age7   = np.where((d[:,:,0] >= 7.0) & (d[:,:,0] < 8.5))
age758   = np.where((d[:,:,0] >= 7.5) & (d[:,:,0] < 8.0))
age8   = np.where((d[:,:,0] >= 8.0) & (d[:,:,0] < 9.0))
age9   = np.where((d[:,:,0] >= 9.0) & (d[:,:,0] < 10.0))
age10  = np.where((d[:,:,0] >= 10.0) & (d[:,:,0] < 10.3))
age103 = np.where((d[:,:,0] == 10.3))

#####################################################################
#"""
title = 'SN08ge'
f435f555_4 = pickle.load(open( "sn2008ge_f435f555_4.p", "rb" ))
f625f814_4 = pickle.load(open( "sn2008ge_f625f814_4.p", "rb" ))
f435f555_5 = pickle.load(open( "sn2008ge_f435f555_5.p", "rb" ))
f625f814_5 = pickle.load(open( "sn2008ge_f625f814_5.p", "rb" ))
#"""
"""
title = 'SN08ha'
f435f555_4 = pickle.load(open( "sn2008ha_f435f555_4.p", "rb" ))
f625f814_4 = pickle.load(open( "sn2008ha_f625f814_4.p", "rb" ))
f435f555_5 = pickle.load(open( "sn2008ha_f435f555_5.p", "rb" ))
f625f814_5 = pickle.load(open( "sn2008ha_f625f814_5.p", "rb" ))
"""
"""
title = 'SN10ae'
f435f555_4 = pickle.load(open( "sn2010ae_f435f555_4.p", "rb" ))
f625f814_4 = pickle.load(open( "sn2010ae_f625f814_4.p", "rb" ))
f435f555_5 = pickle.load(open( "sn2010ae_f435f555_5.p", "rb" ))
f625f814_5 = pickle.load(open( "sn2010ae_f625f814_5.p", "rb" ))
"""
"""
title = 'SN10el'
f435f555_4 = pickle.load(open( "sn2010el_f435f555_4.p", "rb" ))
f625f814_4 = pickle.load(open( "sn2010el_f625f814_4.p", "rb" ))
f435f555_5 = pickle.load(open( "sn2010el_f435f555_5.p", "rb" ))
f625f814_5 = pickle.load(open( "sn2010el_f625f814_5.p", "rb" ))
"""
#####################################################################

print "Begin plotting Isochrones..."
h = [6, 6] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [6, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)
#plots = plt.subplot(gs[0])

c1plt = plt.subplot2grid((2,2), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W",fontdict = font)
plt.ylabel("F555W",fontdict = font)
#c1plt.scatter(np.subtract(F435W[age70],  F555W[age70]),  F555W[age70],  label = 'Log(Age) = 7.0', c="r",marker='o')
c1plt.scatter(np.subtract(F435W[age71],  F555W[age71]),  F555W[age71],  label = 'Log(Age) = 7.1', c="y",marker='o')
c1plt.scatter(np.subtract(F435W[age72],  F555W[age72]),  F555W[age72],  label = 'Log(Age) = 7.2', c="g",marker='o')
c1plt.scatter(np.subtract(F435W[age73],  F555W[age73]),  F555W[age73],  label = 'Log(Age) = 7.3', c="c",marker='o')
c1plt.scatter(np.subtract(F435W[age74],  F555W[age74]),  F555W[age74],  label = 'Log(Age) = 7.4', c="b",marker='o')
#c1plt.scatter(np.subtract(F435W[age75],  F555W[age75]),  F555W[age75],  label = 'Log(Age) = 7.5', c="m",marker='o')
#c1plt.scatter(np.subtract(F435W[age76],  F555W[age76]),  F555W[age76],  label = 'Log(Age) = 7.6', c="r",marker='o' )
#c1plt.scatter(np.subtract(F435W[age77],  F555W[age77]),  F555W[age77],  label = 'Log(Age) = 7.7', c="y",marker='o' )
#c1plt.scatter(np.subtract(F435W[age78],  F555W[age78]),  F555W[age78],  label = 'Log(Age) = 7.8', c="g",marker='o' )
#c1plt.scatter(np.subtract(F435W[age79],  F555W[age79]),  F555W[age79],  label = 'Log(Age) = 7.9', c="c",marker='o' )
#c1plt.scatter(np.subtract(F435W[age80],  F555W[age80]),  F555W[age80],  label = 'Log(Age) = 8.0', c="b",marker='o' )
#c1plt.scatter(np.subtract(F435W[age10],  F555W[age10]),  F555W[age10],  label = 'Log(Age) >= 10.0 & < 10.3',c="y",marker='o' )
#c1plt.scatter(np.subtract(F435W[age103], F555W[age103]), F555W[age103], label = 'Log(Age) == 10.3 & < 7.5', c="r",marker='o' )
#c1plt.scatter(np.subtract(f435f555_4[0],   f435f555_4[1]),   f435f555_4[1],   label = 'S/N 4, Radius 30pix',  c="b",marker='D')
c1plt.scatter(np.subtract(f435f555_5[0],   f435f555_5[1]),   f435f555_5[1],   label = 'S/N 5, Radius 30pix',  c="w",marker='D')
#####c1plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.1)
c1plt.legend(loc=4, borderaxespad=0.)
c1plt.set_ylim(bottom=-2.0, top=-9.0) #sn08ge
#c1plt.set_ylim(bottom=2.0, top=-9.0) #sn08ha
#c1plt.set_ylim(bottom=-1.0, top=-11.0) #sn10ae
#c1plt.set_ylim(bottom=-1.0, top=-6.0) #sn10el
plt.title(title+': CMD for Z = 0.017, Y = 0.26')

c2plt = plt.subplot2grid((2,2), (1,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F625W - F814W",fontdict = font)
plt.ylabel("F625W",fontdict = font)
#c2plt.scatter(np.subtract(F625W[age70],  F814W[age70]),  F814W[age70],  label = 'Log(Age) = 7.0',  c="r",marker='o')
c2plt.scatter(np.subtract(F625W[age71],  F814W[age71]),  F814W[age71],  label = 'Log(Age) = 7.1',  c="y",marker='o')
c2plt.scatter(np.subtract(F625W[age72],  F814W[age72]),  F814W[age72],  label = 'Log(Age) = 7.2',  c="g",marker='o')
c2plt.scatter(np.subtract(F625W[age73],  F814W[age73]),  F814W[age73],  label = 'Log(Age) = 7.3',  c="c",marker='o')
c2plt.scatter(np.subtract(F625W[age74],  F814W[age74]),  F814W[age74],  label = 'Log(Age) = 7.4',  c="b",marker='o')
#c2plt.scatter(np.subtract(F625W[age75],  F814W[age75]),  F814W[age75],  label = 'Log(Age) = 7.5',  c="m",marker='o')
#c2plt.scatter(np.subtract(F625W[age76],  F814W[age76]),  F814W[age76],  label = 'Log(Age) = 7.6',  c="r",marker='o')
#c2plt.scatter(np.subtract(F625W[age77],  F814W[age77]),  F814W[age77],  label = 'Log(Age) = 7.7',  c="y",marker='o')
#c2plt.scatter(np.subtract(F625W[age78],  F814W[age78]),  F814W[age78],  label = 'Log(Age) = 7.8',  c="g",marker='o')
#c2plt.scatter(np.subtract(F625W[age79],  F814W[age79]),  F814W[age79],  label = 'Log(Age) = 7.9',  c="c",marker='o')
#c2plt.scatter(np.subtract(F625W[age80],  F814W[age80]),  F814W[age80],  label = 'Log(Age) = 8.0',  c="b",marker='o')
#c2plt.scatter(np.subtract(f625f814_4[0],   f625f814_4[1]),   f625f814_4[1],   label = 'S/N 4, Radius 30pix',  c="b",marker='D')
c2plt.scatter(np.subtract(f625f814_5[0],   f625f814_5[1]),   f625f814_5[1],   label = 'S/N 5, Radius 30pix',  c="w",marker='D')
#c2plt.scatter(np.subtract(F625W[age7],   F814W[age7]),   F814W[age7],   label = 'Log(Age) >= 7.0 & < 7.5',  c="w",marker='o')
#c2plt.scatter(np.subtract(F625W[age758],  F814W[age758]),  F814W[age758],  label = 'Log(Age) >= 7.5 & < 8.0',  c="m",marker='o' )
#c2plt.scatter(np.subtract(F625W[age8],   F814W[age8]),   F814W[age8],   label = 'Log(Age) >= 8.0 & < 9.0',  c="b",marker='o' )
#c2plt.scatter(np.subtract(F625W[age9],   F814W[age9]),   F814W[age9],   label = 'Log(Age) >= 9.0 & < 10.0', c="g",marker='o' )
#c2plt.scatter(np.subtract(F625W[age10],  F814W[age10]),  F814W[age10],  label = 'Log(Age) >= 10.0 & < 10.3',c="y",marker='o' )
#c2plt.scatter(np.subtract(F625W[age103], F814W[age103]), F814W[age103], label = 'Log(Age) == 10.3 & < 7.5', c="r",marker='o' )
c2plt.legend(loc=4, borderaxespad=0.)
c2plt.set_ylim(bottom=-3.0, top=-9) #sn08ge
#c2plt.set_ylim(bottom=0.0, top=-9) #sn08ha
#c2plt.set_ylim(bottom=-4.0, top=-9) #sn10ae
#c2plt.set_ylim(bottom=-1.0, top=-6.0) #sn10el
print "Save and show plot : " + title

plt.savefig(title +'_Comparison.png')
#plt.savefig("SN08ha_Comparison.png")
#plt.savefig("SN10ae_Comparison.png")
#plt.savefig("SN10el_Comparison.png")
