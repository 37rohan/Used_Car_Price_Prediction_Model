# Import necessary module
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from prepro import DataFrame

feature = ['year', 'km_driven', 'mileage', 'max_power', 'seats']
def app(df):
    df = DataFrame()

    # Give title
    st.title("Visualize Data")

    # Creat a section for scatter plot
    st.header("Scatterplot")

    # Create a mulit-select option to get y-axis from the user.
    # It is for telling relationship btwn predicting column and other columns by using Scatterplot
    feature_list = st.multiselect("Select y-axis values:", ('km_driven', 'mileage', 'max_power', 'seats'))

    #if 'year' in feature_list:
     #   fig = plt.figure(figsize=(12, 5))
      #  st.subheader(f"Scatter plot between year and price")
       # sns.scatterplot(x='selling_price', y='year', data=df,hue='year')
        #st.pyplot(fig)

    if 'km_driven' in feature_list:
        fig = plt.figure(figsize=(12, 5))# For Setting Graph size
        st.subheader(f"Scatter plot between km_driven and price")
        sns.scatterplot(x='selling_price', y='km_driven', data=df,hue="km_driven",)
        st.pyplot(fig)

    if 'mileage' in feature_list:
        fig = plt.figure(figsize=(12, 5))
        st.subheader(f"Scatter plot between mileage and price")
        sns.scatterplot(x='selling_price', y='mileage', data=df,hue='mileage')
        st.pyplot(fig)

    if 'max_power' in feature_list:
        fig = plt.figure(figsize=(12, 5))
        st.subheader(f"Scatter plot between max_power and price")
        sns.scatterplot(x='selling_price', y='max_power', data=df,hue='max_power')
        st.pyplot(fig)
        
    if 'seats' in feature_list:
        fig = plt.figure(figsize=(12, 5))
        st.subheader(f"Scatter plot between seats and price")
        sns.scatterplot(x='selling_price', y='seats', data=df,hue='seats')
        st.pyplot(fig)

    # Create a section for Visualisation Selector
    st.header("Type of Visualization")
    
    # Create a multiselect option to create plots or charts.
    plot_type = st.multiselect("Select charts or plots:", ('Histogram', 'Box Plot', 'Correlation Heatmap'))

    # Create plot for histogram.
    if ("Histogram" in plot_type):
        st.subheader("Histogram")
        # Take column from user.
        hist_column = st.selectbox("Select the column to create its histogram", ('km_driven', 'mileage', 'max_power', 'seats'))
        # Plot the chart.
        fig = plt.figure(figsize=(12, 5))
        plt.title(f"Histogram for {hist_column}")#For giving title to the graph on the basis of user choice
        sns.histplot(x=df[hist_column], bins = 'sturges', edgecolor = 'black')
        st.pyplot(fig)

    # Create plot for boxplot.
    if ("Box Plot" in plot_type):
        st.subheader("Boxplot")
        # Take column from user.
        box_column = st.selectbox("Select the column to create its boxplot", ('km_driven', 'mileage', 'max_power', 'seats'))
        # Plot the chart.
        fig = plt.figure(figsize=(12, 2))
        plt.title(f"Box plot for {box_column}")
        sns.boxplot(df[box_column])
        st.pyplot(fig)

    # Create Correlation Heatmap.
    if ("Correlation Heatmap" in plot_type):
        st.subheader("Correlation Heatmap")
        # Plot the chart.
        fig = plt.figure(figsize=(12, 10))
        ax = sns.heatmap(df.corr(), annot=True)
        bottom, top = ax.get_ylim() # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5) # Increasing the bottom and decreasing the bottom margins respectively.
        st.pyplot(fig)
