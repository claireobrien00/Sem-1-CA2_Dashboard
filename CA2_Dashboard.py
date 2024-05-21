import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Data Visualization Dashboard')

# Instructions for the user
st.write("""
This dashboard allows you to explore the data and visualize different aspects of it.
""")

# Function to load data from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/yourusername/yourrepository/main/yourdatafile.csv'
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

columns = st.multiselect("Select columns", df.columns)

if columns:
    st.write(df[columns])

    # Correlation matrix
    st.subheader('Correlation Matrix')
    correlation_matrix = df[columns].corr()
    st.write(correlation_matrix)
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, ax=ax)
    st.pyplot(fig)

    # Pairplot
    st.subheader('Pairplot')
    pairplot = sns.pairplot(df[columns])
    st.pyplot(pairplot)

# Bar chart
st.header('Bar Chart')
selected_column = st.selectbox("Select column for bar chart", df.columns)
if selected_column:
    bar_data = df[selected_column].value_counts()
    st.bar_chart(bar_data)

# Line chart
st.header('Line Chart')
selected_line_columns = st.multiselect("Select columns for line chart", df.columns)
if selected_line_columns:
    st.line_chart(df[selected_line_columns])

# Area chart
st.header('Area Chart')
selected_area_columns = st.multiselect("Select columns for area chart", df.columns, default=df.columns[:2])
if selected_area_columns:
    st.area_chart(df[selected_area_columns])

# Custom plot with Matplotlib/Seaborn
st.header('Custom Plot')
custom_plot_column = st.selectbox("Select column for custom plot", df.columns)
if custom_plot_column:
    fig, ax = plt.subplots()
    sns.histplot(df[custom_plot_column], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# Instructions to run the app
st.write("To run this app, use the command: `streamlit run dashboard.py`")

# Additional information
st.write("For more information, visit the [Streamlit documentation](https://docs.streamlit.io/).")


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