import streamlit as st
import pandas as pd


# Title of the app
st.title('Data Visualization Dashboard')

# Instructions for the user
st.write("""
This dashboard allows you to explore the data and visualize different aspects of it.
""")

# Function to load data from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/claireobrien00/CA2_Dashboard/main/CA2_Dashboard.csv'
    data = pd.read_csv(url)
    return data

# Load the data
df = load_data()

# Display the raw data
st.header('Raw Data')
st.dataframe(df)

# Select a subset of the data
st.header('Data Analysis')
st.write("Select columns to visualize")

