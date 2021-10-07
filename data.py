# Import necessary module
import streamlit as st
from prepro import DataFrame



def app(df):
    df = DataFrame()
    # Title
    st.title("Look to the Dataset")

    # Create expander for seeing Dataset
    with st.expander("View Dataset"):
        st.table(df.head(500))

    # Creating a row with three columns to show info about columns.
    col1,col2,col3 = st.columns(3)

    # Creating a section to show description about dataset.
    st.header("Dataset Description")

    with col1:
        # Show the Summary of dataset.
        if st.checkbox("Dataset Summary"):
            st.table(df.describe())
    
    with col2:
        # See Any Null Values
        if st.checkbox("See Null values"):
            st.text(df.isnull().sum())
    
    with col3:
        # Show the describtion of dataset.
        if st.checkbox("Dataset Shape"):
            st.text(df.shape)

    # Create a row with three columns to show info about columns.
    col_1, col_2, col_3 = st.columns(3)

    # Add checkbox to show the columns name
    with col_1:
        if st.checkbox("Show columns name"):
            st.table(df.columns)

    # Add checkbox to show the columns datatype
    with col_2:
        if st.checkbox("View columns datatype"):
            dtypes_df = df.dtypes.apply(lambda x: x.name)
            st.table(dtypes_df)

    # Add checkbox to show the columns data.
    with col_3:
        if st.checkbox("View column data"):
            column_data = st.selectbox("Select column", tuple(df.columns))
            st.write(df[column_data])
