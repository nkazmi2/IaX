# -*- coding: utf-8 -*-
"""
Created on Fri May 30 09:58:19 2014

@author: Nova
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 13:23:45 2014

@author: Nova
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 09:43:26 2014

@author: Nova
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv
from itertools import izip
import pickle
import glob


filename = open('sn2008ge_F435W_F555W_snr3.csv')
data = np.recfromcsv(filename, names=['a','a','a'])
newxcoord = []
newycoord = []
for i in range(len(data)):
    newxcoord.append(data[i][0] - 3200)
    newycoord.append(data[i][1] - 3370)

with open('test.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(izip(newxcoord,newycoord))
"""
f = []
data = []
coord = []
f = glob.glob('sn2008ge_*.csv')
for i in range(len(f)):
    coord = np.genfromtxt(f[i], delimiter = ',')
print coord

for i in range(len(f)):
    photfile = open(f[i],'r')
    print photfile
    
    for line in photfile:
        columns = line.split()
        data.append(columns)
    print data
"""
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
""" 
test = np.where((star <= 2) & (snr814 >= 2.9) & (snr814 <=3.5) &
        ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))
print snr814[test]
print np.mean(f814Abs[test])
print np.mean(snr814[test])

#3.0000   0.8000   3.4000   5.6000   -3.8880   -2.7340   -4.4500   -5.1220
#5.9000   3.0000   2.5000   1.7000   -4.6930   -4.4110   -4.0620   -3.7560
#4.4000   4.7000   3.0000   3.5000   -4.3270   -4.8470   -4.2860   -4.5880
#3.1000   1.7000   3.5000   3.0000   -3.8980   -3.6830   -4.5060   -4.412080

print np.subtract(-4.4110,-3.8880)
print np.subtract(-4.412080,-4.2860)
# -3.8880
# -4.4110
# -4.2860 
# -4.412080
import pyregion
identify = pyregion.open('../SN2008GE/sn2008ge_prog.reg') #sn08ge
#identify = pyregion.open(folder + '/'+ title +'final.reg') #sn08ha
#r = pyregion.open(folder + '/'+ title +'coord.reg')
r = pyregion.open('../SN2008GE/sn2008ge_20141015_coord2.reg')
save = []
badX = []
badY = []
fix  = []

for i in range(len(identify)):
    if (pyregion.ShapeList(identify[i].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
        fix.append(i)

print len(identify)    
print len(r)
print len(fix)

for i in range(len(fix)):
    r[fix[i]].attr[1]["color"] = 'yellow'

for i in range(len(r)):
    r1 = pyregion.ShapeList(r[i].attr[1].get("color"))
    if (r1[0] == 'c'):
        save.append(i) 
 
for j in range(len(save)):
    badX.append(r[save[j]].coord_list[0] - .5)
    badY.append(r[save[j]].coord_list[1] - .5)
import numpy as np

class Student(object):
    
    def __init__(self, name, classes):
        print "I'm the constructor!"
        self.name = name
        self.classes = classes
        
    def __str__(self):
        output = '%s:'%self.name
        for clas in self.classes:
            output+=str(clas)
            if clas != self.classes[-1]:
                output+=', '
        return output
        
    def getName(self):
        return self.name
        
me = Student('Sean', ['Physics', 'Computer Science', 'Underwater Basket Weaving'])   
print me.getName()
print str(me)

#435 555
print np.subtract(                    -2.7340,                     -4.4110)
print np.subtract(np.subtract(-3.8880,-2.7340),np.subtract(-4.6930,-4.4110))
s1 =  np.subtract(-2.7340,-4.4110) / np.subtract(np.subtract(-3.8880,-2.7340),np.subtract(-4.6930,-4.4110))
print "Slope : ", s1
b1 = np.subtract(-4.4110,s1*(np.subtract(-4.4110,-4.6930)))
print "B-int : ", b1
#y1 = (s1*(np.subtract(-4.4110,-4.6930))) + b1
y1 = (s1*2.0) + b1
print "Y-pt  : ", y1
print (s1*1.7) + b1
x1 = np.subtract(-4.4110,b1)/s1
print "X0-pt : ", x1
print np.subtract(                    -5.1220,                     -3.7560)
print np.subtract(np.subtract(-4.4500,-5.1220),np.subtract(-4.0620,-3.7560))
s2 =  np.subtract(-5.1220,-3.7560)/np.subtract(np.subtract(-4.4500,-5.1220),np.subtract(-4.0620,-3.7560))
print "Slope : ", s2
b2 = np.subtract(-3.7560,s2*(np.subtract(-4.0620,-3.7560)))
print "B-int : ", b2
#y2 = (s2*(np.subtract(-3.7560,-4.0620))) + b2
y2 = (s2*2.5) + b2
print "Y-pt  : ", y2
print (s2*1.8) + b2
x2 = np.subtract(-3.7560,b2)/s2
print "X0-pt : ", x2
#625 814
print np.subtract(                     -4.8470,                      -3.6830)
print np.subtract(np.subtract(-4.3270 ,-4.8470),np.subtract(-3.8980 ,-3.6830))
s3 =  np.subtract(-4.8470,-3.6830)/np.subtract(np.subtract(-4.3270 ,-4.8470),np.subtract(-3.8980 ,-3.6830))
print "Slope : ", s3
b3 = np.subtract(-3.6830,s3*(np.subtract( -3.8980,-3.6830)))
print "B-int : ", b3
#y3 = (s3*(np.subtract(-3.6830,-3.8980))) + b3
y3 = (s3*2.0) + b3
print "Y-pt  : ", y3
print (s3*1.7) + b3
x3 = np.subtract(-3.6830,b3)/s3
print "X0-pt : ", x3

print np.subtract(                   -4.5880,                       -4.412080)
print np.subtract(np.subtract(-4.2860,-4.5880),np.subtract(-4.5060 ,-4.412080))
s4 =  np.subtract(-4.5880,-4.412080)/np.subtract(np.subtract(-4.2860,-4.5880),np.subtract(-4.5060 ,-4.412080))
print "Slope : ", s4
b4 = np.subtract(-4.412080,s4*(np.subtract(-4.5060,-4.412080)))
print "B-int : ", b4
#y4 = (s4*(np.subtract(-4.412080,-4.5060))) + b4
y4 = (s4*2.5) + b4
print "Y-pt  : ", y4
print (s4*1.8) + b4
x4 = np.subtract(-4.412080,b4)/s4
print "X0-pt : ", x4


###############################################################################
#rect = patches.Rectangle((-2,ybotmax), width=7, height=-1,
                         #color='grey',
                         #alpha=0.3)
#This was an iffy move,using the sn =3 of a point that's not plotted, I don't like it

f555min3    = -4.4110 #555
f555min3435 = -4.6930 
f435min3    = -3.8880 
f435min3555 = -2.7340 #555

#print np.subtract(                    -2.7340,                     -4.4110)
#print np.subtract(np.subtract(-3.8880,-2.7340),np.subtract(-4.6930,-4.4110))
s1 = np.subtract(-2.7340,-4.4110) / np.subtract(np.subtract(-3.8880,-2.7340),np.subtract(-4.6930,-4.4110))
b1     = f555min3 - (s1*(np.subtract(-4.4110,-4.6930)))

ptsR = np.array([[-2,ybotmax],
                 [-2,f555min3],
                 [np.subtract(f555min3,b1)/s1,f555min3], #need the x value
                 [2.0,((2.0*s1)+b1)],  #this is okay              
                 [2.0,ybotmax]])
polyR = Polygon(ptsR, color='grey', alpha=0.15,closed = True)

c1plt.add_patch(polyR)
#############
min3l       = np.where(f625f814_4[0][5] == 3.0)
f625min3    = -4.2860
f625min3814 = -4.5880

#top = np.subtract(f625f814_4[0][1][min3l], f625min3814)
#bottom = np.subtract(np.subtract(f625f814_4[0][0][min3l], f625f814_4[0][1][min3l]) , np.subtract(f625min3, f625min3814))
#slope  = top/bottom
#bval   = f625f814_4[0][1][min3l] - (slope*(np.subtract(f625f814_4[0][0][min3l],f625f814_4[0][1][min3l])))
##print slope, bval
##s1     = -1.125
##b1     = f625f814_4[0][1][min3l] - (s1*f625f814_4[0][0][min3l])

#flippt = (np.subtract(f625f814_4[0][1][min3l],bval))/np.abs(slope)
#toppt  = ((2.5*slope)+bval)
#print f625f814_4[0][1][min3l] # ymin of s/n = 3
#print (np.subtract(f625f814_4[0][1][min3l],bval))/np.abs(slope) #flippt  
#print ((2.5*slope)+bval) #toppt
#print np.subtract(f625f814_4[0][1][min3l],toppt)/np.subtract(flippt, 2.5) #slope of flippt
#s2  = np.subtract(f625f814_4[0][1][min3l],toppt)/np.subtract(flippt, 2.5) #slope of flippt
#print f625f814_4[0][1][min3l] - (s2*f625f814_4[0][0][min3l]) #bvalue
#b2  = f625f814_4[0][1][min3l] - (s2*f625f814_4[0][0][min3l])
#print np.subtract(f625f814_4[0][1][min3l],-b2)/s2
#bad = np.subtract(f625f814_4[0][1][min3l],-b2)/s2

#print np.subtract(                   -4.5880,                       -4.412080)
#print np.subtract(np.subtract(-4.2860,-4.5880),np.subtract(-4.5060 ,-4.412080))
s4 =  np.subtract(-4.5880,-4.412080)/np.subtract(np.subtract(-4.2860,-4.5880),np.subtract(-4.5060 ,-4.412080))
#print "Slope : ", s4
b4 = np.subtract(-4.412080,s4*(np.subtract(-4.5060,-4.412080)))
#print "B-int : ", b4
#y4 = (s4*(np.subtract(-4.412080,-4.5060))) + b4
y4 = (s4*2.5) + b4
#print "Y-pt  : ", y4
#print (s4*1.8) + b4
x4 = np.subtract(-4.412080,b4)/s4
#print "X0-pt : ", x4
pts = np.array([[-2,ybotmax],
                [-2,f625f814_4[0][1][min3l]],
                [x4,f625f814_4[0][1][min3l]], #need the x value                
                #[np.subtract(f625f814_4[0][1][min3l],b1)/s1,f625f814_4[0][1][min3l]], #need the x value
                [2.5,y4],  #this is okay              
                [2.5,ybotmax]])
poly = Polygon(pts, color='grey', alpha=0.15,closed = True)

c2plt.add_patch(poly)

#c2plt.add_patch(rect)
###############################################################################


from numpy import *
import pylab
# data to fit
x = random.rand(6)
y = random.rand(6)

# fit the data with a 4th degree polynomial
z4 = polyfit(x, y, 4) 
p4 = poly1d(z4) # construct the polynomial 

z5 = polyfit(x, y, 5)
p5 = poly1d(z5)

xx = linspace(0, 1, 100)
pylab.plot(x, y, 'o', xx, p4(xx),'-g', xx, p5(xx),'-b')
pylab.legend(['data to fit', '4th degree poly', '5th degree poly'])
pylab.axis([0,1,0,1])
pylab.show()

import numpy


import scipy.optimize as optimization
# Generate artificial data = straight line with a=0 and b=1
# plus some noise.
xdata = numpy.array([0.0,1.0,2.0,3.0,4.0,5.0])
ydata = numpy.array([0.1,0.9,2.2,2.8,3.9,5.1])
# Initial guess.
x0    = numpy.array([0.0, 0.0, 0.0])
sigma = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0])

def func(x, a, b, c):
    return a + b*x + c*x*x

print optimization.curve_fit(func, xdata, ydata, x0, sigma)

#from pylab import *
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D
#import matplotlib.patches as patches
from matplotlib.patches import Polygon
ax = plt.gca()
pts = np.array([[0,0], [4,0], [2,np.sqrt(5**2 - 2**2)]])
Triangle = Polygon(pts, color='grey', alpha=0.3)
ax.add_patch(Triangle)
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.show()


fig = plt.figure(figsize=(10,10))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
#ax = fig.add_subplot(1, 1, 1, projection='3d')
ax = Axes3D(fig)

z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

c = x + y

ax.scatter(x, y, z, c=c)

#p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

## surface_plot with color grading and color bar
#ax = fig.add_subplot(1, 2, 2, projection='3d')
#p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#cb = fig.colorbar(p, shrink=0.5)

fig = plt.figure()
ax = fig.add_subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.set_ylim(-2,2)
plt.show()

import numpy as np
#import pyregion

folder   = "SN2008HA"
name     = 'sn2008ha_new.phot'
print "Open file"
data = np.loadtxt('../' +folder + '/' + name)
print "Set up array"
sharp   = data[:, 6]
roond   = data[:, 7] # round is already a special word
crowd   = data[:, 9]
cut = np.where(sharp <= 3)
DataOut = np.array(np.c_[sharp, sharp[cut],roond[cut],crowd[cut]])
print DataOut
print "This is stupid"
np.savetxt('test.txt', DataOut, fmt = "%1.4f", header ='Sharp Round Crowd')

#data = np.load("../quick_sub.py")
#print data

#one = np.loadtxt('one.txt')
#two = np.loadtxt('two.txt')
#ich = []
#ich = np.where(list(np.any(x not in two for x in one) and np.any(y not in two for y in one)))
#print one[ich]

data = np.loadtxt("../SN2008HA/sn2008ha_new.phot")
data    = np.array(data)
data    = data.astype(float)
star    = data[:,10] # type
snr435  = data[:,19] # signal to noise
snr555  = data[:,32]
snr625  = data[:,45]
snr814  = data[:,58]
xcoord  = data[:, 2]
ycoord  = data[:, 3]
xsn      = 1726.352
ysn      = 3172.530
r = pyregion.open('../SN2008HA/sn2008ha_coord.reg')
save = []
X = []
Y = []

for i in range(len(r)):
    r1 = pyregion.ShapeList(r[i].attr[1].get("color"))
    if (r1[0] == 'c'):
        save.append(i) 
print len(save)
for j in range(len(r)):
    X.append(r[save[j]].coord_list[0] -.5)
    Y.append(r[save[j]].coord_list[1] -.5)
#X = (np.around(X, decimals=2))
#Y = (np.around(Y, decimals=2))

####
#print len(X), type(X[0])
#print len(Y), type(Y[0])
#print len(xcoord), type(xcoord[0])
#print len(ycoord), type(ycoord[0])

ich = []
eep = []
ich = np.where((star <= 2) & (snr435 >= 3) & (snr555 >= 3) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100) & list(np.any(x not in X for x in xcoord) and np.any(y not in Y for y in ycoord)))
eep = np.where((star <= 2) & (snr435 >= 3) & (snr555 >= 3) & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))
#np.savetxt('test.txt',xcoord[ich],fmt = "%1.4f")
#np.savetxt('withbad.txt',xcoord[eep],fmt = "%1.4f")
#np.savetxt('bad.txt',X,fmt = "%1.4f")
#list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))
print "Filter   ", len(xcoord[ich])
print "No Filter", len(xcoord[eep])

import pickle
#import glob
import numpy as np
title = 'sn2008ha'
catalog = []
catalog = pickle.load(open(title + '_List.p', 'rb'))

#print np.shape(catalog)

print catalog[0]
print catalog[1]
print catalog[2]
print catalog[3]
print catalog[4]
print catalog[5]
print catalog[6]
print catalog[7]
print catalog[8]
print catalog[9]
print catalog[10]
print catalog[11]
print catalog[12]
print catalog[13]
print catalog[14]
print catalog[15]
print catalog[16]
print catalog[17]
print catalog[18]
print catalog[19]

#f625f814_4 = pickle.load(open( "sn2008ha_f625f814_r1_4.p", "rb" ))
#f435f555_5 = pickle.load(open( "sn2008ha_f435f555_r1_5.p", "rb" ))
#f625f814_5 = pickle.load(open( "sn2008ha_f625f814_r1_5.p", "rb" ))
#f435f555_6 = pickle.load(open( "sn2008ha_f435f555_r1_6.p", "rb" ))
#f625f814_6 = pickle.load(open( "sn2008ha_f625f814_r1_6.p", "rb" ))
#f435f555_7 = pickle.load(open( "sn2008ha_f435f555_r1_7.p", "rb" ))
#f625f814_7 = pickle.load(open( "sn2008ha_f625f814_r1_7.p", "rb" ))
#f435f555_8 = pickle.load(open( "sn2008ha_f435f555_r1_8.p", "rb" ))
#f625f814_8 = pickle.load(open( "sn2008ha_f625f814_r1_8.p", "rb" ))

i = 3
for n in range(10): 
    i += 1
    if (n % 2 == 0): 
        print abs(n-(i))
    elif (n % 2 != 0):
        i += 1
        print abs((n)-(i)+1)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import glob

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

#name = []
#name = glob.glob('*.dat')
#name = '
#f     = np.loadtxt(
#f2    = open(name[1])
#f3    = open(name[2])
#f4    = open(name[3])
#f5    = open(name[4])

# 175 rows, start at 0, the max is at [174]
# Ignore the first 11 rows

f   = open('Z017Y26.dat')
row = []
row = [f.readline().strip().split() for i in range(16776)]
row = np.array(row)

#d = []

#d.append(np.loadtxt('Z017Y26.dat'))
#d = np.array(d)

for i in range(11,16776):#16765L, 21L
    d.append(row[:][i])
d = np.array(d)

#print d
#print np.shape(d) #(1L, 16776L, 21L)
#Length = 16776
#logAGE = []
#F435W = []
#F555W = []

#logAGE = d[:,:,0]
#F435W  = d[:,:,7]
#F555W  = d[:,:,10]



#row2 = [f2.readline().strip().split() for i in range(175)]
#row2 = np.array(row2)

#row3 = [f3.readline().strip().split() for i in range(175)]
#row3 = np.array(row3)

#row4 = [f4.readline().strip().split() for i in range(175)]
#row4 = np.array(row4)

#row5 = [f5.readline().strip().split() for i in range(175)]
#row5 = np.array(row5)

#print row[:][0]
#print row[:][1]
#print row[:][2]
#print row[:][3]
#print row[:][4]
#print row[:][5]
#print row[:][6]
#print row[:][7]
#print row[:][8]
#print row[:][9]
#print row[:][10]

#data = []
#for i in range(11,175):
#    data.append(row[:][i])
#data = np.array(data)


#print d[:][0]
#print d[:][1]
#print d[:][2]
#print d[:][3]
#print d[:][4]
#print d[:][5]
#print d[:][6]
#print d[:][7]
#print d[:][8]
#print d[:][9]
#print d[:][10]
#print d[:][11]
#print d[:][12]
#data2 = []
#for i in range(11,175):
#    data2.append(row2[:][i])
#data2 = np.array(data2)

#diff2 = []
#for i in range(len(data2[:,10])):
#    diff2.append(np.subtract(float(data2[i,7]), float(data2[i,10])))   
    
#data3 = []
#for i in range(11,175):
#    data3.append(row3[:][i])
#data3 = np.array(data3)

#diff3 = []
#for i in range(len(data3[:,10])):
#    diff3.append(np.subtract(float(data3[i,7]), float(data3[i,10]))) 
    
#data4 = []
#for i in range(11,175):
#    data4.append(row4[:][i])
#data4 = np.array(data4)

#diff4 = []
#for i in range(len(data4[:,10])):
#    diff4.append(np.subtract(float(data4[i,7]), float(data4[i,10]))) 
           
#data5 = []
#for i in range(11,175):
#    data5.append(row5[:][i])
#data5 = np.array(data5)

#diff5 = []
#for i in range(len(data5[:,10])):
#    diff5.append(np.subtract(float(data5[i,7]), float(data5[i,10]))) 
#####################################################################
    
# Magnitude of the Milkyway Galaxy for 2010ae
#ACS435   = 0 #F435W
#ACS555   = 0 #F555W	
#ACS625   = 0 #F625W	
#ACS814   = 0 #F814W	

# Median (redshift independent) distance modulus of host galaxy
#dmod    = 0 

# Actual X & Y pixel coordinates of sn
#xsn     = 1796.640
#ysn     = 1931.995
#radius  = 50.0 #pixels

#f555Abs = []
#for i in range(len(data[:,10])):
#     f555Abs.append(float(data[i,10]) - dmod - ACS555)

age7   = np.where((d[:,:,0] >= 7.0) & (d[:,:,0] < 8.5))
age75   = np.where((d[:,:,0] >= 7.5) & (d[:,:,0] < 8.0))
age8   = np.where((d[:,:,0] >= 8.0) & (d[:,:,0] < 9.0))
age9   = np.where((d[:,:,0] >= 9.0) & (d[:,:,0] < 10.0))
age10  = np.where((d[:,:,0] >= 10.0) & (d[:,:,0] < 10.3))
age103 = np.where((d[:,:,0] == 10.3))

diff = []
for i in range(Length):
    diff.append(np.subtract(F435W[i,age], F555W[i,age]))
print np.shape(diff)
print len(F555W[age])
print diff[:][0]
print diff

#f555Abs2 = []
#for i in range(len(data2[:,10])):
#     f555Abs2.append(float(data2[i,10]) - dmod - ACS555)

#f555Abs3 = []
#for i in range(len(data3[:,10])):
#     f555Abs3.append(float(data3[i,10]) - dmod - ACS555)
     
#f555Abs4 = []
#for i in range(len(data4[:,10])):
#     f555Abs4.append(float(data4[i,10]) - dmod - ACS555)

#f555Abs5 = []
#for i in range(len(data5[:,10])):
#     f555Abs5.append(float(data5[i,10]) - dmod - ACS555)

#####################################################################

print "Begin plotting Isochrones..."
h = [5, 5] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [6, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)
#plots = plt.subplot(gs[0])


c1plt = plt.subplot2grid((1,1), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W",fontdict = font)
plt.ylabel("F555W",fontdict = font)
c1plt.scatter(np.subtract(F435W[age7], F555W[age7]), F555W[age7], label = 'Log(Age) >= 7.0 & < 7.5',c="w",marker='o')
c1plt.scatter(np.subtract(F435W[age75], F555W[age75]), F555W[age75], label = 'Log(Age) >= 7.5 & < 8.0',c="m",marker='o' )
c1plt.scatter(np.subtract(F435W[age8], F555W[age8]), F555W[age8], label = 'Log(Age) >= 8.0 & < 9.0',c="b",marker='o' )
c1plt.scatter(np.subtract(F435W[age9], F555W[age9]), F555W[age9], label = 'Log(Age) >= 9.0 & < 10.0',c="g",marker='o' )
c1plt.scatter(np.subtract(F435W[age10], F555W[age10]), F555W[age10], label = 'Log(Age) >= 10.0 & < 10.3',c="y",marker='o' )
c1plt.scatter(np.subtract(F435W[age103], F555W[age103]), F555W[age103], label = 'Log(Age) == 10.3 & < 7.5',c="r",marker='o' )
#c1plt.scatter(np.subtract(F435W, F555W), F555W, label = 'CMD for Z = 0.017, Y = 0.26',c="r",marker='o' )
#c1plt.plot(diff2, f555Abs2, label = 'CMD for Z = 0.'+name[1][1:-7]+' Y = 0.'+name[1][5:-4])
#c1plt.plot(diff3, f555Abs3, label = 'CMD for Z = 0.'+name[2][1:-7]+' Y = 0.'+name[2][5:-4])
#c1plt.plot(diff4, f555Abs4, label = 'CMD for Z = 0.'+name[3][1:-7]+' Y = 0.'+name[3][5:-4])
#c1plt.plot(diff5, f555Abs5, label = 'CMD for Z = 0.'+name[4][1:-7]+' Y = 0.'+name[4][5:-4])
#####c1plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.1)
c1plt.legend(loc=4, borderaxespad=0.)
plt.title('CMD for Z = 0.017, Y = 0.26')
print "Save and show Isochrones..."
plt.savefig("Test.png")

# c1 refers to the cut1
c1plt = plt.subplot2grid((2,2), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.xlabel("Log($T_e$)",fontdict = font)
plt.ylabel("$M_{cur}$(?)",fontdict = font)
c1plt.plot(data[:,2],data[:,4], label = 'Z = 0.'+name[0][1:-7]+' Y = 0.'+name[0][5:-4])
c1plt.plot(data2[:,2],data2[:,4], label = 'Z = 0.'+name[1][1:-7]+' Y = 0.'+name[1][5:-4])
c1plt.plot(data3[:,2],data3[:,4], label = 'Z = 0.'+name[2][1:-7]+' Y = 0.'+name[2][5:-4])
c1plt.plot(data4[:,2],data4[:,4], label = 'Z = 0.'+name[3][1:-7]+' Y = 0.'+name[3][5:-4])
c1plt.plot(data5[:,2],data5[:,4], label = 'Z = 0.'+name[4][1:-7]+' Y = 0.'+name[4][5:-4])

c1plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
        ncol=2, mode="expand", borderaxespad=0.)
#c1plt.semilogx(data[:,2],data[:,4])
# c2 refers to the cut2 
c2plt = plt.subplot2grid((2,2), (1,0), colspan = 2)
plt.gca().invert_yaxis()
plt.xlabel("F435W - F555W",fontdict = font)
plt.ylabel("F555W",fontdict = font)
c2plt.plot(diff, f555Abs, label = 'CMD for Z = 0.'+name[0][1:-7]+' Y = 0.'+name[0][5:-4])
c2plt.plot(diff2, f555Abs2, label = 'CMD for Z = 0.'+name[1][1:-7]+' Y = 0.'+name[1][5:-4])
c2plt.plot(diff3, f555Abs3, label = 'CMD for Z = 0.'+name[2][1:-7]+' Y = 0.'+name[2][5:-4])
c2plt.plot(diff4, f555Abs4, label = 'CMD for Z = 0.'+name[3][1:-7]+' Y = 0.'+name[3][5:-4])
c2plt.plot(diff5, f555Abs5, label = 'CMD for Z = 0.'+name[4][1:-7]+' Y = 0.'+name[4][5:-4])
#c2plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#c2plt.scatter(np.subtract(data[:,8], data[:,11]),data[:,11], c="r",marker='o')
"""
