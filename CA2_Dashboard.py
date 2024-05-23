import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px


# Function to load data from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/claireobrien00/CA2_Dashboard/main/CA2_Dashboard_Livestock.csv'
    data = pd.read_csv(url)
    return data

# Load the data
df = load_data()


# Create choropleth map
fig = px.choropleth(df,
                    locations="Alpha-3 code", 
                    color="Total Livestock", 
                    hover_name="Alpha-3 code",
                    animation_frame="Year",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    projection='natural earth',
                    range_color=(0, 70000)
                   )

# Update layout
fig.update_layout(
    title_text="Total Livestock in European Countries",
    geo_scope="world",
    geo=dict(projection_type="natural earth")
)

# Display the figure in Streamlit
st.plotly_chart(fig)