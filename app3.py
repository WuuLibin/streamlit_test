# python3 -m venv myenv
# source myenv/bin/activate
# pip install -r requirements.txt
# streamlit run app3.py
import streamlit as st
import requests
import json
import pandas as pd

# Make a GET request to the weather API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
result_dict = result.json()  # parse the json string into a dict object

# Extract temperature data
temperature_data = result_dict["temperature"]["data"]
df = pd.DataFrame(temperature_data)

# Sidebar for location selection
st.sidebar.title("Select Location")
locations = df["place"].tolist()
selected_location = st.sidebar.selectbox("Location", locations)

# Display the temperature data as a bar chart
st.write("## Temperature of All Locations")
st.bar_chart(df.set_index("place")["value"])

# Display the temperature for the selected location
selected_temp = df[df["place"] == selected_location]["value"].values[0]
st.write(f"## Temperature at {selected_location}")
st.write(f"The temperature at {selected_location} is {selected_temp}°C.")