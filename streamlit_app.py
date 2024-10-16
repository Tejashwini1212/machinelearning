import streamlit as st
import pandas as pd

st.title('🦾Machine Learning App')

st.info('This application constructs a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Tejashwini1212/dataset/refs/heads/main/iris.csv')
  df

  st.write('**X**')
  X = df.drop('Sepal.Length', axis=1)
  X

  
  st.write('**y**')
  y = df['Sepal.Length']
  y

  with st.expander('Data Visualization'):
    # Sepal.Length,Sepal.Width,Petal.Length,Petal.Width,Species
    st.scatter_chart(data=df, x='Sepal.Width', y='Petal.Width', color='Sepal.Length')
