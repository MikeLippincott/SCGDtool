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
from configparser import ConfigParser
#cd'd location
working_directory=os.getcwd()
os.chdir(working_directory)
config = configparser.ConfigParser()  
config.read('~/config.ini')

config = ConfigParser()
config.read('config.ini')
path=config['Path']['c1']
out=config['Outputfolder']['output']
out


#Concentration1

config = ConfigParser()
config.read('config.ini')
path=config['Path']['c1']
files=pathlib.Path(path).glob("*.txt")
path
c1=[]
for file in files:
    file=str(file)
    trim=re.sub(path,'',file)
    c1.append(trim)
dflst=[]
for i in c1:
    df= pd.read_csv(path+i ,header= None)
    i=str(i).strip('.txt')
    df.columns = ['old']
    df1= df.join(df['old'].str.split('\t', 1, expand=True).rename(columns={0:'Wavelength', 1:'Intensity'}))
    df1.drop(columns =["old"], inplace = True) 
    df1.to_csv(out+i+'.csv',index=False)
    df2=df1 
    df3=df2[['Intensity']]
    Wl=df1[['Wavelength']]
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
conc1=df7

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

#Concentration3
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c3']
    files=pathlib.Path(path).glob("*.txt")
    c3=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c3.append(trim)
    dflst=[]
    for i in c3:
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
    conc3=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration4
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c4']
    files=pathlib.Path(path).glob("*.txt")
    c4=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c4.append(trim)
    dflst=[]
    for i in c4:
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
    conc4=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration5
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c5']
    files=pathlib.Path(path).glob("*.txt")
    c5=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c5.append(trim)
    dflst=[]
    for i in c5:
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
    conc5=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration6
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c6']
    files=pathlib.Path(path).glob("*.txt")
    c6=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c6.append(trim)
    dflst=[]
    for i in c6:
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
    conc6=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration7
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c7']
    files=pathlib.Path(path).glob("*.txt")
    c7=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c7.append(trim)
    dflst=[]
    for i in c7:
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
    conc7=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration8
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c8']
    files=pathlib.Path(path).glob("*.txt")
    c8=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c8.append(trim)
    dflst=[]
    for i in c8:
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
    conc8=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration9
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c9']
    files=pathlib.Path(path).glob("*.txt")
    c9=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c9.append(trim)
    dflst=[]
    for i in c9:
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
    conc9=df7
except IndexError:
    print("list index out of range")
except KeyError:
    print("index are not in column")
else:
    print("No Exception")
finally:
    print('done')

#Concentration10
try:
    config = ConfigParser()
    config.read('config.ini')
    path=config['Path']['c10']
    files=pathlib.Path(path).glob("*.txt")
    c10=[]
    for file in files:
        file=str(file)
        trim=re.sub(path,'',file)
        c10.append(trim)
    dflst=[]
    for i in c10:
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
    conc10=df7
    
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
#y2
try:
    y2=conc2['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y3
try:
    y3=conc3['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y4
try:
    y4=conc4['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y5
try:
    y5=conc5['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y6
try:
    y6=conc6['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y7
try:
    y7=conc7['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y8
try:
    y8=conc8['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y9
try:
    y9=conc9['Average Intensity'].tolist()
except NameError:
    print("name 'conc3' is not defined")
else:
    print("no exception")
finally:
    print("done")
#y10
try:
    y10=conc10['Average Intensity'].tolist()
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
#Conc3
try:
    m3=plt.plot(x,y3,col[2],linewidth=.5,label=labels[2])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
#Conc4
try:
    m4=plt.plot(x,y3,col[3],linewidth=.5,label=labels[3])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
#Conc5 
try:
    m5=plt.plot(x,y3,col[4],linewidth=.5,label=labels[4])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
#Conc6
try:
    m6=plt.plot(x,y3,col[5],linewidth=.5,label=labels[5])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
#Conc7
try:
    m7=plt.plot(x,y3,col[6],linewidth=.5,label=labels[6])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
    
#Conc8 
try:
    m8=plt.plot(x,y3,col[7],linewidth=.5,label=labels[7])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
    
#Conc9
try:
    m9=plt.plot(x,y3,col[8],linewidth=.5,label=labels[8])
except NameError:
    print("name 'y3' is not defined")
except IndexError:
    print("Muted")
else:
    print("no exception")
finally:
    print("done")
    
    
#Conc10   
try:
    m10=plt.plot(x,y3,col[9],linewidth=.5,label=labels[9])
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

