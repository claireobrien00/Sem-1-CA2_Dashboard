import streamlit as st
import pandas as pd
import pydeck as pdk
#import plotly.express as px


# Title of the app
st.title('Data Visualization Dashboard')

# Instructions for the user
st.write("""
This dashboard allows you to explore the data and visualize different aspects of it.
""")

# Function to load data from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/claireobrien00/CA2_Dashboard/main/CA2_Dashboard_Livestock.csv'
    data = pd.read_csv(url)
    return data

# Load the data
df = load_data()

# Display the raw data
st.header('Raw Data')
st.dataframe(df)

# Function to generate choropleth layer
def generate_choropleth_layer(df, color_column):
    # Create a pydeck GeoJSON layer
    choropleth_layer = pdk.Layer(
        'GeoJsonLayer',
        data=df,
        opacity=0.8,
        get_fill_color='[255, color_value, 0]',
        stroked=False,
        get_line_color=[255, 255, 255],
        lineWidthMinPixels=1,
        pickable=True
    )

    return choropleth_layer

# Function to generate map
def generate_map(df, color_column):
    # Set the center of the map
    center = [0, 0]

    # Create choropleth layer
    choropleth_layer = generate_choropleth_layer(df, color_column)

    # Create Deck.GL map
    map_ = pdk.Deck(
        layers=[choropleth_layer],
        initial_view_state=pdk.ViewState(
            latitude=center[0],
            longitude=center[1],
            zoom=1,
            pitch=0
        )
    )

    return map_

# Streamlit app
st.title('Map Visualization')

# Sidebar for user input
color_column = st.sidebar.selectbox('Select the column containing values:', options=df_eu_livestock_country.columns)

# Display sample DataFrame
st.write(df_eu_livestock_country)

# Plot the map
map_ = generate_map(df_eu_livestock_country, color_column)
st.pydeck_chart(map_)