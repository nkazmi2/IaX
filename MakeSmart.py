import numpy as np
#import csv
import pandas
import pickle
import pyregion
################################################### 

def cutdata(SNname, sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn, ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord,
            badX, badY,
            badXL, badYL,
            srp435,srp555,srp625,srp814,
            rnd435,rnd555,rnd625,rnd814,
            crd435,crd555,crd625,crd814,
            TotalSigN):
    print "Make final cuts for", SNname 
    cutL = []
    cutR = []
    cuteverything = []
    if (SNname == 'sn08ha'):
        cutL.append(np.where((star <= 2) 
                & (TotalSigN >=3)
                & (crowd <= crowdmax ) 
                & (crd435 <= .5) & (crd555 <= .36)
                & (crd625 <= .46) & (crd814 <= .75)
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (srp435 <= .15) & (srp555 <= .42)
                & (srp625 <= .16) & (srp814 <= .23)
                & (srp435 >= -.42) & (srp555 >= -.5)
                & (srp625 >= -.53) & (srp814 >= -.4)
                & (roond <= roundmax)
                & (rnd435 >= -.21) & (rnd555 >=  -.25)
                & (rnd625 >= -.01) & (rnd814 >=   0.0)
                & ((snr435 >= 3) & (snr555 >= 3))                 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)       
                & ((((1716.4613  - xcoord)**2 + (3163.7546 - ycoord)**2)**.5) >= 7)    
                & list(np.any(x not in badXL for x in xcoord) and np.any(y not in badYL for y in ycoord)) 
                ))
        cutR.append(np.where((star <= 2) 
                & (TotalSigN >=3)
                & (crowd <= crowdmax )  
                & (crd435 <= 10) & (crd555 <= 6.0)
                & (crd625 <= .5) & (crd814 <= .54)
                & (sharp <= sharpmax) 
                & (sharp >= sharpmin)
                & (srp435 <=  10) & (srp555 <= 4.5)
                & (srp625 <= .73) & (srp814 <=  .4)
                & (srp435 >= -2.55) & (srp555 >= -1.09)
                & (srp625 >= -.53) & (srp814 >= -.47)
                & (roond <= roundmax) 
                & (rnd435 >= -.21) & (rnd555 >=  -.83)
                & (rnd625 >= -.65) & (rnd814 >=  -.01)
                & ((snr625 >= 3) & (snr814 >= 3))                 
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)      
                & list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))
                ))
    elif (SNname == 'sn08ge'):    
        cutL.append(np.where((star <= 2) 
                & (TotalSigN >= 5)
                & ((snr435 >= 8) | (snr555 >= 8))  
                & (roond >=.25)
                #& (crowd >=.6) 
                #& (np.abs(sharp) >= .3)
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= 200) 
                #& ((sharp >= .3) | (sharp <= -.3))
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #& ((f435mag <= 23) | (f555mag <= 23) | (f625mag <= 23) | (f814mag <= 23))             
                #Item 10                
                #& (snr625 >= 10) & (snr814 >= 10) & (snr435 >= 10) & (snr555 >= 10)     
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #Item 5                
                #& (snr625 >= 5) & (snr814 >= 5) & (snr435 >= 5) & (snr555 >= 5)      
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)               
                ))
        cutR.append(np.where((star <= 2) 
                & (TotalSigN >= 5)
                & ((snr625 >= 8) | (snr814 >= 8))   
                & (roond >=.25)
                #& (crowd >=.6) 
                #& (np.abs(sharp) >= .3)
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= 200) 
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #& ((f435mag <= 23) | (f555mag <= 23) | (f625mag <= 23) | (f814mag <= 23))             
                #Item 10                
                #& (snr625 >= 10) & (snr814 >= 10) & (snr435 >= 10) & (snr555 >= 10)     
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #Item 5                
                #& (snr625 >= 5) & (snr814 >= 5) & (snr435 >= 5) & (snr555 >= 5)      
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)               
                ))
    elif (SNname == 'sn10ae'): 
        cutL.append(np.where((star <= 2) 
                & (TotalSigN >=3) 
                & (snr625 >= 10) & (snr814 >= 10) & (snr435 >= 10) & (snr555 >= 10)       
                & (roond <=1) 
                & (crowd <=1) 
                & (sharp <= 1) 
                & (sharp >= -1)
                & (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #& (rnd435 <=  .4) & (rnd555 <=  .4)
                #& (rnd625 <=  .4) & (rnd814 <=  .4)
                #& (rnd435 >= 0.0) & (rnd555 >= 0.0)#& (rnd435 >= -.1) & (rnd555 >= -.1)
                #& (rnd625 >= 0.0) & (rnd814 >= 0.0)#& (rnd625 >= -.1) & (rnd814 >= -.1)
                & ((snr435 >= 3) | (snr555 >= 3))        
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                #& list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cutR.append(np.where((star <= 2) 
                & (TotalSigN >=3) 
                & (crowd <= crowdmax) 
                & (roond <= roundmax) 
                & (srp435 <=  10) & (srp555 <= 5)
                & (srp625 <= .8) & (srp814 <= .8)
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & ((rnd435 >= -.5) & (rnd555 >= -.5) & (rnd625 >= -.5) & (rnd814 >= -.53))
                & ((rnd435 <= 4.2) & (rnd555 <= 4.2) & (rnd625 <= 4.2) & (rnd814 <= 4.2))
                & ((crd435 <= 6.0) & (crd555 <= 6.0) & (crd625 <= 6.0) & (crd814 <= 6.0))
                & ((snr625 >= 3) | (snr814 >= 3))                   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius)  
                #& list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    elif (SNname == 'sn10el'): 
        cutL.append(np.where((star <= 2) 
                & (TotalSigN >= 3) 
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & ((snr435 >= 3) & (snr555 >= 3))   
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                #& list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
        cutR.append(np.where((star <= 2) 
                & (TotalSigN >= 3)  
                & (sharp <= sharpmax) & (sharp >= sharpmin)
                & ((snr625 >= 3) & (snr814 >= 3))    
                & ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= radius) 
                #& list(np.any(x not in badX for x in xcoord) and np.any(y not in badY for y in ycoord))                
                ))
    cuteverything.append(np.where((star <= 2) #&  (TotalSigN >= 2)  
                & (TotalSigN >= 5)
                & ((snr625 >= 8) | (snr814 >= 8) | (snr435 >= 8) | (snr555 >= 8))  
                & (roond <=.25)
                #& (crowd >=.6) 
                #& (np.abs(sharp) >= .3)
                #& ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) <= 200) 
                #Not good either but I thought it could be
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& ((snr625 >= 5) | (snr814 >= 5) | (snr435 >= 5) | (snr555 >= 5))      
                #& ((f435mag <= 23) | (f555mag <= 23) | (f625mag <= 23) | (f814mag <= 23))
                #Bad
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (snr625 >= 5) & (snr814 >= 5) & (snr435 >= 5) & (snr555 >= 5)      
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #& ((f435mag <= 23) | (f555mag <= 23) | (f625mag <= 23) | (f814mag <= 23))
                #index 10
                #& (snr625 >= 10) & (snr814 >= 10) & (snr435 >= 10) & (snr555 >= 10)      
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                #Item 5                
                #& (snr625 >= 5) & (snr814 >= 5) & (snr435 >= 5) & (snr555 >= 5)      
                #& (roond <=1) 
                #& (crowd <=1) 
                #& (sharp <= 1) 
                #& (sharp >= -1)
                #& (f435mag >= 18) & (f555mag >= 18) & (f625mag >= 18) & (f814mag >= 18)
                ))
    return cutL, cutR, cuteverything
################################################### 
def regfile(folder, bluecuts, redcuts,xsn,ysn,xcoord,ycoord,allcuts): 
     
    print "Save into region file"

    #circL     = []
    #commL     = []
    #closL     = []
    #circR     = []
    #commR     = []
    #closR     = []
    circ      = []
    comm      = []
    clos      = []
    #for i in range(len(xcoord[redcuts])):
    #        circL.append('circle(')
    #        commL.append(',')
    #        closL.append(',2)')
    #np.savetxt(folder +'/delL.reg', np.c_[circL,xcoord[redcuts]+.5,commL,ycoord[redcuts]+.5,closL],fmt = "%s",
    #          header ='# Region file format: DS9 version 4.1 #', 
    #          comments = 'global color=green dashlist=8 3 width=1' \
    #           ' font="helvetica 10 normal" select=1' \
    #           ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1' \
    #           '\nimage;' )
    #for i in range(len(xcoord[bluecuts])):
    #        circR.append('circle(')
    #        commR.append(',')
    #        closR.append(',2)')
    #np.savetxt(folder +'/delR.reg', np.c_[circR,xcoord[bluecuts]+.5,commR,ycoord[bluecuts]+.5,closR],fmt = "%s",
    #           header ='# Region file format: DS9 version 4.1 #', 
    #           comments = 'global color=green dashlist=8 3 width=1' \
    #           ' font="helvetica 10 normal" select=1' \
    #           ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1' \
    #           '\nimage;' )  
    for i in range(len(xcoord[allcuts])):
            circ.append('circle(')
            comm.append(',')
            clos.append(',5)')
    np.savetxt(folder +'/Field_Round.2.reg', np.c_[circ,xcoord[allcuts]+.5,comm,ycoord[allcuts]+.5,clos],fmt = "%s",
               header ='# Region file format: DS9 version 4.1 #', 
               comments = 'global color=cyan dashlist=8 3 width=1' \
               ' font="helvetica 10 normal" select=1' \
               ' highlite=1 dash=0 fixed=0 edit=1 delete=1 include=1 source=1' \
               '\nimage;' )
               
################################################### 

def pcklfile(folder, title, star, bluecuts, redcuts, all_cuts, xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord):
    snr435_555  = []
    snr625_814  = []
    all_objects = []
    snr435_555.append(( f435Abs[bluecuts],f555Abs[bluecuts], 
                    f435mag[bluecuts],f555mag[bluecuts],
                    ((unc435[bluecuts]**2 + unc555[bluecuts]**2)**.5 ),
                    unc555[bluecuts],
                    snr435[bluecuts], snr555[bluecuts],
                    (((xsn - xcoord[bluecuts])**2 + (ysn - ycoord[bluecuts])**2)**.5)
                    ))
    snr625_814.append(( f625Abs[redcuts],f814Abs[redcuts],
                    f625mag[redcuts],f814mag[redcuts], 
                    ((unc625[redcuts]**2 + unc814[redcuts]**2)**.5 ),
                    unc814[redcuts],
                    snr625[redcuts], snr814[redcuts],
                    (((xsn - xcoord[redcuts])**2 + (ysn - ycoord[redcuts])**2)**.5)
                    ))
    all_objects.append((f435Abs[all_cuts],f555Abs[all_cuts],
                        f625Abs[all_cuts],f814Abs[all_cuts],
                        f435mag[all_cuts],f555mag[all_cuts],
                        f625mag[all_cuts],f814mag[all_cuts], 
                        ((unc435[all_cuts]**2 + unc555[all_cuts]**2)**.5 ),
                        ((unc625[all_cuts]**2 + unc814[all_cuts]**2)**.5 ),
                        unc435[all_cuts], unc555[all_cuts],
                        unc625[all_cuts], unc814[all_cuts],
                        snr435[all_cuts], snr555[all_cuts],
                        snr625[all_cuts], snr814[all_cuts],
                        (((xsn - xcoord[all_cuts])**2 + (ysn - ycoord[all_cuts])**2)**.5)
                        ))                
    pickle.dump( snr435_555[0] , open(folder + '/' + title + 'f435f555.p', "wb" ) )
    pickle.dump( snr625_814[0] , open(folder + '/' + title + 'f625f814.p', "wb" ) )
    pickle.dump( all_objects[0], open(folder + '/' + title + 'all.p', "wb" ) )

    print "Pickles!"
    
################################################### 
def SNinfo(SNname):
        ##### Things that change for each sn ######
        #[folder, file,
        #ACS435,ACS555,ACS625,ACS814,
        #MW,Host,
        #H435,H555,H625,H814,
        #dmod,xsn,ysn,radius,
        #coordlist, good/bad source list,
        #sharpmax, sharpmin, round, crowd]
    Info = []
    if (SNname == "sn08ge"):
        Info = ['SN2008GE', 'sn2008ge.phot.out', 
                0.046,0.036,0.028,0.020,
                0.011,0.0,
                0.0,0.0,0.0,0.0,
                31.33,
                3817, 2967,#3249.22,3421.6611,
                52,
                'NewCat.reg','NewCatCoord.reg',
                0.6,-0.6,3,2]#0.06,-0.35,1.5,0.2] 
    elif (SNname == "sn08ha"):
        Info = ['SN2008HA', 'sn2008ha_new.phot',
                0.284,0.219,0.174,0.120,
                0.07,0.0,
                0.0,0.0,0.0,0.0,
                31.64,1736.199,3171.792,50,
                'sn2008ha_coord.reg', 'sn2008ha_right.reg',
                0.55,-0.44,2.7,1.7]
    elif (SNname == "sn10ae"):
        Info = ['SN2010AE', 'sn2010ae.phot.out',
                0.509,0.394,0.313,0.215,
                0.124,0.5,
                2.052,1.588,1.262,0.867,
                30.9,1783.3953,1923.19955,70,
                'NewCat.reg','NewCatCoord.reg', 
                0.6,-0.6,3,1.03]#0.5,-0.9,1.0,0.8]#3.0,-0.9,1.5,0.8]#
    elif (SNname == "sn10el"):
        Info = ['SN2010EL', 'sn2010el.phot.out',
                0.033,0.025,0.020,0.014,
                0.008,0.8,
                3.255,2.517,2.001,1.376,
                30.09,2419.791,1563.517,92,
                'NewCat.reg','NewCatCoord.reg',
                0.6,-0.6,3,2]
    return Info
################################################### 
def removBad(folder, good_list, coord_list):    
    print "Filter bad sources...."
    save = []
    pixX = []
    pixY = []
    fix  = []
    k    = []
    l    = []
    pixXL = []
    pixYL = []

    if (folder == "SN2008HA"):
        saveL = []
        fixL  = []
        i = []
        j = []
        identify  = pyregion.open(str(folder) + '/sn2008ha_right.reg') #right
        r         = pyregion.open(str(folder) + '/sn2008ha_coord.reg')  
        identifyL = pyregion.open(str(folder) + '/sn2008ha_left.reg' ) #left
        origcoord = pyregion.open(str(folder) + '/sn2008ha_coord.reg') 
        
        for i in xrange(len(identifyL)):
            if (pyregion.ShapeList(identifyL[i].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
                fixL.append(i)
                #yellow is good
                #cyan is bad

        for i in xrange(len(fixL)):
            origcoord[fixL[i]].attr[1]["color"] = 'yellow'
            

        for i in xrange(len(origcoord)):
            p1 = pyregion.ShapeList(origcoord[i].attr[1].get("color"))
            if (p1[0] == 'c'):
                saveL.append(i) 

        for j in xrange(len(saveL)): 
            pixXL.append(origcoord[saveL[j]].coord_list[0] - 0.5)
            pixYL.append(origcoord[saveL[j]].coord_list[1] - 0.5)
    else:
        identify = pyregion.open(str(folder) + '/' + str(good_list))
        r        = pyregion.open(str(folder)+ '/'  + str(coord_list))  
    ############################### 
    for k in xrange(len(identify)):
        if (pyregion.ShapeList(identify[k].attr[1].get("color"))  == ['y', 'e', 'l', 'l', 'o', 'w']):
            fix.append(k)
            #yellow is good
            #cyan is bad

    for k in xrange(len(fix)):
        r[fix[k]].attr[1]["color"] = 'yellow'
        
    for k in xrange(len(r)):
        r1 = pyregion.ShapeList(r[k].attr[1].get("color"))
        if (r1[0] == 'c'):
            save.append(k) 
 
    for l in xrange(len(save)): 
        pixX.append(r[save[l]].coord_list[0] - 0.5)
        pixY.append(r[save[l]].coord_list[1] - 0.5)

    return pixX, pixY, pixXL, pixYL
    
################################################### 
def textfile(folder, name, star, bluecuts, redcuts, allcuts ,xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd,TotalSigN,
             srp435,srp555,srp625,srp814,
             rnd435,rnd555,rnd625,rnd814,
             crd435,crd555,crd625,crd814): 
     
    print "Save into text file"
    dataOut_1 = []
    dataOut_2 = []
    
    dataOut_1 = np.array(np.c_[star[bluecuts]  ,
        xcoord[bluecuts]+.5 ,ycoord[bluecuts]+.5 ,
        (((xsn - xcoord[bluecuts])**2 + (ysn - ycoord[bluecuts])**2)**.5),
        (f435mag[bluecuts] - f555mag[bluecuts]),
        snr435[bluecuts] ,snr555[bluecuts] ,
        snr625[bluecuts] ,snr814[bluecuts] ,
        f435Abs[bluecuts],f555Abs[bluecuts],
        f625Abs[bluecuts],f814Abs[bluecuts],
        sharp[bluecuts],
        roond[bluecuts],
        crowd[bluecuts],
        srp435[bluecuts],srp555[bluecuts],srp625[bluecuts],srp814[bluecuts],
        rnd435[bluecuts],rnd555[bluecuts],rnd625[bluecuts],rnd814[bluecuts],
        crd435[bluecuts],crd555[bluecuts],crd625[bluecuts],crd814[bluecuts]
        ])
        
    dataOut_2 = np.array(np.c_[star[redcuts] ,
        xcoord[redcuts]+.5 ,ycoord[redcuts]+.5,
        (((xsn - xcoord[redcuts])**2 + (ysn - ycoord[redcuts])**2)**.5),
        (f625mag[redcuts] - f814mag[redcuts]),
        snr435[redcuts] ,snr555[redcuts] ,
        snr625[redcuts] ,snr814[redcuts] ,
        f435Abs[redcuts],f555Abs[redcuts],
        f625Abs[redcuts],f814Abs[redcuts],
        sharp[redcuts],
        roond[redcuts],
        crowd[redcuts],
        srp435[redcuts],srp555[redcuts],srp625[redcuts],srp814[redcuts],
        rnd435[redcuts],rnd555[redcuts],rnd625[redcuts],rnd814[redcuts],
        crd435[redcuts],crd555[redcuts],crd625[redcuts],crd814[redcuts]
        ])
        
    dataOut_all = np.array(np.c_[star[allcuts] ,
        xcoord[allcuts]+.5 ,ycoord[allcuts]+.5,
        (((xsn - xcoord[allcuts])**2 + (ysn - ycoord[allcuts])**2)**.5),
        (f625mag[allcuts] - f814mag[allcuts]),
        TotalSigN[allcuts],
        snr435[allcuts] ,snr555[allcuts] ,
        snr625[allcuts] ,snr814[allcuts] ,
        f435Abs[allcuts],f555Abs[allcuts],
        f625Abs[allcuts],f814Abs[allcuts],
        sharp[allcuts],
        roond[allcuts],
        crowd[allcuts],
        srp435[allcuts],srp555[allcuts],srp625[allcuts],srp814[allcuts],
        rnd435[allcuts],rnd555[allcuts],rnd625[allcuts],rnd814[allcuts],
        crd435[allcuts],crd555[allcuts],crd625[allcuts],crd814[allcuts]
        ])
        
    np.savetxt(folder +'/'+ name + '.cut435555.txt', dataOut_1 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub      '\
               'S/N     S/N 435   S/N 555   S/N 625   S/N 814  AbsMag435  '\
               'AbsMag555 AbsMag625 AbsMag814  Sharp    Round    Crowd   '\
               'Sharp 435    555        625      814    Round 435  555       '\
               '625      814    Crowd 435  555       625     814')

    
    np.savetxt(folder +'/'+ name + '.cut625814.txt', dataOut_2 ,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub      '\
               'S/N     S/N 435   S/N 555   S/N 625   S/N 814  AbsMag435  '\
               'AbsMag555 AbsMag625 AbsMag814  Sharp    Round    Crowd   '\
               'Sharp 435    555        625      814    Round 435  555       '\
               '625      814    Crowd 435  555       625     814')
   
    f_handle = file(folder +'/'+'all.txt', 'a')
    np.savetxt(f_handle, dataOut_all,delimiter='   ', fmt = "%1.4f",
               header ='Object Xpix        Ypix        DisFromSN   Sub      '\
               'S/N     S/N 435   S/N 555   S/N 625   S/N 814  AbsMag435  '\
               'AbsMag555 AbsMag625 AbsMag814  Sharp    Round    Crowd   '\
               'Sharp 435    555        625      814    Round 435  555       '\
               '625      814    Crowd 435  555       625     814')
    f_handle.close()

    print "Text files " + name + ".cut435555.txt & "+ name + '.cut625814.txt made'
    
################################################### 
def viewsnr(star, xsn, ysn, xcoord, ycoord, 
            snr435, snr555, snr625, snr814,
            f435Abs, f555Abs, f625Abs, f814Abs):    
    sn1 = []
    sn2 = []
    sn3 = []
    sn4 = []
    sn1 = np.where((star <= 2) & (snr435 >= 3.0) & (snr435 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))  
    print "Mean f435w Abs Mag at S/N = 3 : ", np.mean(f435Abs[sn1])  
            #print f435Abs[sn1]

    sn2 = np.where((star <= 2) & (snr555 >= 3.0) & (snr555 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)) 
    print "Mean f555w Abs Mag at S/N = 3 : ", np.mean(f555Abs[sn2])
            #print f555Abs[sn2]

    sn3 = np.where((star <= 2) & (snr625 >= 3.0) & (snr625 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100))  
    print "Mean f625w Abs Mag at S/N = 3 : ", np.mean(f625Abs[sn3])
            #print f625Abs[sn3]

    sn4 = np.where((star <= 2) & (snr814 >= 3.0) & (snr814 < 4.0) &
            ((((xsn - xcoord)**2 + (ysn - ycoord)**2)**.5) < 100)) 
    print "Mean f814w Abs Mag at S/N = 3 : ", np.mean(f814Abs[sn4])

######### Open and read in the data file ##########
def main():
    ################################################### 
    ############### declared variables ################
    data    = []
    SigN    = []
    star    = [] # Column 11 the object type
    xcoord  = [] # Column 03 the x pix coordinate
    ycoord  = [] # Column 04 the y pix coordinate

    unc435  = [] # Column 18 SNR for F435W
    unc555  = [] # Column 31 SNR for F555W
    unc625  = [] # Column 44 SNR for F625W
    unc814  = [] # Column 57 SNR for F814W

    snr435  = [] # Column 20 SNR for F435W
    snr555  = [] # Column 33 SNR for F555W
    snr625  = [] # Column 46 SNR for F625W
    snr814  = [] # Column 59 SNR for F814W
    
    sharp   = []
    crowd   = []
    roond   = [] 
       
    radius  = []

    # arrays after the respective cuts

    f435mag = [] # Column 16 F435W Apparent Magnitude
    f555mag = [] # Column 29 F555W Apparent Magnitude
    f625mag = [] # Column 42 F625W Apparent Magnitude
    f814mag = [] # Column 55 F814W Apparent Magnitude
    
    f435Abs = [] # Absolute F435W Magnitudes
    f555Abs = [] # Absolute F555W Magnitudes
    f625Abs = [] # Absolute F625W Magnitudes
    f814Abs = [] # Absolute F814W Magnitudes
    
    #################################################################
    print 'Choose a Supernova! Available SNe:'
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
    
    decpick = raw_input('Do you want to pickle the file       (y/n):')
    dectxt  = raw_input('Do you want make a text file         (y/n):')
    decreg  = raw_input('Do you want make a region file       (y/n):')
    decsnr  = raw_input('Do you want to look at the wavebands (y/n):')
    
    SNstuff = SNinfo(SNname)
    
    folder  = SNstuff[0] 
    name    = SNstuff[1] 
    ACS435  = SNstuff[2]  
    ACS555  = SNstuff[3]  
    ACS625  = SNstuff[4]
    ACS814  = SNstuff[5]
    #MW      = SNstuff[6]
    #Host    = SNstuff[7]
    H435    = SNstuff[8]
    H555    = SNstuff[9]
    H625    = SNstuff[10]
    H814    = SNstuff[11]
    dmod    = SNstuff[12]
    xsn     = SNstuff[13]
    ysn     = SNstuff[14]
    radius  = SNstuff[15]
    
    good_list = SNstuff[16]
    coor_list = SNstuff[17]
    
    sharpmax = SNstuff[18]
    sharpmin = SNstuff[19]
    roundmax = SNstuff[20]
    crowdmax = SNstuff[21]

    print "Opening file: ",name
    print "Extracting ", name, " information..."
    
    #if (SNname == 'sn10el'):
    #    print "HERE! I want this to work!!!"
    #    data.append(pickle.load(open(str(folder) + '/sn10elall.p', 'rb'))) 
    #else:    
    data = pandas.read_csv(str(folder) + '/' + name,delim_whitespace=True, header=None)

    print "Organizing ", name, " information..."

    data    = np.array(data)
    data    = data.astype(float)

    star    = data[:,10] # object type
    SigN    = data[:, 5] # total Signal to noise
    
    sharp   = data[:, 6]
    roond   = data[:, 7] # round is already a special word
    crowd   = data[:, 9]
    
    f435mag = data[:,15] # instramental VEGAMAG magnitude
    f555mag = data[:,28]
    f625mag = data[:,41]
    f814mag = data[:,55]
    
    unc435  = data[:,17] # uncertainty 
    unc555  = data[:,30]
    unc625  = data[:,43]
    unc814  = data[:,56]
        
    snr435  = data[:,19] # signal to noise
    snr555  = data[:,32]
    snr625  = data[:,45]
    snr814  = data[:,58]

    srp435  = data[:,20] # Column 21 Sharp for F435W
    srp555  = data[:,33] # Column 34 Sharp for F555W
    srp625  = data[:,46] # Column 47 Sharp for F625W
    srp814  = data[:,59] # Column 60 Sharp for F814W
    
    rnd435  = data[:,21] # Column 22 Round for F435W
    rnd555  = data[:,34] # Column 35 Round for F555W
    rnd625  = data[:,47] # Column 48 Round for F625W
    rnd814  = data[:,60] # Column 61 Round for F814W
    
    crd435  = data[:,22] # Column 23 Crowd for F435W
    crd555  = data[:,35] # Column 36 Crowd for F555W
    crd625  = data[:,48] # Column 49 Crowd for F625W
    crd814  = data[:,61] # Column 62 Crowd for F814W
    
    xcoord  = data[:, 2]
    ycoord  = data[:, 3]

################################################### 
########### Calculate Absolute Magnitude ##########
################################################### 
    
    print "Calculating Absolute Magnitude..."
    #dmod = 5*log(D(pc)) - 5
    f435Abs = f435mag - dmod - ACS435 - H435
    f555Abs = f555mag - dmod - ACS555 - H555
    f625Abs = f625mag - dmod - ACS625 - H625
    f814Abs = f814mag - dmod - ACS814 - H814
    
################################################### 
############### Deal with bad points ##############
################################################### 
    
    print "Looking in " + folder
     
    badX  = []
    badY  = []  
    badXL = []
    badYL = []  
    #badX, badY, badXL, badYL = removBad(folder, good_list,coor_list)

################################################### 
############### Make final filters ################
################################################### 
       
    cut435555  = []
    cut625814  = []
    cutall     = []
    cut435555, cut625814, cutall = cutdata(SNname,sharpmax,sharpmin,roundmax,crowdmax,radius,
            star, crowd, sharp, roond, 
            xsn,ysn,
            snr435, snr555, snr625, snr814,
            f435mag, f555mag, f625mag, f814mag,
            xcoord, ycoord,
            badX, badY,
            badXL, badYL,
            srp435,srp555,srp625,srp814,
            rnd435,rnd555,rnd625,rnd814,
            crd435,crd555,crd625,crd814,
            SigN)
            
################################################### 
############ Save good arrays to a file ###########
###################################################  

    if (decpick == 'y'):
        print "Where are the pickles??"
        pcklfile(folder,SNname,star,cut435555[0],cut625814[0],cutall[0], xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord)
    else:
        print "No pickles today."
        
################################################### 
        
    if (dectxt == 'y'):
        print "I miss the era of stone tablets"
        textfile(folder,SNname,star,cut435555[0],cut625814[0],cutall[0],xsn,ysn,
             f435Abs,f555Abs,f625Abs,f814Abs,
             f435mag,f555mag,f625mag,f814mag,
             unc435,unc555,unc625,unc814,
             snr435,snr555,snr625,snr814,
             xcoord,ycoord,
             sharp,roond,crowd,
             SigN,
             srp435,srp555,srp625,srp814,
             rnd435,rnd555,rnd625,rnd814,
             crd435,crd555,crd625,crd814)
    else:
        print "Papyrus is going to come back in style."

###################################################  
       
    if (decreg == 'y'):
        regfile(folder,cut435555[0],cut625814[0],xsn,ysn,xcoord,ycoord,cutall[0])
    else:
        print "Moving along"
        
################################################### 
        
    if (decsnr == 'y'):
        print "Look at waveband limits"
        viewsnr(star, xsn, ysn, xcoord, ycoord, 
            snr435, snr555, snr625, snr814,
            f435Abs, f555Abs, f625Abs, f814Abs)
    else:
        print "No waves here"
main() 