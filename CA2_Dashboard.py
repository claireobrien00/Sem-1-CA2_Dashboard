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

# Streamlit app
st.title('Map Visualization')

# Sidebar for user input
selected_column = st.sidebar.selectbox('Select the column containing country codes:', options=df.columns)
value_column = st.sidebar.selectbox('Select the column containing values:', options=df.columns)

# Display sample DataFrame
st.write(df)

# Function to generate map
def generate_map(df, selected_column, value_column):
    # Create a Deck.GL layer
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=df,
        get_position='[lng, lat]',
        get_radius=20000,
        get_fill_color='[255, 0, 0]',
        pickable=True
    )

    # Set the viewport location
    view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)

    # Create the Deck.GL map
    map_ = pdk.Deck(layers=[layer], initial_view_state=view_state)

    # Display the map
    st.pydeck_chart(map_)

# Plot the map
generate_map(df, selected_column, value_column)