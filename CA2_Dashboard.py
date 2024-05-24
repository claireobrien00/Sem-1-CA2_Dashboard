import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import numpy as np


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




# Function to calculate the output of the polynomial equation
def calculate_output(meat, dairy, cereals, oils, date, coefficients_df):
    # Convert the coefficients and variables to numpy arrays
    coefficients = np.array(coefficients)
    
    # Calculate the output using the polynomial equation
    output = (
        coefficients[0] * meat +
        coefficients[1] * dairy +
        coefficients[2] * cereals +
        coefficients[3] * oils +
        coefficients[4] * date +
        coefficients[5] * meat**2 +
        coefficients[6] * meat * dairy +
        coefficients[7] * meat * cereals +
        coefficients[8] * meat * oils +
        coefficients[9] * meat * date +
        coefficients[10] * dairy**2 +
        coefficients[11] * dairy * cereals +
        coefficients[12] * dairy * oils +
        coefficients[13] * dairy * date +
        coefficients[14] * cereals**2 +
        coefficients[15] * cereals * oils +
        coefficients[16] * cereals * date +
        coefficients[17] * oils**2 +
        coefficients[18] * oils * date +
        coefficients[19] * date**2 +
        coefficients[20]  # Intercept
    )
    
    return output

# Streamlit app
st.title('Food Price Indicator Calculator')

# Input form for user to input variables
st.sidebar.header('Enter in order: meat, dairy, cereals, oils, date')

variables = []
for i in range(5):
    variables.append(st.sidebar.number_input(f'Variable {i+1}', value=0.0))

variable_values = { 'meat' : variables[0], 'dairy' : variables[1], 'cereals' : variables[2], 'oils' : variables[3], 'date' : variables[4]
}
print(variable_values[4])

# Read coefficients from a DataFrame
coefficients_df = pd.read_csv('CA2_Dashboard_LinMod.csv')  

# Display coefficients DataFrame
st.sidebar.write('### Coefficients DataFrame:')
st.sidebar.write(coefficients_df)

# Extract coefficients from the DataFrame
coefficients = coefficients_df.iloc[:,1].tolist()

print(coefficients)
# Calculate the output
output = calculate_output(coefficients, variables_values)

# Display the output
st.write('### Output:')
st.write(f'The output of the polynomial equation for the given variables is: {output}')
