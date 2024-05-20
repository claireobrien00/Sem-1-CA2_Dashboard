import streamlit as st
import pydeck as pdk
import pandas as pd

import numpy as np

# Set the title of the app
st.title('Sample Dashboard')

# Create some sample data
@st.cache
def load_data():
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=100)
    data = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=['A', 'B', 'C', 'D'])
    return data

data = load_data()

# Display the data as a table
st.header('Data Table')
st.dataframe(data)

# Line chart
st.header('Line Chart')
st.line_chart(data)

# Bar chart
st.header('Bar Chart')
st.bar_chart(data)

# Add a slider to filter the data
st.header('Data Filter')
date_slider = st.slider('Select a date range', min_value=data.index.min(), max_value=data.index.max(), value=(data.index.min(), data.index.max()))
filtered_data = data.loc[date_slider[0]:date_slider[1]]

# Display filtered data
st.subheader('Filtered Data Table')
st.dataframe(filtered_data)

# Display filtered data in a line chart
st.subheader('Filtered Data Line Chart')
st.line_chart(filtered_data)

# Display filtered data in a bar chart
st.subheader('Filtered Data Bar Chart')
st.bar_chart(filtered_data)

# @st.cache
# def from_data_file(filename):
#     url = (
#         "http://raw.githubusercontent.com/streamlit/"
#         "example-data/master/hello/v1/%s" % filename
#     )
#     return pd.read_json(url)

# try:
#     ALL_LAYERS = {
#         "Bike Rentals": pdk.Layer(
#             "HexagonLayer",
#             data=from_data_file("bike_rental_stats.json"),
#             get_position=["lon", "lat"],
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             extruded=True,
#         ),
#         "Bart Stop Exits": pdk.Layer(
#             "ScatterplotLayer",
#             data=from_data_file("bart_stop_stats.json"),
#             get_position=["lon", "lat"],
#             get_color=[200, 30, 0, 160],
#             get_radius="[exits]",
#             radius_scale=0.05,
#         ),
#         "Bart Stop Names": pdk.Layer(
#             "TextLayer",
#             data=from_data_file("bart_stop_stats.json"),
#             get_position=["lon", "lat"],
#             get_text="name",
#             get_color=[0, 0, 0, 200],
#             get_size=15,
#             get_alignment_baseline="'bottom'",
#         ),
#         "Outbound Flow": pdk.Layer(
#             "ArcLayer",
#             data=from_data_file("bart_path_stats.json"),
#             get_source_position=["lon", "lat"],
#             get_target_position=["lon2", "lat2"],
#             get_source_color=[200, 30, 0, 160],
#             get_target_color=[200, 30, 0, 160],
#             auto_highlight=True,
#             width_scale=0.0001,
#             get_width="outbound",
#             width_min_pixels=3,
#             width_max_pixels=30,
#         ),
#     }
#     st.sidebar.markdown("### Map Layers")
#     selected_layers = [
#         layer
#         for layer_name, layer in ALL_LAYERS.items()
#         if st.sidebar.checkbox(layer_name, True)
#     ]
#     if selected_layers:
#         st.pydeck_chart(
#             pdk.Deck(
#                 map_style="mapbox://styles/mapbox/light-v9",
#                 initial_view_state={
#                     "latitude": 37.76,
#                     "longitude": -122.4,
#                     "zoom": 11,
#                     "pitch": 50,
#                 },
#                 layers=selected_layers,
#             )
#         )
#     else:
#         st.error("Please choose at least one layer above.")
# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )