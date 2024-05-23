import streamlit as st
import pandas as pd
import pydeck as pdk


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

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[0, 0]',
    get_radius=10000,
    get_fill_color='[255, 0, 0]',
    pickable=True
)

# Set the viewport location
view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)

# Create the Deck.GL map
map_ = pdk.Deck(layers=[layer], initial_view_state=view_state)

# Display the map
st.pydeck_chart(map_)
