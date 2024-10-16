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
    culmen_length_mm = st.slider('Culmen length (mm)', 32.1, 59.6, 43.0)
    culmen_depth_mm = st.slider('Culmen depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.slider('body mass (g)', 2700.0, 6300.0, 4207.0)
    gender = st.selectbox('Gender', ('male', 'female'))

# create a dataframe for a input feature
data = {'island': island,
        'culmen_length_mm': culmen_length_mm,
        'culmen_depth_mm':  culmen_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g':  body_mass_g,
        'sex': gender}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X], axis=0)

encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
input_row = df_penguins[:1] # convert each of the value in the column to a unique column name like combining the column name and value name to a new column name


with st.expander('Input features'):
  st.write('**Input Penguins**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  df.write('Encoded input penguin'
  input_row


        

    
    
    

 
