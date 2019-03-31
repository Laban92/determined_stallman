#!/usr/bin/env python
import pandas as pd
import numpy as np

def Heart_rate(d):
    idx = d[d["Predicted_Breath"]==1].index
    count=0
    for i in idx:
        if d.loc[(i-1):(i+1)]["Predicted_Breath"].sum()>= 2:
            count+=1
    return count/(d.tail(1)["Time [s]"]/60)
    
def calorie_expenditure_increase(data_segment1, data_segment2):
    
    hr_change= Heart_rate(data_segment1)/Heart_rate(data_segment2)
    
    Weir_change = 1.44 *(3.94* hr_change + 1.11 * hr_change)
    return Weir_change


def historical_hr_variance(full_historical_hr_data):
    
    return full_historical_hr_data["Predicted_Breath"].var
    
def NREM_duration(nighttime_data):
    
    window_start = 0
    w = 100
    NREM = 0
    for i in range (len(nighttime_data)):
        Window= Heart_rate(np.array(nighttime_data["Predicted_Breath"][window_start:window_start+w]),30)
        Fd_df[column].iloc[i]= Higuchi
        window_start+=1
        i+=1
        if Window.var < historical_hr_variance(full_historical_hr_data):
            NREM+=1
    return NREM
        
def REM_duration(nighttime_data):
    
    window_start = 0
    w = 100
    REM = 0
    for i in range (len(nighttime_data)):
        Window= Heart_rate(np.array(nighttime_data["Predicted_Breath"][window_start:window_start+w]),30)
        Fd_df[column].iloc[i]= Higuchi
        window_start+=1
        i+=1
        if Window.var > 1.2*historical_hr_variance(full_historical_hr_data):
            REM+=1
            
    return REM        
        
        
        