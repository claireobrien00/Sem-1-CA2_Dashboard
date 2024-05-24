import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

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

fig.update_geos(
    # Set the scope to 'europe'
    scope='world',
    # Adjust the center and zoom to focus on Europe
    center=dict(lat=52, lon=10),
    projection_scale=4
)

fig.update_layout(
    title_text="Total Livestock in European Countries"
)
# Display the figure in Streamlit
st.plotly_chart(fig)




# Function to calculate the output of the polynomial equation
def calculate_output(coefficients_df, dictionary):
    # Convert the coefficients and variables to numpy arrays
    
    # Calculate the output using the polynomial equation
     
    output = (
        coefficients[0] * dictionary['meat'] +
        coefficients[1] * dictionary['dairy'] +
        coefficients[2] * dictionary['cereals'] +
        coefficients[3] * dictionary['oils'] +
        coefficients[4] * dictionary['date'] +
        coefficients[5] * dictionary['meat']**2 +
        coefficients[6] * dictionary['meat'] * dictionary['dairy'] +
        coefficients[7] * dictionary['meat'] * dictionary['cereals'] +
        coefficients[8] * dictionary['meat'] * dictionary['oils'] +
        coefficients[9] * dictionary['meat'] * dictionary['date'] +
        coefficients[10] * dictionary['dairy']**2 +
        coefficients[11] * dictionary['dairy'] * dictionary['cereals'] +
        coefficients[12] * dictionary['dairy'] * dictionary['oils'] +
        coefficients[13] * dictionary['dairy'] * dictionary['date'] +
        coefficients[14] * dictionary['cereals']**2 +
        coefficients[15] * dictionary['cereals'] * dictionary['oils'] +
        coefficients[16] * dictionary['cereals'] * dictionary['date'] +
        coefficients[17] * dictionary['oils']**2 +
        coefficients[18] * dictionary['oils'] * dictionary['date'] +
        coefficients[19] * dictionary['date']**2 +
        coefficients[20]  # Intercept
    )
    
    return output

# Streamlit app
st.title('Food Price Indicator Calculator')

# Input form for user to input variables
st.sidebar.header('Enter in order: meat, dairy, cereals, oils, date')

variables = []
variable_labels = ['Meat', 'Dairy', 'Cereals', 'Oils', 'Date']

for i in range(5):
    variables.append(st.sidebar.number_input(f'{variable_labels[i]}', value=0.0))

variable_values = { 'meat' : variables[0], 'dairy' : variables[1], 'cereals' : variables[2], 'oils' : variables[3], 'date' : variables[4]
}

scaler = StandardScaler() #['Meat', 'Dairy','Cereals', 'Date']
minmax_scale = MinMaxScaler() # ['Oils', 'Food Price Index']

variables_array = np.array(list(variable_values.values()))

variables_reshaped = variables_array.reshape(-1, 1)

variables_scaled = minmax_scale.fit_transform(variables_reshaped)


# Read coefficients from a DataFrame
coefficients_df = pd.read_csv('CA2_Dashboard_LinMod.csv')  

# Display coefficients DataFrame
st.sidebar.write('### Coefficients DataFrame:')
st.sidebar.write(coefficients_df)

# Extract coefficients from the DataFrame
coefficients = coefficients_df.iloc[:,1].tolist()

# Calculate the output
final_output = calculate_output(coefficients, variable_values)

output_array2 = np.array(final_output)

output_reshaped2 = output_array2.reshape(1, -1)
output_unscaled = minmax_scale.inverse_transform(output_reshaped2)


# Display the output
st.write('### Output:')
st.write(f'The Food Price Index is estimated to be: {float(output_unscaled)}')
