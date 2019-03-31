import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split 
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold

from lightgbm import LGBMClassifier

data = pd.read_csv("dataset.csv")

excl = ["Id", "Time [s]","label", "tendency", "AVR","II", "RESP", "RESP_right", "V" ]
feats = [f for f in data.columns if f not in excl]

# target variable
train_Y = data['tendency'][1000:]
train_X = data[feats][1000:]

# test ID
test_Y = data['tendency'][:1000]
test_X = data[feats][:1000]

# merge train and test datasets for preprocessing
df = pd.concat([train_X, test_X], axis=0)

folds = KFold(n_splits=5, shuffle=True, random_state=42)
oof_preds = np.zeros(train_X.shape[0])
sub_preds = np.zeros(test_X.shape[0])
for n_fold, (trn_idx, val_idx) in enumerate(folds.split(train_X)):
    trn_x, trn_y = train_X.iloc[trn_idx], train_Y.iloc[trn_idx]
    val_x, val_y = train_X.iloc[val_idx], train_Y.iloc[val_idx]
    
    clf = LGBMClassifier(
        n_estimators=20000,
        learning_rate=0.005,
        num_leaves=70,
        colsample_bytree=.8,
        subsample=.9,
        max_depth=7,
        reg_alpha=.1,
        reg_lambda=.1,
        min_split_gain=.01,
        min_child_weight=2
    )
    
    clf.fit(trn_x, trn_y, 
            eval_set= [(trn_x, trn_y), (val_x, val_y)], 
            eval_metric='auc', verbose=250, early_stopping_rounds=150
           )
    
    oof_preds[val_idx] = clf.predict_proba(val_x, num_iteration=clf.best_iteration_)[:, 1]
    sub_preds += clf.predict_proba(test_X[feats], num_iteration=clf.best_iteration_)[:, 1] / folds.n_splits
    
    print('Fold %2d AUC : %.6f' % (n_fold + 1, roc_auc_score(val_y, oof_preds[val_idx])))
    #del clf, trn_x, trn_y, val_x, val_y

    joblib.dump(clf, 'model_weights.sav')
print('Full AUC score %.6f' % roc_auc_score(test_Y, oof_preds))  