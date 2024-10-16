import streamlit as st
import pandas as pd
import altair as alt

# App title
st.title('🦾Machine Learning App')

# Information
st.info('This application constructs a machine learning model!')




with st.expander('Data'):
    st.write('**Raw data**')
    
    # Load the data from the URL
    df = pd.read_csv('https://raw.githubusercontent.com/Tejashwini1212/dataset/main/penguins_size.csv')
    df

    st.write('**X**')
    X = df.drop('species', axis=1)
    X

    st.write('**y**')
    y = df.species
    y
    

 
