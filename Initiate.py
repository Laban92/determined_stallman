#!/usr/bin/env python
import pandas as pd
import numpy as np
from sklearn.externals import joblib
from lightgbm import LGBMClassifier
import utils

clf = joblib.load("model_weights.sav")
data = pd.read("")

from sklearn.model_selection import train_test_split 

excl = ["Id", "Time [s]","label", "tendency", "AVR","II", "RESP", "RESP_right", "V" ]
feats = [f for f in data.columns if f not in excl]

# target variable
Y = data['tendency']
X = data[feats]



# merge train and test datasets for preprocessing
data["Predicted_Breath"] = clf.predict(X)


Heart_rate = Heart_rate(data)
calorie_expenditure_increase = calorie_expenditure_increase(data,data) #specify segments
NREM_duration = NREM_duration(data)
REM_duration = REM_duration(data)