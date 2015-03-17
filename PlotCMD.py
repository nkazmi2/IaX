# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:12:12 2015

@author: nova
"""
from __future__ import division
import numpy               as np
import matplotlib.pyplot   as plt
import matplotlib.gridspec as gridspec
import pickle
import random 
from   matplotlib.ticker  import MultipleLocator 
from   matplotlib.ticker  import AutoMinorLocator
from   matplotlib.patches import Polygon
from   itertools          import cycle

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
def AGEinfo(d, rawnum):
    logAGE = np.array(d[:,:,0])
    f435w  = np.array(d[:,:,7])
    f555w  = np.array(d[:,:,10])
    f625w  = np.array(d[:,:,12])
    f814w  = np.array(d[:,:,16])
    #limit  = np.array((logAGE >= (rawnum - .05)) & (logAGE <= (rawnum + .5)))
    age    = np.where(logAGE == rawnum)
    
    return f435w, f555w, f625w, f814w, age, logAGE
#####################################################################
def annot(SNannot,Apt435,Apt555,Ab555,Apt625,Apt814,Ab814,radR,radL,c1plt,c2plt):
    #Annotate!

    if (SNannot == 'sn08ge'):
        """
        for i in range(8):
            c1plt.annotate(str(i+1), xy=(np.subtract(Apt435[radL][i], Apt555[radL][i]),Ab555[radL][i]), 
               xytext=(np.subtract(Apt435[radL][i], Apt555[radL][i])+.2,Ab555[radL][i]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )   
        c1plt.annotate(str(25), xy=(np.subtract(Apt435[radL][8], Apt555[radL][8]),Ab555[radL][8]), 
               xytext=(np.subtract(Apt435[radL][8], Apt555[radL][8])+.2,Ab555[radL][8]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )  
        c1plt.annotate(str(14), xy=(np.subtract(Apt435[radL][9], Apt555[radL][9]),Ab555[radL][9]), 
               xytext=(np.subtract(Apt435[radL][9], Apt555[radL][9])+.2,Ab555[radL][9]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )  
        c1plt.annotate(str(19), xy=(np.subtract(Apt435[radL][10], Apt555[radL][10]),Ab555[radL][10]), 
               xytext=(np.subtract(Apt435[radL][10], Apt555[radL][10])+.2,Ab555[radL][10]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )  
        c1plt.annotate(str(21), xy=(np.subtract(Apt435[radL][11], Apt555[radL][11]),Ab555[radL][11]), 
               xytext=(np.subtract(Apt435[radL][11], Apt555[radL][11])+.2,Ab555[radL][11]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )  
        c1plt.annotate(str(22), xy=(np.subtract(Apt435[radL][12], Apt555[radL][12]),Ab555[radL][12]), 
               xytext=(np.subtract(Apt435[radL][12], Apt555[radL][12])+.2,Ab555[radL][12]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )  
        c1plt.annotate(str(26), xy=(np.subtract(Apt435[radL][13], Apt555[radL][13]),Ab555[radL][13]), 
               xytext=(np.subtract(Apt435[radL][13], Apt555[radL][13])+.2,Ab555[radL][13]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                ) 
        """
        for i in range(len(Apt625[radR])):
            c2plt.annotate(str(i+1), xy=(np.subtract(Apt625[radR][i], Apt814[radR][i]),Ab814[radR][i]), 
                xytext=(np.subtract(Apt625[radR][i], Apt814[radR][i])+.2,Ab814[radR][i]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )     
    ###############################
    elif (SNannot == 'sn08ha'):
        c1plt.annotate(str(29+i), xy=(np.subtract(Apt435[radL][i], Apt555[radL][i]),Ab555[radL][i]), 
                               xytext=(np.subtract(Apt435[radL][i], Apt555[radL][i])+.2,Ab555[radL][i]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))#facecolor='black', shrink=0.005),
         
        c1plt.annotate(str(3), xy=(np.subtract(Apt435[radL][4], Apt555[radL][4]),Ab555[radL][4]), 
                               xytext=(np.subtract(Apt435[radL][4], Apt555[radL][4])+.2,Ab555[radL][4]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))
        c1plt.annotate(str(33), xy=(np.subtract(Apt435[radL][5], Apt555[radL][5]),Ab555[radL][5]), 
                               xytext=(np.subtract(Apt435[radL][5], Apt555[radL][5])+.2,Ab555[radL][5]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))
        c1plt.annotate(str(8), xy=(np.subtract(Apt435[radL][6], Apt555[radL][6]),Ab555[radL][6]), 
                               xytext=(np.subtract(Apt435[radL][6], Apt555[radL][6])+.2,Ab555[radL][6]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))
        c1plt.annotate(str(34), xy=(np.subtract(Apt435[radL][7], Apt555[radL][7]),Ab555[radL][7]), 
                               xytext=(np.subtract(Apt435[radL][7], Apt555[radL][7])+.2,Ab555[radL][7]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))
        c1plt.annotate(str(9), xy=(np.subtract(Apt435[radL][8], Apt555[radL][8]),Ab555[radL][8]), 
                               xytext=(np.subtract(Apt435[radL][8], Apt555[radL][8])+.2,Ab555[radL][8]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))
        c1plt.annotate(str(35), xy=(np.subtract(Apt435[radL][9], Apt555[radL][9]),Ab555[radL][9]), 
                               xytext=(np.subtract(Apt435[radL][9], Apt555[radL][9])+.2,Ab555[radL][9]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))      
        c1plt.annotate(str(36), xy=(np.subtract(Apt435[radL][10], Apt555[radL][10]),Ab555[radL][10]), 
                               xytext=(np.subtract(Apt435[radL][10], Apt555[radL][10])+.2,Ab555[radL][10]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))  
        c1plt.annotate(str(37), xy=(np.subtract(Apt435[radL][11], Apt555[radL][11]),Ab555[radL][11]), 
                               xytext=(np.subtract(Apt435[radL][11], Apt555[radL][11])+.2,Ab555[radL][11]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",))  
        for i in range(len(Apt625[radR])):
            c2plt.annotate(str(i+1), xy=(np.subtract(Apt625[radR][i], Apt814[radR][i]),Ab814[radR][i]), 
                xytext=(np.subtract(Apt625[radR][i], Apt814[radR][i])+.2,Ab814[radR][i]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )         
    ###############################
    elif (SNannot == 'sn10ae'):
        """for i in range(len(Apt435[radL])-1):
            c1plt.annotate(str(i+1), xy=(np.subtract(Apt435[radL][i], Apt555[radL][i]),Ab555[radL][i]), 
                               xytext=(np.subtract(Apt435[radL][i], Apt555[radL][i])+.2,Ab555[radL][i]-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                                )               
        #c1plt.annotate(str(17), xy=(np.subtract(Apt435[radL][15], Apt555[radL][15]),Ab555[radL][15]), 
        #                       xytext=(np.subtract(Apt435[radL][15], Apt555[radL][15])+.2,Ab555[radL][15]-.2),
        #                        #textcoords='offset points',
        #                         arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
        #                         )   
        #c1plt.annotate(str(18), xy=(np.subtract(Apt435[radL][16], Apt555[radL][16]),Ab555[radL][16]), 
        #                       xytext=(np.subtract(Apt435[radL][16], Apt555[radL][16])+.2,Ab555[radL][16]-.2),
        #                        #textcoords='offset points',
        #                         arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
        #                         ) 
        #    
        c1plt.annotate(str(6), xy=(np.subtract(Apt435[radL][4], Apt555[radL][4]),Ab555[radL][4]), 
                               xytext=(np.subtract(Apt435[radL][4], Apt555[radL][4])+.2,Ab555[radL][4]-.2),
                                #textcoords='offset points',
                                 arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                                 )                           
        for i in range(len(Apt625[radR])):
            c2plt.annotate(str(i+1), xy=(np.subtract(Apt625[radR][i], Apt814[radR][i]),Ab814[radR][i]), 
                xytext=(np.subtract(Apt625[radR][i], Apt814[radR][i])+.2,Ab814[radR][i]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )   
        """
        for i in range(len(Apt435[radL])-1):
            c1plt.annotate(str(i+1), xy=(np.subtract(Apt435[radL][i]+2.052, Apt555[radL][i]+1.588),Ab555[radL][i]+1.588), 
                               xytext=(np.subtract(Apt435[radL][i]+2.052, Apt555[radL][i]+1.588)+.2,Ab555[radL][i]+1.588-.2),
                                #textcoords='offset points',
                                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                                )               

        c1plt.annotate(str(6), xy=(np.subtract(Apt435[radL][4]+2.052, Apt555[radL][4]+1.588),Ab555[radL][4]+1.588), 
                               xytext=(np.subtract(Apt435[radL][4]+2.052, Apt555[radL][4]+1.588)+.2,Ab555[radL][4]+1.588-.2),
                                #textcoords='offset points',
                                 arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                                 )                   
        for i in range(len(Apt625[radR])):
            c2plt.annotate(str(i+1), xy=(np.subtract(Apt625[radR][i]+1.262, Apt814[radR][i]+0.867),Ab814[radR][i]+0.867), 
                xytext=(np.subtract(Apt625[radR][i]+1.262, Apt814[radR][i]+0.867)+.2,Ab814[radR][i]+0.867-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )        
    ###############################
    elif (SNannot == 'sn10el'):
        for i in range(len(Apt435[radL])):
            c1plt.annotate(str(i+1), xy=(np.subtract(Apt435[radL][i], Apt555[radL][i]),Ab555[radL][i]), 
               xytext=(np.subtract(Apt435[radL][i], Apt555[radL][i])+.2,Ab555[radL][i]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )               
            #c1plt.annotate(str(7), xy=(np.subtract(Apt435[radL][5], Apt555[radL][5]),Ab555[radL][5]), 
            #     xytext=(np.subtract(Apt435[radL][5], Apt555[radL][5])+.2,Ab555[radL][5]-.2),
            #     #textcoords='offset points',
            #     arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
            #     )   
              
        for i in range(len(Apt625[radR])):
            c2plt.annotate(str(i+1), xy=(np.subtract(Apt625[radR][i], Apt814[radR][i]),Ab814[radR][i]), 
                xytext=(np.subtract(Apt625[radR][i], Apt814[radR][i])+.2,Ab814[radR][i]-.2),
                #textcoords='offset points',
                arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
                )          
    """
    c1plt.annotate(str(10), xy=(np.subtract(Apn435[s2][3], Apn555[s2][3]),Abs555[s2][3]), 
               xytext=(np.subtract(Apn435[s2][3], Apn555[s2][3])-.1,Abs555[s2][3]-.1),
                arrowprops=dict(arrowstyle="->",) )
        c1plt.annotate(str(11), xy=(np.subtract(Apn435[s2][4], Apn555[s2][4]),Abs555[s2][4]), 
               xytext=(np.subtract(Apn435[s2][4], Apn555[s2][4])-.1,Abs555[s2][4]-.1),
                arrowprops=dict(arrowstyle="->",) )
                     
    for i in range(3):
        c1plt.annotate(str(i+1), xy=(np.subtract(Apn435[s2][i], Apn555[s2][i]),Abs555[s2][i]), 
               xytext=(np.subtract(Apn435[s2][i], Apn555[s2][i])+.1,Abs555[s2][i]-.1),
                #textcoords='offset points',
            arrowprops=dict(arrowstyle="->",)#facecolor='black', shrink=0.005),
            )  
    
    for i in range(len(f435f555[0][0])):
    c1plt.annotate('', xy=(np.subtract(f435f555[0][2][i],   f435f555[0][3][i]),f435f555[0][3][i]), 
            xycoords = 'data', #(Top of the arrow)
            xytext = (np.subtract(f435f555[0][2][i],   f435f555[0][3][i])+.5,f435f555[0][3][i]+.5), textcoords = 'data', # End of the arrow
           arrowprops = {'arrowstyle':'->'})
    #c1plt.annotate('S'+str(i+1), xy=(0.2,-5.2), xycoords = 'data',
    #             xytext = (np.subtract(f435f555[0][2][i],   f435f555[0][3][i]),f435f555[0][3][i]), 
    #            textcoords = 'offset points')
                
    """
#####################################################################
def iso(c1plt,c2plt,supname,isoAGE,isonum,f435,f555,f625,f814,h435,h555,h625,h814,a435,a555,a625,a814,isoall,decredhost,decrange): 
                
    #c1plt.plot(np.subtract(F435W[AGE], F555W[AGE]), F555W[AGE],  
    #          'k--' , label = 'Age = 10$^{' + str(iag) + '}$ yrs')

    #c2plt.plot(np.subtract(F625W[AGE],  F814W[AGE]),  F814W[AGE],  
    #      'k--', label = 'Age = 10$^{' + str(iag) + '}$ yrs')
                 
    #c1plt.plot(np.subtract(np.subtract(f435[isoAGE],h435), np.subtract(f555[isoAGE],h555)), 
     #       np.subtract(f555[isoAGE],h555),  
     #      'k--' , label = 'Age = 10$^{' + str(isonum) + '}$ yrs')

    #c2plt.plot(np.subtract(np.subtract(f625[isoAGE],h625), np.subtract(f814[isoAGE],h814)),
           # np.subtract(f814[isoAGE],h814),  
           #'k--', label = 'Age = 10$^{' + str(isonum) + '}$ yrs')   
    
    if (decrange == 'y'):
        num = []
        start = isonum - .05
        stop  = isonum + .06 
    
        for i in np.arange(start,stop,0.01):
            #age.append(np.where(LogAge == i))
            num.append(round(i,2))       
        
        # assigning age arrays to one array so that I can loop through it
        age0    = np.where(isoall == num[0])
        age1    = np.where(isoall == num[1])
        age2    = np.where(isoall == num[2])
        age3    = np.where(isoall == num[3])
        age4    = np.where(isoall == num[4])
        age5    = np.where(isoall == num[5])
        age6    = np.where(isoall == num[6])
        age7    = np.where(isoall == num[7])
        age8    = np.where(isoall == num[8])
        age9    = np.where(isoall == num[9])
        age10   = np.where(isoall == num[10])
    
        age = [age0,age1,age2,age3,age4,age5,age6,age7,age8,age9,age10]
        if (decredhost == 'y'):
            for ageInd in xrange(len(age)):
                colors = np.random.rand(4,1)
                c1plt.plot(np.subtract((np.add(f435[age[ageInd]],h435)), (np.add(f555[age[ageInd]],h555))), 
                           (np.add(f555[age[ageInd]],h555)), 
                            c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
                c2plt.plot(np.subtract((np.add(f625[age[ageInd]],h625)), (np.add(f814[age[ageInd]],h814))),
                           (np.add(f814[age[ageInd]],h814)), 
                            c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
        else:
            for ageInd in xrange(len(age)):
                colors = np.random.rand(4,1)
                c1plt.plot(np.subtract(f435[age[ageInd]],f555[age[ageInd]]), 
                       f555[age[ageInd]], c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
                c2plt.plot(np.subtract(f625[age[ageInd]],f814[age[ageInd]]),
                       f814[age[ageInd]], c = colors, label = str(round((10**num[ageInd])*0.000001,2)) + ' Myrs')
    else:
        print "No age range" 
        
    if (decredhost == 'y'):
        print "Reddening by the host galaxy"
        c1plt.plot(np.subtract((np.add(f435[isoAGE],h435)), (np.add(f555[isoAGE],h555))), 
             (np.add(f555[isoAGE],h555)),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#'Age = 10$^{' + str(isonum) + '}$ yrs')
        c2plt.plot(np.subtract((np.add(f625[isoAGE],h625)), (np.add(f814[isoAGE],h814))),
             (np.add(f814[isoAGE],h814)),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#''Age = 10$^{' + str(isonum) + '}$ yrs')
    else:
        c1plt.plot(np.subtract((f435[isoAGE]), (f555[isoAGE])),(f555[isoAGE]),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#'Age = 10$^{' + str(isonum) + '}$ yrs')

        c2plt.plot(np.subtract((f625[isoAGE]), (f814[isoAGE])),(f814[isoAGE]),  
             'k-', lw = 1.0, label = str(round((10**isonum)*0.000001,2)) + ' Myrs')#''Age = 10$^{' + str(isonum) + '}$ yrs')
    
    #This one calculates both the MW and Host reddening
    #c1plt.plot(np.subtract((f435[isoAGE]-a435-h435), (f555[isoAGE]-a555-h555)), 
    #         (f555[isoAGE]-a555-h555),  
    #       'k--' , label = 'Age = 10$^{' + str(isonum) + '}$ yrs')

    #c2plt.plot(np.subtract((f625[isoAGE]-a625-h625), (f814[isoAGE]-a814-h814)),
    #        (f814[isoAGE]-a814-h814),  
    #       'k--', label = 'Age = 10$^{' + str(isonum) + '}$ yrs')
#####################################################################
def met(title):
    d = []
    if (title == 'sn08ha'):
        name = 'Z0060Y26.dat'
    elif (title == 'sn10ae'):
        name = 'Z0096Y26.dat'
    elif (title == 'sn10el'):
        name = 'Z0224Y26.dat'
    elif (title == 'sn08ge'):
        name = 'Z0314Y26.dat'
    d.append(np.loadtxt('Metallicity/'+name))
    d = np.array(d)                
    return d, name
#####################################################################  
def save(name):
    #figname = title + '_' + 'Z' + name[1:-7]+ '.png'
    figname = name + '_' + 'test00' + '.png'
    plt.savefig('Figures/'+ figname)
    print "Save and show plot : " + figname
#####################################################################     
def shade(sn435,sn555,sn625,sn814,yLmax,yRmax,c1plt,c2plt):
    #############
    s1 = -1 
    b1 = -4.0
    x2 = 5#3
    y1 = (s1*x2) + b1
    x1 = sn435 - sn555 #.48# np.subtract(horz1,b1)/s1
    ptsR = []
    ptsR = np.array([[-3,yLmax+4],
                     [-3,sn555],
                     [x1,sn555], #need the x value
                     [x2,y1],           
                     [x2,yLmax+4]])
    polyR = Polygon(ptsR, color='DarkSlateGray', alpha=0.15,closed = True)

    c1plt.add_patch(polyR)
    #############
    s4 = -1 
    b4 = -5.0
    x4 = 5#3 
    y4 = (s4*x4) + b4
    x3 = sn625 - sn814  #.1#np.subtract(horz,b4)/s4
    ptsL = []
    ptsL = np.array([[-3,yRmax+4],
                    [-3,sn814],
                    [x3,sn814], 
                    [x4,y4],           
                    [x4,yRmax+4]])
    polyL = Polygon(ptsL, color='DarkSlateGray', alpha=0.15,closed = True)
    
    c2plt.add_patch(polyL)
#####################################################################

def SNinfo(filename):
    f435f555   = []
    f625f814   = []  
    allobjects = []
    # [dist, conver,                 0, 1,
    # yLmax, yLmin, yRmax, yRmin,    2, 3, 4, 5,
    # xLmax, xLmin, xRmax, xRmin,    6, 7, 8, 9,
    # sn435, sn555, sn625, sn814,    10,11,12,13,
    # age,                           14,   
    # H435,H555,H625,H814,           15,16,17,18,
    # ACS435,ACS555,ACS625,ACS814]   19,20,21,22
    File = []
    if (filename == 'sn08ge'):
        radius = [16.09,34.47,200]#70,150,220  #[34.47,50.56,115]#100.95,200,500
        File = 'SN2008GE'
        info   = [17.95e6,(4.3512), 
                -3.0,-14,-3.0,-14,   #-1.0,-8.5,-3.0,-9.5,   #-4.5, -6.8,-5,-7.7,            
                -3.0,  5.0, -3.0,  5.0,#-0.5,  2.0, -0.5,  2.5, #
                -4.678,-5.388,-5.566,-5.172,
                7.28,
                0.0,0.0,0.0,0.0, 
                0.046,0.036,0.028,0.020] 
    elif (filename == 'sn08ha'):
        radius = [15,30,45]#72.7221, 145.242, 217.863
        File = 'SN2008HA'
        info   = [20e6, (4.8414), 
                -3.50, -6.5, -4.00, -7.0, 
                -0.75,  2.0, -0.75,  2.0,
                -4.04, -4.5, -4.30, -4.5,
                 7.74,
                 0.0,0.0,0.0,0.0,
                 0.284,0.219,0.174,0.120]
    elif (filename == 'sn10ae'):
        radius = [21.5,46,68]#75,146.07,217.863
        File = 'SN2010AE'        
        info   = [13.1e6, (3.17553), 
                -5.50, -8.5, -5.00, -9.0,#-4.0, -7.0, -4.5, -7.5,
                -0.5,  1.8, -0.5,  1.6,#-0.75,  3.5, -0.75,  4.0,
                -6.088,-5.910,-5.677,-5.518,#-4.036,-4.321,-4.415,-4.651, 
                 7.15,
                 2.052,1.588,1.262,0.867,
                 0.509,0.394,0.313,0.215]
    elif (filename == 'sn10el'):
        radius = [29,62,90]#70, 150,220
        File = 'SN2010EL'        
        info   = [9.97e6, (2.4168), 
                -4.0, -8.5, -4.0, -8.0, 
                -0.5,  2.0, -0.75,  2.3,
                -6.122,-5.887,-5.497,-4.547,#-2.867,-3.370,-3.496,-3.171
                 7.29,
                 3.255,2.517,2.001,1.376,
                 0.033,0.025,0.020,0.014]
    f435f555.append(pickle.load(open(str(File)   + '/' + str(filename) + 'f435f555.p', 'rb')))    
    f625f814.append(pickle.load(open(str(File)   + '/' + str(filename) + 'f625f814.p', 'rb')))    
    allobjects.append(pickle.load(open(str(File) + '/' + str(filename) + 'all.p', 'rb')))    

    return radius, info, f435f555, f625f814, allobjects, File
#####################################################################
########################### PICK THE SN!! ###########################
#####################################################################
def main():
    #Abs435 = [] 
    Abs555 = [] 
    #Abs625 = [] 
    Abs814 = []
    Apn435 = [] 
    Apn555 = []
    Apn625 = []
    Apn814 = [] 
    UncXl  = [] 
    UncYl  = []
    UncXr  = [] 
    UncYr  = [] 
    #SN435  = [] 
    #SN555  = []
    #SN625  = [] 
    #SN814  = []
    Radl   = [] 
    Radr   = []   
    ###########################################################################
    print 'Which SNe do you wanna plot?'
    print 'sn08ge \nsn08ha \nsn10ae \nsn10el'
    
    SNname = raw_input('Choose a Supernova:')
    
    print ('You picked %s' %(SNname))
    
    check = raw_input('Is this correct? (y/n)')
    if (check == 'y'):
        print "Let's begin!"
    else:
        SNname = []    
        print "Let's try again"
        SNname = raw_input('Choose a Supernova:')
        print ('You picked %s' %(SNname))
    
    decann  = raw_input('Do you want to annotate the fig   (y/n):')
    decmet  = raw_input('Do you want to plot the isochrone (y/n):')
    decrange= raw_input('Do you want to plot age range?    (y/n):')
    dechost = raw_input('Isochrone reddening, Host Galaxy  (y/n):')
    decshd  = raw_input('Do you want to shade S/N          (y/n):')
    deccol  = raw_input('Would you rather make a Col-Col?  (y/n):')
    decsave = raw_input('Do you want to save the figure    (y/n):')

    ###########################################################################
    radius, info, f435f555, f625f814, AllObjects, File = SNinfo(SNname)
    #dist   = info[0]
    conver = info[1]
    
    yLmax  = info[2]
    yLmin  = info[3]
    yRmax  = info[4]
    yRmin  = info[5]
    
    xLmax  = info[6]
    xLmin  = info[7]
    xRmax  = info[8]
    xRmin  = info[9]
    
    sn435 = info[10]
    sn555 = info[11]
    sn625 = info[12]
    sn814 = info[13]
    iag   = info[14]
    
    H435  = info[15]
    H555  = info[16]
    H625  = info[17]
    H814  = info[18]
    
    ACS435= info[19]
    ACS555= info[20]
    ACS625= info[21]
    ACS814= info[22]
    
    #Abs435 = f435f555[0][0] 
    Abs555 = f435f555[0][1] 
    Apn435 = f435f555[0][2] 
    Apn555 = f435f555[0][3] 
    UncXl  = f435f555[0][4] 
    UncYl  = f435f555[0][5] 
    #SN435  = f435f555[0][6] 
    #SN555  = f435f555[0][7]
    Radl   = f435f555[0][8] 

    s0 = np.where(Radl <= radius[0])
    s1 = np.where(Radl <= radius[1])
    s2 = np.where(Radl <= radius[2])
    
    #Abs625 = f625f814[0][0] 
    Abs814 = f625f814[0][1]
    Apn625 = f625f814[0][2]
    Apn814 = f625f814[0][3] 
    UncXr  = f625f814[0][4] 
    UncYr  = f625f814[0][5] 
    #SN625  = f625f814[0][6] 
    #SN814  = f625f814[0][7] 
    Radr   = f625f814[0][8] 
 
    Abs435_all = AllObjects[0][0] 
    Abs555_all = AllObjects[0][1] 
    Abs625_all = AllObjects[0][2] 
    Abs814_all = AllObjects[0][3] 
    
    #Apn435_all = AllObjects[0][4]
    #Apn555_all = AllObjects[0][5]
    #Apn625_all = AllObjects[0][6]
    #Apn814_all = AllObjects[0][7]
    
    #UncYr_all  = AllObjects[0][8] 
    #UncXr_all  = AllObjects[0][9] 
    
    #unc435_all = AllObjects[0][10]
    #unc555_all = AllObjects[0][11]
    #unc625_all = AllObjects[0][12]
    #unc814_all = AllObjects[0][13]
    
    #SN435_all  = AllObjects[0][14] 
    #SN555_all  = AllObjects[0][15] 
    #SN625_all  = AllObjects[0][16] 
    #SN814_all  = AllObjects[0][17] 
    
    #Radr_all   = AllObjects[0][18] 
    
    r0 = np.where(Radr <= radius[0])
    r1 = np.where(Radr <= radius[1])
    r2 = np.where(Radr <= radius[2])
    
    ###########################################################################
    MetFile = []
    F435W   = []
    F555W   = []
    F625W   = []
    F814W   = []
    AGE     = []
    Metname = []
    ISOALL  = []
    
    if (decmet  == 'y'):
        MetFile, Metname = met(SNname)    
        MetFile = np.array(MetFile)  
        #print d
        #print np.shape(d) #(1L, 16776L, 21L)
        F435W, F555W, F625W, F814W, AGE, ISOALL = AGEinfo(MetFile, iag)
    else:    
        print "No isochrone"
    ###########################################################################
    print "Begin plotting Isochrones..."
    h = [2, 4] # height of the plotted figure
    fig1 = plt.figure(num = 1, dpi = 100, figsize = [9, np.sum(h)], facecolor = 'w')
    gs = gridspec.GridSpec(2, 1, height_ratios = h, hspace = 0.005)

    if (decmet  == 'y'):
        fig1.suptitle('SN 20' + SNname[2:] + ': CMD for Z = 0.' + Metname[1:-7] + ', Y = 0.' + Metname[6:-4], 
            fontdict = font, size=15)
    else:
        fig1.suptitle(SNname + ': Color Mag Diagram', fontdict = font, size=15)

    ###########################################################################
    c1plt = plt.subplot2grid((2,2), (0,0), rowspan = 2)
    plt.gca().invert_yaxis()
    if (deccol == 'y'):
        plt.xlabel("F435W - F555W (mag)",fontdict = font)
        plt.ylabel("F625W - F814W (mag)",fontdict = font)
    else:
        plt.xlabel("F435W - F555W (mag)",fontdict = font)
        plt.ylabel("M$_{F555W}$ (mag)",fontdict = font)

    #c1plt.xaxis.set_minor_locator(AutoMinorLocator()) 
    #c1plt.yaxis.set_minor_locator(AutoMinorLocator())

    #c1plt.yaxis.set_major_locator(MultipleLocator(.5))
    #c1plt.xaxis.set_major_locator(MultipleLocator(.5))
    ###########################################################################
    
    if (SNname == 'notyet'):  
        print "Plotting SN 2010el"
        c1plt.annotate('', xy=(1.1, -5.417), xycoords = 'data',
                 xytext = (1.838, -2.9), textcoords = 'data',
                    arrowprops = {'arrowstyle':'->'})
        c1plt.annotate('A${_v}}$ = 3.4105', xy=(0.3,-5.2), xycoords = 'data',
                 xytext = (2, 3), textcoords = 'offset points')
        
        age_num = [7.6] 
        for i in range(len(age_num)):
            c1plt.plot(np.subtract((F435W[np.where(ISOALL == age_num[i])]-ACS435-H435), (F555W[np.where(ISOALL == age_num[i])]-ACS555-H555)), 
                       (F555W[np.where(ISOALL == age_num[i])]-ACS555-H555),  
                       c=np.random.rand(3,), label = 'Age = 10$^{' + str(age_num[i]) + '}$ yrs')
        print "Plotting SN 2010el"
    else: 
       print "Plotting SN...."

    ###########################################################################
    if (dechost == 'y'):
        c1plt.scatter(np.subtract(np.add(Apn435[s2],H435),   np.add(Apn555[s2],H555)),
               np.add(Abs555[s2],H555), label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)          
        c1plt.scatter(np.subtract(np.add(Apn435[s1],H435),   np.add(Apn555[s1],H555)),
               np.add(Abs555[s1],H555), label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)  
        c1plt.errorbar(np.subtract(np.add(Apn435[s0],H435),  np.add(Apn555[s0],H555)),   
               np.add(Abs555[s0],H555), UncXl[s0],   UncYl[s0], 
               fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(np.add(Apn435[s0],H435),   np.add(Apn555[s0],H555)),
               np.add(Abs555[s0],H555), label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
               c='k',marker='o',s = 25.0)  
    elif (deccol == 'y'):
        c1plt.scatter(np.subtract(Abs435_all[s2],Abs555_all[s2]),
                      np.subtract(Abs625_all[s2],Abs814_all[s2]), label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)          
        c1plt.scatter(np.subtract(Abs435_all[s1],Abs555_all[s1]),
                      np.subtract(Abs625_all[s1],Abs814_all[s1]), label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)  
        #c1plt.errorbar(np.subtract(Apn435[s0],Apn555[s0]),
        #               np.subtract(Apn625[r0],Apn814[r0]), 
        #               np.subtract(UncXl[s0]),
        #               np.subtract(UncYl[s0]), 
        #               fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(Abs435_all[s0],Abs555_all[s0]),
                      np.subtract(Abs625_all[s0],Abs814_all[s0]), label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
                      c='k',marker='o',s = 25.0)
    else: 
        #c1plt.errorbar(np.subtract(Apn435[s2],Apn555[s2]),Abs555[s2], UncXl[s2],   UncYl[s2], 
        #       fmt=None, ecolor="k", marker=None, mew=0 )              
        c1plt.scatter(np.subtract(Apn435[s2],Apn555[s2]),Abs555[s2], label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)       

        #c1plt.errorbar(np.subtract(Apn435[s1],Apn555[s1]),Abs555[s1], UncXl[s1],   UncYl[s1], 
        #       fmt=None, ecolor="k", marker=None, mew=0 )               
        c1plt.scatter(np.subtract(Apn435[s1],Apn555[s1]),Abs555[s1], label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)  

        c1plt.errorbar(np.subtract(Apn435[s0],Apn555[s0]),Abs555[s0], UncXl[s0],   UncYl[s0], 
               fmt=None, ecolor="k", marker=None, mew=0 )
        c1plt.scatter(np.subtract(Apn435[s0],Apn555[s0]),Abs555[s0], label = 'R = ' + str(round(radius[0]*conver,-1))  + " pc" ,
               c='k',marker='o',s = 25.0)  
    
    ###########################################################################
    c2plt = plt.subplot2grid((2,2), (0,1), rowspan = 2)
    plt.gca().invert_yaxis()
    if (deccol == 'y'):
        plt.xlabel("F625W - F814W (mag)",fontdict = font)
        plt.ylabel("F435W - F555W (mag)",fontdict = font)
    else:
        plt.xlabel("F625W - F814W (mag)",fontdict = font)
        plt.ylabel("M$_{F814W}$ (mag)",fontdict = font)
    
    c2plt.tick_params(axis='both',labelbottom = font)
                      
    #c2plt.xaxis.set_minor_locator(AutoMinorLocator()) 
    #c2plt.yaxis.set_minor_locator(AutoMinorLocator())
    
    #c2plt.yaxis.set_major_locator(MultipleLocator(.5))
    #c2plt.xaxis.set_major_locator(MultipleLocator(.5))
    ###########################################################################
 
    if (SNname == 'notyet'):  
        c2plt.annotate('', xy=(1.0, -5.376), xycoords = 'data',
                 xytext = (1.625, -4), textcoords = 'data',
                    arrowprops = {'arrowstyle':'->'})
        c2plt.annotate('A${_v}}$ = 2.2016', xy=(.9,-3.8), xycoords = 'data',
                 xytext = (2, 3), textcoords = 'offset points')
        
        
        age_num = [7.7,7.80,7.85,7.9,8.0] 
        for i in range(len(age_num)):
            #c1plt.plot(np.subtract((F435W[np.where(ISOALL == age_num[i])]-ACS435-H435), (F555W[np.where(ISOALL == age_num[i])]-ACS555-H555)), 
            #           (F555W[np.where(ISOALL == age_num[i])]-ACS555-H555),  
            #           c=np.random.rand(3,), label = 'Age = 10$^{' + str(age_num[i]) + '}$ yrs')

            c2plt.plot(np.subtract((F625W[np.where(ISOALL == age_num[i])]-ACS625-H625), (F814W[np.where(ISOALL == age_num[i])]-ACS814-H814)),
                       (F814W[np.where(ISOALL == age_num[i])]-ACS814-H814),  
                       c=np.random.rand(3,), label = 'Age = 10$^{' + str(age_num[i]) + '}$ yrs')                   
        print "Plotting SN...."       
    else: 
        print "Plotting SN...."
    ###########################################################################
    if (dechost == 'y'):
        c2plt.scatter(np.subtract(np.add(Apn625[r2],H625),   np.add(Apn814[r2],H814)),
               np.add(Abs814[r2],H814), label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
               c='w',marker='o',s = 10.0)          
        c2plt.scatter(np.subtract(np.add(Apn625[r1],H625),   np.add(Apn814[r1],H814)),
               np.add(Abs814[r1],H814), label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 10.0)
        c2plt.errorbar(np.subtract(np.add(Apn625[r0],H625),  np.add(Apn814[r0],H814)),   
               np.add(Abs814[r0],H814), UncXr[r0],   UncYr[r0], 
               fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(np.add(Apn625[r0],H625),   np.add(Apn814[r0],H814)),
               np.add(Abs814[r0],H814), label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
               c='k',marker='o',s = 25.0)  
    elif (deccol == 'y'):
        c2plt.scatter(np.subtract(Abs625_all[r2],Abs814_all[r2]),
                      np.subtract(Abs435_all[r2],Abs555_all[r2]), 
                      label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)          
        c2plt.scatter(np.subtract(Abs625_all[r1],Abs814_all[r1]),
                      np.subtract(Abs435_all[r1],Abs555_all[r1]),
                      label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)
        #c2plt.errorbar(np.subtract(Apn625[r0],Apn814[r0]),
        #               np.subtract(Apn435[s0],Apn555[s0]), 
        #               np.subtract(UncXr[r0]),
        #               np.subtract(UncYr[r0]), fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(Abs625_all[r0],Abs814_all[r0]),
                      np.subtract(Abs435_all[r0],Abs555_all[r0]), 
                      label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 25.0) 
    else:
        #c2plt.errorbar(np.subtract(Apn625[r2],Apn814[r2]),Abs814[r2], 
        #               UncXr[r2],   UncYr[r2], fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(Apn625[r2],Apn814[r2]),Abs814[r2], 
                      label = 'R = ' + str(round(radius[2]*conver,-1)) + " pc" ,
                      c='w',marker='o',s = 10.0)   

        #c2plt.errorbar(np.subtract(Apn625[r1],Apn814[r1]),Abs814[r1], 
        #               UncXr[r1],   UncYr[r1], fmt=None, ecolor="k", marker=None, mew=0 )        
        c2plt.scatter(np.subtract(Apn625[r1],Apn814[r1]),Abs814[r1], 
                      label = 'R = ' + str(round(radius[1]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 10.0)

        c2plt.errorbar(np.subtract(Apn625[r0],Apn814[r0]),Abs814[r0], 
                       UncXr[r0],   UncYr[r0], fmt=None, ecolor="k", marker=None, mew=0 )
        c2plt.scatter(np.subtract(Apn625[r0],Apn814[r0]),Abs814[r0], 
                      label = 'R = ' + str(round(radius[0]*conver,-1)) + " pc" ,
                      c='k',marker='o',s = 25.0)  
 
 
    ########################################################################### 
    if (decmet  == 'y'):
        iso(c1plt,c2plt,SNname,AGE,iag,F435W,F555W,F625W,F814W,H435,H555,H625,H814,ACS435,ACS555,ACS625,ACS814,ISOALL,dechost,decrange)   
    else:
        print "Moving along"
    ###########################################################################  
    if (decann  == 'y'):
        annot(SNname,Apn435,Apn555,Abs555,Apn625,Apn814,Abs814,r2,s2,c1plt,c2plt)
    else:
        print "No annotations"      
    ###########################################################################  
    if (decshd  == 'y'):
        if (dechost == 'y'):
            sn435 = np.add(sn435, H435)
            sn555 = np.add(sn555, H555)
            sn625 = np.add(sn625, H625)
            sn814 = np.add(sn814, H814)
            shade(sn435,sn555,sn625,sn814,yLmax,yRmax,c1plt,c2plt)
        else:
            shade(sn435,sn555,sn625,sn814,yLmax,yRmax,c1plt,c2plt)
    else:
        print "No shading"       
        
    ########################################################################### 
    lL = c1plt.legend(prop = {'family' : 'serif'},loc=4)
    lL.draw_frame(False)

    lR = c2plt.legend(prop = {'family' : 'serif'},loc=4)
    lR.draw_frame(False)
    ########################################################################### 
    if (dechost == 'y'):    
        c1plt.set_ylim(bottom=np.add(yLmax,H555)             , top=np.add(yLmin,H555))
        c1plt.set_xlim(np.subtract(np.add(xLmax,H435),H555)  , np.subtract(np.add(xLmin,H435),H555))
        c2plt.set_ylim(bottom=np.add(yRmax,H814)             , top=np.add(yRmin,H814))          
        c2plt.set_xlim(np.subtract(np.add(xRmax,H625),H814)  , np.subtract(np.add(xRmin,H625),H814))
    elif (deccol == 'y'):     
        "No figure formating"
    else:  
        "No figure formating"
        #c1plt.set_ylim(bottom=yLmax, top=yLmin)
        #c1plt.set_xlim(xLmax,xLmin)
        #c2plt.set_ylim(bottom=yRmax, top=yRmin)  
        #c2plt.set_xlim(xRmax,xRmin)        
    
    ########################################################################### 
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    ########################################################################### 
    if (decsave == 'y'):
        save(SNname)
    else:
        print "Not saving"
    ########################################################################### 

main()