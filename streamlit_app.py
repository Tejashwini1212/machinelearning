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

with st.expander('Data Visualization'):
    st.scatter_chart(data=df, x='culmen_length_mm', y='body_mass_g', color='species')

# data preparations
# species,island,culmen_length_mm,culmen_depth_mm,flipper_length_mm,body_mass_g,sex
with st.sidebar:
    st.header('Input features')
    island = st.selectbox('Island', ('Torgersen', 'Biscoe', 'Dream'))
    gender = st.selectbox('Gender', ('male', 'female'))
    culmen_length_mm = st.slider('Culmen length (mm)', 32.1, 59.6, 43.0)

    
    
    

 
