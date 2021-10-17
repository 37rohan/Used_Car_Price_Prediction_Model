"""This module creates the home page."""

# Import necessary modules.
import streamlit as st

def app():
    st.title("Used Car Prediction App")
    st.text("""
        This web app allows a user to predict the prices of a used car based on their 
        Km Driven, Mileage, Max Power, Seats, Transmission, Owner type parameters.
        """)
    st.image("car.jpg",width=500)