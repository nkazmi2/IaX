# -*- coding: utf-8 -*-
"""
Created on Fri May 30 09:58:19 2014

@author: Nova
"""
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
"""
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
"""
"""
import pickle
#import glob
import numpy as np
title = 'sn2008ha'
catalog = []
catalog = pickle.load(open(title + '_List.p', 'rb'))

#print np.shape(catalog)
"""
"""
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

"""






#f625f814_4 = pickle.load(open( "sn2008ha_f625f814_r1_4.p", "rb" ))
#f435f555_5 = pickle.load(open( "sn2008ha_f435f555_r1_5.p", "rb" ))
#f625f814_5 = pickle.load(open( "sn2008ha_f625f814_r1_5.p", "rb" ))
#f435f555_6 = pickle.load(open( "sn2008ha_f435f555_r1_6.p", "rb" ))
#f625f814_6 = pickle.load(open( "sn2008ha_f625f814_r1_6.p", "rb" ))
#f435f555_7 = pickle.load(open( "sn2008ha_f435f555_r1_7.p", "rb" ))
#f625f814_7 = pickle.load(open( "sn2008ha_f625f814_r1_7.p", "rb" ))
#f435f555_8 = pickle.load(open( "sn2008ha_f435f555_r1_8.p", "rb" ))
#f625f814_8 = pickle.load(open( "sn2008ha_f625f814_r1_8.p", "rb" ))

    
"""
i = 3
for n in range(10): 
    i += 1
    if (n % 2 == 0): 
        print abs(n-(i))
    elif (n % 2 != 0):
        i += 1
        print abs((n)-(i)+1)
"""
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
"""
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
"""
f   = open('Z017Y26.dat')
row = []
row = [f.readline().strip().split() for i in range(16776)]
row = np.array(row)
"""
#d = []

#d.append(np.loadtxt('Z017Y26.dat'))
#d = np.array(d)
"""
for i in range(11,16776):#16765L, 21L
    d.append(row[:][i])
d = np.array(d)
"""
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
"""
age7   = np.where((d[:,:,0] >= 7.0) & (d[:,:,0] < 8.5))
age75   = np.where((d[:,:,0] >= 7.5) & (d[:,:,0] < 8.0))
age8   = np.where((d[:,:,0] >= 8.0) & (d[:,:,0] < 9.0))
age9   = np.where((d[:,:,0] >= 9.0) & (d[:,:,0] < 10.0))
age10  = np.where((d[:,:,0] >= 10.0) & (d[:,:,0] < 10.3))
age103 = np.where((d[:,:,0] == 10.3))
"""
"""
diff = []
for i in range(Length):
    diff.append(np.subtract(F435W[i,age], F555W[i,age]))
print np.shape(diff)
print len(F555W[age])
print diff[:][0]
print diff
"""

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
"""
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
"""
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
