import streamlit as st


def mockup_1():
  st.warning("The following is a pre-generated output and is displayed as an example and also to help save LLM API usage.")
  
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

def mockup_2():
  st.warning("The following is a pre-generated output and is displayed as an example and also to help save LLM API usage.")
  
  st.write("Below is the Python code sample for a Streamlit app that resembles the mock-up image you've provided. It includes the essentials: a sidebar with a stock selection and main content with a line chart representing stock price development over time, as well as a data table showing monthly prices.")

  st.code("""
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Sample data to mimic the graph and table in the mock-up
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    prices = [125, 138, 132, 142, 145, 139, 134, 140, 144, 148, 152, 147]
    
    # Convert the data into a DataFrame for use in Streamlit
    data = pd.DataFrame({"Month": months, "Price": prices})
    
    # The sidebar for stock selection
    st.sidebar.title("Stock Market App")
    selected_stock = st.sidebar.selectbox("Select a Stock", ["Amazon", "Google", "Apple"])
    
    # Main content of the app
    st.title(f"{selected_stock} Stock Price")
    
    # Plotting the stock price line chart.
    plt.figure(figsize=(10, 4))
    plt.plot(months, prices, marker='o', color='red')
    plt.title(f"{selected_stock} Stock Price")
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.grid(True)
    st.pyplot(plt)
    
    # Display the table with the stock prices
    st.table(data)
  """)

  st.write("""
    To run the Streamlit app:

    1. Save the given code to a file, e.g., stock_app.py.
    2. Install Streamlit if you haven't already: pip install streamlit.
    3. Run the app with the command: streamlit run stock_app.py.

    Note that this app generates a static table and chart. In a real-world app, you would likely pull the stock data from a database or an API, and the chart and table would be dynamically updated based on the selected stock. Also, for a production app, you would need to handle more edge cases and possibly add more interactivity and features.
  """)
