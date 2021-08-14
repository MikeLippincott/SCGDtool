#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import configparser
import glob
import os
import re
import os.path
import pathlib
import sys
from tkinter.filedialog import askdirectory
from configparser import ConfigParser as config


#cd'd location


path = askdirectory()
config.read(path + '/config.ini')
path = config['Path']['c1']
out = config['Outputfolder']['output']
out





#Concentration2
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c2']
    files=pathlib.Path(path).glob("*.txt")
    c2=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c2.append(trim)
    dflst=[]
    for i in c2:
        df= pd.read_csv(path+i ,header= None)
        i=str(i).strip('.txt')
        df.columns = ['old']
        df1= df.join(df['old'].str.split('\t', 1, expand=True).rename(columns={0:'Wavelength', 1:'Intensity'}))
        df1.drop(columns =["old"], inplace = True)
        df1.to_csv(out+i+'.csv',index=False)
        df2=df1
        df3=df2[['Intensity']]

        Wl=Wl.astype(float)
        df4=df3.astype(float)
        df4=pd.DataFrame(df4)
        dflst.append(df4)
    newlst=[]
    for i in range(3):
        exec(f'nlst{i}=dflst[i]')
    df5=pd.concat([nlst0,nlst1,nlst2], axis=1)
    df6=df5.mean(axis=1)
    df7 = pd.DataFrame(df6)
    df7.columns=['Average Intensity']
    conc2=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')







#Graph Parameters load
config.read('config.ini')
labels=[]
lst=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']
for q in lst:
    cs=config['Concentrations'][q]
    labels.append(cs)
col=[]
try:
    for c in lst:
        cols=config['Colours'][c]
        col.append(cols)
except KeyError:
    print('Colour Muted')
finally:
    print('done')

x=Wl['Wavelength'].tolist()

#y1
try:
    y1=conc1['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")





    #Conc1
    try:
        m1=plt.plot(x,y1,col[0],linewidth=.5,label=labels[0])
    except NameError:
        print("name 'y3' is not defined")
    else:
        print("no exception")
    finally:
        print("done")
    #Conc2
    try:
        m2=plt.plot(x,y3,col[1],linewidth=.5,label=labels[1])
    except NameError:
        print("name 'y3' is not defined")
    except IndexError:
        print("Muted")
    else:
        print("no exception")
    finally:
        print("done")





        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Average Intensity')

        plt.gca().legend((labels[0],labels[1],labels[2],labels[3],labels[4],labels[5],labels[6],labels[7],labels[8],labels[9],))
        plt.savefig(out+'Nestedgraph.pdf')
        plt.show()
