# Import necessary modules.
import streamlit as st

# Import pages.
import home
import Visualization
import prediction
import data
import contibuters

# Loading Dataset
from prepro import load_data

# Configure the web page.
st.set_page_config(
    page_title = 'Car Price Prediction',
    page_icon = 'car',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

# Create a dict for pages.
pages_dict = {
                "Home": home,
                "Data Summary": data, 
                "Visualize Data": Visualization, 
                "Predict": prediction,
                "Contributers": contibuters
            }

# Load the dataset.
df = load_data()[:-1]

# Create navbar in sidebar.
st.sidebar.title("Navigation")
user_choice = st.sidebar.radio('Go to', ("Home","Data Summary", "Visualize Data", "Predict","Contributers"))


# opening page according to navbar option
if (user_choice == ("Home" or "Contributers" or "Predict")):
    selected_page = pages_dict[user_choice]
    selected_page.app()
elif (user_choice == "Visualize Data" or "Data Summary"):
    selected_page = pages_dict[user_choice]
    selected_page.app(df)# IF a page is using dataset we have to include df in app
else:
    selected_page = pages_dict[user_choice]
    selected_page.app()