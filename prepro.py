#importing Libraries
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor

# Import Dataset
df = pd.read_csv('Car details v3.csv')

@st.cache(hash_funcs={XGBRegressor: id})
def load_data():

    # dropping these features Coz it has no major scope in the predictions
    df.drop(['year','torque','engine','seller_type','fuel'],axis=1,inplace=True)


    # Filling Null values using Mode method coz mean and median isn't usefull to fill object type columns
    df['seats'].fillna(df['seats'].mode()[0], inplace=True)
    df['mileage'].fillna(df['mileage'].mode()[0], inplace=True)
    df['max_power'].fillna(df['max_power'].mode()[0], inplace=True)

    # Filtering required names from complicated names
    # For Car Names
    name = []
    for i in df['name']:
        splt = i.split()[0]#spliting values and taking 0 index value(here we are spliting car names)
        name.append(splt)#appending spltting values in empty name list
    
    #here we change name data in Series format and again save it to the original dataset
    df['name'] = pd.Series(name)

    # For Max Power
    name = []
    for i in df['max_power']:
        splt = i.split()[0]
        name.append(splt)

    df['max_power'] = pd.Series(name)
    df.drop(index=4933,axis=0,inplace=True)
    df['max_power'] = df['max_power'].astype(float).astype(int)
    

    # For Mileage
    name = []
    for i in df['mileage']:
        splt = i.split()[0]
        name.append(splt)

    df['mileage'] = pd.Series(name)
    df['mileage'] = df['mileage'].astype(float)

    # using Label encoder for encoding huge no of string values in object type columns
    LE = LabelEncoder()
    df[df.select_dtypes(include=['object']).columns] = df[df.select_dtypes(include=['object']).columns].apply(LE.fit_transform)
    df['seats'] = df['seats'].astype(int)# typecasting Seats column float to int

    # Storing values in X,y
    y = df['selling_price']
    X = df.drop(['selling_price'],axis=1)
    
    return X, y, df

# Creating a function for DataFrame
@st.cache(hash_funcs={XGBRegressor: id})
def DataFrame():
    df = load_data()[2]
    df = pd.DataFrame(df)

    return df
