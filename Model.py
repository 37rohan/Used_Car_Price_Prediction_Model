#importing Libraries
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error
from math import sqrt

from xgboost import XGBRegressor
from prepro import load_data


@st.cache(hash_funcs={XGBRegressor: id})
def model(df, feature):
    """This function train the model and return the accuracy/"""
    # Load features and target
    X, y = load_data()[0:2]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

    # Importing XGBOOST 
    xgb = XGBRegressor(max_depth=4,n_estimators=1000,learning_rate=0.1,booster='gbtree')# Using booster as gbtree
    xgb.fit(X, y)
    
    acc = xgb.score(X_train, y_train) #ACcuracy of model
    pred_price = xgb.predict(feature)
    pred_price = pred_price[0] # Prediction of model

    # Calculating errors 
    y_test_pred = xgb.predict(X_test)
    rsquare_score = r2_score(y_test, y_test_pred)
    mae = mean_absolute_error(y_test, y_test_pred)
    msle = mean_squared_log_error(y_test, y_test_pred)
    rmse = sqrt(mean_squared_error(y_test, y_test_pred))

    # return model, accuracy, error values
    return xgb, acc*100, pred_price,  rsquare_score*100, mae, msle, rmse