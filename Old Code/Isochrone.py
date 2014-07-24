# -*- coding: utf-8 -*-
"""
Created on Fri May 30 09:58:19 2014

@author: Nova
"""
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

name = []
d    = []
row  = []
diff = []
f435w = []
f555w = []
f625w = []
f814w = []
name = glob.glob('*.dat')


for i in range(len(name)):
    d.append(np.loadtxt(name[i]))
#for j in range(len(d)):
    
f435w.append(np.loadtxt(d[0][:,7]))    
f555w.append(np.loadtxt(d[0][:,10]))
f625w.append(np.loadtxt(d[0][:,12]))    
f814w.append(np.loadtxt(d[0][:,17]))

print d[0][:,1]
#chop = np.where(d[0][:,1])

diff = []

for i in range(6):
    diff.append(np.subtract(d[i][:,7], d[i][:,10]))
    

#for i in range(len(name)):
#    diff.append(np.subtract(d[i][:,7], d[i][:,10]))
    
#####################################################################
"""    
# Magnitude of the Milkyway Galaxy for 2010ae
ACS435   = 0.509 #F435W
ACS555   = 0.394 #F555W	
ACS625   = 0.313 #F625W	
ACS814   = 0.215 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod    = 30.58 

# Actual X & Y pixel coordinates of sn
xsn     = 1796.640
ysn     = 1931.995
radius  = 50.0 #pixels

f555Abs = []
for i in range(len(name)):
     f555Abs.append(float(data[i,10]) - dmod - ACS555)

f555Abs2 = []
for i in range(len(data2[:,10])):
     f555Abs2.append(float(data2[i,10]) - dmod - ACS555)

f555Abs3 = []
for i in range(len(data3[:,10])):
     f555Abs3.append(float(data3[i,10]) - dmod - ACS555)
     
f555Abs4 = []
for i in range(len(data4[:,10])):
     f555Abs4.append(float(data4[i,10]) - dmod - ACS555)

f555Abs5 = []
for i in range(len(data5[:,10])):
     f555Abs5.append(float(data5[i,10]) - dmod - ACS555)
"""
#####################################################################

print "Begin plotting Isochrones..."
h = [6, 6] # height of the plotted figure
plt.figure(num = 1, dpi = 100, figsize = [6, np.sum(h)], facecolor = 'w')
gs = gridspec.GridSpec(1, 1, height_ratios = h, hspace = 0.005)

c1plt = plt.subplot2grid((1,1), (0,0), colspan = 2)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.xlabel("F435W - F555W",fontdict = font)
plt.ylabel("F555W",fontdict = font)
#for m in range(len(name)):
#    c1plt.plot(d[m][:,2],d[m][:,4], label = 'Z = 0.'+name[m][1:-7]+' Y = 0.'+name[m][5:-4])
c1plt.scatter(diff[0],d[0][:,10], label = 'Z = 0.'+name[0][1:-7]+' Y = 0.'+name[0][5:-4])
#c1plt.plot(f435w[1],f555w[1], label = 'Z = 0.'+name[1][1:-7]+' Y = 0.'+name[1][5:-4])
#c1plt.plot(f435w[2],f555w[2], label = 'Z = 0.'+name[2][1:-7]+' Y = 0.'+name[2][5:-4])
#c1plt.plot(f435w[3],f555w[3], label = 'Z = 0.'+name[3][1:-7]+' Y = 0.'+name[3][5:-4])
#c1plt.plot(f435w[4],f555w[4], label = 'Z = 0.'+name[4][1:-7]+' Y = 0.'+name[4][5:-4])
#c1plt.plot(f435w[5],f555w[5], label = 'Z = 0.'+name[5][1:-7]+' Y = 0.'+name[5][5:-4])
c1plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
        ncol=2, mode="expand", borderaxespad=0.)

print "Save and show Isochrones..."
plt.savefig("Test.png")
"""

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

name = []

name = glob.glob('*.dat')

f     = open(name[0])
f2    = open(name[1])
f3    = open(name[2])
f4    = open(name[3])
f5    = open(name[4])

# 175 rows, start at 0, the max is at [174]
# Ignore the first 11 rows
row = [f.readline().strip().split() for i in range(175)]
row = np.array(row)

row2 = [f2.readline().strip().split() for i in range(175)]
row2 = np.array(row2)

row3 = [f3.readline().strip().split() for i in range(175)]
row3 = np.array(row3)

row4 = [f4.readline().strip().split() for i in range(175)]
row4 = np.array(row4)

row5 = [f5.readline().strip().split() for i in range(175)]
row5 = np.array(row5)

print row[:][0]
print row[:][1]
print row[:][2]
print row[:][3]
print row[:][4]
print row[:][5]
print row[:][6]
print row[:][7]
print row[:][8]
print row[:][9]
print row[:][10]

data = []
for i in range(11,175):
    data.append(row[:][i])
data = np.array(data)

diff = []
for i in range(len(data[:,10])):
    diff.append(np.subtract(float(data[i,7]), float(data[i,10])))
    
data2 = []
for i in range(11,175):
    data2.append(row2[:][i])
data2 = np.array(data2)

diff2 = []
for i in range(len(data2[:,10])):
    diff2.append(np.subtract(float(data2[i,7]), float(data2[i,10])))   
    
data3 = []
for i in range(11,175):
    data3.append(row3[:][i])
data3 = np.array(data3)

diff3 = []
for i in range(len(data3[:,10])):
    diff3.append(np.subtract(float(data3[i,7]), float(data3[i,10]))) 
    
data4 = []
for i in range(11,175):
    data4.append(row4[:][i])
data4 = np.array(data4)

diff4 = []
for i in range(len(data4[:,10])):
    diff4.append(np.subtract(float(data4[i,7]), float(data4[i,10]))) 
    
        
data5 = []
for i in range(11,175):
    data5.append(row5[:][i])
data5 = np.array(data5)

diff5 = []
for i in range(len(data5[:,10])):
    diff5.append(np.subtract(float(data5[i,7]), float(data5[i,10]))) 
#####################################################################
    
# Magnitude of the Milkyway Galaxy for 2010ae
ACS435   = 0 #F435W
ACS555   = 0 #F555W	
ACS625   = 0 #F625W	
ACS814   = 0 #F814W	

# Median (redshift independent) distance modulus of host galaxy
dmod    = 0 

# Actual X & Y pixel coordinates of sn
xsn     = 1796.640
ysn     = 1931.995
radius  = 50.0 #pixels

f555Abs = []
for i in range(len(data[:,10])):
     f555Abs.append(float(data[i,10]) - dmod - ACS555)

f555Abs2 = []
for i in range(len(data2[:,10])):
     f555Abs2.append(float(data2[i,10]) - dmod - ACS555)

f555Abs3 = []
for i in range(len(data3[:,10])):
     f555Abs3.append(float(data3[i,10]) - dmod - ACS555)
     
f555Abs4 = []
for i in range(len(data4[:,10])):
     f555Abs4.append(float(data4[i,10]) - dmod - ACS555)

f555Abs5 = []
for i in range(len(data5[:,10])):
     f555Abs5.append(float(data5[i,10]) - dmod - ACS555)

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
c1plt.plot(diff, f555Abs, label = 'CMD for Z = 0.'+name[0][1:-7]+' Y = 0.'+name[0][5:-4])
c1plt.plot(diff2, f555Abs2, label = 'CMD for Z = 0.'+name[1][1:-7]+' Y = 0.'+name[1][5:-4])
c1plt.plot(diff3, f555Abs3, label = 'CMD for Z = 0.'+name[2][1:-7]+' Y = 0.'+name[2][5:-4])
c1plt.plot(diff4, f555Abs4, label = 'CMD for Z = 0.'+name[3][1:-7]+' Y = 0.'+name[3][5:-4])
c1plt.plot(diff5, f555Abs5, label = 'CMD for Z = 0.'+name[4][1:-7]+' Y = 0.'+name[4][5:-4])
c1plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
        ncol=2, mode="expand", borderaxespad=0.1)

"""
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
print "Save and show Isochrones..."
plt.savefig("Test.png")
"""