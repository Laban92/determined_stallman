#!/usr/bin/env python
import numpy as np
import pandas as pd
import os
import glob


for i in range(1,54):
    
    for file in glob.glob("C:/Users/lukic/Desktop/Train model/*.csv"):
        if file.endswith("%.2d" % i +"_Signals.csv"):
            sig= pd.read_csv(file)
        elif file.endswith("%.2d" % i+"_Breaths.csv"):
            resp= pd.read_csv(file)
        elif file.endswith("%.2d" % i+"_Numerics.csv"):
            num = pd.read_csv(file)
      
    num["merger"]= num["Time [s]"]
    sig["merger"]= sig["Time [s]"].astype("int")
    sig = sig.join(num, on= "merger", how="left", rsuffix='_right').drop(["merger", "Time [s]_right", "merger_right"], axis = 1)
    print( str(i)+ " datasets filled")
    sig["label"]= 0
    x=0
    sig["label"]= 0
    for ind, row in resp.iterrows():
        ind = int(sig[sig["Time [s]"] >= int(row.mean())/1000].index[0])
        sig.iloc[ind,sig.columns.get_loc('label')]=1 
    sig.to_csv("dataset_"+ str(i)+".csv")
    print(str(i)+"saved")

data = pd.read_csv("dataset_1.csv")
data["Id"] = 1
for i in range(2,54):
  
    for file in glob.glob("C:/Users/lukic/Desktop/Train model/*.csv"):
        if file.endswith("dataset_"+ str(i)+".csv"):
            sig = pd.read_csv(file)
            sig["Id"] = i
            data = data.append(sig)

    
data.drop([" ABP"," ART"," CVP"," HR"," I", " III", " MCL","Unnamed: 0"],axis=1, inplace=True)

data["tendency"]= 0
for i in range(len(data)):
    if data["label"].iloc[i]==1:
        idx = data.loc[i-5:i+4].index
        #sig.iloc[ind,sig.columns.get_loc('label')]=1 
        data["tendency"].loc[idx]=1
        print(i)
        i+=5
        
data.to_csv("dataset.csv", index = False)