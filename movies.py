import streamlit as st
import pandas as pd
import numpy as np

# Generate a sample dataset
data = {
    "Movie": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
    "Duration": np.random.randint(90, 180, 5),
    "IMDb Rating": np.random.uniform(5.0, 9.0, 5),
    "Genre": ["Action", "Comedy", "Drama", "Thriller", "Horror"],
    "Director": ["Director A", "Director B", "Director C", "Director D", "Director E"],
    "Box Office Gross": np.random.randint(50, 300, 5) * 1e6,
    "Number of Votes": np.random.randint(10000, 100000, 5),
    "Release Year": np.random.randint(2000, 2022, 5)
}

df = pd.DataFrame(data)

# Sidebar for chart selection
st.sidebar.title("Select Chart Type")
chart_type = st.sidebar.selectbox("Chart Type", ["Scatter Chart", "Bar Chart", "Line Chart", "Area Chart"])

# Display the dataset
st.write("## Movie Dataset")
st.write(df)

# Display the selected chart
if chart_type == "Scatter Chart":
    st.write("## Scatter Chart: Movie Duration vs IMDb Rating")
    st.write("This scatter chart shows the relationship between movie duration and IMDb rating.")
    st.scatter_chart(df, x="Duration", y="IMDb Rating")

elif chart_type == "Bar Chart":
    bar_category = st.sidebar.selectbox("Bar Chart Category", ["Genre", "Director"])
    bar_value = st.sidebar.selectbox("Bar Chart Value", ["Box Office Gross", "Number of Votes"])
    st.write(f"## Bar Chart: {bar_category} vs {bar_value}")
    st.write(f"This bar chart shows the {bar_value.lower()} for each {bar_category.lower()}.")
    st.bar_chart(df.groupby(bar_category)[bar_value].sum())

elif chart_type == "Line Chart":
    line_value = st.sidebar.selectbox("Line Chart Value", ["IMDb Rating", "Box Office Gross"])
    st.write(f"## Line Chart: Release Year vs {line_value}")
    st.write(f"This line chart shows the trend of {line_value.lower()} over the years.")
    st.line_chart(df.set_index("Release Year")[line_value])

elif chart_type == "Area Chart":
    st.write("## Area Chart: Release Year vs Box Office Gross")
    st.write("This area chart shows the box office gross over the years.")
    st.area_chart(df.set_index("Release Year")["Box Office Gross"])