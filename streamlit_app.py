import streamlit as st
import pandas as pd
import altair as alt

st.title('🦾Machine Learning App')

st.info('This application constructs a machine learning model!')

with st.expander('Data'):
    st.write('**Raw data**')
    df = pd.read_csv('https://raw.githubusercontent.com/Tejashwini1212/dataset/refs/heads/main/iris.csv')
    st.write(df)  # Display the dataframe

    # Check for missing values
    st.write('**Missing values in each column:**')
    st.write(df.isna().sum())  # Show missing value counts for each column

    st.write('**X**')
    X = df.drop('Sepal.Length', axis=1)
    st.write(X)

    st.write('**y**')
    y = df['Sepal.Length']
    st.write(y)

with st.expander('Data Visualization'):
    # Use Altair for creating the scatter plot with color encoding
    scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
        x='Sepal.Length',
        y='Petal.Width',
        color='Sepal.Width',
        tooltip=['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']  # Tooltip to show details
    ).interactive()

    st.altair_chart(scatter_plot, use_container_width=True)

