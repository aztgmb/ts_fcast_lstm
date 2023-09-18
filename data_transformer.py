# -*- coding: utf-8 -*-
"""data_transformer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YgY4NMkqKMFiABFWfCwxTg5XUhO09gDJ
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def rearrange_data(fx_df):
    data_brljpy = fx_df.rename(columns={data_brljpy.columns[0]: 'date'})
    data_brljpy_n10y = data_brljpy.drop('brl_10y_gov',axis=1)
    data_brjp = data_brljpy_n10y.dropna()
    data_brjp['date'] = pd.to_datetime(data_brjp['date'], format='%Y-%m-%d')
    data_brjp = data_brjp.set_index('date')
    data_brjp_rev = data_brjp[::-1]
    return data_bjrp_rev

def split_data(data_brjp_rev, splt_dt_1, splt_dt_2):
    split_date_train_brjp = pd.Timestamp(splt_dt_1)
    split_date_test_brjp = pd.Timestamp(splt_dt_2)
    train_brjp = data_brjp_rev.loc[:split_date_train_brjp]
    test_brjp = data_brjp_rev.loc[split_date_test_brjp:]
    x_train_brjp = train_brjp[train_brjp.columns[1:]]
    y_train_brjp = train_brjp['PX_LAST']
    x_test_brjp = test_brjp[test_brjp.columns[1:]]
    y_test_brjp = test_brjp['PX_LAST']
    return x_train_bjrp, y_train_bjrp, x_test_bjrp, y_test_bjrp

def scale_data(x_train_bjrp, y_train_bjrp, x_test_bjrp, y_test_bjrp):
    transformer_x_brjp = MinMaxScaler().fit(x_train_brjp)
    transformer_y_brjp = MinMaxScaler().fit(y_train_brjp.values.reshape(-1,1))
    x_rtrain_brjp = transformer_x_brjp.transform(x_train_brjp)
    y_rtrain_brjp = transformer_y_brjp.transform(y_train_brjp.values.reshape(-1,1))
    x_rtest_brjp = transformer_x_brjp.transform(x_test_brjp)
    y_rtest_brjp = transformer_y_brjp.transform(y_test_brjp.values.reshape(-1,1))
    x_tr_t_brjp = x_rtrain_brjp.reshape(x_rtrain_brjp.shape[0], 1, x_rtrain_brjp.shape[1])
    x_tst_t_brjp = x_rtest_brjp.reshape(x_rtest_brjp.shape[0], 1, x_rtest_brjp.shape[1])
    return x_rtrain_brjp, y_rtrain_brjp, x_rtest_brjp, y_rtest_brjp, x_tr_t_brjp, x_tst_t_brjp