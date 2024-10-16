import streamlit as st
import pandas as pd
import altair as alt

# App title
st.title('🦾Machine Learning App')

# Information
st.info('This application constructs a machine learning model!')

# Loading and displaying the data
with st.expander('Data'):
    st.write('**Raw data**')
    
    # Load the data from the URL
    df = pd.read_csv('https://raw.githubusercontent.com/Tejashwini1212/dataset/refs/heads/main/iris.csv')
    
    # Show the DataFrame
    st.write(df)
    
    # Check for missing values
    st.write('**Missing values in each column:**')
    st.write(df.isna().sum())  # Display missing value counts

    # Define features (X) and target (y)
    st.write('**X**')
    X = df.drop('Sepal.Length', axis=1)
    st.write(X)
    
    st.write('**y**')
    y = df['Sepal.Length']
    st.write(y)

# Visualization with proper values
with st.expander('Data Visualization'):
    st.write("**Scatter Plot: Sepal Length vs. Petal Width**")
    
    # Creating a scatter plot using Altair
    scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('Sepal.Length', title='Sepal Length', scale=alt.Scale(zero=False)),
        y=alt.Y('Petal.Width', title='Petal Width', scale=alt.Scale(zero=False)),
        color='Sepal.Width',  # Color by 'Sepal.Width'
        tooltip=['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']  # Tooltip to show details
    ).interactive()

    # Display the chart in Streamlit
    st.altair_chart(scatter_plot, use_container_width=True)
