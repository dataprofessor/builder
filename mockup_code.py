import streamlit as st



st.write("Based on the given mock-up image, here is an example of how you could generate the Streamlit app using Python code:")

st.code("""
  import streamlit as st
  import pandas as pd
  import matplotlib.pyplot as plt
  
  # Create a sample dataframe with states and their population
  data = {
      'States': ['Alabama', 'Alaska', ..., 'Wyoming'],
      'Population': [4900000, 730000, ..., 570000]
  }
  df = pd.DataFrame(data)
  
  # Set the page title and layout
  st.set_page_config(page_title="Population App", layout="wide")
  
  # Title of the app
  st.title("Population App")
  
  # Slider for selecting the year
  year = st.slider('Select a year', 2000, 2024, 2020)
  
  # Display the dataframe as a table
  st.table(df)
  
  # Create a bar plot for the dataframe
  fig, ax = plt.subplots()
  ax.bar(df['States'], df['Population'], color='pink')
  ax.set_xticklabels(df['States'], rotation=90)
  ax.set_ylabel('Population')
  ax.set_title('Population by State')
  
  # Display the plot
  st.pyplot(fig)
""")

st.write("""
Please note the following as you adapt this code to your specific needs:

1. Replace the "..." in the 'States' and 'Population' lists of the dataframe with the actual data points from your application context.
2. Adjust the slider range and default value according to the mock-up image or your requirements.
3. You might want to adjust the bar plot colors, labels, title, and other properties to better match the mock-up.

This script gives a high-level structure for creating a basic Streamlit app that resembles the provided mock-up. You should further customize this code according to the full details of your application's design and requirements.
""")
