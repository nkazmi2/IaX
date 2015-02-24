# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 13:33:54 2015

@author: nova
"""

#import numpy as np
#import random
"""
age = 7.5
print type(age)
start = age - .5
stop  = age + .5    
print start
print stop
for i in np.arange(start,stop,0.1):#for i in range(start, stop):
        print i
"""
#isonum = 7.74
#print str(round((10**isonum),-4))
#print str(round((10**isonum)*0.000001,2))
#print str(round((10**isonum)/100000.0,1))

#for i in np.arange(7.0,8.0,0.01):
    #print i

#print "\nF435W-F555W"

#print np.random.rand(3,1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

x_list = [0.3333333333333333, 0.2886751345948129, 0.25, 0.23570226039551587, 0.22360679774997896, 0.20412414523193154, 0.2, 0.16666666666666666]
y_list = [0.13250359351851854, 0.12098339583333334, 0.12398501145833334, 0.09152715, 0.11167239583333334, 0.10876248333333333, 0.09814170444444444, 0.08560799305555555]
y_err  = [0.003306749165349316, 0.003818446389148108, 0.0056036878203831785, 0.0036635292592592595, 0.0037034897788415424, 0.007576672222222223, 0.002981084130692832, 0.0034913019065973983]

# put x and y into a pandas DataFrame, and the weights into a Series
ws = pd.DataFrame({
    'x': x_list,
    'y': y_list
})
weights = pd.Series(y_err)

wls_fit = sm.wls('x ~ y', data=ws, weights=1 / weights).fit()
ols_fit = sm.ols('x ~ y', data=ws).fit()

# show the fit summary by calling wls_fit.summary()
# wls fit r-squared is 0.754
# ols fit r-squared is 0.701

# let's plot our data
plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, axisbg='w')
ws.plot(
    kind='scatter',
    x='x',
    y='y',
    style='o',
    alpha=1.,
    ax=ax,
    title='x vs y scatter',
    edgecolor='#ff8300',
    s=40
)

# weighted prediction
wp, = ax.plot(
    wls_fit.predict(),
    ws['y'],
    color='#e55ea2',
    lw=1.,
    alpha=1.0,
)
# unweighted prediction
op, = ax.plot(  
    ols_fit.predict(),
    ws['y'],
    color='k',
    ls='solid',
    lw=1,
    alpha=1.0,
)
leg = plt.legend(
    (op, wp),
    ('Ordinary Least Squares', 'Weighted Least Squares'),
    loc='upper left',
    fontsize=8)

plt.tight_layout()
fig.set_size_inches(6.40, 5.12)
plt.savefig("so.png", dpi=100, alpha=True)
plt.show()