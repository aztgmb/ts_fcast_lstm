# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MqBP8YpkmMUF6nblO0v3Nb1QvOrD8GkY
"""

from data_loader import load_data
from data_transformer import FXDataTransformer
from fx_model_keras import lstm_keras
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import math
import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import save_model
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
from kerastuner.tuners import RandomSearch
from kerastuner.engine.hyperparameters import HyperParameters
from pickle import dump,load
import warnings
warnings.simplefilter("ignore", UserWarning)

df = load_data('fx_data.csv')
data_transformer = FXDataTransformer()
df_rearr = data_transformer.rearrange_data(df)
splt_dt_1 = '2018-04-04'
splt_dt_2 = '2018-04-05'
X_train, Y_train, X_test, Y_test = data_transformer.split_data(df_rearr, splt_dt_1, splt_dt_2)
x_rtrain, y_rtrain, x_rtest, y_rtest, x_tr_t, x_tst_t = data_transformer.scale_data(X_train, Y_train, X_test, Y_test)

tuner = RandomSearch(
        lstm_keras(hp, X_train, Y_train),
        objective='mse',
        max_trials=10,
        executions_per_trial=1
        )

tuner.search(
        x=x_tr_t,
        y=y_rtrain,
        epochs=20,
        batch_size=128,
        validation_data=(x_tst_t,y_rtest),
)

best_model = tuner.get_best_models(num_models=1)[0]
Y_pred=best_model.predict(X_test[0].reshape((1,X_test[0].shape[0], X_test[0].shape[1])))
mean_squared_error(y_rtest, Y_pred, squared=False)
save_model(best_model,'lstm_keras.h5')