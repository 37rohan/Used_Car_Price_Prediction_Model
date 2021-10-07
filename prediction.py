import streamlit as st
import numpy as np
import pandas as pd
from Model import model
from prepro import load_data


def app(df):
    st.header("This app uses Extreme Gradient Boosting to predict the price of a used car based on the inputs.")
    st.subheader("Select values:")

    years = st.slider("Years", 0, 30)
    km_driven = st.slider("KM driven", 0, 600000)
    mileage = st.slider("Mileage", 10, 50)
    max_power = st.slider("Max Power", 20, 450)
    seats = st.slider("Seats", 1,10)
    transmission = st.selectbox("Transmission",["Manual","Automatic"])
    owner = st.selectbox("Owner",["First Owner","Second Owner","Third Owner","Fourth & Above Owner","Test Drive Car"])

    if (transmission == "Manual"):
        transmission = 1
    elif (transmission == "Automatic"):
        transmission = 0

    if (owner == "First Owner"):
        owner = 0
    elif (owner == "Second Owner"):
        owner = 2
    elif (owner == "Third Owner"):
        owner = 4
    elif (owner == "Fourth & Above Owner"):
        owner = 1
    else:
        owner = 3    


    df = load_data()[2]

    feature = [[years,km_driven,mileage,max_power,seats,transmission,owner]]
    feature = pd.DataFrame(feature)
    feature = np.reshape(feature,(1,7))
    if (st.button("Predict")):

        acc,pred_price,rsquare_score, mae, msle, rmse = model(df,feature)[1:]
        
        st.success(f"Predicted Price Of Car Rs {round(pred_price)}")
        st.balloons()
        st.info(f"Accuracy of Our Model is {round(acc, 2)}")
        st.info(f"R-squared score of this model is: {rsquare_score:.2}")
        st.info(f"Mean absolute error of this model is: {mae:.3f}")
        st.info(f"Mean squared log error of this model is: {msle:.3f}")
        st.info(f"Root mean squared error of this model is: {rmse:.3f}")