# Forecasting foreign exchange rate time series
This project forecasts Japanese Yen (JPY) to Brazilian Real (BRL) fx rate using LSTM. 
data_loader: data is loaded from csv file and stored as pandas dataframe.
data_transformer: changing date format and inverting temporal order of time series. Then data is split into training and testing sets. Finally data is scaled using minmax scaler.
fx_model_keras: model is created and compiled using LSTM from Keras TensorFlow. Also min and max values for parameters tuning intervals are defined.
main: pulls all previous modules together by importing them. Model is tuned using keras tuner. Predictions are made using the best model. RMSE is the metric used to estimate model's performance. The best model is saved as h5 file.
Docker file creates environment using requirements.txt containing necessary packages and their versions
