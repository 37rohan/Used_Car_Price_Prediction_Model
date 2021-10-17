from os import name
import streamlit as st
import numpy as np
import pandas as pd
from Model import model
from prepro import load_data


def app(df):
    st.header("""This app uses Extreme Gradient Boosting(XGBoost) to predict the price of a used car based on the inputs.
    XGBOOST => Gradient boosting refers to a class of ensemble machine learning algorithms
    that can be used for classification or regression predictive modeling problems.""")
    st.subheader("Select values:")

    name = st.selectbox("Car Brand Name",['Maruti','Skoda','Honda','Hyundai','Toyota',
    'Ford','Renault','Mahindra','Tata','Chevrolet','Fiat','Datsun','Jeep',
    'Mercedes-Benz','Mitsubishi','Audi','Volkswagen', 'BMW', 'Nissan', 
    'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo','Daewoo', 'Kia', 'Force', 
    'Ambassador', 'Ashok', 'Isuzu', 'Opel', 'Peugeot'])
    #years = st.slider("Years", 1983,2020)
    km_driven = st.slider("KM driven", 1, 2300000)
    mileage = st.slider("Mileage", 0.0,42.0)
    max_power = st.slider("Max Power", 0,400)
    seats = st.slider("Seats", 2,14)
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

    if name == 'Maruti':
        name = 20
    if name == 'Hyundai':
        name = 11
    if name == 'Mahindra':
        name = 19
    if name == 'Tata':
        name = 28
    if name == 'Toyota':
        name = 29
    if name == 'Honda':
        name = 10
    if name == 'Ford':
        name = 9
    if name == 'Chevrolet':
        name = 4
    if name == 'Renault':
        name = 26
    if name == 'Volkswagen':
        name = 30
    if name == 'BMW':
        name = 3
    if name == 'Skoda':
        name = 27
    if name == 'Nissan':
        name = 23
    if name == 'Jaguar':
        name = 13
    if name == 'Volvo':
        name = 31
    if name == 'Datsun':
        name = 6
    if name == 'Mercedes-Benz':
        name = 21
    if name == 'Fiat':
        name = 7
    if name == 'Audi':
        name = 2
    if name == 'Lexus':
        name = 17
    if name == 'Jeep':
        name = 14
    if name == 'Mitsubishi':
        name = 22
    if name == 'Land':
        name = 8
    if name == 'Force':
        name = 16
    if name == 'Isuzu':
        name = 12
    if name == 'Ambassador':
        name = 15
    if name == 'Kia':
        name = 0
    if name == 'MG':
        name = 5
    if name == 'Daewoo':
        name = 18
    if name == 'Opel':
        name = 24
    if name == 'Peugeot':
        name = 25
    if name == 'Ashok':
        name = 1

    df = load_data()[2]

    feature = [[name,km_driven,mileage,max_power,seats,transmission,owner]]
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